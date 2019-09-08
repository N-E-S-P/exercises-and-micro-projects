# Write the algorithm def bubble_sort(input_list) that takes an unordered list as input and returns it ordered. The
# idea behind the bubble sort is the following one: at every step of the algorithm, it compares a pair of adjacent
# items. If they are in the right order, analyses the next pair directly, otherwise it swaps them before analysing
# the following pair. The algorithm stops after having compared all the pairs in the list twice, so as to be sure
# that all of them have been put in the right position.


def bubble_sort(input_list):

    for x in input_list:
        for i in range(len(input_list) - 1):                                    # - 1 is necessary, else: LIOoR error!
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]

    return input_list

