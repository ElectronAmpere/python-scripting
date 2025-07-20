# Loop for iterable program
print("For loop")
for step in range(5):
    print(step)

print("While loop")
step = 0
while step < 5:
    print(step)
    step += 1

# Prints all letters except 'e' and 's'
print("continue")
for i in 'geeksforgeeks':

    if i == 'e' or i == 's':
        continue
    print(i)

print("break")
for i in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break

print(i)

print("pass")
# An empty loop
for i in 'geeksforgeeks':
    pass
print(i)

# Else in for loops
print("Else in for loops")
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

# Enumerate (keep track of things)
li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print (i, j)


for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

n = [10, 20]
li = ["Chair", "Table"]

for x in n:
    for y in li:
        print(x, y)

''' 
Since var is even (10), the continue 
statement skips all updates inside the loop every time. 
As a result, var remains unchanged at 10 after the loops.
'''
var = 10
for i in range(10):
    for j in range(2,10,1):
        if var % 2 == 0:
            continue
        else:
            var += 1
print(var)
