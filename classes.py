class Chinpokomon:
    def __init__(self, name, level, chinpokomon_type):
        self.name = name
        self.level = level
        self.attack_power = level * 5
        self.chinpokomon_type = chinpokomon_type
        self.current_health = level * 10
        self.max_health = level * 10
        self.is_knocked_out = False

    def __repr__(self):
        return f"This level {self.level} {self.name} has {self.current_health} hit points remaining. They are a {self.chinpokomon_type} type Chinpokomon"

    def revive(self):
        # Reviving a Chinpokomon will flip it's status to False
        self.is_knocked_out = False
        # A revived Chinpokomon can't have 0 health. This is a safety precaution. revive() should only be called if the pokemon was given some health, but if it somehow has no health, its health gets set to 1.
        if self.current_health == 0:
            self.current_health = 1
        print(f"{self.name} was revived!")

    def lose_health(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()

    def attack(self, opponent_chinpokomon):
        if self.is_knocked_out:
            print(f"{self.name} can't attack because it is knocked out!")
            return
        damage = self.attack_power
        # super effective check
        if self.chinpokomon_type == "grass" and opponent_chinpokomon.chinpokomon_type == "water":
            damage = damage * 2
        elif self.chinpokomon_type == "fire" and opponent_chinpokomon.chinpokomon_type == "grass":
            damage = damage * 2
        elif self.chinpokomon_type == "water" and opponent_chinpokomon.chinpokomon_type == "fire":
            damage = damage * 2
        opponent_chinpokomon.lose_health(damage)

    def knock_out(self):
        self.is_knocked_out = True
        if self.current_health != 0:
            self.current_health = 0

    def gain_health(self, heal):
        old_health = self.current_health
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health
            print(
                f"{self.name} gained {self.max_health - old_health} health points! Now {self.name} has {self.current_health} health points.")
        else:
            print(f"{self.name} gained {heal} health points! Now {self.name} has {self.current_health} health points.")


class Velocirapstar(Chinpokomon):
    def __init__(self, level=5):
        super().__init__("Velocirapstar", "Fire", level)


class Fetuswami(Chinpokomon):
    def __init__(self, level=5):
        super().__init__("Fetuswami", "Water", level)


class Brocoli(Chinpokomon):
    def __init__(self, level=5):
        super().__init__("Brocoli", "Grass", level)


class Donkeytrom(Chinpokomon):
    def __init__(self, level=5):
        super().__init__("Donkeytrom", "Water", level)


class Trainer:
    def __init__(self, name, team, n_of_potions):
        self.name = name
        self.team = team
        self.n_of_potions = n_of_potions
        self.active_chinpokomon = team[0]

    def __repr__(self):
        print(f"The trainer {self.name} has the following Chinpokomon")
        for chinpokomon in self.team:
            print(chinpokomon)
        return f"The current active Chinpokomon is {self.active_chinpokomon.name}"

    def use_potion(self, index_of_the_healed):
        if self.n_of_potions <= 0:
            print("There are no potions left to use!")
        else:
            self.team[index_of_the_healed].gain_health(20)
            print(f"{self.team[index_of_the_healed]} was healed using a potion!")
            self.n_of_potions -= 1

    def attack_trainer(self, opponent_trainer):
        old_health = opponent_trainer.active_chinpokomon.current_health
        self.active_chinpokomon.attack(opponent_trainer.active_chinpokomon)
        damage = old_health - opponent_trainer.active_chinpokomon.current_health
        print(
            f"{self.active_chinpokomon.name} attacked {opponent_trainer.active_chinpokomon.name} and dealt {damage} points of damage!")

    def switch_chinpokomon(self, new_active):
        if len(self.team) > new_active >= 0:
            # You can't switch to a Chinpokomon that is knocked out
            if self.team[new_active].is_knocked_out:
                print(f"{self.team[new_active].name} is knocked out. You can't make it your active Chinpokomon")
            # You can't switch to your current Chinpokomon
            elif new_active == self.active_chinpokomon:
                print(f"{self.active_chinpokomon} is already your active Chinpokomon")
            # Switches the Chinpokomon
            else:
                self.active_chinpokomon = self.team[new_active]
                print(f"Go {self.active_chinpokomon.name}, it's your turn!")
