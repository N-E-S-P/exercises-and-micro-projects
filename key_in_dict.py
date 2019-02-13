def key_in_dict(dictionary, key_list):
    result = set()
    for x in key_list:
        if x in dictionary.keys():
            result.add(dictionary[x])
    return result

