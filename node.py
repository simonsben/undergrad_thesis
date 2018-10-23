from collections import deque
from utilities import network_memory

class polya_node:
    def __init__(self, _red, _black):
        self.init_red = _red
        self.init_black = _black
        self.neighbours = []
        self.drawn_balls = deque()
        self.red = _red
        self.black = _black

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

    def add_neightbour(self, neighbour):
        self.neighbours.append(neighbour)

    def get_ball(self, index):
        if index > self.red + self.black:
            return None
        elif index < self.red:
            return 'r'
        elif index < self.black:
            return 'b'
        return self.drawn_balls[index - self.init_black - self.init_red]

    def __iter__(self):
        return self.neighbours
