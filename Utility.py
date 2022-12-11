import random
from colorama import Fore, Style
from emoji import emojize
import emoji
# from Condition import Condition


# Using Single Inheritance Programming methodology

class Lottery_Balls:

    def __init__(self):
        # Initialise an empty list that will be used to store the Lottery ball number For Today and user Lucky numbers.
        self.Today_WhiteBall = []
        self.Lucky_WhiteBall = []
        self.Today_PowerBall = []
        self.Lucky_PowerBall = []

    # Rule for Making Random numbers for Today’s Powerball Winning Numbers:
    #    •	The first five numbers (purple) are random numbers drawn from 20 numbers.
    #    •	The first five numbers (purple) should be in ascending order.
    #    •	The Powerball number (gold) is a random number drawn from 10 numbers from 1 to 10.

    # Rule for Making Random numbers for Your lucky numbers:
    #    •	The first five numbers (purple) are random numbers drawn from 20 numbers.
    #    •	The first five numbers (purple) should be in ascending order.
    #    •	The Powerball number (gold) is a random number drawn from 10 numbers from 1 to 10.

    def LotteryNumber_Create(self):
        # Creating a Random Number For Today Whiteball Winning Numbers (Using "Randint Function")
        for Number_create in range(0, 5):
            TodayWhiteBall_RandomNumber = random.randint(1, 20)
            # Check if this number has already been picked in the list and make a new one
            while TodayWhiteBall_RandomNumber in self.Today_WhiteBall:
                TodayWhiteBall_RandomNumber = random.randint(1, 20)
            self.Today_WhiteBall.append(TodayWhiteBall_RandomNumber)
            # Sort the Created list in ascending order
            self.Today_WhiteBall.sort()
        # Creating a Random Number For Player Lucky Whiteball Numbers (Using "Sample Function")including Ascending order
        LuckyWhiteBall_RandomNumber = sorted(random.sample(range(1, 20), 5))
        self.Lucky_WhiteBall = LuckyWhiteBall_RandomNumber
        # Creating Powerball for Today Winning Number & Player Lucky numbers
        TodayPowerBall_RandomNumber = random.randint(1, 10)
        self.Today_PowerBall.append(TodayPowerBall_RandomNumber)
        LuckyPowerBall_RandomNumber = random.randint(1, 10)
        self.Lucky_PowerBall.append(LuckyPowerBall_RandomNumber)


class Display(Lottery_Balls):
    def __init__(self):
        super().__init__()

    def Screen_Display(self):
        # Print Powerball Today Winning Numbers
        print("\t\t", Fore.RESET, emojize(':money_bag:') * 40)
        print(Style.BRIGHT, Fore.CYAN + f"\n\t\t\t\t\t\t\tToday's Powerball Winning Numbers: ", Fore.LIGHTMAGENTA_EX,
              f"\n\t\t\t\t\t\t\t\t", *self.Today_WhiteBall, Style.BRIGHT,
              Fore.LIGHTYELLOW_EX, *self.Today_PowerBall)  # "*" used to remove index like "[]" or ","
        # Print Lucky Winning numbers
        print(Style.BRIGHT, Fore.CYAN + f"\n\t\t\t\t\t\t\tYour Lucky Numbers: ", Fore.LIGHTMAGENTA_EX,
              f"\n\t\t\t\t\t\t\t\t", *self.Lucky_WhiteBall, Style.BRIGHT,
              Fore.LIGHTYELLOW_EX, *self.Lucky_PowerBall)  # "*" used to remove index like "[]" or ","
        print("\n\t\t", Fore.RESET, (emojize(':money_bag:') * 40), Fore.RESET)

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


def Ticket():
    Lottery_Ticket = Display()
    Lottery_Ticket.LotteryNumber_Create()
    Lottery_Ticket.Screen_Display()
    Lottery_Ticket.Counter()
