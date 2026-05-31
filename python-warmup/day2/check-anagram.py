#Anagram: Two words or strings contain the same letters with the same frequency, just in a different order.

def check_anagram(str1, str2):
    cleaned_str1 = "".join(str1.lower().split())
    cleaned_str2 = "".join(str2.lower().split())

    char_count_1 = {}
    char_count_2 = {}

    if len(cleaned_str1) != len(cleaned_str2):
        return False
    else:
        for c in cleaned_str1:
            if c in char_count_1:
                char_count_1[c] += 1
            else:
                char_count_1[c] = 1
        for c in cleaned_str2:
            if c in char_count_2:
                char_count_2[c] +=1
            else:
                char_count_2[c] = 1
        if char_count_1 == char_count_2:
            return True
        else:
            return False

print(check_anagram("rail safety", "fairy tales"))