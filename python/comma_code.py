# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
# and a space, with and inserted before the last item.


def comma_code(list_value):
    new_list = []
    for item in list_value[0:-2]:
        new_list.append(str(item))
    new_list = [", ".join(new_list)]
    new_list = new_list + [str(list_value[-2]).strip(',')]
    new_list = [", ".join(new_list)]
    new_list = new_list + ['and ' + str(list_value[-1])]
    new_list = [" ".join(new_list)]
    return new_list

