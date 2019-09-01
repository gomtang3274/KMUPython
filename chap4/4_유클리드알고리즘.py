# 유클리드 알고리즘을 이용한 최대공약수 구하기
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("a >"))
b = int(input("b >"))

print("{} 와 {}의 최대공약수는 {}입니다".format(a, b, gcd(a, b)))
