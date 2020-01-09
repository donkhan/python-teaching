
def determinant(a,b,c):
    return b*b - 4 * a * c

def root(b,a):
    return b /  (2*a)

def solve(a,b,c):
    d = determinant(a,b,c)

    if d < 0:
        import math
        print(root(-1 * b , a),"+",math.sqrt(-1*d)/(2*a),"i," ,root(-1 * b , a),"-",math.sqrt(-1*d)/(2*a),"i")
    elif d == 0:
        print(root(-1*b,a),",",root(-1*b,a))
    if d > 0:
        import math
        print(root(-1*b+math.sqrt(d),a),",",root(-1*b-math.sqrt(d),a))

solve(1,-5,6)
solve(1,4,4)
solve(1,0,4)

# x^2 - 5x + 6
# x^2 + 4x + 4
# x^2 + 4

# ax^2+bx+c = 0