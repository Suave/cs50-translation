def find_seat(people_n, seats_map):
    seats_map_tmp = seats_map
    for r_idx, row in enumerate(seats_map):
        print("r_idx, ", r_idx, "row", row)
        for idx, seat in enumerate(row):
            print("c_idx", idx, "seat", seat)
            if seat == "1":
                print("occupied")
                next

            if seat == "0":
                row[idx] = "1"
                n = people_n - 1
                while n > 0:
                    if row[idx+n] == "1":
                        #return -1, seats_map
                        print("occupied")
                        next
                    row[idx+n] = "1"
                    n -= 1

    return (r_idx, idx), seats_map

seat_map = [["0", "1", "1", "0"], ["0", "0", "0", "1"], ["1", "0", "1", "0"]]

r, m = find_seat(3 ,seat_map)
print(r, m)

'''                
row_n, column_n = input("Please input number of row and column: ").split(" ")
n = int(row_n)
m = int(column_n)

seat_map = []
r = 0
while r < n:
    row = input("Please input seat of row ", r+1)
    seat_map.append([*row])
    r += 1

event_n = input("Please input number of event: ")
q = int(event_n)

e = 0
while e < q:
    event = input("Please input event: ").split(" ")
    if event[0] == 'in':
        find_seat(int(event[1]), seat_map)
    elif event[0] == 'out':
        # TODO
'''