from classes import Chinpokomon, Trainer

velocirapstar = Chinpokomon("Velocirapstar", 10, 10, "fire", 8, False)
brocoli = Chinpokomon("Brocoli", 10, 8, "grass", 10, False)
fetuswami = Chinpokomon("Fetuswami", 10, 9, "water", 10, False)
donkeytrom = Chinpokomon("Donkeytrom", 11, 7, "water", 10, False)

cartman = Trainer("Cartman", [velocirapstar, fetuswami], 2, velocirapstar)
kenny = Trainer("Kenny", [brocoli, donkeytrom], 0, donkeytrom)

