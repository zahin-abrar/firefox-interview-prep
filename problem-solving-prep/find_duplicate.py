def find_duplicate(items: list) -> list:
    result = []
    duplicates = set()

    for item in items:
        if item in duplicates and item not in result:
            result.append(item)
        else:
            duplicates.add(item)

    return result

print(find_duplicate(["login", "cart", "login", "checkout", "cart"]))