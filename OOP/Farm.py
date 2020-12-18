# ffr = open('farm.txt', 'r')
# ffw = open('farm.txt', 'w')

class Horse(object):
    def __init__(self, name, hunger=0, boredom=0):
        print("New little foal was born in a farm!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __pass_time1(self):
        self.hunger -= 1
        self.boredom -= 1

    def talk(self):
        print('Hello! My name is ', self.name, ". Now I'm feeling ", self.mood, "\n")
        self.__pass_time()

    def eat(self):
        print("Thanks!")
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time1()

    def play(self, fun=4):
        print("OMG!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def golos(self):
        print("Eho-ho")
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "breathtaking!"
        elif 5 <= unhappiness <= 10:
            m = "good."
        elif 10 < unhappiness <= 15:
            m = "so-so."
        else:
            m = "terrible..."
        return m


class Pig(object):
        def __init__(self, name, hunger=0, boredom=0):
            print("New little animal was born in a farm!")
            self.name = name
            self.hunger = hunger
            self.boredom = boredom

        def __pass_time(self):
            self.hunger += 1
            self.boredom += 1

        def __pass_time1(self):
            self.hunger -= 1
            self.boredom -= 1

        def talk(self):
            print(' My name is ', self.name, ". Now I'm feeling ", self.mood, "\n")
            self.__pass_time()

        def eat(self):
            print("Thanks!")
            if self.hunger < 0:
                self.hunger = 0
            self.__pass_time1()

        def play(self, fun=4):
            print("OMG!")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.__pass_time()

        def voice(self):
            print("Ooi-ooi")
            self.__pass_time()

        @property
        def mood(self):
            unhappiness = self.hunger + self.boredom
            if unhappiness < 5:
                m = "breathtaking!"
            elif 5 <= unhappiness <= 10:
                m = "good."
            elif 10 < unhappiness <= 15:
                m = "so-so."
            else:
                m = "terrible..."
            return m


class Cow(object):
        def __init__(self, name, hunger=0, boredom=0):
            print("New little cow was born in a farm!")
            self.name = name
            self.hunger = hunger
            self.boredom = boredom

        def __pass_time(self):
            self.hunger += 1
            self.boredom += 1

        def __pass_time1(self):
            self.hunger -= 1
            self.boredom -= 1

        def talk(self):
            print('Hello! My name is ', self.name, ". Now I'm feeling ", self.mood, "\n")
            self.__pass_time()

        def eat(self):
            print("Thanks!")
            if self.hunger < 0:
                self.hunger = 0
            self.__pass_time1()

        def play(self, fun=4):
            print("OMG!")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.__pass_time()

        def voice(self):
            print("Mooooo")
            self.__pass_time()

        @property
        def mood(self):
            unhappiness = self.hunger + self.boredom
            if unhappiness < 5:
                m = "breathtaking!"
            elif 5 <= unhappiness <= 10:
                m = "good."
            elif 10 < unhappiness <= 15:
                m = "so-so."
            else:
                m = "terrible..."
            return m


class Squirrel(object):
    def __init__(self, name, hunger=0, boredom=0):
        print("New little cow was born in a farm!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __pass_time1(self):
        self.hunger -= 1
        self.boredom -= 1

    def talk(self):
        print('Hello! My name is ', self.name, ". Now I'm feeling ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Thanks!")
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time1()

    def play(self, fun=4):
        print("OMG!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def voice(self):
        print("Peep!")
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "breathtaking!"
        elif 5 <= unhappiness <= 10:
            m = "good."
        elif 10 < unhappiness <= 15:
            m = "so-so."
        else:
            m = "terrible..."
        return m


def main():
    f = None
    while f != 0:
        x = int(input("Write a number to select an animal: 1-horse, 2-pig, 3-cow, 4-squirrel: "))
        if x == 1:
            crit_name = input("Write the name of the foal: ")
            crit1 = Horse(crit_name)
        elif x == 2:
            crit_name = input("Write the name of the pig: ")
            crit1 = Pig(crit_name)
        elif x == 3:
            crit_name = input("Write the name of the calf: ")
            crit1 = Cow(crit_name)
        elif x == 4:
            crit_name = input("Write the name of the squirrel: ")
            crit1 = Squirrel(crit_name)
        else:
            f = 0
            print("Sorry! The program doesn't have a property number", x, ". Try again")
            main()
        if f != 0:
            farm(crit1)


def farm(crit):
    choice = None
    while choice != "0":
        print("""
            My happy farm
            0 - Exit 
            1 - Learn about the health of the little animal
            2 - Feed the little animal
            3 - Play with little animal
            4 - Voice
            5 - Create a new little animal
            6 - Select an animal from farm
            """)
        choice = input("Your choice: ")
        print()
        if choice == "0":
            print("You went to another little animal.")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        elif choice == "4":
            crit.voice()
        elif choice == "5":
            print("Yep! We are creating a new little animal.")
            ffw.write("1")
            main()
        # elif choice == "6":
        #     xx = input("Which animal do you want to choose: 1-horse, 2-pig, 3-cow, 4-squirrel\n")
        #     if xx == "1":
        #         ffr.readline(1)
        #         print(ffr.readline(1))
        #         for i in ffr:
        #             i = i.split()
        #             for so in i:
        #                 if so == 1:
        #                     print("Horse")
        #                 if so == 2:
        #                     print("Pig")
        #                 if so == 3:
        #                     print("Cow")
        #                 if so == 4:
        #                     print("Squirrel")
        else:
            print("Sorry! The program doesn't have a property number ", choice)



main()
