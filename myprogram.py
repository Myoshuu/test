def Main():
    print(' ') #space
    print('Welcome to my Menu Program')
    print('--------------------------')
    print('1. Calculator')
    print('--------------------------')

    opt = input('Choose the menu number : ')
    def Selection():
        if opt == '1':
            def nameSelection():
                name = input('What is your name : ')
                if name == 'user':
                    from subprocess import call
                    call(['python', 'calculator.py'])
            nameSelection()
    Selection()    
Main()