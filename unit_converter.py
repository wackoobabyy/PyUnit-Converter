# Jimoh Olamilekan Ridwanlah
# 25/18456
# Computer Science 

import sys

def process_length_conversion():
    """Matches Phase 2: Handles distance logic (Km <-> Miles)."""
    print("\n--- LENGTH MENU ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    
    sub_choice = input("Select direction (1 or 2): ")
    
    try:
        val_input = input("Enter value to convert: ")
        value_to_convert = float(val_input) # Nomenclature matches design

        if sub_choice == '1':
            # 1 km = 0.621371 miles
            result = value_to_convert * 0.621371
            print(f"\n>> {value_to_convert} km = {result:.4f} miles")
        elif sub_choice == '2':
            # 1 mile = 1.60934 km
            result = value_to_convert * 1.60934
            print(f"\n>> {value_to_convert} miles = {result:.4f} km")
        else:
            print("Invalid sub-option selected.")

    except ValueError:
        print("(!) Error: Invalid format. Please enter a number.")

def process_weight_conversion():
    """Matches Phase 2: Handles mass logic (Kg <-> Lbs)."""
    print("\n--- WEIGHT MENU ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    sub_choice = input("Select direction (1 or 2): ")

    try:
        val_input = input("Enter value to convert: ")
        value_to_convert = float(val_input) # Nomenclature matches design

        if sub_choice == '1':
            # 1 kg = 2.20462 lbs
            result = value_to_convert * 2.20462
            print(f"\n>> {value_to_convert} kg = {result:.4f} lbs")
        elif sub_choice == '2':
            # 1 lb = 0.453592 kg
            result = value_to_convert * 0.453592
            print(f"\n>> {value_to_convert} lbs = {result:.4f} kg")
        else:
            print("Invalid sub-option selected.")

    except ValueError:
        print("(!) Error: Invalid format. Please enter a number.")

def start_interface():
    """Matches Phase 2: The main entry point/controller."""
    print("=== PyUnit Engineering Converter ===")
    
    while True:
        print("\n[MAIN MENU]")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Exit Program")
        
        main_choice = input("Select category: ")

        if main_choice == '1':
            process_length_conversion()
        elif main_choice == '2':
            process_weight_conversion()
        elif main_choice == '3':
            print("Exiting tool...")
            sys.exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    start_interface()
