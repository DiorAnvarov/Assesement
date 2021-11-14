import random
class RandNumbers:
    def __init__(self):
        print("Hello")
        try:
            self.limit = int(input("How many numbers should be returned?: "))
            self.small = int(input("Enter the lowest number: "))
            self.big = int(input("Enter the highest number: "))
            self.retrive(self.limit, self.small, self.big)

        except:
            print("Error try again")

    def retrive(self, limit,small,big):
        for i in range(limit):
            print(random.randint(small, big))

run = RandNumbers()