test_results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_cart", "status": "failed"},
    {"name": "test_logout", "status": "passed"},
]

def failed_test_name(results: list[dict]) -> list[str]:
    failed_tests = []
    for result in results:
        status = result.get("status", "unknown")
        if status == "failed":
            failed_tests.append(result.get("name", "unknown_test"))
    return failed_tests

print(failed_test_name(test_results))