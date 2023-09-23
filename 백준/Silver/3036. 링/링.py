from fractions import Fraction
n=int(input())
a = list(map(int, input().split()))
a1 = a[0]
for i in a[1:]:
    c = Fraction((2*a1),(2*i))
    print(f'{c.numerator}/{c.denominator}')