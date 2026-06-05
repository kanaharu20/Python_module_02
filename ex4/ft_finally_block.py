#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self._message = message

    def __str__(self) -> str:
        return self._message


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_name: str) -> str:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name.capitalize()}: [OK]")
    return plant_name


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print(
        "Testing valid plants...\n"
        "Opening watering system"
    )
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print(
        "Testing invalid plants...\n"
        "Opening watering system"
    )
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
