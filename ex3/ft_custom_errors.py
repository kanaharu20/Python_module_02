#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unkown plant error") -> None:
        self._message = message

    def __str__(self) -> str:
        return self._message

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass


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
    except  WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")

    Exces = [PlantError(f"The {plant_name} plant is wilting!"), WaterError("Not enough water in the tank!")]

    for exce in Exces:
        try:
            raise exce
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print(f"\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
