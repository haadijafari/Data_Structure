import os
from Polynomial import *


class Menu:
    def __init__(self) -> None:
        self.A = Polynomial()
        self.B = Polynomial()

    def menu(self):
        while (True):
            os.system('cls')
            menuOptions = [
                'Set Polynomial A',
                'Set Polynomial B',
                'Add',
                'Subtract',
                'Multiply',
                'Derivative A',
                'Integral A',
                'f(x) = ?\t(for Poly A)'
            ]

            print('_____________ Menu _____________', end='\n\n')
            print('POLYNOMIAL PYTHON PROGRAM\n',
                  '\tPowerd by: The H\n')
            for i in range(len(menuOptions)):
                print('[', i+1, '] ', menuOptions[i], sep='')

            print('\n[0] Exit\n\n')

            # Displaying A polynomial
            print("A Polynomial: ", end='')
            self.A.display()

            # Displaying B polynomial
            print("B Polynomial: ", end='')
            self.B.display()

            choice = input('\nEnter your choice: ').strip().split()[0]
            os.system('cls')

            if choice == '1':
                self.setPoly(self.A)
            elif choice == '2':
                self.setPoly(self.B)
            elif choice == '3':
                result = Polynomial()
                result.head = self.A.add(self.B)
                print('A: ',end='')
                self.A.display()
                print('B: ',end='')
                self.B.display()
                print('\n\n')
                print('\n\nResult is: ', end='')
                result.display()

                input('\nPress Enter to proceed!...')

            elif choice == '4':
                result = Polynomial()
                result.head = self.A.sub(self.B)
                print('A: ',end='')
                self.A.display()
                print('B: ',end='')
                self.B.display()
                print('\n\n')
                print('\n\nResult is: ', end='')
                result.display()

                input('\nPress Enter to proceed!...')

            elif choice == '5':
                result = Polynomial()
                result.head = self.A.multiply(self.B)
                print('A: ',end='')
                self.A.display()
                print('B: ',end='')
                self.B.display()
                print('\n\n')
                print('\n\nResult is: ', end='')
                result.display()

                input('\nPress Enter to proceed!...')

            elif choice == '6':
                result = Polynomial()
                print('A: ',end='')
                self.A.display()
                print('\n\n')
                result.head = self.A.derivative()
                print('\n\nResult is: ', end='')
                result.display()

                input('\nPress Enter to proceed!...')

            elif choice == '7':
                result = Polynomial()
                result.head = self.A.integral()
                print('A: ',end='')
                self.A.display()
                print('\n\n')
                print('\n\nResult is: ', end='')
                result.display()

                input('\nPress Enter to proceed!...')

            elif choice == '8':
                x = float(input('Please enter a value as x: '))
                fx = self.A.f_x_(x)
                print('A: ',end='')
                self.A.display()
                print('\n\n')
                print('\nf(', x, ') = ', fx, sep='', end='\n\n')
                input('\nPress Enter to proceed!...')
                
            elif choice == '0':
                break
            
            else:
                print('Enter a valid choice!')
                input('\nPress Enter to proceed!...')

    def setPoly(self, AorB):
        while (True):
            os.system('cls')
            if AorB == self.A:
                print('Current A is: ', end='')
            elif AorB == self.B:
                print('Current B is: ', end='')
            AorB.display()
            print('[1] Add Term',
                  '[2] Clear',
                  '\n[0] Back', sep='\n')
            choice = input('Enter your choice: ').strip().split()[0]

            if choice == '1':
                coef = float(input('Coef = '))
                exp = int(input('Exp = '))

                AorB.addTerm(coef, exp)

            elif choice == '2':
                AorB.head = None

            elif choice == '0':
                break
            else:
                input('Enter a valid choice!')
