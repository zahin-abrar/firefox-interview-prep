response = {
    "id": 101,
    "name": "standard_user",
    "role": "tester"
}
def validate_required_fields(data: dict, required_fields: list[str]) -> list[str]:
    missing_field = []

    for field in required_fields:
        if field not in data:
            missing_field.append(field)

    return missing_field

print(validate_required_fields(response, ["id", "name", "email"]))