#Character Counter

def character_counter(counted_string):

    count = 0
    for character in counted_string:
        count += 1  

    return count

counted_string = str(input('Input Text: '))

print(character_counter(counted_string))