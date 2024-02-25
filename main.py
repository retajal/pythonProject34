#home work page 49
def errorcode (x) :
    match x :
        case "400":
            return "bad request"
        case "401":
            return "unauthorised"
        case "403":
            return "forbidden"
        case "404":
            return "not found"
        case "501":
            return "not implemented"
        case "502":
            return "service temporarily"
        case "503":
            return "service unavailable "
        case "505":
            return "internal server error"

x = input(" give me an error code")
print(errorcode(x))

#home totorial 4
name = input("what is your name ")
a = int(input("give me a "))
b = int(input("give me b "))
c = int(input("give me c"))
d = int(input("give me d "))

def solvecubic (a , b , c , d ) :
    b1 = (-b**3)/(27*a**3)+(b*c)/(6*a**2)-(d)/(2*a)
    b2 = ((-b**3)/(27*a**3)+(b*c)/(6*a**2)-(d)/(2*a)**2)
    b3 = ((c)/(3*a)-(b**2)/(9*a**2)**3)
    b4 = (b)/(3*a)
    x = ( b1+ b2+ b2)**(1/3) + (b1 - b2 + b3 )**(1/3) - (b4)
print(x)