def gcd(a, b):
    '''(int, int) -> int
    Returns gcd of int a and b.
    >>> gcd(-24, 36)
    12
    '''
    gcd = 1

    for i in range(1, min(abs(a), abs(b)) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def reduce(a, b):
    '''(int, int) -> (int, int)
    Returns a tuple of ints that represents the fraction a, b reduced.
    If fraction is negative, will go on numerator.
    >>> reduce(24, -26)
    (-12, 13)
    '''

    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return int(abs(a) / gcd(a,b)), int(abs(b) / gcd(a,b))
    
    elif a > 0 and b < 0:
        return -1 * int(a / gcd(a,b)), -1 *int(b / gcd(a,b))
    
    elif a < 0 and b > 0:
        return int(a/gcd(a,b)), int(b/gcd(a,b))

    elif a == 0 and b != 0:
        return 0, 1
    

def to_string(a, b):
    '''(int, int) -> str
    Returns a string to represent fraction a, b i.e.'-2/3'.
    >>> to_string(-3, 5)
    '-3/5'
    >>> to_string(10, 11)
    '1 1/11'
    '''
    if a == 0:
        return str(0)

    elif b == 1:
        return str(a)
    
    elif abs(a) > abs(b):
        whole = abs(a) // abs(b)
        num = abs(a) % abs(b)
        num, den = reduce(num, abs(b))
        if a * b < 0:
            return str(-1 * whole) + " " + str(num) + "/" + str(den)
        else:
            return str(whole) + " " + str(num) + "/" + str(den)
    else:
        return str(a) + "/" + str(b)

def to_frac(string):
    '''(str) -> (int, int)
    Returns a tuple that the string fraction represents.
    >>> to_frac('-2/3')
    (-2, 3)
    '''
    if "/" not in string:
        return int(string), 1
    else:
        whole = ""
        if " " in string:
            whole, string = string.split(" ")
        index_slash = string.index("/")
        a = int(string[0 : index_slash].strip())
        b = int(string[index_slash + 1:].strip())
        if whole != "":
            if int(whole) < 0:
                return -1 * (abs(int(whole)) * b + a), b
            else:
                return int(whole) * b + a, b
    return a, b

def add(a, b, c, d):
    '''(int, int, int, int) -> (int, int)
    Returns the sum of two fractions a/ b and c/d.
    >>> add(2, 3, -4, 5)
    (-2, 15)
    '''
    num = a * d + b * c
    den = b * d
    num, den = reduce(num, den)
    return num, den

def subtract(a, b, c, d):
    '''(int, int, int, int) -> (int, int)
    Returns the difference of two fractions a/b and c/d.
    >>> subtract(2, 3, -4, 5)
    (22, 15)
    '''
    num = a * d - b * c
    den = b * d
    num, den = reduce(num, den)
    return num, den

def multiply(a, b, c, d):
    '''(int, int, int, int) -> (int, int)
    Returns the product of two fractions a/b and c/d.
    >>> multiply(1, 5, 2, -3)
    (-2, 15)
    '''
    num = a * c
    den = b * d
    num, den = reduce(num, den)
    return num, den

def divide(a, b, c, d):
    '''(int, int, int, int) -> (int, int)
    Returns the quotient of two fractions a/b and c/d.
    >>> divide(1, 5, 2, -3)
    (-3, 10)
    '''
    num = a * d
    den = b * c
    num, den = reduce(num, den)
    return num, den

def equals(a, b, c, d):
    '''(int, int, int, int) -> bool
    Returns True if fractions a/b and c/d are equal. Returns False otherwise.
    >>> equals(1, -2, -2, 4)
    True
    '''
    a, b = reduce(a, b)
    c, d = reduce(c, d)
    return a == c and b == d
