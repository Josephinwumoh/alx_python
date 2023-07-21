def validate_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check for the presence of uppercase, lowercase letters, and digits
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    # Check for the presence of spaces
    if ' ' in password:
        return False

    # Return True if all conditions are met
    return has_uppercase and has_lowercase and has_digit
