'''
(Q) - A function to read a file and count the frequency of each word
'''

def count_word(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"\'')
                word_count[word] = word_count.get(word,0) + 1
    return word_count

file_path = "coding-questions/count_frequency_word.txt"
print(count_word(file_path))