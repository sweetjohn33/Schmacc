from Objects.Deck import Deck
from Objects.Land import Land
from Objects.Card_classes import *

FOREST1 = Land("Forest")
MEADOW1 = Land("Meadow")
MOUNTAIN1 = Land("Mountain")
SNOW1 = Land("Snow")
MARSH1 = Land("Marsh")
DESERT1 = Land("Desert")
FOREST2 = Land("Forest")
MEADOW2 = Land("Meadow")
MOUNTAIN2 = Land("Mountain")
SNOW2 = Land("Snow")
MARSH2 = Land("Marsh")
DESERT2 = Land("Desert")


ELITE = Deck([EliteCreature("Baby Chicken of Death", 6, 9, 9, "Meadow", "Snow"),
                                         EliteCreature("Armadillo Turtle", 11, 11, 2, "Marsh", "Forest"),
                                         EliteCreature("Ding-aDinga-....Saurus", 6, 4, 14, "Mountain", "Snow"),
                                         EliteCreature("Wan Shi Tong", 10, 10, 4, "Desert", "Marsh"),
                                         EliteCreature("Phoenix", 10, 6, 8, "Desert", "Meadow"),
                                         EliteCreature("Le Flop Dog", 6, 8, 10, "Snow", "Desert"),
                                         EliteCreature("Da Pig", 10, 10, 10, "Meadow", "Snow"),
                                         EliteCreature("Wasabi Ice Cream Dragon", 5, 7, 12, "Snow", "Forest"),
                                         EliteCreature("Mongoose Dragon", 8, 6, 10, "Desert", "Meadow")], "creature")

NORMAL = Deck([NormalCreature("Tortuga_Luchadora", {"add_defense(" : [5, ["self"], 0]}, 5, 6, 5, "Marsh", "Snow"),
                                          NormalCreature("Baby Phoenix", 8, 5, 3, "Desert", "Meadow"),
                                          NormalCreature("Polar Bear Fruit Salesman", 5, 5, 6, "Snow", "Mountain"),
                                          NormalCreature("Headsman", 3, 6, 7, "Meadow", "Desert"),
                                          NormalCreature("Baby Ice Dragon", 3, 5, 6, "Snow", "Desert"),
                                          NormalCreature("Assassin", 4, 4, 8, "Meadow", "Forest"),
                                          NormalCreature("Trojan Donkey", 8, 4, 2, "Meadow", "Marsh"),
                                          NormalCreature("Fox Deer", 6, 2, 6, "Mountain", "Forest"),
                                          NormalCreature("Big Bad Blowing Butcher", 5, 2, 7, "Mountain", "Forest")
                                          ], "creature")

BASIC = Deck([BasicCreature("El_Flamingodingo", 5, 2, 8, "Meadow", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Sneaky Soviet Mole", 4, 6, 2, "Meadow", "Snow"),
                                         BasicCreature("Sneaky Soviet Mole", 4, 6, 2, "Meadow", "Snow"),
                                         BasicCreature("Penguin Knight", 2, 5, 5, "Snow", "Desert"),
                                         BasicCreature("Penguin Knight", 2, 5, 5, "Snow", "Desert"),
                                         BasicCreature("DJ Meow Mix", 4, 4, 4, "Forest", "Snow"),
                                         BasicCreature("DJ Meow Mix", 4, 4, 4, "Forest", "Snow"),
                                         BasicCreature("Guard Dawgs", 7, 1, 4, "Desert", "Mountain"),
                                         BasicCreature("Guard Dawgs", 7, 1, 4, "Desert", "Mountain"),
                                         BasicCreature("Scorpius", 3, 3, 6, "Desert", "Forest"),
                                         BasicCreature("Gogoat", 3, 3, 6, "Mountain", "Marsh"),
                                         BasicCreature("Bush Whacking Nun", 4, 2, 6, "Meadow", "Desert"),
                                         BasicCreature("Platypus-Bear", 5, 2, 5, "Marsh", "Meadow"),
                                         BasicCreature("Platypus-Bear", 5, 2, 5, "Marsh", "Meadow")
                                         ], "creature")

BUILDING = Deck([Building("Defense Silo", 12, 4),
                                   Building("Defense Silo", 12, 4),
                                   Building("Defense Silo", 12, 4),
                                   Building("Defense Silo", 12, 4),
                                   Building("Hospital", 20, 2),
                                   Building("Hospital", 20, 2),
                                   Building("Hospital", 20, 2),
                                   Building("Hospital", 20, 2),
                                   Building("Trading Port", 14, 4),
                                   Building("Trading Port", 14, 4),
                                   Building("Trading Port", 14, 4),
                                   Building("Trading Port", 14, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Farm", 18, 2),
                                   Building("Farm", 18, 2),
                                   Building("Farm", 18, 2),
                                   Building("Farm", 18, 2),
                                   Building("The Wall", 6, 7),
                                   Building("The Wall", 6, 7),
                                   Building("The Wall", 6, 7),
                                   Building("The Wall", 6, 7),
                                   ], "building")

SPELL = Deck([Spell("Smite"),
                                Spell("Horny Rabbit 1"),
                                Spell("Horny Rabbit 2"),
                                Spell("Holier Than Thou Rabbit"),
                                Spell("Creature Revival"),
                                Spell("Creature Revival"),
                                Spell("Creature Revival"),
                                Spell("Graveyard Swap"),
                                Spell("Graveyard Swap"),
                                Spell("Harsh Winds"),
                                Spell("Harsh Winds"),
                                Spell("Defense Swap"),
                                Spell("Defense Swap"),
                                Spell("Ability Swap"),
                                Spell("Ability Swap"),
                                Spell("Health Swap"),
                                Spell("Health Swap"),
                                Spell("Offense Swap"),
                                Spell("Wasabi Ice Cream"),
                                Spell("Wasabi Ice Cream"),
                                Spell("Terrain Haggel"),
                                Spell("Terrain Haggel"),
                                Spell("The Snuffer"),
                                Spell("The Snuffer"),
                                Spell("Reflector"),
                                Spell("Reflector"),
                                Spell("No Pain No Gain"),
                                Spell("No Pain No Gain"),
                                Spell("Frost Feet"),
                                Spell("Frost Feet"),
                                Spell("Hail Storm"),
                                Spell("Hail Storm"),
                                Spell("Devastating Heat"),
                                Spell("Devastating Heat"),
                                Spell("Sand Storm"),
                                Spell("Sand Storm"),
                                Spell("Celestial Omegahuru"),
                                Spell("Celestial Omegahuru"),
                                Spell("Foggy Woods"),
                                Spell("Foggy Woods"),
                                ], "spell")