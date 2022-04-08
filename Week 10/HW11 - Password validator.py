def validate_password(password, min_length = 8, min_uppers = 1, min_lowers = 1, min_numbers = 1, min_specials = 1):
    # Function to validate a given password. Parameters can be given when the function is called, otherwise
    # default values will be used
    # 
    # This functions returns to value. a bool of whether the password was valid, and a string containing the reason or reasons why the password was invalid    
    length = len(password)

    numbers = 0
    alphas = 0
    uppercases = 0
    lowercases = 0
    specials = 0

    for character in password:
        if character.isdigit():
            #print(character, "digit")
            numbers += 1
        elif character.isalpha():
            alphas += 1
            if character.isupper():
                #print(character, "uppercare alpha")
                uppercases += 1
            else:
                #print(character, "lowercase alpha")
                lowercases += 1
        else:
            #print(character, "punctuation")
            specials += 1

    # If statements no longer nested to be able to return multiple errors at once.


    # If any issues with the password are found, set valid to false and add the reason to the error string
    valid = True
    error = ""
    if length < min_length:
        valid = False
        error += "not long enough. "

    if uppercases < min_uppers:
        valid = False
        error += "not enough uppercases. "

    if lowercases < min_lowers:
        valid = False
        error += "not enough lowercases. "

    if numbers < min_numbers:
        valid = False
        error += "not enough numbers. "

    if specials < min_specials:
        valid = False
        error += "not enough special characters. "
        
    # Return bool for valid or not and the string containing the reason for the error, if there was one
    return valid, error

def main():
    while True:
        print("Enter password. Enter Q to cancel.")
        password = input(">")

        # Cancel if user enters "Q"
        if password == "Q":
            print("Cancelling...")
            break

        is_valid, error = validate_password(password)
        if is_valid:
            # If password is valid, break loop
            print("Password is valid.")
            break
        else:
            # If password is invalid, tell user why
            print("Invalid password. Reason:", error)


main()