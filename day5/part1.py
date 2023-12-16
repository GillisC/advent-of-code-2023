
def read_file():
    input = open("day5\input.txt", "r")
    return input.readlines()

def get_line(map_name: str):
    for line_num, line in enumerate(lines):
        if line.strip() == map_name.strip():
            return line_num + 1
    print(f"Couldn't find line matching with: {map_name}")

def get_seeds():
    seeds = lines[0].strip().split(" ")
    return [seeds[i] for i in range(1, len(seeds))]

# Maps an input integer to a destination integer
def map_line(input: int, arr: list[str]) -> int:
    length = int(arr[2])
    src_start = int(arr[1])
    src_end = src_start+length
    dest_start = int(arr[0])
    output: int

    if src_start <= input <= src_end:
        offset = input-src_start
        output = dest_start+offset
    else:
        output = input
    print(f"{input} -> {output}")
    return output

def map_value(key: int, map_name: str) -> int:
    value = key
    line_num = get_line(map_name)
    while True:
        if line_num >= len(lines):
            break
        if lines[line_num].strip() == "":
            break
        else:
            line = lines[line_num]
            values = line.strip().split(" ")

            length = int(values[2])
            src_start = int(values[1])
            src_end = src_start+length
            dest_start = int(values[0])
            
            if src_start <= value <= src_end:
                offset = value-src_start
                output = dest_start+offset
                return output
        
        line_num += 1
    return value


def main():
    global lines
    lines = read_file()
    seeds = get_seeds()

    locations = []
    for seed in seeds:
        #print(f"Seed {seed}")
        seed, initial_seed = int(seed), int(seed)
        seed = map_value(seed, "seed-to-soil map:")
        seed = map_value(seed, "soil-to-fertilizer map:")
        seed = map_value(seed, "fertilizer-to-water map:")
        seed = map_value(seed, "water-to-light map:")
        seed = map_value(seed, "light-to-temperature map:")
        seed = map_value(seed, "temperature-to-humidity map:")
        location = map_value(seed, "humidity-to-location map:")
        
        locations.append(location)
    print(min(locations))
    

if __name__ == "__main__":
    main()
