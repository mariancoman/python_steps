import random
import time

# pachetul de carti (D), cartile date initial jucatorului(J) si dealerului(D)
A =[2,3,4,5,6,7,8,9,10,'A','J','Q','K']
P = A * 4
J = []
D = []
r = 1


def initializare():

    # imparte cartile j-JUCATOR d-DEALER

    while len(J) <= 1:

        a = random.randint(0, len(P)-1)
        J.append(P[a])
        P.pop(a)

    while len(D) <= 1:

        a = random.randint(0, len(P)-1)
        D.append(P[a])
        P.pop(a)

    print(J,D)
    pass


def numar(m):

    # converteste cartea in valoare numerica ( A = 10 )

    t = 0

    if m in ('J','Q','K'):
        t = t + 10
    elif m == 'A':
        t=t+10
    else:
        t=t+m
    return t


def numar_asi(M):

    # afla cati asi sunt extrasi de unul din jucatori

    n = 0

    for i in M:
        if i == 'A':
            n += 1
    return n


def suma(M):

    # insumeaza catile unui jucator ( tine cont si de asi)
    t = 0
    for i in M:
        t = t+numar(i)

    n = numar_asi(M)            # valorifica asii:
    while (n>0) and (t > 21):
        t = t-9
        n = n-1

    return t


def afisare_carti(M):

    # mod 'mai elegant' de a afisa cartile

    c = ''
    for i in M:
        if i in range(1,11):
            c = c + '['+ str(i) + ']'
        else:
            c = c + '['+ i + ']'
    return c


def afisare_situatie():

    # afisaza situatia cartilor pe fata

    print('PLAYER:', afisare_carti(J), '__SUM:', suma(J))
    print('DEALER:', afisare_carti(D), '__SUM:', suma(D))
    pass

def afisare_runda_jucator():

    # runda de joc in care jucatorul nu vede cartea a doua a dealerului

    global r

    print('PLAYER', afisare_carti(J), '__SUM:', suma(J))
    print('DEALER: ['+str(D[0])+'][X]')
    r = int(input('WHAT NOW? HIT: 1 STAY: 0'))
    if r == 1:
        time.sleep(2)
        a = random.randint(0, len(P)-1)
        J.append(P[a])
        P.pop(a)
    elif r == 0:
        print('PLAYER STOPS AT:', suma(J))
        time.sleep(1.5)
        print('DEALER CARDS:', afisare_carti(D), '__SUM:', suma(D))
        time.sleep(1.5)
        r = 0

def afisare_runda_dealer():

    # runda de joc in care dealerul incearca sa bata scorul jucatorului

    while suma(D)<21 and suma(D)<suma(J):
        time.sleep(2)
        a = random.randint(0, len(P) - 1)
        D.append(P[a])
        P.pop(a)
        afisare_situatie()

def concluzii():

    # interpretarea rezultatelor

    if suma(D)>21:
        print('DEALER BUSTS')
    elif suma(D) == suma(J):
        print('TIE')
    elif suma(D) > suma(J):
        print('DEALER WINS')
    else:
        print('PLAYER WINS')


initializare()

while r == 1:                            # e variabila care zice daca mai vrea sa joace

    afisare_runda_jucator()
    if suma(J) > 21:                     # daca suma cartilor jucatorului e peste 21 nu mai are rost
        afisare_situatie()
        print('PLAYER BUSTS')
        r = 0

if suma(D) <= 21 and suma(J) <= 21:      # de aici se joaca cu cartile ''
    afisare_situatie()
    afisare_runda_dealer()

    concluzii()
