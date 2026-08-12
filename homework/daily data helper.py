class DailyMessage:
    def __init__(self):
        self.message=""
    def get_message(self):
        self.message=input("Enter message: ")
    def print_message(self):
        print(self.message.upper())
class HelperSession:
    def __init__(self):
        print("Session started")
    def __del__(self):
        print("Session ended")
def create_session():
    s=HelperSession()
    return s
class PairFinder:
    def find_pair(self,numbers,target):
        for i,num in enumerate(numbers):
            for j,num2 in enumerate(numbers):
                if i!=j and num+num2==target:
                    return i,j
        return None
daily_text=DailyMessage()
daily_text.get_message()
daily_text.print_message()
session=create_session()
numbers=[10,20,30,40,50,60]
target=int(input("Enter target sum: "))
p=PairFinder()
answer=p.find_pair(numbers,target)
if answer:
    print("Index pair:",answer)
else:
    print("No pair found")