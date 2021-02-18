class Chinpokomon:
  def __init__(self, name, level, atack_power, type, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.attack_power = attack_power
    self.type = type
    self.current_health = current_health
    self.max_heatlh = level * 10
    self.is_knocked_out = is_knocked_out

  def lose_heatlh(self, damage):
    new_health = self.current_health - damage
    self.current_health = new_health
    return self.current_health
    print("{name} lost {damage} health points! Now {name} has {current_health} health points.".format(name = self.name, damage = damage, current_health = self.current_health))

  def gain_health(self, heal):
    new_health = self.current_health + heal
    self.current_health = new_health
    return self.current_health
    print("{name} gained {heal} health points! Now {name} has {current_health} health points.".format(name = self.name, heal = heal, current_health = self.current_health))

  def knock_out(self):
    if self.current_health == 0:
      self.is_knocked = True
      print("{name} was knocked out!".format(name = self.name))

  def attack(self, opponent_chinpokomon):
    damage = self.attack_power
    if self.type == grass and opponent_pokemon.type == water:
      damage = damage * 2
    elif self.type == fore and opponent_pokemon.type == grass:
      damage = damage * 2
    elif self.type == water and opponent_pokemon.type == fire:
      damage = damage * 2
    opponent_chinpokomon.lose_health(damage)
    print("{opponent} was attacked and lost {damage} health points!".format(opponent = opponent_chinpokomon, damage = damage))
