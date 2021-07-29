class AnagramChecker:
    def __init__(self) -> None:

        with open('words.txt') as words_file:
            content = words_file.readlines()
            self.words = [line.strip() for line in content]

    def is_valid_word(self, word):
        return word in self.words 

    def __is_anagram_of(self, user_word, other_word) -> bool:
        return sorted(user_word) == sorted(other_word)

    def get_anagrams(self, user_word):
        anagrams = []

        for dict_word in self.words:
            if (self.__is_anagram_of(user_word, dict_word)) and (user_word != dict_word):
                anagrams.append(dict_word)

        return anagrams