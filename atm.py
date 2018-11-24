#######################################################################################################################################
# Imported packages, methods, functions as per requirement
#######################################################################################################################################
import os
import time
import csv_file
from datetime import datetime

#######################################################################################################################################
# Globally decelared variables.
#######################################################################################################################################
STORED_MONEY = 27000
TIME_OUT_SEC = 5
DEFAULT_PIN = 1234
NO_OF_ATTEMPTS = 3
TOTAL_AMMOUNT = STORED_MONEY #Assigned temporarily 
 
#######################################################################################################################################
# The below function provides UI insstructions to the user.
#######################################################################################################################################
def ui_design():
    print('\n\t\t\t\t\t Welcome to the Bank!')
    print('\t\t\t****************************************************')
    print('\t\t\t\t\t Please select....')
    print('\t\t\t 1. Deposit \t\t 4. Previous Deposites')
    print('\t\t\t 2. Withdraw \t\t 5. Previous Widrawals')
    print('\t\t\t 3. Balance Enquity \t 6. Pin Change')
    print('\t\t\t 7. Exit')

#######################################################################################################################################
# The following function takes choice as parameter and performas operations according to it.
#######################################################################################################################################
def operation_(users_choice):
    global TOTAL_AMMOUNT, DEFAULT_PIN

    #Mid of the while if there is no input this block of code will execute
    if users_choice is '':
        print('You have not given any input! Please try again\n')
        time.sleep(1)
    
    #If choice is 1 deposite feature will execute
    elif users_choice == '1':
        ammount_to_depo = input('Enter the ammount you want to deposite: \t')
        ammount_to_depo = int(ammount_to_depo)
        TOTAL_AMMOUNT = TOTAL_AMMOUNT + ammount_to_depo
        print(f'You have successfully deposited your ammount.')


    #If choice is 2 withdraw feature will execute
    elif users_choice == '2':
        ammount_to_withdraw = input('Enter the ammount you want to withdraw: \t')
        ammount_to_withdraw = int(ammount_to_withdraw)
        input_pin = input('Enter PIN: \t')

        if int(input_pin) == DEFAULT_PIN:
            if TOTAL_AMMOUNT >= 0 and TOTAL_AMMOUNT >= ammount_to_withdraw:
                TOTAL_AMMOUNT  = TOTAL_AMMOUNT - ammount_to_withdraw
                print(f'Your account has been debited by Rs. {ammount_to_withdraw}')
                
            else:
                print('You don\'t have sufficient balance!')
                time.sleep(TIME_OUT_SEC)
                os.system('cls')
                main()
        else:
            print('You have entered a wrong PIN')
            time.sleep(TIME_OUT_SEC)
            os.system('cls')
            main()


    #This feature depends on recored stored in file
    elif users_choice == '3':
        print(f'Your total ballance is: {TOTAL_AMMOUNT}')

    elif users_choice == '4':
        print('Previous Deposite.')

    elif users_choice == '5':
        print('Previous withdrawal.')

    elif users_choice == '6':
        print('Pin Change.')
    
    elif users_choice == '7':
        print('Bye!');
    
    else: 
        print('You have selected a wrong option!')
        print('Please try again.')

#######################################################################################################################################
# The main function that controls all the operations performed on the system.
#######################################################################################################################################
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
        else:
            print('You have given a wrong input! Please try again.')

        menu_option = input('Please enter your input. \t')

    else:
        print('You have not given any input! Please try again\n')
        time.sleep(TIME_OUT_SEC)
        os.system('cls')
        main()

#######################################################################################################################################
# Entry point of the module.
#######################################################################################################################################
main()