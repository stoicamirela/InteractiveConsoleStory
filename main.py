from time import sleep


class Weapon:

    def __init__(self, name):
        self.name = name

    def set_points(self, points):
        self.points = points

    def set_power(self, capacity):
        self.capacity = capacity

    def display_name(self):
        print("I am a weapon")


class Gun(Weapon):
    def display_name(self):
        print("I am a gun.")

class Sword(Weapon):
    def display_name(self):
        print("I am a sword")


class Bow(Weapon):
    def display_name(self):
        print("I am a bow")


if __name__ == '__main__':
    gun = Gun("gun")
    gun.set_power(100)
    gun.display_name()

    sword = Sword("sword")
    sword.set_power(70)
    sword.display_name()

    bow = Bow("Bow")
    bow.set_power(50)
    bow.display_name()

    name = input("What is your name? ")
    print("Welcome to my story", name, "!")
    sleep(1)

    print("You are in a dungeon with 3 doors in front of you.")
    print("You will think things through to get out of the dungeon.")
    sleep(1)
    choice1 = int(input("What is your choice between door 1, 2, 3? "))

    if choice1 == 1:
        print("You are facing a dragon with 7 heads!")
        sleep(1)
        choice2 = input("Choose your weapon, between gun, sword, bow: ")

        if choice2 == "gun":
            gun.set_points(80)
            print("You've got:", gun.capacity, "power.")
            sleep(1)
            print("You won with:", gun.points, end="!")

        elif choice2 =="sword":
            sword.set_points(30)
            print("You've got:", sword.capacity, "power.")
            sleep(1)
            print("You most likely died from exhaustion. You lost with:", sword.points)

        elif choice2 =="bow":
            bow.set_points(5)
            print("You've got:", bow.capacity, "power.")
            sleep(1)
            print("You've lost with:", bow.points, "points for a nice try. Dragons bodies are very strong")

    elif choice1 == 2:
        print("You are facing a troll!")
        sleep(1)
        choice2 = input("Choose your weapon, between gun, sword, bow: ")

        if choice2 =="gun":
            gun.set_points(100)
            print("You've got:", gun.capacity, "power.")
            sleep(1)
            print("You won with:", gun.points, end="!")

        elif choice2 =="sword":
            sword.set_points(80)
            print("You've got:", sword.capacity, "power.")
            sleep(1)
            print("You won with:", sword.points, end="!")

        elif choice2 =="bow":
            bow.set_points(20)
            print("You've got:", bow.capacity, "power.")
            sleep(1)
            print("You lost with:", bow.points, ". Trolls have strong bodies.")

    elif choice1 == 3:
        print("You are facing a Mercurius! Attention cause he's the fastest monster you could've met!")
        sleep(1)
        choice2 = input("Choose your weapon, between gun, sword, bow: ")

        if choice2 =="gun":
            gun.set_points(95)
            print("You've got:", gun.capacity, "power.")
            sleep(1)
            print("You won with:", gun.points, "points.")

        elif choice2 =="sword":
            sword.set_points(20)
            print("You've got:", sword.capacity, "power.")
            sleep(1)
            print("You lost with:", sword.points, "because being that fast they can also beat you up.")

        elif choice2 =="bow":
            bow.set_points(60)
            print("You've got:", bow.capacity, "power.")
            sleep(1)
            print("You've won with:", bow.points, "points. You almost lost, but you went fast. Kudos!")
