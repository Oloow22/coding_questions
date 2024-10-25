def sort_list(input_list):
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    
    return sorted_list


input_list = [5, 2, 8, 2, 1, 9, 4, 7, 6, 3, 6, 8]
print("Input List:", input_list)

sorted_list = sort_list(input_list)
print("Sorted List without Duplicates:", sorted_list)