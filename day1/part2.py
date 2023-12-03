

num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
nums = "0123456789"


def slide_first(s: str):
    for i in range(0, len(s)):
        for j in range(i+3, len(s)+3):
            string = s[i:j]
            if s[i] in nums:
                return s[i]
            elif string in num_dict.keys():
                return num_dict.get(string)
    return s[i]

def slide_last(s: str):
    for i in range(len(s), -1, -1):
        for j in range(len(s)-4, -2, -1):
            string = s[j:i]
            if s[i-1] in nums:
                return s[i-1]
            elif string in num_dict.keys():
                return num_dict.get(string)

def simplify_string(s: str):
    new_s = s
    for key in num_dict:
        if key in s:
            new_s = new_s.replace(key, num_dict.get(key))
    return new_s

def get_concat(line: str):
    lo = 0
    hi = len(line)-1

    while line[lo] not in nums:
        lo += 1

    while line[hi] not in nums:
        hi -= 1

    concat = line[lo] + line[hi]
    return int(concat)

def main():
    input_text = open("input.txt", "r")
    lines = input_text.readlines()

    total = 0

    for line in lines:
        first = slide_first(line)
        last = slide_last(line)
        #print(f"First result: {first}")
        #print(f"Last result: {last} \n")
        res = first + last

        total += int(res)

    print(f"Sum of line: {total}")


def test():
    string = "5bszzkpcdxqkvkf7tgcone2"
    a = "onenine"
    print(a[len(a)-1])
    print(slide_last(a))

if __name__ == "__main__":
    main()
    
    test()