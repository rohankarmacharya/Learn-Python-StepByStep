"""
break → stop the loop completely.

continue → skip current iteration & move to next.
"""

# Example : break
for i in range(1,10):
    if i==5:
        break
    print(i)

# Example: continue
for i in range (1,10):  # 1 → 9
    if i % 2 == 0:   # skip even numbers
        continue
    print(i)  # print only odd numbers