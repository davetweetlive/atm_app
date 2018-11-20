"""Imported packages, methods, functions as per requirement"""
from datetime import datetime

"""Globally decelared variables"""
STORED_MONEY = 27000
TIME_OUT_SEC = 5
menu_option = input('Please enter your input. \t')

"""the below function provides UI insstructions to the user"""
def ui_design():
    print('\n\t\t\t\t\t Welcome to the Bank!')
    print('\t\t\t****************************************************')
    print('\t\t\t\t\t Please select....')
    print('\t\t\t 1. Deposit \t\t 4. Previous Deposites')
    print('\t\t\t 2. Widrawal \t\t 5. Previous Widrawals')
    print('\t\t\t 3. Balance Enquity \t 6. Pin Change')

"""The following function takes choice as parameter and performas operations according to it """
def operation_(users_choice)
        if users_choice == '1':
            print('you want to deposit')

        elif users_choice == '2':
            print('you want to withdraw.')

        elif users_choice == '3':
            print('Balance Enquity.')

        elif users_choice == '4':
            print('Previous Deposite.')

        elif users_choice == '5':
            print('Previous Widrawals.')

        elif users_choice == '6':
            print('Pin Change.')

        else: 
            print('You have selected a wrong option!')
            print('Please try again.')

"""The controller function controlls all the operations performed on the system and this is designed as a main function"""
def controller():
    print('Controller is working!')

controller()