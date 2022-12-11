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


def Ticket():
    Lottery_Ticket = Display()
    Lottery_Ticket.LotteryNumber_Create()
    Lottery_Ticket.Screen_Display()


