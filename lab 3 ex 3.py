player1= {"Health": 100 , "EXP": 70, "Energy": 50}
player2 ={"Health": 20 , "EXP": 80, "Energy": 30}

def print_player_info(player):
    for key in player.keys():
        print (key)

    for value in player.values():
        print (value)

    for key in player.keys():
        print(player [key])

print_player_info(player1)
print_player_info(player2)

