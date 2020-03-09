loc_ics = []
loc_zer = []
curent=[0,'X']


def adaugare(num,loc):
    # adauga "loc" in lista de locatii ics (num = 1) /zer (num = 0)
    if num == 1:
        loc_ics.append(loc)
    else:
        loc_zer.append(loc)


def imprimare(rand, spa_ics, spa_zer):

    M = ['NUL', '  ', '  ', '  ']
    c = ''
    for i in range(rand*3-2, rand*3+1):
        if i in spa_ics:
            M[i-((rand-1)*3)] = '><'
        elif i in spa_zer:
            M[i-((rand-1)*3)] = '()'
    c = c + M[1]+'|'+M[2]+'|'+M[3]

    return c


def linie():
    #   imprima linia de separator
    return '--+--+--'


def plotare(loc_ics,loc_zer):
    # imprima tabelul in functie de starea actuala
    print('      ')
    print(imprimare(1, loc_ics, loc_zer))
    print(linie())
    print(imprimare(2, loc_ics, loc_zer))
    print(linie())
    print(imprimare(3, loc_ics, loc_zer))


def victorie(spa_ics,spa_zer):
    # afla daca exista vr-un castigator

    t = 'nimeni'
    vic = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    suma = spa_ics + spa_zer
    tot = [1,2,3,4,5,6,7,8,9]

    for v in vic:
        if set(v).issubset(set(spa_ics)):
            t = 'felicitari X, ai castigat!'
        elif set(v).issubset(set(spa_zer)):
            t = 'felicitari ZERO, ai castigat!'

    if set(tot).issubset(set(suma)):
        t = 'REMIZA!'

    return t


def main():

    primu = ''

    while primu not in ['x','X',0]:

         primu = input(print('salut! Hai sa jucam. cu ce vrei sa fi X/0 ?'))

    if primu == 'X' or primu == 'x':
        print('vei juca cu X')
        c = 1
    elif primu == '0':
        print('vei juca cu 0')
        c = 0
    else:
        print('acesta nu e un argument valid')
        pass

    plotare(loc_ics, loc_zer)

    while victorie(loc_ics,loc_zer) == 'nimeni':
            try:
                m = int(input(print('jucator cu', curent[c], ', unde vrei sa pui?')))
            except ValueError:
                print("The input was not a valid integer")

            if m not in loc_ics and m not in loc_zer and m in range(1,10):
                adaugare(c,m)
            else:
                print('locul e ocupat sau nu exista, mai gandeste-te')
                c = (c + 1) % 2  # schimba X/0
            c = (c+1) % 2  # schimba X/0
            plotare(loc_ics,loc_zer)

    print(' ')
    print(victorie(loc_ics,loc_zer))


main()
