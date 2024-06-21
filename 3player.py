player1_name=input('Enter Your Name: ')
player2_name=input('Enter Your Name: ')
player3_name=input('Enter Your Name: ')

player1_point=0
player2_point=0
player3_point=0

while True:
    print('Select Your Choice from the below \n1.Paper\n2.Scissor\n3.Stone')
    player1_choice=input(f'{player1_name} Enter Your Choice: ')
    player2_choice=input(f'-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n{player2_name} Enter Your Choice: ')
    player3_choice=input(f'-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n{player3_name} Enter Your Choice: ')
    if player1_choice=='paper' or player1_choice=='1':
        if player2_choice=='scissor' or player2_choice=='2':
            if player3_choice=='stone':
                player1_point=+1
                player2_point=+1
                player3_point=+1
                print(f'{player2_name} Defeated {player1_name}\n{player3_name} Defeated {player2_name}\n{player1_name} Defeated {player3_name}')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')
    elif player1_choice=='paper':
        if player2_choice=='paper':
            if player3_choice=='scissor':
                player3_point=+2
                print(f'{player3_name} Defeated {player1_name} and {player2_name}')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')
    
    elif player1_choice=='paper':
        if player2_choice=='paper':
            if player3_choice=='stone':
                player1_point=+1
                player2_point+1
                print(f'{player1_name} and {player2_name} Defeated {player3_name} ')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='paper':
        if player2_choice=='paper':
            if player3_choice=='paper':
                print(f'Its a Tie')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='scissor':
        if player2_choice=='scissor':
            if player3_choice=='stone':
                player3_point=+2
                print(f'{player3_name} Defeated {player1_name} and {player2_name}')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='scissor':
        if player2_choice=='scissor':
            if player3_choice=='paper':
                player1_point=+1
                player2_point=+1
                print(f'{player1_name} and {player2_name} Defeated {player3_name}')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='scissor':
        if player2_choice=='scissor':
            if player3_choice=='scissor':
                print(f'Its a Tie')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='stone':
        if player2_choice=='stone':
            if player3_choice=='paper':
                player3_point=+2
                print(f'{player3_name} Defeated {player1_name} and {player2_name}')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='stone':
        if player2_choice=='stone':
            if player3_choice=='scissor':
                player1_point=+1
                player2_point=+1
                print(f'{player1_name} and {player2_name} Defeated {player3_name}')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')

    elif player1_choice=='stone':
        if player2_choice=='stone':
            if player3_choice=='stone':
                player1_point=+1
                player2_point=+1
                print(f'Its a Tie')
                print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')    

    else:
        print('Hey choose only from the above')

    c=int(input('If you want to continue - Press 1\nOR\nIf you want to quit - Press 0'))
    if c==0:
        print(f'Total scores:\n{player1_name}: {player1_point}\n{player2_name}: {player2_point}\n{player3_name}: {player3_point}')
        if player1_point>player2_point and player1_point>player3_point:
            print(f'Congratulations!!!{player1_name} You are the winner of this game')
        elif player2_point>player1_point and player2_point>player3_point:
            print(f'Congratulations!!!{player2_name} You are the winner of this game')
        else:
            print(f'Congratulations!!!{player3_name} You are the winner of this game')
        break
    

