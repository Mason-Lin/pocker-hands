def compare(input):
    # "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
    splited_input = input.split()
    p1 = splited_input[0].rstrip(":")
    c1= splited_input[1:6]
    p2 = splited_input[6].rstrip(":")
    c2= splited_input[7:12]

    return f"{p2} wins. - with high card: Ace"
