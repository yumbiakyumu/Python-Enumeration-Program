from enum import Enum

# Define an Enum for school days
class SchoolDays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4

# Function to get unit codes based on selected day
def UnitCodes(lectures):
    # Determine the unit code based on the selected day
    if lectures == SchoolDays.MONDAY:
        return "CMT 407"
    elif lectures == SchoolDays.TUESDAY:
        return "CMT 408"
    elif lectures == SchoolDays.WEDNESDAY:
        return "CMT 429"
    elif lectures == SchoolDays.THURSDAY:
        return "CMT 432"
    else:
        return "Invalid day"  

# Main function to manage user input and display the selected day's unit code
def main():
    print("Welcome To Unit CODE MANAGER")
    print("Available DAYS:")
    for lectures in SchoolDays:
        # Print the names and values of the available school days
        print(f"{lectures.name} {lectures.value}")

    while True:  # Loop until a valid day is selected
        try:
            chosen_day = int(input("Enter the day number: ")) 
            selected_day = SchoolDays(chosen_day)  
            info = UnitCodes(selected_day)  
            print("You have selected:", info)  
            break  
        except ValueError:
            print("Please enter a valid day number.")  # If invalid input is given, prompt user to enter a valid number

if __name__ == "__main__":
    main()  