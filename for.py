
print("--- for 반복 ---")
a = ['cat', 'dog', 'fish']
for animal in a:
    print(animal, end=" ")
else:
    print("")


print("--- break ---")
for i in range(10):
    if i > 5:
        break
    else:
        print(i, end=", ")
print("")



print("--- 복합자료형을 사용하는 for ---")
l = [('둘리', 10),('치킨',100),('돈',1000)]
for data in l:
    print("이름: %s, 가격: %d" % data)


for name, age in l:
    print("이름: {0}, 가격: {1}".format(name, age))


print("--- 1~10합 구하기 ---")
s=0
for i in range(1,11):
   s += i
print(s)


print("--- continue ---")
for i in range(10):
    if i<=5:
        continue
    print(i, end=' ')
else :
    print("")


print("--- 구구단 ---")
for i in range(1, 10):
    for j in range(1, 10):
        print("{0} X {1}".format(i, j), end="  ")
    print("")


print("--- 구구단 (쌤) ---")
for i in range(1, 10):
    for j in range(1, 10):
        print(str(j) + " X " + str(i) + " = "+str(i*j), end="\t")
    print("")


print("--- 삼각형 이중for문 ---")
z=1
for i in range(5):
    for j in range(z):
        print("*", end="")
    z+=1
    print("")



print("--- 삼각형 이중for문 (쌤) ---")
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end="")
    print("")



print("--- 삼각형 for문 (반복) ---")
for i in range(1, 6):
    print("*" * i)



print("--- 역삼각형 ---")
z=5
for i in range(5):
    for j in range(z):
        print("*", end="")
    z-=1
    print("")



print("---  역삼각형 이중for문 (쌤) ---")
for i in range(5, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print("")


print("--- 역삼각형 for문 (반복) ---")
for i in range(5, 0, -1):
    print("*" * i)



