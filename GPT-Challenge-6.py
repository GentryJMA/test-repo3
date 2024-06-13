def list_reversal(input_list):

    new_list = []

    for element in input_list:
        new_list.append(element)
    new_list = new_list[::-1]

    return new_list



input_list = [1,2,3,4,5,6,7,8,9,10]
print(list_reversal(input_list))