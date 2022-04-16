class Array:

    def __init__(self, capacity, fill_value=None):
        # Array based on list built-in
        self.items = list()

        # Set default items
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)