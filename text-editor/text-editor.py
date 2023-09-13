filename = input("Enter filename: ")

with open(filename, "w") as file:
    text = input("Enter text: ")
    file.write(text)

print(f"Text written to {filename}")
