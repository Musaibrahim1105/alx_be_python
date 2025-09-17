number = int(input("Enter a number to see its multiplication table: "))

for j in range(1, 11):
    product = number * j
    print(f"{number} * {j} = {product}")
