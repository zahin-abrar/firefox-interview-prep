#Problem: normalize strings before comparison
#Python string cleaning methods: strip(), lower(), upper(), split()

def normalize_string(str1, str2):
    cleaned_str1 = " ".join(str1.strip().lower().split())
    cleaned_str2 = " ".join(str2.strip().lower().split())

    return cleaned_str1 == cleaned_str2

print(normalize_string("   hello", "hello       1"))