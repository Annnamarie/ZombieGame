#Annamarie Cortes Submission
def main_menu():
    #Instructions and Intro
    print('Zombie Adventure Game')
    print('You and your team have decided to go to the Hospital to gather supplies essential for survival')
    print('Collect all 9 items to win the game, or be consumed by the zombies!')
    print('Move commands: go South, go North, go East, go West')
    print('Add to Inventory: get "item name" ')
    print('Enter "exit" to exit the game')

def move_rooms(current_room, move, rooms):
    #moving rooms
    current_room = rooms[current_room][move]
    return current_room

def get_item(current_room, move, rooms, inventory):
    #add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']

def main():
    #dictionary for connecting rooms

    rooms = {
        'Main Lobby' : {'North': 'Emergency Department', 'South': 'Gift Shop', 'East':'Patient Rooms'},
        'Emergency Department' : {'item': 'Med Tools', 'South': 'Main Lobby', 'East': 'Security'},
        'Gift Shop': {'item': 'Clothes', 'North': 'Main Lobby'},
        'Security' : {'item': 'Gun', 'North': 'Morgue','South': 'Patient Rooms', 'West': 'Emergency Department',
                      'East':'Research Lab' },
        'Patient Rooms' : {'item':' Radios/Communication Device', 'North':'Security', 'South': 'Cafeteria',
                           'West':'Main Lobby', 'East': 'Pharmacy'},
        'Cafeteria': {'item': 'Food', 'North': 'Patient Rooms', 'East': 'Supply Room'},
        "Admin's Office": {'item': 'Zombie Research Book', 'West': 'Morgue', 'South': 'Research Lab'},
        'Research Lab': {'item': 'Zombie Vaccine', 'North': "Admin's Office", 'West': 'Security'},
        'Pharmacy': {'item': 'Medications', 'West': 'Patient Rooms', 'South': 'Supply Room'},
        'Supply Room': {'item':'Bandages', 'North':'Pharmacy', 'West': 'Cafeteria'},
        'Morgue' : ''
    }

    s = ''
    #list for storing inventory
    inventory = []
    #starting room
    current_room = 'Main Lobby'

    main_menu()

    while True:
        if current_room == 'Morgue':
            #win
            if len(inventory) == 9:
                print('Congratulations! You have collected all the items to defeat the zombies and ensure human survival')
                print('Thanks for playing the game. Hope you enjoyed it')
                break
            else:
                #gameover
                print('Oh no! You have entered the Morgue where the zombies reside')
                print('You have not collected all the items to defeat the zombie!')
                print('You and your team have been devoured and humankind have lost all hope')
                print('Thank you for playing')
                break
        print('You are in the ' + current_room)
        print('Inventory: ',inventory)

        if current_room != 'Morgue' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------------------------------------------')
        move = input('Enter your move: ').title().split()

        #user command to move rooms
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_rooms(current_room, move[1], rooms)
        #user command to get item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You picked up the {}'.format(rooms[current_room]['item']))
            print('---------------------------------------------------------------------')
            get_item(current_room, move, rooms, inventory)
        elif move[0] == 'Exit':
            print('You have exited the game. Thanks for playing')
            break
        #if user enters invalid command
        else:
            print('Invalid move, please try again')
        #if user enters exit


main()