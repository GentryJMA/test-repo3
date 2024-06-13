def vowel_counter(input_sentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in input_sentence:
        if char in vowels:
            count += 1
        else:
            count += 0
    return count




input_sentence = 'This sentence uses a few vowels '
print(vowel_counter(input_sentence))