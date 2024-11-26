import random
#create a bag with 10 marbles
bag = ('green', 'green', 'red', 'black', 'red', 'green', 'green', 'red', 'green', 'white')
#starting amount of money
start_wallet = 1000
#current money amount
wallet = start_wallet
#result of last round
result = 0
#how many rounds
rounds = 3
#last marble
marble = 'none'
#welecome user to game
print(f'You start the game with {start_wallet} gold pieces')
#loop drawing marbles
for draw in range(1, rounds+1):
    #how much was bet
    bet = int(input(f'Current Wallet : {wallet} Last draw : {marble} \nRound {draw} - How much do you want to bet?: '))
    #draw marble
    marble = random.choice(bag)
    #win or loss
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10 * bet
    elif marble == 'white':
        result = -5*bet
    else:
        result = -bet
    #cal win or loss/result and new amount/purse
    wallet += result
    #lose game if lose half ofo money
    if wallet < 0.5 * start_wallet:
        print(f'Game over: You lost too much gold!!!')
        break
    #pring result
    print(f'wallet: {wallet}, last result: ({marble}): {result}')
    print('')
#print final results
print('starting/ ending wallet: ', start_wallet, '/', wallet)
print('gain/loss: ', ((wallet - start_wallet)/start_wallet*100), '%')