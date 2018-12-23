import random
import math

# "You have 6 Ability scores to roll for: Strength, Dexterity, Constitution, Intellect, Charisma, and Wisdom. 
    # You can either roll 4 6-sided die and record the cumulative total of the highest 3 dice 6 times 
        # or take the “standard set” which is 15,14,13,12,10,8. 
    # You do not need to assign these scores yet, but you can if you want to."
# from: https://www.instructables.com/id/DD-5E-Character-Creation/

num_dice = 4
#todos: create a simple graphical user interface that has a button that's used to "generate a character with random stats"

#gets a number of dice to build into an array
def dice_array_builder(num_dice):
    character_dice_array = []
    num_dice= 4
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
    #print(character_dice_array)
    print(first_character_array)
    print(second_character_array)
    print(third_character_array)
    print(forth_character_array)
    print(fifth_character_array)
    print(sixth_character_array)

    # adding up the top 3 dice in a roll and storing it into a variable
    first_character_sum = first_character_array[0]+first_character_array[1]+first_character_array[2]
    second_character_sum = second_character_array[0]+second_character_array[1]+second_character_array[2]
    third_character_sum = third_character_array[0]+third_character_array[1]+third_character_array[2]
    forth_character_sum = forth_character_array[0]+forth_character_array[1]+forth_character_array[2]
    fifth_character_sum = fifth_character_array[0]+fifth_character_array[1]+fifth_character_array[2]
    sixth_character_sum = sixth_character_array[0]+sixth_character_array[1]+sixth_character_array[2]

    #printing to make sure that I have the right number of variable names
    print(first_character_sum)
    print(second_character_sum)
    print(third_character_sum)
    print(forth_character_sum)
    print(fifth_character_sum)
    print(sixth_character_sum)

dice_array_builder(num_dice)


class Character:
    def __init__(strength, dexterity, constitution, intellect, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intellect = intellect
        self.wisdom = wisdom
        self.charisma = charisma

