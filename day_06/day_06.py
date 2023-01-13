

def find_repeating_chars(stream: str, num: int) -> int:
    for i in range(len(stream) - num + 1):
        chars = []
        for j in range(num):
            if stream[i+j] in chars:
                break
            else:
                chars.append(stream[i+j])
        if len(chars) == num:
            # found a non-repeating substring of the required length
            return i + num
    return -1


if __name__ == "__main__":
    stream = ""
    with open("./test.txt") as f:
        stream = f.readline()
    stream = stream[:-1] # strip the newline off
    print(f"Part 1 solution: {find_repeating_chars(stream, 4)}")
    print(f"Part 2 solution: {find_repeating_chars(stream, 14)}")
    