def writefile(*param):
    with open("../homeWorks/mainText.txt", "a") as file:
        for i in param:
            print(i, file=file, end=" ")



def program1():
    lists = [1,3,5,5,3,3,1]
    number = int(input('input a number to check: '))
    times = int(input('how many times the number should be repeated: '))
    count = [0] * 6
    for i in lists:
        count[i] += 1
    for i in range(6):
        if i == number:
            if count[i] == times:
                print(lists, number, times, True)
                writefile('answer first program: ',number, times, True, '\n')
            else:
                print(lists, number, times, False)
                writefile('answer first program: ',number, times, False, '\n')


def program2():
    world = list(input('input word: '))
    letters = [0]*26
    for i in world:
        i = i.lower()
        number = ord(i) - 97
        letters[number] =+ 1
    for i in range(26):
        if letters[i] == 0:
            print(chr(i+97),end='')
        writefile('answer second program: ', chr(i+97), '\n')

def program3():
    x = int(input('input x: '))
    b = int(input('input b: '))
    writefile('answer fourth program: ', x > b)
    return x > b


def program4():
    katet = int(input('input katet: '))
    gipotenuza = katet / 0.5
    katet2 = round(((gipotenuza ** 2 - katet ** 2) ** 0.5), 1)
    print('gipotenuza =',katet2)
    writefile('answer fourth program: gipotenuza =',katet2)


def program5():
    nameis = input('input first and second name: ')
    writefile(' '.join(reversed(nameis.split())))
    return ' '.join(reversed(nameis.split()))

def program6():
    number_left = list(map(int,input('input turn left ').split()))
    number_right = list(map(int,input('input turn right ').split()))
    sum_left = ((sum(number_left)) // 4)
    sum_right = ((sum(number_right)) // 4)
    if sum_left > sum_right:
        turn = sum_left - sum_right
        print('answer sixth program: ',turn, 'full turn left')
    elif sum_left < sum_right:
        turn = sum_right - sum_left
        print(turn, 'full turn right')
        writefile('answer sixth program: ',turn, 'full turn right')
    else:
        print('0 turn')
        writefile('answer sixth program: ','0 turn')

def program7():
    number = int(input('input number: '))
    import random
    return random.randint(0, number - 1)

def program8():
    summa_vklada = float(input('input the amount of the deposit: '))
    srok = int(input('input the term of the deposit in months: '))
    x = 1
    procent = 7 / 100
    while x <= srok:
        summa_vklada += summa_vklada * procent
        x += 1
        print('after', srok, 'months deposit amount will be', round(summa_vklada, 4))
        writefile('answer eighth program: after', srok, 'months deposit amount will be', round(summa_vklada, 4))
        return summa_vklada

def program9():
    number1 = int(input('input number 1: '))
    number2 = int(input('input number 2: '))
    x = number2 * number1
    print(x)
    writefile('answer ninth program: ',x)
    return x


def program10():
    x = int(input('input number of number: '))
    f1 = 0
    f2 = 1
    print(f1, f2, end=' ')
    for i in range (2,x):
        f1, f2 = f2, f1 + f2
        x -= 1
        print(f2, end=' ')

def program11():
    member = int(input('input a member of the progression: '))
    ariphmetic = int(input('input the difference of ariphmetic progression: '))
    ordinal = int(input('input  the ordinal number of a member of the progression: '))
    for i in range(1,ordinal+1):
        member =+ member + ariphmetic
    print(member)
    writefile('answer eleventh program: ',member)


def program12():
    hight = int(input('input the height of the isosceles triangle: '))
    number = hight - ( hight - 1 )
    for i in range(hight+1):
        value1 = hight - 1 - i
        value2 = hight - 1 + i
        value3 = number - 1 + i
        for j in range(value2):
            print(value3 if j > value1 else ' ', end=' ')
        print()

def program13():
    number = int(input('input the height of the triangle: '))
    a = []
    for i in range(number + 1):
        a.append([1]+[0]*number)
    for i in range(1,number +1):
        for j in range(1, i+1):
            a[i][j]=a[i-1][j]+a[i-1][j-1]
    for i in range(0,number+1):
        for j in range(0,i+1):
            print(a[i][j],end=' ')
            writefile(a[i][j])
        print()
        writefile('\n')

#
def program14():
    number = int(input('input number: '))
    stepen = 4
    degree = int(input('input degree of number: '))
    for i in range(stepen):
        number **= degree
    print(number)
    writefile('answer fourteenth program: ',number)
