from colorama import Fore, Style, Back
from emoji import emojize
import emoji


# ********************Information on Colorama Module********************
# Style.RESET_ALL = Resets foreground, background, and brightness used on our coding
# Fore.color = This will make the Printout color
# Fore.Reset = reset to default color used
# Fore.Back = To make a Background color on printout

def Welcome_Text():
    print("\n", Fore.LIGHTGREEN_EX, emojize(':money_bag:') * 25,
          Fore.BLACK, Style.BRIGHT, Back.LIGHTBLUE_EX, "WELCOME TO", Style.RESET_ALL,
          Fore.BLACK, Style.BRIGHT, Back.LIGHTGREEN_EX, "POWERBALL", Style.RESET_ALL,
          Fore.BLACK, Style.BRIGHT, Back.LIGHTBLUE_EX, "LOTTERY", Style.RESET_ALL,
          Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, emojize(':money_bag:') * 25, Fore.RESET)


def No_ExitText():
    print("\n", Fore.GREEN, Style.BRIGHT, (emoji.emojize(':waving_hand:') * 35))
    print(Fore.LIGHTCYAN_EX, "\n\t\t\tThank you for Playing With US!!", Fore.LIGHTCYAN_EX,
          "\n\t\t\t\t Have a Nice day!!!", Fore.YELLOW, emojize(':handshake: ') * 3, Fore.RESET, )
    print("\n", Fore.GREEN, Style.BRIGHT, (emoji.emojize(':waving_hand:') * 35))
    exit()


def Invalid_ExitText():
    # When the user input Invalid Input it will display the below Text
    print("", Fore.GREEN, Style.BRIGHT, (emoji.emojize(':waving_hand:') * 35))
    print(Fore.LIGHTCYAN_EX, "\n\t\t\t\t\tInvalid Input")
    print(Fore.LIGHTCYAN_EX, "\n\t\t\tThank you for Playing With US!!", Fore.LIGHTCYAN_EX,
          "\n\t\t\t\t Have a Nice day!!!", Fore.YELLOW, emojize(':handshake: ') * 3, Fore.RESET, )
    print("\n", Fore.GREEN, Style.BRIGHT, (emoji.emojize(':waving_hand:') * 35))
    exit()
