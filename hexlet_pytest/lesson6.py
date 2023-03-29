class Right(object):

    def __init__(self):
        self.items = []

    def add_item(self, good, count):
        self.items.append({'good': good, 'count': count})

    def get_items(self):
        return self.items

    def get_count(self):
        return sum(good['count'] for good in self.items)

    def get_cost(self):
        return sum(good['count'] * good['good']['price'] for good in self.items)
