def create_profile(profiles):
    name = input("\nIndicate your name: ")
    surname = input("\nIndicate your last name: ")
    email = input("\nIndicate your email: ")
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
        print("\n########################################")
        for profile in profiles:
            print(f"\nProfile Information: {profile}")
            print(f"\nName: {profiles[profile]["name"]}")
            print(f"\nLast Name: {profiles[profile]["surname"]}")
            print(f"\nAge: {profiles[profile]["age"]}")
            print(f"\nEmail: {profiles[profile]["email"]}")
            print("\n########################################")

def check_profile(profile, profiles)
    if profile not in profiles:
        print("\nThe provided username is not part of our database")
    else:
        print("\n########################################")
        print(f"\nProfile Information: {profile}")
        print(f"\nName: {profiles[profile]["name"]}")
        print(f"\nLast Name: {profiles[profile]["surname"]}")
        print(f"\nAge: {profiles[profile]["age"]}")
        print(f"\nEmail: {profiles[profile]["email"]}")
        print("\n########################################")