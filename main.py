import fractions
import equations
import userInput

def main():
    print("Welcome to grade 9 math helper!")
    print(" ")
    print("You will pick between a variety of one step and two step equations to practise 10 times.")

    correctAns = 0
    attempts = 0
    
    playAgain = True
    while playAgain == True:

        print(" ")
        choiceAndEqn = userInput.get_option()
        print(choiceAndEqn)
        userAnswer = userInput.get_answer()
        solution = userInput.eqn_solver(choiceAndEqn)
        corretAnswer = userInput.compare(userAnswer, solution)
        if corretAnswer == True:
            print("You got it correct!")
            correctAns += 1
            attempts += 1
            print(f"Your correct answer rate it {(correctAns/attempts) * 100} %")
            print("")

        else:
            print(f"You got it wrong, the correct answer was {solution}")
            attempts += 1
            print(f"Your correct answer rate it {correctAns/attempts}")

        while True:
            try:
                again = input("Would you like to try another question ? (y/n): ")

                if again == "n":
                    correctAns = 0
                    attempts = 0
                    playAgain = False
                    break

                elif (again != "n") and (again != "y"):
                    raise exception

                else:
                    break


            except:
                print("Please only enter 'y' for yes or 'n' for no!")
    

if __name__ == '__main__':
 main()
