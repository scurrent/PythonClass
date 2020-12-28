# This is a sample Python script.

def my_for(iteratble) :
    iterator = iter(iteratble)
    while True:
        try :
            print(next(iterator))
        except StopIteration :
            break


print(my_for("scott"))


class Counter :
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <self.high :
            num = self.current
            self.current += 1
            return num
        raise StopIteration



def current_beat():
    nums = (1,2,3,4)
    i= 0
    while True :
        if i >= len(nums) : i = 0
        yield nums[i]
        i+= 1

counter = current_beat()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

def yes_or_no():
    answer = "yes"
    while True:

        yield answer
        if answer == "no" :
         #   print("set yes")
            answer = "yes"
        else :
            answer = "no"

truer = yes_or_no()
print(next(truer))
print(next(truer))
print(next(truer))
print(next(truer))

#for x in Counter(0, 11):
#    print(x)