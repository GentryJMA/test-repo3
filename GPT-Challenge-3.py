#reverses words in a sentence

def reverse_worder(normal_sentence):
    
    sentence_list = normal_sentence.split()
    reverse_sentence = sentence_list[::-1]
    reverse_sentence = ' '.join(reverse_sentence)
    
    
    return reverse_sentence

normal_sentence = 'This sentence isnt normal' 

print(reverse_worder(normal_sentence))