
def read_file():
    input = open("day4\input.txt", "r")
    return input.readlines()


def calculate_points(num_wins):
    if num_wins == 0:
        return 0
    else:
        return 2**(num_wins-1)

def create_dict(number_of_cards):
    dict = {k+1:0 for k in range(number_of_cards)}
    return dict

def update_dict(dict, card_number, num_wins):
    start = card_number + 1
    for _ in range(num_wins):
        dict[start] = dict.get(start) + 1
        start += 1


def main():
    input = read_file()
    total: int = len(input)
    dict = create_dict(len(input))
    for line_num, line in enumerate(input):
        curr_card = line_num + 1

        line = line.strip().split("|")
        win = line[0].strip().split(" ")
        winning = [win[i] for i in range(2, len(win))]
        lose = line[1].strip().split(" ")
        my_nums = [lose[i] for i in range(0, len(lose)) if i != '']
        
        for _ in range(1 + dict.get(curr_card)):
            num_wins = 0
            for i in winning:
                if i == "":
                    continue
                if i in my_nums:
                    num_wins += 1
            #print(f"Card {curr_card} has {num_wins} number of wins")
            update_dict(dict, curr_card, num_wins)
        #points = calculate_points(num_wins)
        #total += points + (points * dict.get(curr_card))
    for i in dict:
        total += dict.get(i)
    print(dict)
    print(total)

if __name__ == "__main__":
    main()