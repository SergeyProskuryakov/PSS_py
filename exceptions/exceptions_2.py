# Программа спрашивает год рождения. Необходимо учесть, что помимо
# года рождения может быть введён любой мусор. Дождаться корректного ввода, не используя функцию isdigit

god_rojdeniya = None
while god_rojdeniya == None:
    try:
        god_rojdeniya = input('введите год рождения: ')
    except:
        print('год рождения нужно вводить числами!')
