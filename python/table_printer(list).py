# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table
# with each column right-justified. Assume that all the inner lists will contain the same number of strings.


# example of input_list
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# actual algorithm -ad hoc for 3 columns, not generalized... :(
def table_printer(input_list):

    col_widths = [len(max(x, key=len)) for x in input_list]

    print('TABLE'.center(sum(col_widths) + max(col_widths), '='))

    for elem_1, elem_2, elem_3 in zip(*input_list):
        print(elem_1.rjust(max(col_widths)), elem_2.rjust(max(col_widths)), elem_3.rjust(max(col_widths)))

    return '='.center(sum(col_widths) + max(col_widths), '=')

