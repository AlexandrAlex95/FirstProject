import functions
import myProjectForGithub.tasks
while True:
    try:
        your_name = input('input your name: ')
        if your_name.isnumeric():
            print("input name string")
            functions.writefile(" user name incorrect",your_name,"\n")
        elif your_name.isalpha():
            functions.writefile(" user name: ",your_name,"\n")
            def alll():
                while True:
                    try:
                        print('program name:'
                        '\n1. checking the repetition of a number from the list [1,3,5,5,3,3,1]'
                        '\n2. displays letters that are not in the input word'
                        '\n3. comparison x>b'
                        '\n4. finding the gipotrnuza of a triangle by its leg'
                        '\n5. changes the sequence of the name'
                        '\n6. counts the number of full movers'
                        '\n7. output of a random number'
                        '\n8. calculation of the deposit amount  (7%)'
                        '\n9. multiplication'
                        '\n10. fibonacci'
                        '\n11. arithmetic progression'
                        '\n12. triangle with the height H'
                        '\n13. pascal triangle'
                        '\n14. tetration '
                        '\n15. tasks'
                        '\n0. exit')

                        programm_name = int(input('input number the program do you need? '))
                        print('Hello', your_name, 'you chose program number', programm_name, '\n')
                        functions.writefile('number the program: ',programm_name,"\n")
                        def pr1():
                            if programm_name == 1:
                                while True:
                                    try:
                                        functions.program1()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 2
                            elif programm_name == 2:
                                while True:
                                    try:
                                        functions.program2()
                                    except Exception:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 3
                            elif programm_name == 3:
                                while True:
                                    try:
                                        print(functions.program3())
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 4
                            elif programm_name == 4:
                                while True:
                                    try:
                                        print(functions.program4())
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 5
                            elif programm_name == 5:
                                while True:
                                    try:
                                        print(functions.program5())
                                    except Exception:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 6
                            elif programm_name == 6:
                                while True:
                                    try:
                                        functions.program6()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 7
                            elif programm_name == 7:
                                while True:
                                    try:
                                        print(functions.program7())
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 8
                            elif programm_name == 8:
                                while True:
                                    try:
                                        functions.program8()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 9
                            elif programm_name == 9:
                                while True:
                                    try:
                                        functions.program9()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 10
                            elif programm_name == 10:
                                while True:
                                    try:
                                        functions.program10()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 11
                            elif programm_name == 11:
                                while True:
                                    try:
                                        functions.program11()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 12
                            elif programm_name == 12:
                                while True:
                                    try:
                                        functions.program12()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 13
                            elif programm_name == 13:
                                while True:
                                    try:
                                        functions.program13()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
                            # 14
                            elif programm_name == 14:
                                while True:
                                    try:
                                        functions.program14()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')
        #15
                            elif programm_name == 15:
                                while True:
                                    try:
                                        myProjectForGithub.tasks.tasks()
                                    except ValueError as c:
                                        print("ERROR! You can not input letters and any symbols!")
                                        functions.writefile('ERROR! Input letters or any symbols!\n')
                                    while True:
                                        try:
                                            doing = int(input('\nrepit program? \n0 - repit program \n1 - restart full session \n2 or any number- exit \n'))
                                            functions.writefile('action after the end of the program: ', doing,'\n')
                                            if doing == 0:
                                                pr1()
                                            elif doing == 1:
                                                alll()
                                            elif doing == 2:
                                                exit()
                                        except ValueError as c:
                                            print("ERROR! You can not input letters and any symbols!")
                                            functions.writefile('ERROR! Input letters or any symbols!\n')('ERROR! Input letters or any symbols!\n')
                            elif programm_name == 0:
                                functions.writefile('exit the program!\n')
                                exit()
                            # finish
                            else:
                                print('but program', programm_name, 'dont exist, so choose another program!')
                                functions.writefile('non-existent program\n')
                            return alll()
                        pr1()
                    except ValueError:
                        print("incorrect value, please try again")
                        functions.writefile('incorrect value!\n')
            alll()
        else:
            print("symbols can not be entered!")
            functions.writefile('enter symbols!\n')
    except Exception as ex :
        print("\ninput correct value \n",ex)
        functions.writefile('incorrect value!\n')
    except KeyboardInterrupt:
        print("Have a good Day")
