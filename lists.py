names = ["Denis", "Lucas", "Aline", "Thais", "Kelvyn"]
print(f"Original list:\n {names}")

names.append("Du")
names.append("Kayque")
names.append("Thiago")
for name in names:
    print(name)

print("Sorting the names")
names.sort()
for name in names:
    print(name)
