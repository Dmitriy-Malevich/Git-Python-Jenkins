name = []
print("Press to exit 'q'")
while True:
    names = input("Enter your name: ")
    if names == "q":
        break
    name.append(names)
print("Complete list of names:")
for f_name in name:
    print(f_name)
