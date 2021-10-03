"""exercism bob module."""


def response(hey_bob):
    """
    Model responses for input text.

    :param hey_bob string - The input provided.
    :return string - The respons.
    """
    answer = 'Whatever.'

    hey_bob = hey_bob.strip()
    yelling = hey_bob.isupper()
    asking_question = len(hey_bob) > 0 and hey_bob[-1] == '?'

    if asking_question and yelling:
        answer = "Calm down, I know what I'm doing!"
    elif asking_question:
        answer = 'Sure.'
    elif yelling:
        answer = 'Whoa, chill out!'
    elif hey_bob == '':
        answer = 'Fine. Be that way!'

    return answer
