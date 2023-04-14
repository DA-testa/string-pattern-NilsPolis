def read_file_input(filename):
    try:
        with open(f"./tests/{filename}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        raise ValueError("File not found")
    except:
        raise ValueError("Error reading file")
    
    pattern = contents[0].strip()
    text = contents[1].strip()
    
    return pattern, text

def read_user_input():
    pattern = input().rstrip()
    text = input().rstrip()
    
    return pattern, text

def read_input():
    input_type = input().rstrip()
    
    if input_type == 'I':
        return read_user_input()
    elif input_type == 'F':
        filename = "06"
        if str(filename[-1]) == "a":
            raise ValueError("Invalid filename")
        return read_file_input(filename)
    else:
        raise ValueError("Invalid input type")
def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    prime = 101
    base = 256

    pattern_hash = 0
    text_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        text_hash = (text_hash * base + ord(text[i])) % prime

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+len(pattern)]:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = ((text_hash - ord(text[i]) * (base**(len(pattern)-1))) * base + ord(text[i+len(pattern)])) % prime

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
