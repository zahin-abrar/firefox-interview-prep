def sanitize_filename(test_name: str, timestamp: str):
    sanitized_test_name = test_name.replace(":","_").replace("/", "_").replace(" ", "_").replace(".", "_")
    extension = ".png"
    return sanitized_test_name+"_"+timestamp+extension

print(sanitize_filename("tests/test_login.py::test valid login", "20260611_101500"))