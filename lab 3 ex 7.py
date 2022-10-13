
import random
player1 = {"Health" : 100 , "EXP" : 60 , "Money": 200, 1 : "One"}
def damage_taken():
    damage = int(input("Enter a number: "))
    b = damage * 2
    a = random.randint(0,b)
    c = 100 - a
    d = 60 + a 
    print ("The player has taken", a, "ammount of health")
    damage_taken = a - 100
    health_update = {"Health": c}
    exp_update = {"EXP": d}
    player1.update(health_update)
    player1.update(exp_update)
    print (player1)

damage_taken()


