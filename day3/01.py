

excluded_list = ['.'] + list(f'{i}' for i in range(0, 11))

def is_adjacent(lines, i, j):
    indexes = [(i-1, j), (i, j-1), (i+1, j), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for index in indexes:
        x, y = index[0], index[1]
        if 0 <= x < len(lines) and 0 <= y < len(lines[x]):
            if lines[x][y] not in excluded_list:
                return True
    return False

def parse_number(lines, i, j):
    idx = j
    result = 0
    should_include = False
    while(idx < len(lines[i]) and '0' <= lines[i][idx] <= '9'):
        result *= 10
        if not should_include:
            should_include = is_adjacent(lines, i, idx)
        result += int(lines[i][idx])
        idx += 1
    return result, should_include, idx

def get_sum(lines):
    result = 0
    for i in range(len(lines)):
        j = 0
        while(j < len(lines[i])):
            if '0' <= lines[i][j] <= '9':
                number, should_include, j = parse_number(lines, i, j)
                if should_include:
                    result += number
            else:
                j += 1
    return result


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        print(get_sum(list(line.strip() for line in lines)))