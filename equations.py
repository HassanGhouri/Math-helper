import random
import fractions

def sign(eqn):
    
    sign = "+"
    
    if sign in eqn:
        return(sign)
    
    else:
        return("-")
    

def gen_eqnA():
    '''() -> str
    Returns equation of form x + b = c '''

    sign = "+"
    
    b = random.randint(-10,10)
    c = random.randint(-10,10)

    if b > -1 :
        sign = "+"
        
    else:
        sign = "-"

    return(f"x {sign} {abs(b)} = {c}")


def solve_eqnA(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form x + b = c as a tuple that represents a fraction.
     >>> solve_eqnA("x - 3 = -5")
     (-2, 1)
     '''
    
    answer = eqn[eqn.index("=") + 2:]
    
    sign = " "
    
    if "+" in eqn:
        sign = "+"
        
    else:
        sign = "-"

    b = eqn[eqn.index(sign) + 2: eqn.index("=") - 1]

    if sign == "+":
        x = int(answer) - int(b)

    else:
        x = int(answer) + int(b)
    
    return(x, 1)

    

def gen_eqnB():
    '''() -> str
    Returns equation of form ax = c.
    '''

    a = random.randint(-10, 10)
    c = random.randint(-10,10)

    return(f"{a}x = {c}")


def solve_eqnB(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form ax = c as a tuple that represents a fraction.
    >>> solve_eqnB("-3x = -5")
    (5, 3)
    '''

    a = eqn[0 : eqn.index("x")]
    c = eqn[eqn.index("=") + 2:]

    if int(a) == 0 and int(c) != 0:
        return("No Solution")
    
    elif int(a) == 0 and int(c) == 0:
        return 0,0

    else:
        c, a = fractions.reduce(int(c),int(a))
        return(c, a)
    

def gen_eqnC():
    '''() -> str
    Returns equation of form x/a = c.'''

    a = random.randint(-10,10)
    c = random.randint(-10,10)

    return(f"x/{a} = {c}")

def solve_eqnC(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form x/a = c as a tuple that represents a fraction.
    >>> solve_eqnC("x/-3 = -5")
    (15, 1)
    '''

    a = eqn[eqn.index("/") + 1: eqn.index("=") ]
    c = eqn[eqn.index("=") + 2:]

    if int(a) == 0 and int(c) != 0:
        return(0, 0)

    elif int(c) == 0:
        return(0, 0)
    
    else:
        return(int(c)*int(a),1)


def gen_eqnD():
    '''() -> str
    Returns equation of form ax + b = c.'''

    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)

    signEq = "+"
    
    if b < 0:
        signEq == "-"

    return(f"{a}x {signEq} {abs(b)} = {c}")

    
def solve_eqnD(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form ax + b = c as a tuple that represents a fraction.
    >>> solve_eqnD("-2x + 1 = -5")
    (3, 1)
     '''

   
    signS = sign(eqn[eqn.index("x"): eqn.index("=")])
    a = eqn[0: eqn.index("x") ]
    b = eqn[eqn.index("x") + 4: eqn.index("=") - 1]
    c = eqn[eqn.index("=") + 2:]


    if signS == "-":
        rightSide  = int(c) + int(b)

    else:
        rightSide = int(c) - int(b)
        

    if (rightSide == 0) and (int(a) == 0):
        return(0, 0)

    elif rightSide == 0 and a != 0:
        return(0,1)

    elif int(a) == 0:
        return("No Solution")

    else:
        a, rightSide= fractions.reduce(int(a), rightSide)
        
        return(fractions.reduce(rightSide,a))


def gen_eqnE():
    '''() -> str
    Returns equation of form x/a + b = c.'''
    
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)

    signEq = "+"

    if b < 0:
        signEq = "-"

    return(f"x/{a} {signEq} {abs(b)} = {c}")


def solve_eqnE(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form x/a + b = c as a tuple that represents a fraction.
    >>> solve_eqnE("x/4 + 1 = -5")
    (-24, 1)
     '''
    blankSpace = " "
    signS = sign(eqn[eqn.index(" "):  eqn.index("=")])
    a = eqn[eqn.index("/") +  1 : eqn.index(blankSpace) ]
    b = eqn[eqn.index(blankSpace) + 3 : eqn.index("=") - 1]
    c = eqn[eqn.index("=") + 2:]

    if signS == "+":
        rightSide  = int(c) + (int(b) * -1)

    else:
        rightSide  = int(c) - (int(b) * -1)
        
    if int(a) == 0 or rightSide == 0:
        return(0,0)
    
    else:
        return((rightSide * int(a)), 1)

def gen_eqnF():
    '''() -> str
    Returns equation of form (x + b)/a = c.
    '''
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)

    sign = "+"
    
    if b < 0:
        sign = "-"

    return(f"(x  {sign} {abs(b)} )/ {a} = {c}")

def solve_eqnF(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form (x + b)/a = c as a tuple that represents a fraction.
    >>> solve_eqnF("(x - 5)/4 = -5")
    (-15, 1)
     '''
    signE = sign(eqn)
    a = eqn[eqn.index("/")+ 1: eqn.index("=") + -1]
    b = eqn[eqn.index(signE) + 2: eqn.index(")")]
    c = eqn[eqn.index("=") + 2:]

    rightSide = int(c) * int(a)


    if signE == "+":
        rightSide -= int(b)

    elif signE == "-":
        rightSide += int(b)

    if int(a) == 0:
        return("No Solution")

    return(rightSide, 1)

def gen_eqnG():
    '''() -> str
    Returns equation of form a(x + b) = c.
    '''

    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)

    sign = "+"
    
    if b < 0:
        sign = "-"

    return(f"{a}(x {sign} {abs(b)}) = {c}")

def solve_eqnG(eqn):
    '''(str) -> (int, int)
    Returns solution to equation of form a(x + b) = c as a tuple that represents a fraction.
    >>> solve_eqnG("4(x - 5) = -5")
    (15, 4)
    '''

    signE = sign(eqn[eqn.index("("): eqn.index(")")])
    a = eqn[0: eqn.index("(")]
    b = eqn[eqn.index("x") + 4: eqn.index(")")]
    c = eqn[eqn.index("=") + 2:]

    if int(a) == 0:
        return("No Solution")

    else:
        rightSide = int(c) / int(a)
        if signE == "+":
            rightSide -= int(b)
            
        elif signE == "-" :
            rightSide += int(b)

        x = round(rightSide, 2)
        
        return(x,1)

for i in range(50):
    x = gen_eqnG()
    print(x)
    print(solve_eqnG(x))
