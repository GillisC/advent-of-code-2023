
def read_file():
    input = open("day4\input.txt", "r")
    return input.readlines()


def calculate_points(num_wins):
    if num_wins == 0:
        return 0
    else:
        return 2**(num_wins-1)

def main():
    total = 0
    for line_num, line in enumerate(read_file()):
        #print(f"Current Line: {line_num+1}")
        line = line.strip().split("|")
        win = line[0].strip().split(" ")
        winning = [win[i] for i in range(2, len(win))]
        lose = line[1].strip().split(" ")
        my_nums = [lose[i] for i in range(0, len(lose)) if i != '']
    
        #print(f"Winning: {winning}\nLosing: {losing}")
        num_wins = 0
        for i in winning:
            if i == "":
                continue
            if i in my_nums:
                num_wins += 1
        total += calculate_points(num_wins)
    print(total)

if __name__ == "__main__":
    main()