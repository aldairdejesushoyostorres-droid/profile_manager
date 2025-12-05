def create_profile(profiles):
    name = input("\nIndicate your name: ")
    surname = input("\nIndicate your last name: ")
    email = surname = input("\nIndicate your email: ")
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