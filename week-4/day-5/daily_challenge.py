def sort_words(s):
    word_list = s.split(',')
    word_list.sort()
    return ','.join(word_list)

def sort_words_list_comp(s):
    words = []

print('input: without,hello,bag,world')
print(f'output:{sort_words("without,hello,bag,world")}')