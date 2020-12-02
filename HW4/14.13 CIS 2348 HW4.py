# Gabriel Daniels
# PSID: 1856516

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary


def partition(user_ids, i, k):
    # picking middle element as pivot
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]
    # variables
    done = False
    l = i
    h = k
    while not done:
        # increment l while user_ids[l] is less than pivot
        while user_ids[l] < pivot:
            l = l + 1
        # decrement h while user_ids[h] is greater than pivot
        while pivot < user_ids[h]:
            h = h - 1
        """  If there are zero or one items remaining,
                      all ids are partitioned. Return h """
        if l >= h:
            done = True
        else:
            # swap user_ids[l] with user_ids[h]
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            # update l and h
            l = l + 1
            h = h - 1
    return h


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called


def quicksort(user_ids, i, k):
    # had to make sure variable was referring to global variable at the top
    # of the code
    global num_calls
    # increments num_calls everytime function is called
    num_calls += 1
    # sets pivot as int 0
    pivot = 0
    # if there are one or zero items to sort, partition is already sorted
    if i >= k:
        return
    # call partition function, pivot is from last item of low partition
    pivot = partition(user_ids, i, k)
    # sorts low and high partition
    quicksort(user_ids, i, pivot)
    quicksort(user_ids, pivot + 1, k)
    return


if __name__ == "__main__":
    # user_ids assigned to empty list
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
