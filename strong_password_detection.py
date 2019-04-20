# Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
# password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
# and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.


def strong_password_detection(stringa):
    import re
    good_password = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$')
    password = good_password.search(stringa)
    try:
        if password.group():
            yay = 'Strong password.'
            return yay
    except:
        boo = "Invalid password."
        return boo


