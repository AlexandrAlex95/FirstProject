def tasks():
    def lesson1():
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        for i in a:
            if i < 5:
                print(i, end="")
        print()
    lesson1()
    def lesson2():
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        spisok = []
        for i in a:
            for g in b:
                if i == g:
                    spisok.append(i)
        print(spisok)
        print()
    lesson2()

    def lesson3():
        a = {'Alan','James','Tom','Mikle','Jhon'}
        print(sorted(a))
        print(sorted(a,reverse= True))
    lesson3()

    def lesson4():
        super_list = input("input numbers,for ended write : ").split(" ")
        for i in super_list:
            int(i)
        for i in range(len(super_list)):
            if super_list.count(super_list[i]) >= 2:
                print(super_list[i], "не уникальны")
                continue
            print(super_list[i], "уникальна")
    lesson4()

    def lesson5():
        my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
        keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
        print(keys)
    lesson5()
    def lesson6():
        a = input('input number: ')
        print(int(a,16))
    lesson6()

    def lesson8():
        x = input('input world: ')
        if x == ''.join(reversed(x)):
            print(x)
        else:
            print('world non polindrom')
    lesson8()

    def lesson9():
        seconds = int(input('input seconds: '))
        days = seconds // (24 * 3600)
        seconds %= 24 * 3600
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        print(f'{days}:{hours}:{minutes}:{seconds}')
    lesson9()

    def lesson10():
        numbers = input('input numbers: ')
        x = numbers.split(',')
        b = list(x)
        c = tuple(x)
        print(b)
        print(c)
    lesson10()

    def lesson11():
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        print(a[0],a[-1])
    lesson11()

    def lesson13():
        n = int(input('number n: '))
        n2 = n ** 2
        n3 = n ** 3
        na = n + n2 + n3
        print(na)
    lesson13()

    def lesson14():
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,224,237,1,3,4,7]
        for i in a:
            if i == 237:
                break
            if i%2 == 0:
                print(i,end=" ")
    lesson14()

    def lesson15():
        a = [1,2,3,6,8]
        b = [6,6,7,1]
        for i in a:
            if i not in b:
                print(i,end=' ')
    lesson15()

    def lesson17():
        number = int(input('input number: '))
        i = 0
        while number > 0:
            x = number % 10
            number = number // 10
            i += x
        print(i)
    lesson17()

    def lesson18():
        x = input('input worlds: ')
        print(x.count(input('input latters: ')))
    lesson18()

    def lesson19():
        x = 1
        y = 2
        x,y = y,x
        print(x,y)
    lesson19()

    def lesson20():
        tupled = (
            {1: 'Tom', 2: 'Jane', 3: 'Bob'},
            {'number': '+784792', 'home': '2', 'street': 'mira'},
            {10: 'car', 4: 'travel', 7: 1, 30: 2}
              )

        super_dict = {}
        for i in tupled:
            for k,v in i.items():
                if super_dict.get(k) is None:
                    super_dict[k] = []
                if v not in super_dict.get(k):
                    super_dict[k].append(v)
        print(super_dict)
    lesson20()

    def lesson21():
        string1 = "ipsum dolor sit amet, dolor ipsum consectetur ipsum adipisicing elit. Adipisci alias animi atque aut corporis" \
                  "doloremque dolor dolores excepturi in ipsum ipsum" \
                  "incidunt minus numquam, dolor Lorem perferendis dolor quasi dolor quibusdam sunt temporibus, totam velit voluptas voluptates!".lower().split(
            " ")

        def most_frequent(list):
            counter = 0
            num = list[0]
            for i in list:
                cirr = list.count(i)
                if cirr > counter:
                    counter = cirr
                    num = i
            return num

        print(most_frequent(string1))

        string2 = "ipsum dolor sit amet, dolor ipsum consectetur ipsum adipisicing elit Adipiscicmdkcm alias animi atque aut corporis doloremque dolor dolores excepturi in ipsum ipsum incidunt minus numquam, dolor Lorem perferendis dolor quasi dolor quibusdam sunt temporibus, totam velit voluptas voluptates".split(
            " ")

        def most_length_word():
            maxSTR = ""
            count12 = 0
            for elem in string2:
                count11 = 0
                for k in elem:
                    count11 += 1
                    if count11 > count12:
                        count12 = count11
                        maxSTR = elem
            print(maxSTR)

        most_length_word()

    lesson21()

    def lesson24():
        x = {}
        for i in range(int(input('input quantity of countries: '))):
            country,*cites = input('input country and her cites: ').split()
            for j in cites:
                x[j] = country
        print(*(x[input('input name cites: ')] for _ in range(int(input('input quantity of cites: ')))), sep="\n")
    lesson24()




