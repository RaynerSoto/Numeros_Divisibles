import Divisibles
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    Divisibles.resultado(191)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = input('Ingrese el número que desea procesar para saber si es primo o no: ')
    if x.isdigit() == True or (x[0] == '-' and x[1:].isdigit()):
        Divisibles.resultado(int(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
