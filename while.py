
print("--- while loop ---")
count = 1
while count < 11:
    print(count, end=" ")
    count += 1
else:
    print("")



print("--- 1~10까지 합 구하기 ---")
count = 1
sum = 0
while count <= 10:
    sum+=count
    count+=1
print("합 {0}".format(sum))


print("--- break, continue, else 적용 ---")
i=0
while i<10:
    i += 1
    if i<5:
        continue
    print(i, end=" ")
    if i>=10:
        break
    else:
        print("~")
print("!")



print("--- 무한루프 ---")
while True:
    pass # 이러면 프로그램 안끝남
