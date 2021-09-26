"""
Palindrome class realization.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack


class Palindrome:
    """
    Palindrom finding class.
    """

    @staticmethod
    def read_file(file_r):
        """
        Method which reades file
        """
        with open(file_r, encoding="utf-8") as file:
            words_list = []
            if "txt" in file_r:
                split_part = "\n"
            else:
                split_part = " "
            for i in file:
                if not i.startswith(" +cs="):
                    i = i.split(split_part)
                    words_list.append(i[0])
        return words_list

    def find_palindromes(self, file, file_name):
        """
        method which finds palindroms.
        """
        words_list = self.read_file(file)
        stack = ArrayStack()
        result = []
        for word in words_list:
            word_len = len(word)
            if word_len == 1.0:
                result.append(word)
            else:
                word_mid = word_len // 2
                middle = word_len % 2
                for i in range(word_len):
                    if i < word_mid:
                        stack.push(word[i])
                    elif middle == 1 and i == word_mid:
                        continue
                    else:
                        if stack.pop() != word[i]:
                            check = False
                            break
                        check = True
                if check is True:
                    result.append(word)
        self.write_to_file(result, file_name)
        return result

    @staticmethod
    def write_to_file(words_list, file_name):
        """
        Method which writes info into the file.
        """
        file = open(file_name, 'w', encoding="utf-8")
        for i in words_list:
            file.write(i + "\n")
        file.close()


x = "x\n"
print(x[:-1])
print(x.split("\n")[0])
