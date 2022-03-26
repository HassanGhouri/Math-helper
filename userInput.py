import fractions
import equations

def get_option():
    '''() -> int
    Returns user's selection from menu - validates selection.
    '''
    while True:
        try:
            options = "abcdefg"
            
            print("Equation Type : A, x + b = c, One Step")
            print("Equation Type : B, ax = c, One Step")
            print("Equation Type : C, x/a = c, One Step")
            print("Equation Type : D, ax + b = c, Two Step")
            print("Equation Type : E, x/a + b = c, Two Step")
            print("Equation Type : F, x+b / a = c, Two Step")
            print("Equation Type : G, a(x+b) = c, Two Step")
            print(" ")
                  
            print("These are your options for equation types.")
            selection = input("Enter your selection: ")

            if (selection.lower())  in options and (len(selection) == 1):
                x = eval(f"equations.gen_eqn{selection.upper()}()")

                return(f"Your Selected equation type: {selection.upper()}!, Equation: {x}")
                
                break
    
            else:
                raise Exception

        except:
            print("Please only enter a letter corresponding to your selection !")
            print(" ")


def get_answer():
    '''() -> str
    Gets answer from user - validates answer i.e. that it is an integer or fraction and returns answer.
    '''
    while True:
        try:
            answer = input("Enter your answer: ")
            answer = fractions.to_frac(answer)
            return(answer)

        except:
            print("Please only enter an integer or a fraction in the form a/b !")

def eqn_solver(statement):
    eqnType = statement[29:30]
    eqn = statement[43:]

    return(eval(f"equations.solve_eqn{eqnType}(eqn)"))
    

def compare(ans, solution):
    '''(str, (int, int)) -> bool

    Returns True if the answer and solution are equivalent and False otherwise.
     >>> compare("2", (2, 1))
     True
     >>> compare("3/4", (3, 4))
     True
     >>> compare("3/6", (1, 2))
     True
     '''

    a, b = ans
    c,d = solution

    return(fractions.equals(a,b,c,d))
