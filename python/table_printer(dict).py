
def table_printer(dictionary):
    longest_item = 0
    for item in dictionary:
        if len(item) > longest_item:
            longest_item = len(item)
    print('TABLE'.center(longest_item + longest_item * 2, '='))
    for item, amount in dictionary.items():
        print(item.ljust(longest_item) + str(amount).rjust((longest_item * 2)))
    return '='.center(longest_item + longest_item * 2, '=')
