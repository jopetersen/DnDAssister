# the purpose of this separate doc is to introduce classes to the initial utility for the popular
# fantasy tabletop RPG, Dungeons & Dragons (5th Edition)

import random
import math

class Character:
    def __init__(name, strength, dexterity, constitution, intellect, wisdom, charisma):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intellect = intellect
        self.wisdom = wisdom
        self.charisma = charisma
        # will also need to add gear & HP at some point
    #reference https://www.w3schools.com/python/python_classes.asp 

#create an empty character
test_character = Character("test_name", 0, 0, 0, 0, 0, 0)

#setting a global variable of num_dice for a character creation so that I can use a character builder
num_dice= 4

#initializing an empty character name, but is a global variable
character = ""

def character_builder(num_dice, character):
    character_name = str(input("What is your character's name? "))
    # get a character's name
    character_dice_array = []
    dice_counter=num_dice*6
    # multiplying by 6 so that we can roll 4 dice 6 times

    # defining the first set of arrays:
    first_character_array = []
    second_character_array = []
    third_character_array = []
    forth_character_array=[]
    fifth_character_array = []
    sixth_character_array = []

    first_character_sum=0
    second_character_sum=0
    third_character_sum=0
    forth_character_sum=0
    fifth_character_sum = 0
    sixth_character_sum = 0
    # while dice_counter > 0:
    #     random.seed()
    #     character_dice_array.append(math.trunc(random.random()*10))
    #     while dice_counter >=20:
    #         first_character_array=first_character_array.append((math.trunc(random.random()*10)))
    #     dice_counter=dice_counter-1
    # create new arrays from the character_dice_array
    while dice_counter > 20: 
        random.seed()
        first_character_array.append((math.trunc(random.random()*10)))
        dice_counter=dice_counter-1
        #sorting the array from highest to lowest
        first_character_array.sort(reverse=True)
        # determine which 3 indexes in an array are the largest, then add them
    # first_character_sum=first_character_array[0]+first_character_array[1]+first_character_array[2]
    while dice_counter > 16: 
        random.seed()
        second_character_array.append((math.trunc(random.random()*10)))
        dice_counter=dice_counter-1
        second_character_array.sort(reverse=True)
    while dice_counter > 12: 
        random.seed()
        third_character_array.append((math.trunc(random.random()*10)))
        dice_counter=dice_counter-1
        third_character_array.sort(reverse=True)
    while dice_counter > 8: 
        random.seed()
        forth_character_array.append((math.trunc(random.random()*10)))
        dice_counter=dice_counter-1
        forth_character_array.sort(reverse=True)
    while dice_counter > 4: 
        random.seed()
        fifth_character_array.append((math.trunc(random.random()*10)))
        dice_counter=dice_counter-1
        fifth_character_array.sort(reverse=True)
    while dice_counter > 0: 
        random.seed()
        sixth_character_array.append((math.trunc(random.random()*10)))
        dice_counter=dice_counter-1
        sixth_character_array.sort(reverse=True)
    
    # testing to make sure that the arrays are properly printing
    # print(first_character_array)
    # print(second_character_array)
    # print(third_character_array)
    # print(forth_character_array)
    # print(fifth_character_array)
    # print(sixth_character_array)

    # adding up the top 3 dice in a roll and storing it into a variable
    first_character_sum = first_character_array[0]+first_character_array[1]+first_character_array[2]
    second_character_sum = second_character_array[0]+second_character_array[1]+second_character_array[2]
    third_character_sum = third_character_array[0]+third_character_array[1]+third_character_array[2]
    forth_character_sum = forth_character_array[0]+forth_character_array[1]+forth_character_array[2]
    fifth_character_sum = fifth_character_array[0]+fifth_character_array[1]+fifth_character_array[2]
    sixth_character_sum = sixth_character_array[0]+sixth_character_array[1]+sixth_character_array[2]

    #building an array from the sums
    sum_array = []
    sum_array.append(first_character_sum)
    sum_array.append(second_character_sum)
    sum_array.append(third_character_sum)
    sum_array.append(forth_character_sum)
    sum_array.append(fifth_character_sum)
    sum_array.append(sixth_character_sum)
    print ("Here is an array sum: ", sum_array)

    def strength_updater (sum_array):
        #will need to prevent someone from using the same thing more than once.    
        temp_strength = int(input("Which value would you like to use for your strength stat?"))
        if temp_strength in sum_array:
            # add the strength value to the character (will need to look up the character first)

        else: 
            #print "that number doesn't exist, please try again"

    character_builder(num_dice)