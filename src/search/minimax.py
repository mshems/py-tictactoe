

class MiniMaxSearch(object):
    def __init__(self):
        self.count = 0
        self.explored = set()

    def max_value(self, state, a, b):
        self.count += 1
        value = float('-inf')

        if state in self.explored:
            return state.evaluate()

        if state.terminal():
            self.explored.add(state)
            return state.evaluate()

        for action in state.actions():
            result = state.result(action)

            if result in self.explored:
                return state.evaluate()

            value = max(value, self.min_value(result, a, b))
            self.explored.add(result)

            if value >= b:
                return value
            else:
                a = max(a, value)
        return value

    def min_value(self, state, a, b):
        self.count += 1
        value = float('inf')

        if state in self.explored:
            return state.evaluate()

        if state.terminal():
            self.explored.add(state)
            return state.evaluate()

        for action in state.actions():
            result = state.result(action)

            if result in self.explored:
                return state.evaluate()

            value = min(value, self.max_value(result, a, b))
            self.explored.add(result)

            if value <= a:
                return value
            else:
                b = min(b, value)
        return value

    def decide_min(self, state):
        self.count = 0
        best = self.max_value(state, float('-inf'), float('inf'))
        for action in state.actions():
            if best == self.min_value(state.result(action), float('-inf'), float('inf')):
                print self.count
                return action
