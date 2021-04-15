import random
suite = ('Spades','Clubs','Hearts','Diamonds')
ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')

points = (1,2,3,4,5,6,7,8,9,10,0,10,10)

deck = [(c, s, v) for c, v in zip(ranks, points) for s in suite]

playing = True

print('LOWEST POINTS GAME')
print('Declare Your Cards when you think you have the lowest points')
print('POINTS:')
print('Ace - 1')
print('Two - 2')
print('Three - 3')
print('Four - 4')
print('Five- 5')
print('Six - 6')
print('Seven - 7')
print('Eight - 8')
print('Nine- 9')
print('Ten- 10')
print('Jack - 0')
print('Queen - 10')
print('King - 10')
print()
print()

input('Press Enter To Continue...')

print()
print()

Hand = []
Bot_Hand = []
a = 0
random.shuffle(deck)
for x in deck:
    if a<5:
        deck.remove(x)
        Hand.append(x)
        a+=1
a=0

for x in deck:
    if a<5:
        deck.remove(x)
        Bot_Hand.append(x)
        a+=1

while playing:
    print(Hand[0],'\n',Hand[1],'\n',Hand[2],'\n',Hand[3],'\n',Hand[4])
    total_points = Hand[0][2]+Hand[1][2]+Hand[2][2]+Hand[3][2]+Hand[4][2]
    print('points = ',total_points)

    Bot_total_points = Bot_Hand[0][2]+Bot_Hand[1][2]+Bot_Hand[2][2]+Bot_Hand[3][2]+Bot_Hand[4][2]

    print()

    print('Do You Want to Declare or Continue?','\n',"For Declare type 'd'",'\n',"For Continue type 'c'")

    print()

    answer1 = input('Do you Want to Declare(d) or Continue(c)?')

    if answer1.lower()[0] == 'c':
        new_card = deck.pop()
        print()
        print(new_card)
        print('Do you wish to Keep the New Card? Y/N')
        
        answer2 = input('Yes or No:')
        if answer2.upper()[0] == 'Y': 
            print('Which Index Card would you like to remove for the new card?')
            old_card = int(input('What is Index of the card to be removed?'))

            Hand.pop(old_card)

            Hand.append(new_card)
        elif answer2.upper()[0] == 'N':
            pass
        else:
            print()
            print('It seems that you wrote something other than Y or N so it was Assumed NO')
            print()
            input('Press Enter To Continue...')
    
    elif answer1.lower()[0] == 'd':
        if total_points > Bot_total_points:
            print()
            print()
            print('You Lose!')
            print()
            playing = False
            print('BOT HAND:')
            print(Bot_Hand[0],'\n',Bot_Hand[1],'\n',Bot_Hand[2],'\n',Bot_Hand[3],'\n',Bot_Hand[4])
            print(Bot_total_points)
        elif total_points < Bot_total_points:
            print()
            print()
            print('You Win!')
            print()
            playing = False
            print('BOT HAND:')
            print(Bot_Hand[0],'\n',Bot_Hand[1],'\n',Bot_Hand[2],'\n',Bot_Hand[3],'\n',Bot_Hand[4])
            print(Bot_total_points)
        else:
            print()
            print()
            print('Draw!')
            print()
            playing = False
            print('BOT HAND:')
            print(Bot_Hand[0],'\n',Bot_Hand[1],'\n',Bot_Hand[2],'\n',Bot_Hand[3],'\n',Bot_Hand[4])
            print(Bot_total_points)

    if Bot_total_points > total_points:
        Bot_new_card = deck.pop()
        x = random.randrange(0,4)
        Bot_Hand.pop(x)

        Bot_Hand.append(Bot_new_card)

    