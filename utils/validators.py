def validate_positive(value, name):
    if value < 0:
        print(f"Error: {name} cannot be negative")
        return False
    return True

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter numeric values.")