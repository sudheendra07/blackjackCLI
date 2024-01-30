def get_card():
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    card = random.choice(deck)
    return card

def hand_sum(hand):
    sum = 0
    for card in hand:
        if isinstance(card, int):
            sum += card
        elif card == 'A':
            if sum > 10:
                sum += 1
            else:
                sum += 11
        else:
            sum += 10
    return sum

def yesorno():
    while True:
        try:
            ans = input('Answer yes or no: ').lower()
            
            if ans not in ['y', 'n', 'yes', 'no']:
                raise ValueError(f'Enter a valid choice for yes or no')
            break
        except ValueError as e:
            print(f'Error: {e}')
    return ans

if __name__ == "__main__":
    import random
    
    # print('Do you want to play blackjack? (y/n)')
    # consent = yesorno()

    consent = 'y'

    if consent == 'y' or consent == 'yes':
        while True:
            try:
                bank_amount = int(input('\nEnter initial amount with you (>$0): $'))
                if bank_amount <= 0:
                    raise ValueError('Bank initial amount must be positive')
                break
            except ValueError as e:
                print(f'Error: {e}')

    bank_initial = bank_amount
    

    while consent == 'y' or consent == 'yes':
        while True:
            try:
                bet = int(input(f'\nEnter bet amount (<=${bank_amount}): $'))
                if bet > bank_amount:
                    raise ValueError(f'Bet must be within bank amount (${bank_amount})')
                break
            except ValueError as e:
                print(f'Error: {e}')
        
        player_hand = []
        dealer_hand = []
        player_sum = 0
        dealer_sum = 0
        gameover = False
        for _ in range(2):
            player_hand.append(get_card())
        dealer_hand.append(get_card())
        
        player_sum = hand_sum(player_hand)
        dealer_sum = hand_sum(dealer_hand)
        player_stop = False
        
        if player_sum == 21:
            print(f'\nPlayer hand = {player_hand}')
            print(f'Dealer hand = {dealer_hand}\n')
            gameover = True
            print(f'Player sum is 21, dealer full hand = {dealer_hand}, dealer sum = {dealer_sum}')
            if dealer_sum >= 10:
                dealer_hand.append(get_card())
                dealer_sum = hand_sum(dealer_hand)
                print(f'Dealer draws another card. Dealer full hand = {dealer_hand}, dealer sum = {dealer_sum}')
            
            if (dealer_sum) == 21:
                print('Game is tied!')
            else:
                print('Player wins!')
                bank_amount += bet

        while not gameover:
            
            while not player_stop:
                
                print(f'\nPlayer hand = {player_hand}, player sum = {player_sum}')
                print(f'Dealer hand = {dealer_hand}, dealer sum = {dealer_sum}\n')
                if player_sum > 21:
                    player_stop = True
                    gameover = True
                    print('Player busted! Dealer wins!')
                    bank_amount -= bet
                elif player_sum == 21:
                    player_stop = True
                    print('Player reached 21! Dealer\'s turn!')
                else:
                    print('Hit (y) or stay (n)?: ')
                    cont = yesorno()
                    if cont == 'n' or cont == 'no':
                        player_stop = True
                    else:
                        player_hand.append(get_card())
                        player_sum = hand_sum(player_hand)               
                
            if gameover:
                break
            dealer_hand.append(get_card())
            dealer_sum = hand_sum(dealer_hand)
            print(f'\nPlayer hand = {player_hand}, player sum = {player_sum}')
            print(f'Dealer hand = {dealer_hand}, dealer sum = {dealer_sum}\n')
            if 17 <= dealer_sum <= 21:
                gameover = True
                if dealer_sum > player_sum:
                    print('Dealer wins!')
                    bank_amount -= bet
                elif player_sum > dealer_sum:
                    print('Player wins!')
                    bank_amount += bet
                else:
                    print('Game tied!')
            elif dealer_sum > 21:
                gameover = True
                print('Dealer bust! Player wins!')
                bank_amount += bet
        
        print(f'Bank amount = {bank_amount}')
        if bank_amount > 0:
            print('Do you want to play blackjack? (y/n): ')
            consent = yesorno()
        else:
            print('\nYou\'re out of cash! Game over!')
            consent = 'n'

    print(f'Initial = ${bank_initial}, final = ${bank_amount}\n$$$ gain = ${bank_amount-bank_initial}')