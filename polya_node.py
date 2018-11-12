from collections import deque
from utilities import network_memory
from utilities import balls_added


# Class definition for a polya node
class polya_node:
    def __init__(self, _red, _black, _id):
        self.init_red = _red                     # Initial number of red balls
        self.init_black = _black                 # Initial number of black balls
        self.total_balls = _red + _black         # Total number of initial balls in node
        self.super_urn_balls = self.total_balls  # Total number of balls in super urn (base)
        self.red = _red                          # Running total of red balls
        self.black = _black                      # Running total of black balls
        self.weight = _red / self.total_balls    # Fraction of red to total balls

        self.neighbours = []                     # List of neighbouring nodes
        self.drawn_balls = deque()               # List of added balls
        self.degree = 0                          # Degree of node

        self.id = _id                            # Node ID
        self.current_n = -1                      # Utility value for iterating on node (see methods)

    # Add ball to urn
    def add_ball(self, ball):
        self.drawn_balls.append(ball)  # Add drawn ball

        # Add ball to node's current count
        if ball == 'r':
            self.red += balls_added
        else:
            self.black += balls_added

        # If drawn ball is farther back then network memory, forget it
        while len(self.drawn_balls) > network_memory:
            removed = self.drawn_balls.popleft()

            if removed == 'r':
                self.red -= 1
            else:
                self.black -= 1
        self.update_weight()

    # Add neighbour to node
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
        self.degree = len(self.neighbours)
        self.super_urn_balls += neighbour.total_balls

    # Update the weight of the node based on the new balls
    def update_weight(self):
        self.weight = self.red / (self.red + self.black)

    # Returns whether the node is a leaf node
    def is_leaf(self):
        return len(self.neighbours) == 1

    # Returns the number of red balls at the given step
    def get_red_count(self, step):
        num_red = self.red
        if step >= len(self.drawn_balls) and step > 0:
            new_red_count = 0
            for i in range(step, len(self.drawn_balls)):
                if self.drawn_balls[i] == 'r':
                    new_red_count += balls_added
            num_red -= new_red_count

        return num_red

    # Base method to allow iteration on object
    def __iter__(self):
        self.current_n = -1
        return self

    # Runs through the iteration of the object
    def __next__(self):
        self.current_n += 1
        if self.current_n >= len(self.neighbours):
            raise StopIteration
        return self.neighbours[self.current_n]

    # toString method
    def __str__(self):
        return str(self.black) + 'b' + str(self.red) + 'r (' + str(self.degree) + ')'
