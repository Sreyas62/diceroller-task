import random

dice_faces = {
    1: '''
        -------
        |     |
        |  o  |
        |     |
        -------''',
    2: '''
        -------
        | o   |
        |     |
        |   o |
        -------''',
    3: '''
        -------
        | o   |
        |  o  |
        |   o |
        -------''',
    4: '''
        -------
        | o o |
        |     |
        | o o |
        -------''',
    5: '''
        -------
        | o o |
        |  o  |
        | o o |
        -------''',
    6: '''
        -------
        | o o |
        | o o |
        | o o |
        -------'''
}

def roll_dice(num_dice):

    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def display_results(rolls):

    for roll in rolls:
        print(dice_faces[roll])
        print()

def main():
    num_dice = int(input("Enter the number of dice to roll: "))
    rolls = roll_dice(num_dice)
    display_results(rolls)

if __name__ == "__main__":
    main()
