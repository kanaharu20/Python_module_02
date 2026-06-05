#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.args = (message,)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.args = (message,)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.args = (message,)


def ft_custom_errors() -> None:
    plant_name = "tomato"
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError(f"The {plant_name} plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")

    errors = [
        PlantError(f"The {plant_name} plant is wilting!"),
        WaterError("Not enough water in the tank!")
        ]

    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
