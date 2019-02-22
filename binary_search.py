# Write the algorithm def binary_search(item, ordered_list, start, end),
# that takes an item to search (i.e. item), an ordered list and a starting and ending positions in the list
# as input, and returns the position of item in the list if it is included in it, and None otherwise. The
# approach implemented by the binary search is described as follows. First, it checks if the middle
# element of the list between start and end (included) is equal to item, and returns its position in
# this case. Otherwise, 1) if the middle element is lesser than item the search is executed in the part
# of the list that follows the middle element, while 2) if the middle element is greater than item the
# search is executed in the part of the list that precedes the middle element.


def binary_search(item, ord_list, start, end):

    if item not in ord_list[start-1:end]:
        return None
    else:
        if item == start:
            return ord_list.index(start)
        elif item == end:
            return ord_list.index(end)
        else:
            middle = ord_list[(len(ord_list[start:end + 1]) // 2)]
            if middle == item:
                return ord_list.index(item)
            elif middle < item:
                middle += 1                                         # else: infinite recursion
                start = middle
                return binary_search(item, ord_list, start, end)
            elif middle > item:
                middle -= 1                                         # else: infinite recursion
                end = middle
                return binary_search(item, ord_list, start, end)


