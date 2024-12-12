class Pet:
    def init(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 30:
            self.hunger -= 20
            self.happiness += 10
            print(f"{self.name} поїв і тепер щасливиЙ!")
        else:
            print(f"{self.name} не хоче їсти.")

    def play(self):
        if self.energy >= 20:
            self.happiness += 70
            print(f"{self.name} бавиться")
        else:
            print(f"{self.name} втомлений, щоб гратись.")
    def status(self):
        print(f"""
        Ім'я: {self.name}
        Вид: {self.species}
        Голод: {self.hunger}
        Енергія: {self.energy}
        Щасливий: {self.happiness}
        """)
