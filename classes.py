class Chinpokomon:
    def __init__(self, name, level, attack_power, chinpokomon_type, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.attack_power = attack_power
        self.chinpokomon_type = chinpokomon_type
        self.current_health = current_health
        self.max_health = level * 10
        self.is_knocked_out = is_knocked_out

    def lose_health(self, damage):
        new_health = self.current_health - damage
        self.current_health = new_health
        print(
            "{name} lost {damage} health points! Now {name} has {current_health} health points.".format(name=self.name,
                                                                                                        damage=damage,
                                                                                                        current_health=self.current_health))
        return self.current_health

    def attack(self, opponent_chinpokomon):
        damage = self.attack_power
        if self.chinpokomon_type == "grass" and opponent_chinpokomon.chinpokomon_type == "water":
            damage = damage * 2
        elif self.chinpokomon_type == "fire" and opponent_chinpokomon.chinpokomon_type == "grass":
            damage = damage * 2
        elif self.chinpokomon_type == "water" and opponent_chinpokomon.chinpokomon_type == "fire":
            damage = damage * 2
        opponent_chinpokomon.lose_health(damage)
        print("{opponent} was attacked and lost {damage} health points!".format(opponent=opponent_chinpokomon.name,
                                                                                damage=damage))

    def knock_out(self):
        if self.current_health == 0:
            print("{name} was knocked out!".format(name=self.name))
        self.is_knocked_out = True

    def gain_health(self, heal):
        new_health = self.current_health + heal
        self.current_health = new_health
        print(
            "{name} gained {heal} health points! Now {name} has {current_health} health points.".format(name=self.name,
                                                                                                        heal=heal,
                                                                                                        current_health=self.current_health))
        return self.current_health


class Trainer:
    def __init__(self, name, team, n_of_potions, active_chinpokomon):
        self.name = name
        self.team = team
        self.n_of_potions = n_of_potions
        self.active_chinpokomon = active_chinpokomon

    def use_potion(self):
        if self.n_of_potions <= 0:
            print("There are no potions left to use!")
        else:
            self.active_chinpokomon.gain_health(10)
            print("{active_chinpokomon} was healed using a potion!".format(active_chinpokomon=self.active_chinpokomon.name))
            new_number_of_potions = self.n_of_potions - 1
            self.n_of_potions = new_number_of_potions

    def attack_trainer(self, opponent_trainer):
        opponent_chinpokomon = opponent_trainer.team[opponent_trainer.active_chinpokomon]
        self.active_chinpokomon.attack(opponent_chinpokomon)

    def switch_chinpokomon(self, switched_to_chinpokomon):
        switched_chinpokomon = self.active_chinpokomon
        self.active_chinpokomon = switched_to_chinpokomon
        print("{trainer} switched {switched_chinpokomon} to {active_chinpokomon}".format(trainer=self.name,
                                                                                         switched_chinpokomon=switched_chinpokomon,
                                                                                         active_chinpokomon=self.active_chinpokomon))
