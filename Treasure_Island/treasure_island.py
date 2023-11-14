print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \\
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|

 _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
''')

print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if direction == 'left':
    lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
                 'Type "swim" to swim across.\n').lower()
    if lake == 'wait':
        color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one '
                      'blue. Which colour do you choose?\n').lower()
        if color == 'yellow':
            print('You walk through the door and find yourself on an island. A shark then runs up onto the island, '
                  'mouth open, ready to eat you. That\'s when instead of eating you, he throws up $100,000,'
                  '000 worth of gold and dies. You win!')
        elif color == 'blue':
            print('You walk into an elevator shaft and fall 100 floors. Game Over.')
        elif color == 'red':
            print('You walk through the door only to end up in the middle of a puddle. Then out of nowhere, '
                  'plugged in hairdryers fall from the ceiling, electrocuting you to your death. Game Over.')
        else:
            print('You chose a door that doesn\'t exist. You lose, game over.')
    elif lake == 'swim':
        print('You swam straight into the oncoming boats propellers, the one you shouldve waited for. Game Over.')
    else:
        print('You chose an option that doesn\'t exist. You lose, game over.')
elif direction == 'right':
    print('You were trampled by a herd of elephants. Game Over.')
else:
    print('You chose a direction that wasn\'t listed. You lose, game over.')
