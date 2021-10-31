"""exercism variable length quantity module."""


def encode(numbers):
    """Encode a (hex) number with VLQ"""
    output = []
    for current in numbers:
        number_output = []
        if current == 0:
            number_output.append(0)

        while current > 0:
            rest = current % 128
            if len(number_output) > 0:
                rest += 128

            number_output.append(rest)
            current = current // 128

        output.extend(number_output[::-1])

    return output

def decode(bytes_):
    """Decode a (hex) number with VLQ"""
    output = []
    carry = []
    value = 0
    for current in bytes_:
        if current >= 128 and len(bytes_) == 1:
            raise ValueError("Incomplete VLQ sequence.")

        if current >= 128:
            carry.append(current)
        elif len(carry) == 0:
            output.append(current)
        else:
            carry.append(current)
            multiplier = 1
            carry = carry[::-1]
            for byte in carry:
                value += (byte % 128) * multiplier
                multiplier *= 128

            output.append(value)
            value = 0
            carry = []

    return output
