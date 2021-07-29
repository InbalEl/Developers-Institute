from anagram_checker import AnagramChecker

def is_valid_input(user_input: str):
    user_input = user_input.strip()
    return user_input.isalpha() and (len(user_input.split()) == 1)
        

def display_anagrams(user_input, anagrams):
    print(f'Your word was: {user_input}, which is a valid word')
    print('The anagrams for your word are:')
    for anagram in anagrams:
        print(anagram)

def main():
    new_checker = AnagramChecker()
    prompt_str = 'Enter a word to check or q to quit: '
    user_input = input(prompt_str)

    while user_input != 'q':
        
        if is_valid_input(user_input):
            user_input = user_input.upper()
            new_checker.is_valid_word(user_input)
            anagrams = new_checker.get_anagrams(user_input)
            display_anagrams(user_input, anagrams)
        
        else:
            print('Invalid input')
        
        user_input = input(prompt_str)
    


if __name__ == '__main__':
    main()