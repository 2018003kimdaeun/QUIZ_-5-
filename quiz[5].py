var = int(input("몇 단까지 출력할까요? "))
print(var, type(var))

def gugudan(table):
    print("구구단을 출력합니다.")
    if table < 1:
        print("1 이상의 숫자를 입력해주세요.")
        return
    for x in range(1, table + 1):
        print("------[" + str(x) + "단]------")
        for y in range(1, table + 1):
            print(f"{x} x {y} = {x * y}")

gugudan(var)

