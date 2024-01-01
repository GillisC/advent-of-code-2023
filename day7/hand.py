from collections import Counter


class Hand():

    def __init__(self, hand: str, bid: str) -> None:
        self.hand: str = hand
        self.convert_to_hex()
        self.bid: int = int(bid)

    def get_hand(self) -> list[str]:
        return list(self.hand)

    
    def get_hand_value(self) -> int:
        return int(self.hand.encode("utf-8").hex())
        

    def get_bid(self) -> int:
        return self.bid
    

    def convert_to_hex(self):
        self.hand = self.hand.replace("T", "A")
        self.hand = self.hand.replace("J", "B")
        self.hand = self.hand.replace("Q", "C")
        self.hand = self.hand.replace("K", "D")
        self.hand = self.hand.replace("A", "E")

    # Checks if there is {count} amount in {dict}
    def check_count(self, dict: Counter, count: int) -> bool:
        for key in dict.keys():
            if dict.get(key) == count:
                return True
        return False


    def five_of_a_kind(self) -> bool:
        dict = Counter(self.get_hand())
        return self.check_count(dict, 5)


    def four_of_a_kind(self) -> bool:
        dict = Counter(self.get_hand())
        return self.check_count(dict, 4)


    def full_house(self) -> bool:
        dict = Counter(self.get_hand())
        three = self.check_count(dict, 3)
        two = self.check_count(dict, 2)
        return three and two

    
    def three_of_a_kind(self) -> bool:
        dict = Counter(self.get_hand())
        return self.check_count(dict, 3)
        

    def two_pair(self) -> bool:
        first_pair: bool = False
        dict = Counter(self.get_hand())
        for key in dict.keys():
            if dict.get(key) == 2 and not first_pair:
                first_pair = True
            elif dict.get(key) == 2 and first_pair:
                return True
        return False
        
    
    def one_pair(self) -> bool:
        dict = Counter(self.get_hand())
        return self.check_count(dict, 2)
        
    
    def high_card(self) -> bool:
        dict = Counter(self.get_hand())
        for key in dict.keys():
            if dict.get(key) > 1:
                return False
        return True
    
    
    def evaluate(self) -> int:
        if self.five_of_a_kind():
            return 6
        elif self.four_of_a_kind():
            return 5
        elif self.full_house():
            return 4
        elif self.three_of_a_kind():
            return 3
        elif self.two_pair():
            return 2
        elif self.one_pair():
            return 1
        else:
            return 0
            
    
    def print_evaluation(self) -> str:
        if self.five_of_a_kind():
            print(f"Five of a kind:  {self.five_of_a_kind()}\n")
        elif self.four_of_a_kind():
            print(f"Four of a kind:  {self.four_of_a_kind()}\n")
        elif self.full_house():
            print(f"Full house:      {self.full_house()}\n")
        elif self.three_of_a_kind():
            print(f"Three of a kind: {self.three_of_a_kind()}\n")
        elif self.two_pair():
            print(f"Two pair:        {self.two_pair()}\n")
        elif self.one_pair():
            print(f"One pair:        {self.one_pair()}\n")
        else:
            print(f"High card:       {self.high_card()}\n")


    def __str__(self) -> str:
        return f"Hand: {self.hand}\nBid: {self.bid}\n"
    
    def __gt__(self, other):
        return self.get_hand_value() > other.get_hand_value()
