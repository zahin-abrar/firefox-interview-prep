def remove_duplicate(items: list) -> list:
    unique_list = []
    unique_set = set()

    for item in items:
        if item not in unique_set:
            unique_list.append(item)
            unique_set.add(item)

    return unique_list

print(remove_duplicate([1, 2, 2, 3, 1, 5, 6, 1, 9]))