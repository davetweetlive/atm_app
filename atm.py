def ui_design():
    print('\n\t\t\t\t\t Welcome to the Bank!')
    print('\t\t\t****************************************************')
    print('\t\t\t\t\t Please select....')
    print('\t\t\t 1. Deposit \t\t 4. Previous Deposites')
    print('\t\t\t 2. Widrawal \t\t 5. Previous Widrawals')
    print('\t\t\t 3. Balance Enquity \t 6. Pin Change')
ui_design()

while True:
    users_choice = input('Please enter your input. \t')
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