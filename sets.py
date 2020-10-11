s = set()

print(f"Before: {s}")
s.add(1)
s.add(2)
s.add(3)
s.add(1)
s.add(1)  # sets never repeat, like in math
print(f"After: {s}")

if len(s) > 1:
    print(f"The set has {len(s)} elements.")
else:
    print(f"The set has {len(s)} element.")
