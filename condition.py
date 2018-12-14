
# 조건문

print("--- if ~ else ---")
a=10
if a>5 :
    print("a가 5보다 큼")
else :
    print("a가 5보다 작음")



print("--- if ~ elif ~ else ---")
n = -2
if n > 0 :
    print("양수")
elif n < 0 :
    print("음수")
else :
    print("0")


order = "spam"
if order == "spam":
    price = 100
elif order == "egg":
    price = 50
elif order == "bread":
    price = 70

print(price)


print("--- 삼항 연산자 (tenary operator) ---")
# in java
# Syetem.out.println(a>5 ? 'big' : 'small'')
print('big' if a > 5 else 'small')



