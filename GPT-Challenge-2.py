#Word Counter

def word_counter(text):
    count = 0
    words = text.split()
    
    for word in words:
        count = len(words)

    return count



text = str('Woah Thats Crazy Its counting the words im ')
print(word_counter(text))