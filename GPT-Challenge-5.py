def consonant_counter(input_sentence):
    
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for char in input_sentence:
        if char in consonants:
            count += 1
    return count

input_sentence = "This is a sentence"
print(consonant_counter(input_sentence))