

def parse_input():
    lines = open("day6\input.txt", "r").readlines()
    
    times = lines[0].strip().split(" ")
    times = [i for i in times if i != ""][1::]
    
    distances = lines[1].strip().split(" ")
    distances = [i for i in distances if i != ""][1::]

    time = ""
    for i in times:
        time += i
    time = int(time)

    distance = ""
    for i in distances:
        distance += i
    distance = int(distance)

    return time, distance

#  Returns the number of ways to win 
def get_number_of_losses(time: int, dist: int):
    losses = 0
    winning_dist = dist
    
    for t in range(1, time):
        time_left = time-t
        distance_traveled = time_left*t
        if distance_traveled < winning_dist:
            losses += 1
        else:
            print(f"Broke at t={t}")
            break
    
    for t in range(time, 1, -1):
        dt = time-t
        distance_traveled = dt*t
        if distance_traveled < winning_dist:
            losses += 1
        else:
            print(f"Broke at t={t}")
            break
    return losses

    
def main():
    time, distance = parse_input()
    
    print(time)
    print(distance)
    total = 1

    losses = get_number_of_losses(time, distance)
    print(f"Losses: {losses}, Total wins: {time-losses}")


if __name__ == "__main__":
    main()