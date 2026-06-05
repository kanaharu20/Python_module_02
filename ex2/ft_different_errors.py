#!/usr/bin/env python3

def garden_operations(operation_number:int) -> None:
    if operation_number == 0:
        i = int ("abc")
    elif operation_number == 1:
        i = 1/0
    elif operation_number == 2:
        open("/non/existent/file","r").close()
    elif operation_number == 3:
        i = "abc"
        j = 3
        k = i + j

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    test = [0,1,2,3]
    for i in test:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
