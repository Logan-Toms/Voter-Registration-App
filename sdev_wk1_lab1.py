"""sys module to allow exiting the program""" 
import sys

# Data Validation Functions
def check_age(age_input):
    """Check the age input and return True if age is valid, otherwise False."""
    try:
        age = int(age_input)
        if age < 1 or age > 120:
            return False
        return True
    except ValueError:
        return False

def is_valid_state(state):
    """Check if the state is a valid US state abbreviation."""
    valid_states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    return state.upper() in valid_states

def is_us_citizen(citizenship):
    """Check if the user claimed to be a US citizen."""
    return citizenship.lower() == 'us'

# Main Voter Registration Function

def register_voter():
    """Guide the user through the voter registration process."""

    # Helper function allows exiting the program
    def get_input(prompt):
        value = input(prompt).strip()
        if value.lower() == 'exit':
            print("Exiting the voter registration process. Goodbye!")
            sys.exit() # Exit the program
        return value

    # Get the basic details using the helper function
    first_name = get_input("Enter your first name: ")
    last_name = get_input("Enter your last name: ")
    age = get_input("Enter your age: ")

    # Validate age
    while not check_age(age):
        print("Invalid age. Please enter a valid age between 1 and 120.")
        age = get_input("Enter your age: ")
    # If age is less than 18, inform the user
    if int(age) < 18:
        print("Sorry, you are not eligible to vote as you are below 18 years of age.")
        return
    citizenship = get_input("Enter your country of citizenship (e.g. US): ")

    # Check citizenship
    if not is_us_citizen(citizenship):
        print("Sorry, only US citizens are eligible to vote.")
        return

    state = get_input("Enter your state of residence (2 letter code, e.g. CA): ").upper()

    # Validate state
    while not is_valid_state(state):
        print("Invalid state code. Please enter a valid 2 letter US state code.")
        state = get_input("Enter your state of residence: ").upper()

    zipcode = get_input("Enter your zip code: ")

    # Basic zip code validation (5 digits)
    while len(zipcode) != 5 or not zipcode.isdigit():
        print("Invalid zip code. Please enter a valid 5 digit zip code.")
        zipcode = get_input("Enter your zip code: ")

    # If all data is valid print report
    print("\nCongratulations you have successfully registered to vote!")
    print(f"Name: {first_name} {last_name}")
    print(f"Age: {age}")
    print("U.S. Citizen: Yes")
    print(f"State: {state}")
    print(f"Zip code: {zipcode}")
    print("""\nThanks for trying the Voter Registration Application.
          \nYour voter registration card should be shipped within 3 weeks.""")

# Main function to run the voter registration program
def main():
    """Main function to run the voter registration program."""
    while True:
        print("\n--- Voter Registration ---")
        print("1. Register to vote")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_voter()
        elif choice == "2":
            print("Exiting the voter registration program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

main()
