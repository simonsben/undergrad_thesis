from utilities.utilities import balls_added


# Class definition for a polya node
class polya_node:
    def __init__(self, _red, _black, _id):
        self.init_red = _red                     # Initial number of red balls
        self.init_black = _black                 # Initial number of black balls
        self.init_total = _red + _black

        self.red = _red                          # Running total of red balls
        self.black = _black                      # Running total of black balls
        self.last_red = _red
        self.last_black = _black

        self.neighbours = []                     # List of neighbouring nodes
        self.drawn_balls = []                    # List of added balls
        self.degree = 0                          # Degree of node

        self.id = _id                            # Node ID
        self.current_n = -1                      # Utility value for iterating on node (see methods)

    # Add ball to urn
    def add_ball(self, ball, full_memory=True):
        self.drawn_balls.append(ball)  # Add drawn ball

        # Add ball to node's current count
        if ball == 0:
            self.red += balls_added
        else:
            self.black += balls_added

        if not full_memory:
            # TODO implement finite memory thang
            raise ValueError('Have yet to implement...')

    # Add neighbour to node
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
        self.degree = len(self.neighbours)
        self.super_urn_balls += neighbour.init_total

    def add_neighbours(self, neighbours):
        self.neighbours = neighbours
        self.degree = len(self.neighbours)

    # Returns whether the node is a leaf node
    def is_leaf(self):
        return len(self.neighbours) == 1

    def lock_optimization(self):
        self.init_red = self.last_red = self.red
        self.init_black = self.last_black = self.black

    def lock_step(self):
        self.last_red = self.red
        self.last_black = self.black

    def clear_node(self):
        self.last_red = self.red = self.init_red
        self.last_black = self.black = self.init_black
        self.drawn_balls = []

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
