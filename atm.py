########################################################################
# Imported packages, methods, functions as per requirement
########################################################################
import os
import time
from datetime import datetime

########################################################################
# Globally decelared variables.
########################################################################
STORED_MONEY = 27000
TIME_OUT_SEC = 5
DEFAULT_PIN = 1234
NO_OF_ATTEMPTS = 3

########################################################################
# The below function provides UI insstructions to the user.
########################################################################
def ui_design():
    print('\n\t\t\t\t\t Welcome to the Bank!')
    print('\t\t\t****************************************************')
    print('\t\t\t\t\t Please select....')
    print('\t\t\t 1. Deposit \t\t 4. Previous Deposites')
    print('\t\t\t 2. Widrawal \t\t 5. Previous Widrawals')
    print('\t\t\t 3. Balance Enquity \t 6. Pin Change')

############################################################################
# The following function takes choice as parameter and performas operations
# according to it.
############################################################################
def operation_(users_choice):
    if users_choice is '':
        print('You need to enter some input!')
        time.sleep(1)
    
    elif users_choice == '1':
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
    
    elif users_choice == '7':
        print('Bye!');
    
    else: 
        print('You have selected a wrong option!')
        print('Please try again.')

#############################################################################
# The main function that controls all the operations performed on the system.
#############################################################################
def main():
    ui_design()
    menu_option = input('Please enter your input. \t')

    # Menu loop.
    while menu_option:

        # function call for operational choice
        operation_(menu_option)

        continue_choice = input('Do you still want to continue? Y/N\t')

        if continue_choice == 'y' or continue_choice == 'Y' or continue_choice == 'YES' or continue_choice == 'yes':
            os.system('cls')
            main()

        elif continue_choice == 'n' or continue_choice == 'N' or continue_choice == 'NO' or continue_choice == 'no':
            os.system('cls')
            print('\t\t\t\tThank you! Visit again')
            time.sleep(TIME_OUT_SEC)
            os.system('cls')
            main()
        menu_option = input('Please enter your input. \t')

    else:
        print('You need to enter some input!')
        time.sleep(TIME_OUT_SEC)
        os.system('cls')
        main()

########################################################################
# Entry point of the module.
########################################################################
main()