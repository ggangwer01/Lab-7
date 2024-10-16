#the authors name are Mac and Gwyneth

def first_letter_k(word):
    if word.startswith('k'):
        return True
    else:
        return False


word_test_4= "zibra"
word_test_5= "kangaroo"

print(first_letter_k("key"))
print(first_letter_k(word_test_4))
print(first_letter_k(word_test_5))

