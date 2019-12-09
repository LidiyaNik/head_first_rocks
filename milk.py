
for i in reversed(range(1,20)):
    word = ' '
    if(i<=19) and (i>=11):
        word = ' бутылок '
    else:
        if (i % 10) == 1:
            word = ' бутылка '
        elif i % 10 in (2, 3, 4):
            word = ' бутылки '
    print(str( i ) + word + ' молока на борту.')
    print(str( i ) + word + ' на борту.')
    print('Берешь одну, пускаешь ко дну!')

    if (i-1) == 0:
        print('Нет бутылок молока на борту!')

    else:
            new_word = ' '
            if ((i-1) <= 19) and ((i-1) >= 11):
                new_word = ' бутылок '
            else:
                if ((i-1) % 10) == 1:
                    new_word = ' бутылка '
                elif (i-1) % 10 in (2, 3, 4):
                    new_word = ' бутылки '
                else:
                    new_word = ' бутылок '
            print(str(i-1) + new_word + 'молока на борту!')