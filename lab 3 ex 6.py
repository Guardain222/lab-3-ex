import random
while True:
    damage = int(input("Enter a number: "))

    def compute_experience(damage):
        b = damage * 2
        a = random.randint(0,b)
        print("The player has taken", a, "ammount of damage")

    compute_experience(damage)




