password = 0
position = 50
oldPassword = 0

with open("Day1Input.txt", "r") as input:
    for line in input:
        line = line.strip()
        if not line:
            continue

        sign = 1 if line[0] == "R" else -1
        number = int(line[1:])
        value = sign * number

        prev = position
        position += value

        # count how many multiples of 100 were crossed (or landed on)
        if position > prev:
            crossings = (position // 100) - (prev // 100)
        elif position < prev:
            # use (x-1)//100 to make the start exclusive when moving down
            crossings = ((prev - 1) // 100) - ((position - 1) // 100)
        else:
            crossings = 0

        password += abs(crossings)

        print("Prev:", prev, "Position:", position, "Crossings:", crossings, "Password:", password)
