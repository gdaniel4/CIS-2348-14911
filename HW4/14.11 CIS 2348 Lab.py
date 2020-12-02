# Gabriel Daniels
# PSID 1856516


# numbers are entered as 'one' and split into individual intergers


def selection_sort_descend_trace(numbers):
    # i meaning index, hence the '-1' inside the len() function
    for i in range(len(numbers) - 1):
        # Find index of largest element
        max_num = i
        # starts at index of the number right next to max_num at every iteration of the
        # outer loop
        for j in range(i + 1, len(numbers)):
            # if number next to max_num > max_num, indexes switch
            if numbers[j] > numbers[max_num]:
                max_num = j

        # Swap numbers[i] and numbers[max_num]
        temp = numbers[i]
        numbers[i] = numbers[max_num]
        numbers[max_num] = temp

        # turns all intergers in numbers into individual strings
        # joins strings of numbers with space in between each interger
        x = ' '.join([str(num) for num in numbers])
        # print concatenated strings with space at the end of the whole list
        print(x + ' ')


if __name__ == '__main__':
    # list numbers = [] turns every string created from split into
    # integers in list
    numbers = [int(num) for num in input().split()]
    selection_sort_descend_trace(numbers)


