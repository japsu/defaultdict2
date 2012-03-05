from collections import defaultdict

class defaultdict2(defaultdict):
    def __missing__(self, key):
        value = self.default_factory(key)
        self[key] = value
        return value
        
