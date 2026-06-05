#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int | None:
    try:
        print(f"Input data is '{temp_str}'")
        temp_int = int(temp_str)
    except ValueError:
        print(
            f"Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{temp_str}'\n"
        )
        return None
    try:
        if temp_int > 40:
            raise ValueError(f"Caught input_temperature error: {temp_int}°C "
                             "is too hot for plants (max 40°C)\n")
        if temp_int < 0:
            raise ValueError(f"Caught input_temperature error: {temp_int}°C "
                             "is too cold for plants (min 0°C)\n")
    except ValueError as e:
        print(e)
        return None
    print(f"Temperature is now {temp_int}°C\n")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
