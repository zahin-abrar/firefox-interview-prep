example_logs = [
    {"test_name": "test_login", "status": "PASS", "duration_ms": 1200},
    {"test_name": "test_checkout", "status": "FAIL", "duration_ms": 3400},
    {"test_name": "test_logout", "status": "PASS", "duration_ms": 800},
    {"test_name": "test_profile_pic", "status": "SKIP", "duration_ms": 0}
]

def analyze_test_runs(logs):
    total_pass = 0
    total_fail = 0
    total_skip = 0
    duration_list = []
    summary = {"total_passed": "", "total_failed": "", "success_rate": "", "slowest_pass": ""}
    longest_test_name = ""

    for log in logs:
        if log["status"] == "PASS":
            total_pass += 1
        elif log["status"] == "FAIL":
            total_fail += 1
        elif log["status"] == "SKIP":
            total_skip += 1
        duration_list.append(log["duration_ms"])

    number_of_valid_tests = len(logs) - total_skip
    sorted_duration = sorted(duration_list)
    longest_running_test = sorted_duration[len(sorted_duration) - 1]

    for log in logs:
        if log["duration_ms"] == longest_running_test:
            longest_test_name = log["test_name"]
    success_rate = round(((total_pass/number_of_valid_tests)*100), 2)

    if len(logs) > 0:
        summary["total_passed"] = str(total_pass)
        summary["total_failed"] = str(total_fail)
        summary["success_rate"] = str(success_rate)
        summary["slowest_pass"] = longest_test_name
    else:
        summary["success_rate"] = str(0)

    return summary

print(analyze_test_runs(example_logs))