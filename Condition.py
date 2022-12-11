from Utility import *


class Condition(Lottery_Balls):
    def __init__(self):
        super().__init__()

    def Counter(self):
        # Count How Much Correct WhiteBall and PowerBall in the List
        correct_whiteball = 0
        correct_powerball = 0
        # Count Correct Number of WhiteBall on the List
        for lucky_numer in self.Lucky_WhiteBall:
            for today_numer in self.Today_WhiteBall:
                if today_numer == lucky_numer:
                    correct_whiteball += 1
        # Count Correct Number of PowerBall on the List
        for lucky_power in self.Lucky_PowerBall:
            for today_power in self.Today_PowerBall:
                if today_power == lucky_power:
                    correct_powerball += 1

        # Conditions to pay the Player based on the Correct number of WhiteBall and PowerBall
        if correct_whiteball == 5 and correct_powerball == 1:
            print('\t\t\t\t\t\t\tCorrect White Balls and the Powerball:', Fore.LIGHTGREEN_EX, 'Jackpot $324,000,000')
            print('\t\t\t\t\t\t\t', Fore.RED, emojize(':red_heart:') * 2, Fore.RED, emojize(':red_heart:') * 2,
                  Fore.RED, emojize(':red_heart:') * 2, Fore.RED, emojize(':red_heart:') * 2,
                  Fore.RED, emojize(':red_heart:') * 2, Fore.RED, emojize(':red_heart:') * 2, Fore.RESET)
        elif correct_whiteball == 5 and correct_powerball != 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Balls, but no Powerball:', Fore.LIGHTGREEN_EX,
                  '$1,000,000', Fore.LIGHTBLUE_EX, emojize(':glowing_star:') * 6, Fore.RESET)
        elif correct_whiteball == 4 and correct_powerball == 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Balls and the Powerball:', Fore.LIGHTGREEN_EX,
                  '$10,000', Fore.LIGHTYELLOW_EX, emojize(':winking_face_with_tongue:') * 3, Fore.RESET)
        elif correct_whiteball == 4 and correct_powerball != 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Balls, but no Powerball:', Fore.LIGHTGREEN_EX,
                  '$100', Fore.YELLOW, emojize(':money-mouth_face:' * 3), Fore.RESET)
        elif correct_whiteball == 3 and correct_powerball == 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Balls and the Powerball:', Fore.LIGHTGREEN_EX,
                  '$100', Fore.YELLOW, emojize(':money-mouth_face:' * 3), Fore.RESET)
        elif correct_whiteball == 3 and correct_powerball != 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Balls, but no Powerball:', Fore.LIGHTGREEN_EX,
                  '$7', Fore.YELLOW, emojize(':money_with_wings:' * 2), Fore.RESET)
        elif correct_whiteball == 2 and correct_powerball == 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Balls and the Powerball:', Fore.LIGHTGREEN_EX,
                  '$7', Fore.YELLOW, emojize(':money_with_wings:' * 2), Fore.RESET)
        elif correct_whiteball == 1 and correct_powerball == 1:
            print(f'\t\t\t\t\t\t\t {correct_whiteball} Correct White Ball and the Powerball:', Fore.LIGHTGREEN_EX,
                  '$4', Fore.YELLOW, emojize(':money_bag:'), Fore.RESET)
        elif correct_whiteball != 1 and correct_powerball == 1:
            print('\t\t\t\t\t\t\t No White Balls, Just the Powerball:', Fore.LIGHTGREEN_EX,
                  '$4', Fore.YELLOW, emojize(':money_bag:'), Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX, f"\t\t\t\t\t\t\t\t\tSORRY {emoji.emojize(':sad_but_relieved_face: ') * 2}")
            print(Fore.LIGHTRED_EX, "\t\t\t\t\t\t\t\t\tTry again!", Fore.RESET)


def Price():
    Lottery_Price = Condition()
    Lottery_Price.Counter()
