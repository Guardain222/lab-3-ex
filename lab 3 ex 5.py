player = {"Health": 100 , "EXP": 70, "Energy": 50}


def print_player(player):
    #print(player)
    for i in player.values():
        print (i)

        

ask_player = str(input("Enter for see status"))
print_player(player)
