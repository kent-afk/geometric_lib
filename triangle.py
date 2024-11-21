def area(a, b, c):
    if(a + b > abs(c) and a + c > abs(b) and b + c > abs(a)):
        p = (a + b + c) / 2 
        return (p*(p-a)*(p-b)*(p-c))**0.5 # before return semi-perimeter changed on geron formula;
    else:
        return False # added verification of existing triangle

def perimeter(a, b, c):
    if(a + b > abs(c) and a + c > abs(b) and b + c > abs(a)):
        return a + b + c
    else:
        return False