from collections import deque
from utilities import network_memory


class polya_node:
    def __init__(self, _red, _black, _id):
        self.init_red = _red
        self.init_black = _black
        self.neighbours = []
        self.drawn_balls = deque()
        self.red = _red
        self.black = _black
        self.id = _id
        self.weight = _red / (_red + _black)
        self.current_n = 0

    def add_ball(self, ball, num_balls=1):
        self.drawn_balls.append(ball)   # Add drawn ball

        # Add ball to node's current count
        if ball == 'r':
            self.red += num_balls
        else:
            self.black += num_balls

        # If drawn ball is farther back then network memory, forget it
        while len(self.drawn_balls) > network_memory:
            removed = self.drawn_balls.popleft()

            if removed == 'r':
                self.red -= 1
            else:
                self.black -= 1
        self.update_weight()

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def update_weight(self):
        self.weight = self.red / (self.red + self.black)

    def get_ball(self, index):
        if index > self.red + self.black:
            return None
        elif index < self.red:
            return 'r'
        else:
            return 'b'

    def __iter__(self):
        return self

    def __next__(self):
        self.current_n += 1
        if self.current_n >= len(self.neighbours):
            self.current_n = 0
            raise StopIteration
        else:
            return self.neighbours[self.current_n]

    def __str__(self):
        return str(self.weight)
