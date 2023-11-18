#function to play 
def start():
    print("----------------Welcome to the game!----------------")
    current_floor = 'ground_floor'
    current_room = 'start'

    while True:
        print(floors[current_floor]['rooms'][current_room]['description'])
        user_input = input("What will you do? ").lower()

        if user_input in floors[current_floor]['rooms'][current_room]['moves']:
            next_room = floors[current_floor]['rooms'][current_room].get(user_input)
            if next_room == 'trap':
                print(floors[current_floor]['rooms'][next_room]['description'])
                print("Game Over!")
                break
            elif next_room == 'win':
                print(floors[current_floor]['rooms'][next_room]['description'])
                print("Congratulations! You won!")
                break
            else:
                current_room = next_room
                if isinstance(floors[current_floor]['rooms'][current_room], dict):
                    current_floor = current_room
                else:
                    print(floors[current_floor]['rooms'][current_room]['description'])
                    print("Game Over!")
                    break
        else:
            print("Invalid move! Try again.")




if __name__ == "__main__":


    #floors rooms and its description
    floors = {
        'ground_floor':{
        'rooms':{
            'start':{
                'name':'Start',
                'description':'This is the start of the game. You can move (right/left):',
                'moves':['right','left'],
                'right':'first_floor',
                'left':'trap'
            },
            'trap':{
                'name':'Trap',
                'description':'You have died'
            }
        }
        },
        'first_floor':{
            'rooms': {
                'start':{
                    'name':'First Floor Start',
                    'description':'You are on the first floor, you can move (up/down):',
                    'moves': ['up','down','right'],
                    'up':'trap',
                    'down':'ground_floor',
                    'right':'top_floor'
                },
                'trap':{
                    'name':'Fall Trap',
                    'description':'You fell into a trap and died'
                }
            }
        },
        'top_floor':{
            'rooms': {
                'start':{
                    'name':'Top Floor Start',
                    'description':'You are on top floor, you can move (right/left):',
                    'moves': ['right','left'],
                    'right':'trap',
                    'left':'win'
                },
                'trap':{
                    'name':'Trap',
                    'description':'Congratulations! You won! Sike You died'
                },
                'win':{
                    'name':'Win',
                    'description':'Congratulations! You won!'
                }
            }
        }
    }
    start()




