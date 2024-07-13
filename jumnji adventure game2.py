import random
import time

total_score = 0
max_turns = 10
current_turn = 1


def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)


def update_score(points):
    global total_score
    total_score += points
    print_pause('Your current score is: {}'.format(total_score), 0.5)


def start_game():
    global total_score, current_turn
    total_score = 0
    current_turn = 1

    print_pause('Welcome to the Jumanji Adventure!', 0.5)
    print_pause(
        'You and your friends find an old game called "Jumanji" in an old '
        'room at the school.', 0.5)
    print_pause(
        'Once you start playing, you are transported to a mysterious jungle '
        'filled with wild animals and unknown dangers.', 0.5)
    print_pause(
        'You need to make smart decisions to survive and escape the game. '
        'Your goal is to find the magical jewel and return home.', 0.5)
    print_pause(
        'Be aware of the traps and challenges that await you. Good luck!', 0.5)

    first_choice()


def first_choice():
    global current_turn

    while True:
        print_pause(
            '\nYou come across a fork in the road in the jungle. The thick '
            'trees loom overhead, casting eerie shadows on the path.', 0.5)
        print_pause(
            '1: Follow the path to the dark cave, rumored to be haunted by '
            'ancient spirits.', 0.5)
        print_pause(
            '2: Take the path leading to the roaring river, known for its '
            'treacherous currents.', 0.5)
        choice = input('Enter 1 or 2: ')

        if choice == '1':
            dark_cave()
            break
        elif choice == '2':
            roaring_river()
            break
        else:
            print_pause('Invalid choice, please enter 1 or 2.', 0.5)


def dark_cave():
    global current_turn

    while True:
        print_pause(
            '\nYou cautiously enter the dark cave. The air is cold and damp, '
            'and you hear the sound of dripping water echoing through the '
            'cavern.', 0.5)
        print_pause(
            '1: Investigate the noises, hoping to find something valuable.', 0.5)
        print_pause(
            '2: Quickly exit the cave, fearing what might be lurking in the '
            'shadows.', 0.5)
        choice = input('Enter 1 or 2: ')

        if choice == '1':
            if random.choices([True, False], weights=[60, 40])[0]:
                print_pause(
                    'You discover a hidden treasure guarded by friendly '
                    'creatures! They give you the magical jewel.', 0.5)
                print_pause('You can now return home.', 0.5)
                update_score(50)
                end_game(True)
            else:
                print_pause(
                    'A wild animal appears and you barely escape with your '
                    'life!', 0.5)
                update_score(-10)
                second_choice()
            break
        elif choice == '2':
            print_pause(
                'You safely exit the cave and continue your journey, but the '
                'memory of the dark cave will stay in your mind.', 0.5)
            update_score(0)
            second_choice()
            break
        else:
            print_pause('Invalid choice, please enter 1 or 2.', 0.5)


def roaring_river():
    global current_turn

    while True:
        print_pause(
            '\nYou arrive at the roaring river. The water is turbulent and '
            'fast-moving, with sharp rocks jutting out along the riverbank.', 0.5)
        print_pause(
            '1: Use the raft to cross the river, risking the swift current.', 0.5)
        print_pause(
            '2: Follow the riverbank on foot, looking for a safer crossing.', 0.5)
        choice = input('Enter 1 or 2: ')

        if choice == '1':
            if random.choices([True, False], weights=[60, 40])[0]:
                print_pause(
                    'You skillfully navigate the raft and find a safe spot '
                    'across the river. The jungle on the other side is lush '
                    'and full of life.', 0.5)
                update_score(20)
                second_choice()
            else:
                print_pause(
                    'The raft overturns, and you struggle to stay afloat. You '
                    'manage to grab on to a rock and pull yourself to safety.', 0.5)
                update_score(-20)
                end_game(False)
            break
        elif choice == '2':
            print_pause(
                'You find a safe path along the riverbank. The sound of the '
                'rushing water is calming, and you make steady progress.', 0.5)
            update_score(10)
            second_choice()
            break
        else:
            print_pause('Invalid choice, please enter 1 or 2.', 0.5)


def second_choice():
    global current_turn

    while True:
        print_pause(
            '\nYou find a small village in the middle of the jungle. The '
            'villagers are wary of strangers but seem willing to help.', 0.5)
        print_pause(
            '1: Enter the village to ask for help. The village elder might '
            'have useful information.', 0.5)
        print_pause(
            '2: Continue through the jungle safely, trusting your instincts.', 0.5)
        choice = input('Enter 1 or 2: ')

        if choice == '1':
            print_pause(
                'The villagers welcome you and offer you food and rest. The '
                'village elder tells you stories of the magical jewel and the '
                'monsters that guard it.', 0.5)
            update_score(15)
            third_choice()
            break
        elif choice == '2':
            if random.choices([True, False], weights=[60, 40])[0]:
                print_pause(
                    'You get lost in the dense jungle. The underbrush is thick '
                    'and difficult to navigate.', 0.5)
                update_score(-30)
                end_game(False)
            else:
                print_pause(
                    'You stumble upon the magical jewel in the jungle! It '
                    'glows with a mystical light.', 0.5)
                update_score(40)
                end_game(True)
            break
        else:
            print_pause('Invalid choice, please enter 1 or 2.', 0.5)


def third_choice():
    global current_turn

    while True:
        print_pause(
            '\nWhile exploring the village, you are confronted by a large army '
            'of wolves. Their eyes glimmer under the moonlight.', 0.5)
        print_pause(
            '1: Gather your strength and fight the wolves with your friends, '
            'using whatever you can find as weapons.', 0.5)
        print_pause(
            '2: Accept your fate and live the rest of your life in the jungle, '
            'hoping to avoid further dangers.', 0.5)
        choice = input('Enter 1 or 2: ')

        if choice == '1':
            if random.choices([True, False], weights=[60, 40])[0]:
                print_pause(
                    'You and your friends bravely fight the wolves and emerge '
                    'victorious. Among the wolves\' den, you find the magical '
                    'jewel.', 0.5)
                print_pause(
                    'You can now return home finally! Congratulations.', 0.5)
                update_score(60)
                end_game(True)
            else:
                print_pause(
                    'Despite your efforts, the wolves overpower you. You are '
                    'forced to retreat and live in the jungle.', 0.5)
                update_score(-20)
                end_game(False)
            break
        elif choice == '2':
            print_pause(
                'You accept your fate and decide to live peacefully in the '
                'jungle. The villagers occasionally bring you supplies, and '
                'you learn to survive.', 0.5)
            update_score(-10)
            end_game(False)
            break
        else:
            print_pause('Invalid choice, please enter 1 or 2.', 0.5)


def end_game(won):
    global current_turn

    delay = 0.5

    if won:
        print_pause(
            '\nCongratulations, you won the game and found the magical jewel!', delay)
        if total_score >= 100:
            print_pause('You\'ve achieved an excellent score!', delay)
        else:
            print_pause('You did well but could have scored higher.', delay)
    else:
        print_pause(
            '\nGame over. You were unable to find the jewel and are stuck in '
            'Jumanji.', delay)
        if total_score <= 0:
            print_pause(
                'Your score has dropped to zero. Returning to the start of the game.', delay)
            start_game()
        else:
            print_pause('Try again to improve your score.', delay)

    while True:
        play_again = input('\nWould you like to play again? (yes/no): ').lower()
        if play_again == 'yes':
            start_game()
            break
        elif play_again == 'no':
            print_pause('Thanks for playing Jumanji Adventure! Goodbye!', delay)
            break
        else:
            print_pause('Invalid choice, please enter yes or no.', delay)


start_game()
