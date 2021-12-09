from random import randrange

from zntrack import Node, dvc, zn


@Node()
class RandRange:
    maximum = dvc.params()
    number = zn.metrics()

    def __call__(self, maximum):
        self.maximum = maximum

    def run(self):
        self.number = {"number": randrange(self.maximum)}


if __name__ == "__main__":
    rand_range = RandRange()
    rand_range(4096)
