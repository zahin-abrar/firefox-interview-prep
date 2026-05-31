#Problem: Count failed test statuses

def count_failed_test(result):
    count = 0
    failed_test_case_names = []

    for i in result:
        status = i.get("status", "").lower()

        if status == "failed":
            count += 1
            failed_test_case_names.append(i.get("name"))
    return count, failed_test_case_names

print(count_failed_test([
    {"name": "test_login", "status": "passed"},
    {"name": "test_search", "status": "failed"},
    {"name": "test_checkout", "status": "failed"},
]))
