test_results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_cart", "status": "failed"},
    {"name": "test_logout", "status": "passed"},
]

def count_test_status(results: list[dict]) -> dict[str, int]:
    total_passed = 0
    total_failed = 0

    for result in results:
        if result["status"] == "passed":
            total_passed += 1
        elif result["status"] == "failed":
            total_failed += 1

    return ({
        "passed": total_passed,
        "failed": total_failed
    })

print(count_test_status(test_results))