consonant = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "Y", "V", "X", "Z")
vowel = ("A", "E", "I", "O", "U")

x = input("Enter the word: ")

f_letter = x[0]
f_Str_letter = str(f_letter)
f_CStr_letter = f_Str_letter.upper()

if f_CStr_letter in consonant:
    print("The word", x, "is a consonant")
    word_length = len(x)
    remove_fletter = x[1 : word_length]
    pig_latin = remove_fletter + f_CStr_letter + "ay"
    print("The word entered in Pig Latin is: ", pig_latin)
elif f_CStr_letter in vowel:
    print("The word", x, "is a vowel")
    pig_latin = x + "way"
    print("The word entered in Pig Latin is: ", pig_latin)
else:
    print("Invalid enter")

