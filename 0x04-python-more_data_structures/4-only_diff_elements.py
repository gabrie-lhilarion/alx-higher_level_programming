def only_diff_elements(set_1, set_2):
    
    result_set = set()

   
    for element in set_1:
       
        if element not in set_2:
            result_set.add(element)

    
    for element in set_2:
       
        if element not in set_1:
            result_set.add(element)

    return result_set

