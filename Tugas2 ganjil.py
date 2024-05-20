


num = int(input("Enter Number (1-20): "))
if num >= 1 and num <= 20:
    for i in range(num):
        print(i*i)
elif num > 20:
    print(f"Number out of range: {num}")
    exit()
else:
    print(f"Number cannot Negative: {num}")
    exit()
