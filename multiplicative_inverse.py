import csv

def width_function(width:int):

    # make a 2d table
    table = []

    # go through every value and insert x * y
    for x in range(99):
        
        basis_array = []
        for y in range(99):
            basis_array.append(x * y % width)
        
        table.append(basis_array)

    # initialize counter
    number_of_inverses = 0

    # find multiplicative inverses based on the table. These are where x * y == 1

    # print("Inverses:")

    for x in range(width):
        for y in range(width):
            if(table[x][y] == 1):
                # print(f'({x}, {y})')
                number_of_inverses += 1

    return ([width, number_of_inverses])

print_array = []

for i in range(1, 99):
    print_array.append(width_function(i))

with open('table3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(print_array)
