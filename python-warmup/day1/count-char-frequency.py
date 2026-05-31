#Problem: Count frequency of characters in a string.
#Dictionary: stores key, value

def check_frequency(val):
    freq = {}
    for c in val:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

print(check_frequency("banana"))