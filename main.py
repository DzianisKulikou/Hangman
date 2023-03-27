from word_list import *


guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов
tries = 6
flag_start = 'да'

print('Здравствуйте, давайте сыграем в палача!')


def checking_letters(let):  # Проверки правельности ввода
    x1 = let
    letter = x1
    while letter > '':
        c = letter[-1]
        if 1040 > ord(c) or ord(c) > 1071:
            x1 = input('Вы ввели не допустимые символы, попробуйте ещё раз: ')
            x1 = x1.upper()
            letter = x1
        else:
            letter = letter[:-1]
    return x1


def play(word):
    global flag_start, tries, guessed_letters, guessed_words, word_completion
    while tries > 0:
        print(display_hangman(tries))
        print('У вас есть', tries, 'попыток, чтоб угадать загаданное слово')
        print(word_completion)
        letter = input('Назовите букву или слово целиком: ')
        letter = letter.upper()
        let1 = checking_letters(letter)
        if len(let1) > 1:  # Проверка на слово
            if let1 in guessed_words:
                print('Вы уже называли это слово!')
            elif let1 == word:
                print('Поздравляю, вы совершенно верно назвали слово!')
                flag_start = input('Хотите ли сыграть ещё раз? (да/нет): ')
                tries = 6
                guessed_letters = []
                guessed_words = []
                break
            else:
                guessed_words.append(let1)
                print('Вы неправильно назвали слово!')
                tries -= 1
        else:  # Проверка на букву
            if let1 in guessed_letters:
                print('Вы уже называли этe букву!')
            else:
                for i in range(len(word)):
                    if let1 == word[i]:
                        print('Вы угадали букву!')
                        guessed_letters.append(let1)
                        word_completion = word_completion[:i] + let1 + word_completion[i+1:]
                        if '_' not in word_completion:
                            print('Поздравляю, вы совершенно верно угадали слово!')
                            flag_start = input('Хотите ли сыграть ещё раз? (да/нет): ')
                            tries = 6
                            guessed_letters = []
                            guessed_words = []
                if let1 not in word:
                    print('Вы не угадали букву!')
                    guessed_letters.append(let1)
                    tries -= 1
    if tries == 0:
        print(display_hangman(tries))
        print('Вам не удалось угадать слово, и вы были повешены!')
        print('Ваше загаданное слово было:', word)
        flag_start = input('Хотите ли сыграть ещё раз? (да/нет): ')
        tries = 6
        guessed_letters = []
        guessed_words = []


while flag_start.lower() == 'да':
    word = get_word()
    word_completion = '_' * len(word)
    play(word)

print('До скорых встреч!')
