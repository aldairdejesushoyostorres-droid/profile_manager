import profile_functions

# 1. LOAD PROFILES ON STARTUP (Replaces 'profiles = dict()')
profiles = profile_functions.load_profiles()

print("\nWelcome to our system!")

while True:
    while True:
        try:
            print("\nSelect one of the following options:")
            print("\n1) View all profiles")
            print("\n2) Create a profile")
            print("\n3) Update a profile")
            print("\n4) Delete a profile")
            print("\n5) View a specific profile")
            choice = int(input("\nIndicate your choice: "))
            if choice < 1 or choice > 5:
                print("\nYou have to select one of the available options, try again!")
            else:
                break
        except ValueError:
            print("\nYou have to provide a valid numeric option, try again!")

    match choice:
        case 1:
            profile_functions.view_profiles(profiles)
        case 2:
            profile_functions.create_profile(profiles)
        case 3:
            profile_name = input("\nIndicate the username for updating such a profile: ")
            profile_functions.update_profile(profile_name, profiles)
        case 4:
            profile_name = input("\nIndicate the username for deleting such a profile: ")
            profile_functions.delete_profile(profile_name, profiles)
        case 5:
            profile_name = input("\nIndicate the username of the profile to view: ")
            profile_functions.check_profile(profile_name, profiles)
    
    while True:
        try:
            print("\nDo you want to perform another action?")
            print("\n1) Yes, I do")
            print("\n2) No, I do not")
            option = int(input("\nOption: "))
            if option not in {1,2}:
                print("\nYou have to select one of the provided options, try again")
            else:
                break
        except ValueError:
            print("\nYou have to provide a valid numeric answer, try again")
    
    if option == 1:
        pass
    else:
        # 2. SAVE PROFILES BEFORE EXIT
        profile_functions.save_profiles(profiles)
        break


print("\nProcess Finished!")