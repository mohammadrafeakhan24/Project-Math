# Rich is a python library which help to style output

from rich.console import Console 
from rich.markdown import Markdown
from SequenceAndSeries.ap import ap


console = Console()  # creating a console object




def welcome():
    message = """# WELCOME TO PROJECT-MATH

       What operation do you want to perform:
      1. Sequence and Series
      2. Complex Number
      3. Basic Calculator
      4. Finding the value of trignometric ratio

    Please select operation from '1' '2' '3' or '4'
    """
    resultMsg = Markdown(message)
    console.print(resultMsg)

welcome()








def sqAndSeries(): 
            choice1Welcome = """# You have chossen Seqence and Series
            Please choose from AP or GP:
            For AP type '1'
            For GP type '2'
            """
            resultChoice1 = Markdown(choice1Welcome)
            console.print(resultChoice1)
            ans4sqAndSeries = input(">> Enter your choice: ")
            
            if ans4sqAndSeries == '1':
                console.print("You have selected AP")
            elif ans4sqAndSeries == '2':
                console.print("You have selected GP")






def selection():
    choice = input(">> Enter your choice: ")
    if choice == '1':
        sqAndSeries()
    elif choice == '2':
        complexno()
    elif choice == '3':
        basicCalculator()
    elif choice == '4':
        angleValue()
    else:
        console.print("Please Enter a valid input")

selection()









