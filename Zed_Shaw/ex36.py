from sys import exit

def childhood_diary():
    print('Blurred it is')

def impostor_me_what():
    print('I want something else, PLEASE!!!!')
    print('This is how I feel most of the time...')
    print('Is this impostor though? Don\'t think so, aah am blabbering again!')
    print('Sorry, this is kinda boring, let\'s go back?')
    start()

def today():
    fast = True
    print(f'I am happy coz fast is {fast} today!')

def read_now():
    f = open('aditi_.txt')
    print(f.read())

def start():
    print('Hey there! Welcome :)')
    print('In this game, Imma tell you about me.')
    print('My childhood seems ... wanna know?')
    print('I also seem to have impostor syndrome.')

    print('Anyway, what do you wanna know about?')
    print('Or you could just ask me about today!')
    print('Or we could read from a file.')
    choice = input('> ')

    if choice == 'childhood':
        childhood_diary()
    elif choice == 'impostor':
        impostor_me_what()
    elif choice == 'today':
        today()
    elif choice == 'file':
        read_now()
    else:
        print('you really wanna go away or was that a typing error?')
        print('imma assume error, and you just as clumsy as me! L.O.L')
        print('k, bye!')
        exit(0)


start()
