class LRUCache:

        # @param capacity, an integer
        def __init__(self, capacity):
             self.capacity = capacity
             self.cache = collections.OrderedDict()

        # @return an integer
        def get(self, key):
            try:
                # try popping element out
                value = self.cache.pop(key)
                self.cache[key] = value
                return value
            except KeyError:
                return -1
                
        # @param key, an integer
        # @param value, an integer
        # @return nothing
        def set(self, key, value):
            # Try popping it anyways, regardless of if key is actually in there
            try:
                self.cache.pop(key)
            # If cannot be found in cache
            except KeyError:
                # Check capacity
                if len(self.cache) == self.capacity:
                    self.cache.popitem(last=False)
            self.cache[key] = value
                
