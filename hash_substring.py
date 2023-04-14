# python3
def read_input(filename=None):
    if filename is not None:
        try:
            with open(f"./test/{filename}") as f:
                contents = f.readlines()
        except FileNotFoundError:
            raise ValueError("Missing File")
        except:
            raise ValueError("Reading Error")

        pattern = contents[0].strip()
        text = contents[1].strip()  
    else:
        pattern = input().rstrip()
        text = input().rstrip()

    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 101
    base = 256

    p_hash = 0
    t_hash = 0
    for i in range(len(pattern)):
        p_hash = (p_hash * base + ord(pattern[i])) % prime
        t_hash = (t_hash * base + ord(text[i])) % prime

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+len(pattern)]:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            t_hash = ((t_hash - ord(text[i]) * (base**(len(pattern)-1))) * base + ord(text[i+len(pattern)])) % prime

    return occurrences

if __name__ == '__main__':
    input_type = input().rstrip()

    if input_type == 'I':
        pattern, text = read_input()
    elif input_type == 'F':
        filename = "06"
        if str(filename[-1]) == "a":
            raise ValueError("Invalid filename")
        pattern, text = read_input(filename)
    else:
        raise ValueError("Invalid input type")

    print_occurrences(get_occurrences(pattern, text))
