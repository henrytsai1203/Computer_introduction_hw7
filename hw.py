class Judge:
    def __init__(self, answer: str) -> None:
        self.answer = answer

    def guess(self, num: str) -> bool:
        a = 0
        b = 0

        Alist = [True]*len(self.answer)

        for i in range(len(self.answer)):
            if(self.answer[i]==num[i]):
                a = a+1
                Alist[i] = False
        
        for i in range(len(self.answer)):
            for j in range(len(self.answer)):
                if(self.answer[i]==num[j]  and Alist[i]==True):
                    b = b+1
                    Alist[i] = False

        print(f"Your guess is {num}; the result is {a}A{b}B")

        if (a == len(self.answer) and b==0):
            return True
        else:
            return False


def read_input(guess_len: int) -> str:
    
    guess = input("Enter your guess:\n")
    numset = set(guess)
    isnum = 1
    for i in numset:
        if i not in {'0','1','2','3','4','5','6','7','8','9'}:
            isnum = 0

    while (guess_len != len(guess) or len(numset)!= len(guess) or isnum==0):
        guess = input("Invalid, please enter your guess again:\n")
        numset = set(guess)
        isnum = 1
        for i in numset:
            if i not in {'0','1','2','3','4','5','6','7','8','9'}:
                isnum = 0

    return guess
    

def enter_answer() -> str:
    return input()
