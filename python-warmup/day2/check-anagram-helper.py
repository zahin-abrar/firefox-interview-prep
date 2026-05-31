def dict_builder(val):
    freq = {}

    for c in val:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    return freq

def check_anagram(str1, str2):
    cleaned_str1 = "".join(str1.lower().split())
    cleaned_str2 = "".join(str2.lower().split())

    if len(cleaned_str1) != len(cleaned_str2):
        return False

    return (
        dict_builder(cleaned_str1) == dict_builder(cleaned_str2)
    )

print(check_anagram("rail safety", "fairy tales"))