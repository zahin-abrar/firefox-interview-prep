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

    for key in expected:
        if key not in actual:
            missing_keys.append(key)

    for key in actual:
        if key not in expected:
            unexpected_keys.append(key)

    for key in expected:
        if key in actual:
            if expected[key] != actual[key]:
                mismatched_values[key] = {
                    "expected": expected[key],
                    "actual": actual[key]
                }

    return {
        "missing_keys": missing_keys,
        "unexpected_keys": unexpected_keys,
        "mismatched_values": mismatched_values
    }

print(compare_dictionaries(expected_dict, actual_dict))