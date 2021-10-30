"""exercism forth module."""


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class Forth():
    """
    An evaluator for a very simple subset of Forth.

    Supports the following words:
    - `+`, `-`, `*`, `/` (integer arithmetic)
    - `DUP`, `DROP`, `SWAP`, `OVER` (stack manipulation)

    Also supports defining new words using the
     customary syntax: `: word-name definition ;`.
    """
    def __init__(self):
        # for now, backed by an list
        self.stack = []
        self.OPERATIONS = ['+', '-', '*', '/']
        self.STACK_OPERATIONS = ['DUP', 'DROP', 'SWAP', 'OVER']
        # for now, backed by a dict
        self.USER_FUNCTIONS = {}

    def __push(self, value):
        self.stack.append(value)

    def __pop(self):
        return self.stack.pop(len(self.stack) - 1)

    def __len(self):
        return len(self.stack)

    def __error_check(self, data):
        if len(data) == 1 and (data in self.OPERATIONS or data in self.STACK_OPERATIONS):
            raise StackUnderflowError("Insufficient number of items in stack")

    def __check_user_defined(self, data):
        if data.startswith(":"):
            return True

        return False

    def __parse_user_func(self, args):
        # discard starting :
        args.pop(0)
        # discard trailing ;
        args.pop(len(args) - 1)
        name = args.pop(0)
        if name.isnumeric():
            raise ValueError("illegal operation")

        # resolve any references to user functions
        for index, arg in enumerate(args):
            arg = arg
            if arg in self.USER_FUNCTIONS:
                # 0th only?
                args[index] = self.USER_FUNCTIONS.get(arg)[0]

        self.USER_FUNCTIONS[name] = args

    def __choose_operation(self, args):
        for arg in args:
            if arg.isnumeric():
                self.__push(int(arg))
            elif arg in self.USER_FUNCTIONS:
                self.__choose_operation(self.USER_FUNCTIONS.get(arg))
            elif arg in self.OPERATIONS:
                self.__math_operation(arg)
            elif arg in self.STACK_OPERATIONS:
                self.__operation(arg)
            else:
                raise ValueError("undefined operation")

    def __operation(self, operation):
        if self.__len() == 0:
            raise StackUnderflowError("Insufficient number of items in stack")

        result = self.__pop()
        if operation == 'DUP':
            self.__push(result)
            self.__push(result)
            return
        elif operation == 'DROP':
            return

        if self.__len() == 0:
            raise StackUnderflowError("Insufficient number of items in stack")

        if operation == 'SWAP':
            number = self.__pop()
            self.__push(result)
            self.__push(number)
        elif operation == 'OVER':
            number = self.__pop()
            self.__push(number)
            self.__push(result)
            self.__push(number)

        return

    def __math_operation(self, operation):
        if self.__len() < 2:
            raise StackUnderflowError("Insufficient number of items in stack")

        result = self.__pop()
        while self.__len() > 0:
            number = self.__pop()
            if operation == "+":
                result += number
            elif operation == "-":
                result = number - result
            elif operation == "*":
                result *= number
            elif operation == "/":
                if result == 0:
                    raise ZeroDivisionError("divide by zero")
                result = int(number / result)

        self.__push(result)
        return

    def __get_stack(self):
        return self.stack

    def evaluate(self, input_data):
        """Evaluate input as if for a Forth program and return resulting stack."""
        for data in input_data:
            data = data.upper()
            self.__error_check(data)
            args = data.split(" ")
            if self.__check_user_defined(data):
                self.__parse_user_func(args)
                continue

            self.__choose_operation(args)

        return self.__get_stack()

def evaluate(input_data):
    forth_program = Forth()
    return forth_program.evaluate(input_data)
