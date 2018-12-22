import random
import numpy
import math
#for x in range (10):
 #   print (random.randint(1,10))

# array sample: array = [CONTENT, CONTENT]
# array = []
# Then, to add items you do:
# array.append('a')

#random_seed = random.seed(random.randint(1,100000))
num_dice = int(input("Enter a number "))

#gets a number of dice to build into an array
def dice_array_builder(num_dice):
    character_dice_array = []
    dice_counter=num_dice*6
    # multiplying by 6 so that we can roll 4 dice 6 times
    

    while dice_counter > 0:
        #seed=random.randint(1,100)
        random.seed()
        #seed = seed+1
        character_dice_array.append(math.trunc(random.random()*10))
        #what about using random.random?
        #character_dice_array.append(random.seed(random.randint(1,10)))
        dice_counter=dice_counter-1
    print(character_dice_array)
    
   
   
    #for i in range (len(character_dice_array)):
    #   print(character_dice_array)

dice_array_builder(num_dice)
#print("character dice array: ", character_dice_array)
 
#something like this maybe
#>>> import math
#>>> math.trunc(random.random()*10)
#5
# >>>