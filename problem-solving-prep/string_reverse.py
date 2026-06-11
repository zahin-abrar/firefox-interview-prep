def reverse_str(word):
    reversed_word = ""
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    return reversed_word
print(reverse_str("apple"))