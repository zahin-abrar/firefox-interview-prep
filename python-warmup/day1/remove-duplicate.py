#Problem: Remove duplicates while preserving order
#New concept: set() --> set is a collection but does not keep insertion order in the way we rely on for output, does not allow duplicate and is not accessible by index. Useful for fast lookup

def remove_duplicate(values):
    result = []
    seen = set()

    for i in values:
        if i not in seen:
            result.append(i)
            seen.add(i)

    return result

print(remove_duplicate([1, 2, 2, 3, 1, 4]))
