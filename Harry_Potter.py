print()
print("*** Harry Potter and the Duel for the Light ***")
print()
print("""It's May 2, 1998 and the Battle of Hogwarts has almost reached it's finale.
The last horcrux, Nagini, has just been beheaded by Neville Longbottom.
Now it is up to Harry Potter to duel Lord Voldemort and take him down once and for all.""")
print()

print("Help Harry duel Lord Voldemort and save the wizarding world.")
print()
print("""Harry's and Voldemort's health will both start at 5.
Fire spells at Voldemort until his health reaches 0 and before he kills Harry.
Pay close attention to the success of Harry's spells - they have different strengths.
Watch out for avada kedavra - that means instant death!""")
print()

import random
import time 

# function to determine Voldemort's attack
def vold_attack ():
    """ Determines Voldemort's attack value"""
    # dictionary of spells with the associated damages
    vold_spell_dic = {"avada kedavra": 15, "crucio": 3, "sectumsempra": 4, "expulso": 2, "bombarda": 3, "imperio": 1, "relashio": 2}
    # list of spells to be used, multiples for everything except Avada
    vold_spells_to_use = ["avada kedavra", "crucio", "crucio", "crucio","sectumsempra","sectumsempra", "sectumsempra", "expulso", "expulso", "bombarda", "bombarda", "imperio", "imperio", "relashio", "relashio"]

    attack_spell = random.choice(vold_spells_to_use)
    
    if attack_spell == "avada kedavra":
        print("Oh, no! Harry's been struck with 'avada kedavra', the killing curse!")
    
    else:
        print("Voldemort attacks Harry with {}".format(attack_spell))
        print()

    vold_attack_value = vold_spell_dic[attack_spell]

    return vold_attack_value

# function to determine Harry's attack
def harry_attack ():
    """Determines Harry's attack value"""
    # dictionary of spells with associated damages
    harry_spell_dic = {"stupefy": 4, "expelliarmus": 5, "incendio": 3, "petrificus totalus": 3, "confundus": 2, "wingardium leviosa": 2, "immobulus": 3}
    # list of spells to select
    harry_spells_to_use = ["stupefy", "expelliarmus", "incendio", "petrificus totalus", "confundus", "wingardium leviosa", "immobulus"]
    # use random.sample to create a sublist
    spell_choices = random.sample(harry_spells_to_use,2)
    # print the list and ask user to choose which one
    print("Which spell should Harry attack with?")
    print("1.", spell_choices[0])
    print("2.", spell_choices[1])
    
    # need to validate user input. Run a loop that tests if entry is valid, if it is break the loop
    choice_is_valid = False 

    while choice_is_valid == False:
        choice = (input("Choose 1 or 2: "))

        # if user chooses one of the correct choices, choice_is_valid turns True and breaks the loop
        if choice == "1" or choice == "2": 
            choice = int(choice)
            choice_is_valid = True

        else:
            print("That is not a valid choice.")
            print()

    print()
    harry_attack_spell = spell_choices[choice-1]

    print()
    print("Wands at the ready.")
    input("Press return to fire {}!".format(harry_attack_spell))
    print()

    # calculate the attack value
    harry_attack_value = harry_spell_dic[harry_attack_spell]

    return harry_attack_value


# function to determine loser
def who_lost_damage(harry_attack_value,vold_attack_value):
    """ Determines the loser of the duel as well as the damage dealt"""

    if harry_attack_value == vold_attack_value:
        loser = None

    elif harry_attack_value > vold_attack_value:
        loser = "Voldemort"

    else:
        loser = "Harry"

    damage = abs(harry_attack_value - vold_attack_value)

    return (loser, damage)

def harry_new_health(harry_health, damage):
    """ Calculates Harry's new health score"""

    harry_health = harry_health - damage

    return harry_health

def vold_new_health(vold_health, damage):
    """Calculated Voldy's new health score"""

    vold_health = vold_health - damage

    return vold_health

def print_health_scores(harry_health, vold_health):
    """Prints both player's health scores"""
    print("Harry's health is:", harry_health)
    print("Voldemort's health is:", vold_health)
    print()
    if harry_health > 0 and vold_health > 0:
        time.sleep(1)
        input("Press return to duel ")
    print()
    print("       ***")
    print()

def the_duel():
    """ Runs the dueling game """

    harry_health = 5
    vold_health = 5

#     Set up a loop that runs when Voldy's AND Harry's health is greater than zero
    while harry_health > 0 and vold_health > 0:

        time.sleep(1)
        print_health_scores(harry_health, vold_health)
        #determine the attack value of each player
        harry_attack_amount = harry_attack() 
        vold_attack_amount = vold_attack()
        time.sleep(1)

        #determine who the loser is
        loser, damage = who_lost_damage(harry_attack_amount,vold_attack_amount)
        if loser != None:
            print()
            print("The loser is:", loser)
            print()

        #determine new health scores
        #if the users are tied, no changes
        if loser == None:
            print()
            print("It's a tie!")
            print("No damage was dealt to either duelist.")
            print()


        #if the loser is Harry, calculate Harry's new health score
        elif loser == "Harry":
            harry_health = harry_new_health(harry_health, damage)

        #if loser is Voldy, calculate Voldy's new health score
        else:
            vold_health = vold_new_health(vold_health, damage)


    if vold_health <= 0:
        print()
        print("Congratulations! Harry has defeated Lord Voldemort")
    
    if harry_health <= 0:
        print()
        print("Harry has been defeated by Voldemort. The wizarding world will fall.")

def run_game():

    while True:
        the_duel()
        print()

        play_again = input("Would you like to play again? Y or N> ").upper()
        print()
        if play_again.startswith("N") == True:
            break
    print("""For your bravery in helping Harry fight Lord Voldemort, you are hearby granted the Order of Merlin, Third Class. 
    Our thanks to you, and farewell!""")

run_game()
    

