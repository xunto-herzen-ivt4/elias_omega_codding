from base_numeral_system import base_ns


def encode_word(item):
    result = [0]
    number = item

    while number > 1:
        code = base_ns.convert(number, 2).integer

        number = len(code) - 1
        result = code + result

    return result


def encode(data: list):
    # Encode phrase
    result = []
    for item in data:
        result += encode_word(item)
    return result


def decode(k: list):
    k = k[:]
    result = []

    n = 1
    while len(k) > 0:
        group = k[:n+1]

        if group[0] == 0:
            result.append(n)
            k = k[1:]
            n = 1
        else:
            k = k[n + 1:]
            n = int(base_ns.convert_to_dec(base_ns.NumberBased(2, group)))



    return result
