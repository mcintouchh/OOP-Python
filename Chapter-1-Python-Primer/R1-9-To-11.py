# question #9 What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
for i in range(50,90,10):
    print(i,end=" ")
print()

#question #10 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
for i in range(8,-10,-2):
    print(i,end=" ")
print()

#question #11 Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
print([2**i for i in range(9)])