

def parse_input():
    lines = open("day6\input.txt", "r").readlines()
    
    times = lines[0].strip().split(" ")
    times = [i for i in times if i != ""][1::]
    
    distances = lines[1].strip().split(" ")
    distances = [i for i in distances if i != ""][1::]


    times = [int(i) for i in times]
    distances = [int(i) for i in distances]
    return times, distances

#  Returns the number of ways to win 
def get_number_of_wins(time: int, dist: int):
    wins = 0
    winning_dist = dist
    
    for t in range(1, time):
        dt = time-t
        distance_traveled = dt*t
        if distance_traveled > winning_dist:
            wins += 1
    return wins

    
def main():
    times, distances = parse_input()
    #print(f"times: {times}")
    #"print(f"distances: {distances}")
    
    total = 1
    for i in range(len(times)):
        n_wins = get_number_of_wins(times[i], distances[i])
        total *= n_wins
        print(f"Race {i+1} had {n_wins} number of winning setups")

    print(f"Result: {total}")


if __name__ == "__main__":
    main()