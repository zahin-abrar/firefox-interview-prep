def count_character(text: str) -> dict[str, int]:
    character_count = {}
    for s in text:
        if s == " ":
            continue
        if s not in character_count:
            character_count[s] = 1
        else:
            character_count[s] += 1
    return character_count

print(count_character("apple apple"))

