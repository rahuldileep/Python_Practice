from collections.abc import Iterable, Iterator

class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.pos = 0

    def __next__(self):
        try:
            value = self.collection[self.pos]
            self.pos +=  1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection():
    def __init__(self):
        self.collection = []

    def __iter__(self):
        return AlphabeticalOrderIterator(self.collection)

    def add_item(self,item):
        self.collection.append(item)

collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")
