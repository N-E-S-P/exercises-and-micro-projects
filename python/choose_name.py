# write some code that defines a variable, name, and assign to it a string that is your name. If your first name is
# shorter than 5 characters, use your last name. If your last name is also shorter than 5 characters, use the
# combination of you first and last name.


def name_script(first_name, last_name):
    name = first_name + " " + last_name
    if len(first_name) < 5:
        name = last_name
        if len(last_name) < 5:
            name = first_name + " " + last_name
    return name

