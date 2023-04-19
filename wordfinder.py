"""get choice from random libraries"""
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,wf_file):
        """get the file link for the Dic"""
        self.wf_file = wf_file
        self.word_list = self.import_list()
        print(f"{len(self.word_list)} words read")

    def import_list(self):
        """import all the words in the file"""
        import_file = open(self.wf_file,"r")
        return import_file.readlines()

    def random(self):
        """get random word from the import file"""
        # print(choice(self.word_list))
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):

    def __init__(self,wf_file):
        """get list form super class"""
        super().__init__(wf_file)
        self.word_list = self.remove_special_char()

    def remove_special_char(self):
        """remove special char"""
        final_list = []
        new_list = [word for word in self.word_list if not word.startswith("#") and not word.isspace()]

        for item in new_list:
            final_list.append(item.strip())
        return final_list





