#!/usr/bin/env python3

def input_temperature(temp_str:str) -> int:
    try:
        temp_int = int(temp_str)
        print(f"Input data is '{temp_str}'\n"
              f"Temperature is now {temp_int}°C")
        return temp_int
    except ValueError:
        print(f"Input data is '{temp_str}'\n"
              f"Caught main error: invalid literal for int() with base 10: '{temp_str}'\n")
    finally:
        print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    print()
    input_temperature("abc")
