def convert_cm_to_inches():
    try:
        cm = float(input("Enter a length in centimeters: "))

        if cm < 0:
            print("Invalid entry. Length cannot be negative.")
        else:
            # Convert to inches
            inches = cm / 2.54
            print(f"{cm} cm is equal to {inches:.2f} inches.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
convert_cm_to_inches()
