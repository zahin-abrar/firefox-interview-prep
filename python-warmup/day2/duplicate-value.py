#Problem: Given a list, return duplicate values only once.

def find_duplicate(items):
    result = []
    seen = set()
    duplicates = set()


    if not items:
        return items
    else:
        for i in items:
            if i in seen:
                if i not in duplicates:
                    result.append(i)
                    duplicates.add(i)
            else:
                seen.add(i)
        return result

print(find_duplicate(["a", "b", "a", "a", "b", "c", "d", "e", "e"]))



