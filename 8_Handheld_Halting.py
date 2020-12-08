from Handheld_Halting_input import input

instructions = input.split("\n")
j=0

while j < len(instructions):
    while instructions[j].startswith("acc"):
        j += 1

    accumulator = 0
    i = 0
    executed = set()

    while i < len(instructions):
        if i in executed:
            break
        executed.add(i)
        type, value = instructions[i].split(" ", 2)
        value = eval(value)
        if type == "acc":
            accumulator += value
            i += 1
        elif (type == "jmp" and i!=j) or (type == "nop" and i==j):
            i = i + value
        else:
            i += 1
    if i >= len(instructions):
        print(accumulator)
        break
    else:
        j += 1
