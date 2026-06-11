expected_dict = {
    "id": 101,
    "name": "standard_user",
    "role": "tester"
}
actual_dict = {
    "id": 102,
    "name": "standard_user",
    "email": "user@test.com"
}

def compare_dictionaries(expected: dict, actual: dict)-> dict:
    missing_keys = []
    unexpected_keys = []
    mismatched_values = {}

    for key1, key2 in zip(expected, actual):
        if key1 != key2:
            missing_keys.append(key1)
            unexpected_keys.append(key2)
        if key1 not in missing_keys and key2 not in unexpected_keys:
            if expected[key1] != actual[key2]:
                mismatched_values["expected"] = expected[key1]
                mismatched_values["actual"] = actual[key2]

    return {
        "missing_keys": missing_keys,
        "unexpected_keys": unexpected_keys,
        "mismatched_values": mismatched_values
    }

print(compare_dictionaries(expected_dict, actual_dict))