from Message import Welcome_Text, Invalid_ExitText, No_ExitText
from Utility import Ticket
from colorama import Fore


# Welcome_Text()
def Powerball_LotteryTicket():
    Welcome_Text()
    # Ask the Player to click "ENTER" so that the Ticket can be Genereted
    Start = input(f"Click {Fore.LIGHTBLUE_EX}'Enter' {Fore.RESET}to play: ")
    while Start == "":
        Ticket()
        Play_again = input(f"\nDo you Want to Play Again? {Fore.LIGHTBLUE_EX}YES/NO: ")
        # Adding Condition for the User to play the Game again.
        if Play_again == "y" or Play_again == "Y" or Play_again == "YES" or Play_again == "yes" or Play_again == "Yes":
            continue
        elif Play_again == "n" or Play_again == "N" or Play_again == "NO" or Play_again == "no" or Play_again == "No":
            No_ExitText()
        else:
            Invalid_ExitText()

