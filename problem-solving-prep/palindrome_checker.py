def reverse_string(string: str) -> str:
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    print(reversed_string)
    return reversed_string

def is_palindromes(string: str):
    normalized_string = "".join(string.lower().split())
    print(normalized_string)
    reversed_string = reverse_string(normalized_string)
    if normalized_string == reversed_string:
        return True
    else:
        return False

print(is_palindromes("              madam         "))