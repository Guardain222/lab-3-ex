import random
player = {"Health is": 100 ,
 "Money is" : 200,
 "exp is": 100,
 "Player Alive" : True
   }


damage = int(input("Enter a number: "))

def compute_experience(damage):
    b = damage * 2
    a = random.randint(0,b)
    print("The player has taken", a, "ammount of damage")

#compute_experience(damage)

def take_damage(player, damage):
    a = compute_experience(damage)
    b = 
    player ["Health"] = 100 - a
    player
    
take_damage(player , damage )


