password = 0
position = 50

with open("Day1Input.txt", "r") as input:
    for line in input:
        line = line.strip()
        if not line:
            continue

        sign = 1 if line[0] == "R" else -1
        number = int(line[1:])
        value = sign * number
        
        position+=value
        if position%100 == 0:
            password+=1

    print(password)


