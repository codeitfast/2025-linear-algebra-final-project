width = 27

# make a 2d table that that does module of width and multiplies the values of x and y from 0 to 99
table = [[(x * y) % width for x in range(width)] for y in range(width)]

# make program to find where x * y modulo = 1
for y in range(width):
    for x in range(width):
        if table[y][x] == 1:
            print(f'{x} * {y} = 1')

# print out the table in 2d form

#for row in table:
#    print(row)


# do the same but for addition
table2 = [[(x + y) % width for x in range(width)] for y in range(width)]

#for row in table2:
#    print(row)

# output table to csv file
import csv


with open('table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table)

with open('table2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table2)

# make program to find where x + y modulo 27 = 1
for y in range(width):
    for x in range(width):
        if table2[y][x] == 1:
            print(f'{x} + {y} = 1')