def solution(src):
    result = src[0]
    count = 0
    current_char = src[0]

    for char in src:
        if char == current_char:
            count += 1
        else:
            result += convert_count(count)
            count = 1
            current_char = char

    result += convert_count(count)

    return result

def convert_count(count):
    return chr(count + ord('A') - 1)