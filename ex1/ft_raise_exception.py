#! /usr/bin/env python3

def input_temperature(temp_str:str) -> int:
    try:
        print(f"Input data is '{temp_str}'")
        i = int(temp_str)
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}'\n")
        return
    try:
        if i > 40:
            raise ValueError(f"Caught input_temperature error: {i}°C "
                             "is too hot for plants (max 40°C)\n")
        if i < 0:
            raise ValueError(f"Caught input_temperature error: {i}°C "
                             "is too cold for plants (min 0°C)\n")
    except ValueError as e:
        print(e)
        return
    print(f"Temperature is now {i}°C\n")
    return i

def test_tmperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")
    print("All tests completed - program didn't crash!")

if __name__ =="__main__":
    test_tmperature()