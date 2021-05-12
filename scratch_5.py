

####Displays the game list
def display_game(game_list):
    print("Here is the game list :")
    print(game_list)


####################################

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
         choice = input('Pick a postion (0,1,2): ')

         if choice not in ['0','1','2']:
             print("Sorry, invalid input")

    return int(choice)

def replacement_list(game_list,position):
    user_placement = input("Please enter string to replace at the position: ")
    game_list[position] = user_placement

    return game_list


def gameon_choice():
    gameon = 'wrong'
    while gameon not in ['Y','N']:
         gameon = input('Keep playing? Y or N: ')

         if gameon not in ['Y','N']:
             print("Sorry, I didnt understand. Please select Y or N")

         if gameon == "Y":
            return True

         else:
            return False

gameon = True
game_list = [1,2,3]

while gameon_choice():
    display_game(game_list)
    position = position_choice()
    game_list= replacement_list(game_list,position)
    display_game(game_list)
    gameon = gameon_choice()
    continue
