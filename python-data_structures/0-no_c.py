def no_c(my_string):
    result = []


    for char in my_string:
        if char != 'c' and char != 'C':

            result.append(char)

    new_string = ''.join(result)

    return new_string