fruits = ["apple", "banana", "strawberry"]

for x in fruits:
    print(x)
else:
    print("\n" + "Looping terminado!")

print("--------------------------------------------------")

for x in [1,2,3]:
    print(x)

print("--------------------------------------------------")

for x in "banana":
    print(x)

print("--------------------------------------------------")

for x in range(6):
    print(x)

print("--------------------------------------------------")

for x in range(1, 6):
    print(x)

print("--------------------------------------------------")

for x in range(1, 6, 2):
    print(x)

print("--------------------------------------------------")

for x in ["apple", "banana", "strawberry"]:
    if x == "banana":
        continue
    print(x)

print("--------------------------------------------------")

for x in ["apple", "banana", "strawberry"]:
    if x == "banana":
        break
    print(x)

print("--------------------------------------------------")

for x in ["apple", "banana", "strawberry"]:
    pass
