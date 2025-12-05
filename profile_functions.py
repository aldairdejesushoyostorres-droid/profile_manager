# NEW ABSTRACTION FUNCTION
def display_profile_details(username, profile_data):
    """Handles the formatted printing of a single user's profile data."""
    print("\n########################################")
    print(f"\nProfile Information: {username}")
    print(f"\nName: {profile_data["name"]}")
    print(f"\nLast Name: {profile_data["surname"]}")
    print(f"\nAge: {profile_data["age"]}")
    print(f"\nEmail: {profile_data["email"]}")
    print("\n########################################")

def create_profile(profiles):
    name = input("\nIndicate your name: ")
    surname = input("\nIndicate your last name: ")
    email = str.lower(input("\nIndicate your email: "))
    while True:
        try:
            age = int(input("\nIndicate your age: "))
            if age < 0 or age > 100:
                print("\nPlease, provide a valid age. Try again!")
            else:
                break
        except ValueError:
            print("\nYou have to provide your age in numeric format")
    while True:
        username = input("\nIndicate your username: ")
        if username in profiles:
            print("\nThe provided username already exists, indicate another one, please")
        else:
            break
    profile = {
        "name": name,
        "surname": surname,
        "age": age,
        "email": email
    }

    profiles[username] = profile

def view_profiles(profiles):
    if len(profiles) == 0:
        print("\nWe can't see anything yet because there are no users")
    else:
        # Calls the new abstraction function for each profile
        for username, profile_data in profiles.items(): 
            display_profile_details(username, profile_data)


def check_profile(username, profiles): # Renamed 'profile' to 'username' for clarity
    if username not in profiles:
        print("\nThe provided username is not part of our database")
    else:
        # Calls the new abstraction function for the found profile
        display_profile_details(username, profiles[username])


def update_profile(profile, profiles):
    if profile not in profiles:
        print("\nWe can't update a non-existing profile")
    else:
        while True:
            try:
                print("\nWhat do you want to update?")
                print("\n1) Your name")
                print("\n2) Your last name")
                print("\n3) Your age")
                print("\n4) Your email")
                choice = int(input("\nOption: "))
                if choice not in {1,2,3,4}:
                    print("\nYou have to select one of the possible options, try again")
                else:
                    break
            except ValueError:
                print("\nYou have to provide a valid numeric option, try again")
        match choice:
            case 1:
                profiles[profile]["name"] = input("\nNew name: ")
            case 2:
                profiles[profile]["surname"] = input("\nNew last name: ")
            case 3:
                while True:
                    try:
                        profiles[profile]["age"] = int(input("\nNew age: "))
                        if profiles[profile]["age"] < 0 or profiles[profile]["age"] > 100:
                            print("\nYou have to provide a valid age, please.")
                        else:
                            break
                    except ValueError:
                        print("\nYou have to provide a valid numeric answer, try again!")
            case 4:
                profiles[profile]["email"] = input("\nNew email: ")

def delete_profile(profile, profiles):
    if profile not in profiles:
        print("\nWe can't delete a profile that is not part of our database")
    else:
        profiles.pop(profile)
        print("\nWe successfully deleted the profile!\nThe profile no longer exists")