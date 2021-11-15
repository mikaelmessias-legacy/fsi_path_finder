class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

        self.solid_ground = []
        self.rocky_ground = []
        self.sandy_ground = []
        self.marsh_ground = []

        self.rewards = []
        self.weights = {}

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls or id in self.rewards

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]

        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics

        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)

        return results

    def cost(self, from_node, to_node):
        return self.weights.get(to_node)

    def validate_state(self, state):
        (x, y) = state

        if state in self.walls:
            return False, False
        elif x <= 0 or x >= self.width or y <= 0 or y >= self.height:
            return False, True

        return True, False
