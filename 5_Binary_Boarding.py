from Binary_Boarding_input import input

max_id = 0
seats = []
for seat in input.split('\n'):
    start_y, end_y = 0, 127
    start_x, end_x = 0, 7
    for char in seat[:7]:
        middle = int((end_y+start_y)/2)
        if char == "F":
            end_y = middle
        else:
            start_y = middle
    for char in seat[7:]:
        middle = int((end_x+start_x)/2)
        if char == "L":
            end_x = middle
        else:
            start_x = middle
    seat_id = end_y*8+end_x
    seats.append(seat_id)
    max_id = max(max_id, seat_id)

seats = sorted(seats)
print([a+1 for a,b in zip(seats, seats[1:]) if b-a>1])
print(sorted(seats))

print(max_id)
