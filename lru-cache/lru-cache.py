from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.odict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.odict:
            return -1
        else:
            self.odict.move_to_end(key)
            return self.odict[key]

    def put(self, key, value):
        if key in self.odict:
            self.odict[key] = value
            self.odict.move_to_end(key)
        else:
            self.odict[key] = value
            if len(self.odict) > self.capacity:
                self.odict.popitem(last = False)