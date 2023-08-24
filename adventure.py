# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_sleep(message):
    time.sleep(2)
    print(message)


def intro():
    print_sleep('You find yourself standing in an open field, '
                'filled with grass and yellow wildflowers.')
    print_sleep(f'Rumor has it that a {character} is somewhere around '
                'here, and has been terrifying the nearby village.')
    print_sleep('In front of you is a house.')
    print_sleep('To your right is a dark cave.')
    print_sleep('In your hand you hold your trusty (but not very '
                'effective) dagger.')


def ending():
    response = input('Would you like to play again? (y/n)\n').lower()
    if response == 'y':
        print_sleep('Excellent! Restarting the game ...')
        run_game()
    elif response == 'n':
        print_sleep('Thanks for playing! See you next time.')
    else:
        print_sleep('That is not a valid option')
        ending()


def fight(items):
    if 'sword' in items:
        print_sleep(f'As the {character} moves to attack, you unsheath your '
                    'new sword.')
        print_sleep('The Sword of Ogoroth shines brightly in your hand '
                    'as you brace yourself for the attack.')
        print_sleep(f'But the {character} takes one look at your shiny new toy'
                    ' and runs away!')
        print_sleep(f'You have rid the town of the {character}. '
                    'You are victorious!')
    else:
        print_sleep('You do your best...')
        print_sleep(f'but your dagger is no match for the {character}.')
        print_sleep('You have been defeated!')
    ending()


def run(items):
    print_sleep("You run back into the field. Luckily, you don't seem "
                "to have been followed.")
    main_action(items)


def cave(items):
    print_sleep('You peer cautiously into the cave.')
    if 'sword' in items:
        print_sleep("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
    else:
        print_sleep('It turns out to be only a very small cave.')
        print_sleep('Your eye catches a glint of metal behind a rock.')
        print_sleep('You have found the magical Sword of Ogoroth!')
        print_sleep('You discard your silly old dagger and take the sword '
                    'with you.')
        items.append('sword')

    print_sleep('You walk back out to the field.')
    main_action(items)


def house(items):
    print_sleep('You approach the door of the house.')
    print_sleep('You are about to knock when the door opens and '
                f'out steps a {character}.')
    print_sleep(f"Eep! This is the {character}'s house!")
    print_sleep(f'The {character} attacks you!')
    if 'sword' not in items:
        print_sleep('You feel a bit under-prepared for this, '
                    'what with only having a tiny dagger.')
    sub_action(items)


def sub_action(items):
    response = input('Would you like to (1) fight or (2) run away?\n')
    if response == '1':
        fight(items)
    elif response == '2':
        run(items)
    else:
        print_sleep('That is not a valid option')
        sub_action(items)


def main_action(items):
    print_sleep('\nEnter 1 to knock on the door of the house.')
    print_sleep('Enter 2 to peer into the cave.')
    response = input('What would you like to do?\n'
                     '(Please enter 1 or 2.)\n')
    if response == '1':
        house(items)
    elif response == '2':
        cave(items)
    else:
        print_sleep('That is not a valid option')
        main_action(items)


def run_game():
    items = []
    global character
    character = random.choice(['pirate', 'wicked fairie', 'gorgon'])
    intro()
    main_action(items)


run_game()
