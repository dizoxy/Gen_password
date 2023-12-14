import random

#Везде будут повторяться символы

#Тут будут все символы
def Full(number,length):

    for n in range(number):
        password1 =''
        for i in range(length):
            chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

#Тут повторяются цифры
def Num(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '1234567890'
            if chars == '':
                password1 += random.choice(chars)
            else:
                password1 += random.choice(chars)

        return password1


#Цифры и буквы
def NumLet(number, length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1


# ТОлько буквы в разных индексах
def LetterFull(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

#Буквы заглавные
def LetterUp(number, length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

# Буквы в нижнем регистре
def LettDuwn(number, length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = 'abcdefghijklnopqrstuvwxyz'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

def Simbol(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '+-/*!&$#?=@<>'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1


def LettUpSimbol(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

def LettDuwnSimbol(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyz'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1


def LettUpNumber(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1


def LettDuwnNumber(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = 'abcdefghijklnopqrstuvwxyz1234567890'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

def NumberSimbols(number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '+-/*!&$#?=@<>1234567890'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1


def FullUpLett (number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1

def LetterFullSimbols (number,length):
    for n in range(number):
        password1 = ''
        for i in range(length):
            chars = '+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz'
            if chars == '':
                password1 += random.choice(chars)

            else:
                password1 += random.choice(chars)
        return password1



# +-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890

print(LetterFull(1,20)+f' -- Только буквы в разных индексах')
print(Full(int(1), int(30)) + f' -- Всё вместе')
print(Num(1,20)+f' -- ТОлько цифры')
print(NumLet(1,20)+f' -- Цифры и буквы')
print(LetterUp(1,20) + f' -- Буквы в верхнем регистре')
print(LettDuwn(1,20) + f' -- Буквы в нижнем регистре')
print(Simbol(1,20) + f' -- Спецсимволы')
print(LettUpSimbol(1,20) + f' -- Спецсимволы и заглавные буквы')
print(LettDuwnSimbol(1,20) + f' -- Спецсимволы и нижний регистр букв')
print(LettUpNumber(1,20) + f' -- Буквы в верхнем регистре и цифры')
print(LettDuwnNumber(1,20) + f' -- Буквы в нижнем регистре и цифры')
print(NumberSimbols(1,20) + f' -- Спецсимволы и цифры')
print(FullUpLett(1,20) + f' -- Спецсимволы, цифры и буквы в верхнем регистр')
print(LetterFullSimbols(1,20) + f' -- Спецсимволы и буквы в разных регистрах')

