

def cancellation(list, stop_word):
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    output_list = []
    n = len(list)
    for x in range (n):
        if list[x] != stop_word:
            output_list.append(list[x])
        else:
            break

    return output_list


def copy_all_but_skip_word(input_list, skip_word):
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    output_list = []
    n = len(input_list)
    for x in range(n):
        if input_list[x] == skip_word:
            pass
        else:
            output_list.append(input_list[x])
            
    return output_list

def my_average(input_list):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''

    average_result = 0
    n = len(input_list)
    for x in range(n):
        average_result += input_list[x]

    return(average_result/n)
