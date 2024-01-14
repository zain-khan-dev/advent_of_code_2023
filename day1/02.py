class Constants:
    THREE_DIGITS = 3
    FOUR_DIGITS = 4
    FIVE_DIGITS = 5
    NUMS_MAP = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}


def guess_number(idx, size, line, is_reversed=False):
    if idx + size < len(line):
        digits = line[idx: idx + size].upper()
        if is_reversed:
            digits = digits[::-1]
        if digits in Constants.NUMS_MAP:
            return Constants.NUMS_MAP[digits]
    return None

def check_number(line, idx, is_reversed=False):
    return guess_number(idx, Constants.THREE_DIGITS, line, is_reversed) or guess_number(idx, Constants.FOUR_DIGITS, line, is_reversed) or guess_number(idx, Constants.FIVE_DIGITS, line, is_reversed)    



def get_number(line):
    result = 0
    for idx in range(len(line)):
        if '0' <= line[idx] <= '9':
            result += ord(line[idx]) - ord('0')
            break
        number = check_number(line, idx)
        if number:
            result += number
            break
    result *= 10
    reversed_line = line[::-1]
    for idx in range(len(reversed_line)):
        if '0' <= reversed_line[idx] <= '9':
            result += ord(reversed_line[idx]) - ord('0')
            break
        number = check_number(reversed_line, idx, True)
        if number:
            result += number
            break
    return result

if __name__ == "__main__":
    result = 0
    with open("01.txt") as file:
        text = file.readlines()
        for line in text:
            number = get_number(line)
            result += number
    print(result)