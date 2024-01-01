from hand import Hand

def parse_input():
    lines = open("day7\input.txt", "r").readlines()
    output = []

    for line in lines:
        line = line.strip().split(" ")
        formatted_line = [i for i in line if i != ""]
        output.append(formatted_line)
    
    return output


def main():
    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    high = []

    lines = parse_input()
    for i in lines:
        hand = Hand(i[0], i[1])
        value = hand.evaluate()
        match value:
            case 6:
                five.append(hand)
            case 5:
                four.append(hand)
            case 4:
                full.append(hand)
            case 3:
                three.append(hand)
            case 2:
                two.append(hand)
            case 1:
                one.append(hand)
            case _:
                high.append(hand)
    
    five.sort(reverse=True)
    four.sort(reverse=True)
    full.sort(reverse=True)
    three.sort(reverse=True)
    two.sort(reverse=True)
    one.sort(reverse=True)
    high.sort(reverse=True)

    final = five + four + full + three + two + one + high
    total = 0

    for rank, hand in enumerate(final):
        #print((len(final)-rank))
        hand.print_evaluation()
        total += (len(final)-rank) * hand.get_bid()
    
    print(f"Total: {total}")

if __name__ == "__main__":
    main()