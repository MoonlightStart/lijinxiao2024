
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    
    '''method1
    return {index: element for index, element in enumerate(input_list)}
    '''

    '''method2'''
    return_dict = {}
    length = len(input_list)  
    for i in range(length):  
        return_dict[i] = input_list[i]  
    return return_dict



