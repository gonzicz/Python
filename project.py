import sys

wyrazenie_lista = []
nawias_l = []
OPERATORY = ('+', '-', '*', '%')
POZ_OPER = (('*', '%'), ('-'), ('+'))


def main():
    print("\t\t\t\t\t PROSTY KALKULATOR")
    print("""
    Ten prosty kalkulator wykonuje podstawowe operacje:
    - mnożenie;
    - dzielenie modulo;
    - dodawanie;
    - odejmowanie

    Posiada 'zabezpieczenia':
    - wstawisz dwa operatory obok siebie - wywali błąd i obliczy głupoty
    - zapomnisz nawiasu - wywali błąd

    Jeśli chcesz użyc liczby ujemnej daj ją w nawias.\n""")

    print("\tPrzykład:")
    print("\t 2+2*2 =", end=" ")
    print(zadanie("2+2*2"))
    print("\t(2+2)*2 =", end=" ")
    print(zadanie("(2*2)*2"))
    print("\t(2+2)*2+9%2*8+2-3+(-3) =", end=" ")
    print(zadanie("(2+2)*2+9%2*8+2-3+(-3)"), "\n")
    zadanie_uzytkownika()


def parser(wyrazenie):
    error = 0
    for c in wyrazenie:
        if c == '(':
            error += 1
        elif c == ')':
            error -= 1
    if error != 0:
        sys.exit("Błąd składniowy - brak nawiasu")
    else:
        f_nawias = False
        f_operatora = False
        f_cyfry = False
        for c in wyrazenie:
            try:
                znak = int(c)  # sprawdz czy znak jest cyfrą
                f_operatora = False
                if f_cyfry:  # jeśli jest to kolejna cyfra liczby
                    dodaj_cyfre(znak, f_cyfry, f_nawias)
                else:
                    dodaj_cyfre(znak, f_cyfry, f_nawias)
                    f_cyfry = True
            except ValueError:
                f_cyfry = False  # to jest operator
                if c in OPERATORY:
                    if c == '-' and f_nawias == True:
                        f_operatora = False
                    if f_operatora:
                        sys.exit("NIELEGALNE WYRAŻENIE")
                    else:
                        dodaj_znak(c, f_nawias)
                        f_operatora = True
                if c == '(':
                    f_nawias = True
                if c == ')':
                    f_nawias = False
                    w_nawias()


def oblicz(lista):
    while len(lista) > 1:
        for op in range(len(POZ_OPER)):
            for el in range(len(lista)):
                try:
                    if str(lista[el]) in POZ_OPER[op]:
                        rezultat = operacje(lista, el, lista[el])
                        del lista[el - 1]
                        del lista[el - 1]
                        del lista[el - 1]
                        lista.insert(el - 1, rezultat)
                except IndexError:
                    break
    return lista[0]


def dodaj_cyfre(cyfra, flaga, nawias):
    if nawias == 0:
        if flaga == 0:  # jesli jest to pierwsza cyfra wyrażenia
            wyrazenie_lista.append(cyfra)
        else:
            index = len(wyrazenie_lista)
            liczba = wyrazenie_lista[index - 1] * 10 + cyfra
            wyrazenie_lista.insert(index - 1, liczba)
            del wyrazenie_lista[index]
    else:
        if flaga == 0:
            nawias_l.append(cyfra)
        else:
            index = len(nawias_l)
            liczba = nawias_l[index - 1] * 10 + cyfra
            nawias_l.insert(index - 1, liczba)
            del nawias_l[index]


def dodaj_znak(znak, nawias):
    if nawias == 0:
        if wyrazenie_lista == []: wyrazenie_lista.append(0)
        wyrazenie_lista.append(znak)
    else:
        if nawias_l == []: nawias_l.append(0)
        nawias_l.append(znak)


def operacje(lista, index, op):
    x = lista[index - 1]
    y = lista[index + 1]
    if op == '+':
        x += y
    elif op == '-':
        x -= y
    elif op == '*':
        x *= y
    elif op == '%':
        x %= y
    return x

def w_nawias():
    oblicz(nawias_l)
    wyrazenie_lista.append(nawias_l[0])
    del nawias_l[0]


def zadanie(tekst):
    parser(''.join(tekst.split()))
    wynik = oblicz(wyrazenie_lista)
    wyrazenie_lista.pop()
    return wynik


def zadanie_uzytkownika():
    print("Aby zakończyć wciśnij ENTER")
    uzytkownik = input("wpisz wyrazenie(zatwierdz ENTEREM):")
    while uzytkownik != '':
        print("wynik =", zadanie(uzytkownik))
        uzytkownik = input("wpisz wyrazenie(zatwierdz ENTEREM):")
    if uzytkownik == '':
        print("\nTo już koniec \nDziękuję za zabawe :)")

main()
