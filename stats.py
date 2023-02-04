class DataCapture:
    def __init__(self):
        self.values = []
        self.counts = [0] * 1000
        self.built = False
    
    def add(self, value):
        self._validate_input(value)
        self.values.append(value)
        self.counts[value-1] += 1

    def build_stats(self):
        self.built = True
        return self

    def _check_built(self):
        if not self.built:
            raise Exception("Statistics not built yet. Call build_stats() first.")

    def less(self, value):
        self._check_built()
        self._validate_input(value)
        return sum(self.counts[:value-1])

    def greater(self, value):
        self._check_built()
        self._validate_input(value)
        return sum(self.counts[value:])

    def between(self, start, end):
        self._check_built()
        self._validate_input(start)
        self._validate_input(end)
        return sum(self.counts[start-1:end])

    def _validate_input(self, value):
        if not isinstance(value, int) or value <= 1 or value >= 1000:
            raise ValueError("Invalid input. Value must be an integer between 1 and 999.")
