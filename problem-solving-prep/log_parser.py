log_text = """2026-06-11 10:00:01 | INFO | Starting test_login
2026-06-11 10:00:02 | ERROR | test_login failed
2026-06-11 10:00:03 | WARN | Screenshot not found
2026-06-11 10:00:04 | INFO | Browser closed"""

def count_log_severity(log: str) -> dict[str, int]:
    log_by_line = log.split("\n")

    normalized_log = []

    severity_count = {}

    for log in log_by_line:
        normalized_log.append(log.split("|"))

    for log in normalized_log:
        severity = log[1].strip()
        if severity not in severity_count:
            severity_count[severity] = 1
        else:
            severity_count[severity] += 1

    return severity_count

print(count_log_severity(log_text))