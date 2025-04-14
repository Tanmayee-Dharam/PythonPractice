print("Number Pattern 1 ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

print()  #adding a blank line between patterns

print("Number Pattern 2")
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print("")