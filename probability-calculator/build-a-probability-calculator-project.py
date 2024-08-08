import copy
import random

class Hat:
    def __init__(self,**kargs):
        self.contents = []
        if kargs == {}:
            raise TypeError('Class Hat will always be created with at least one ball.')
        for color, amount in kargs.items():
            for _ in range(amount):
                self.contents.append(color)

    def draw(self, amount):
        if amount >= len(self.contents):
            contents = self.contents[:]
            self.contents = []
            return contents
        return_contents = []
        for _ in range(amount):
            index = random.randint(0, len(self.contents)-1)
            return_contents.append(self.contents.pop(index))
        return return_contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    numerator = 0
    expected_balls = Hat(**expected_balls).contents
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        #print(drawn_balls,'->', expected_balls)
        for i, expected_color in enumerate(expected_balls):
            try:
                drawn_balls.pop(drawn_balls.index(expected_color))
                if i == len(expected_balls)-1:
                    numerator += 1
            except:
                break
    return numerator / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,expected_balls={'red':2, 'green':1}, num_balls_drawn=5, num_experiments=1000)
print(probability)