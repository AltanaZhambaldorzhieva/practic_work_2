country = input('Введите название страны: ')
word = country.split()
if len(word) == 2:
    print(word[0], word[1], sep='\n')


