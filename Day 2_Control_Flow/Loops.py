# while loop: Repeats while condition is true.

count = 1
while count <= 5:
    print(count)
    count += 1

# for loop: Used to loop over a sequence (list, string, range, etc.)
for i in range(1, 6):
    print(i)


# Loop Control
# break → exit loop early
# continue → skip current iteration

for i in range(1, 6):
    if i == 3:
        continue  # skips 3
    if i == 5:
        break  # stops at 5
    print(i)
