def add(*args):
    print(sum(args))


add(1, 2, 3, 4, 5)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(n=2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"] # Code will have error if model is not initialized
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        # get() returns None if the element is not present


car1 = Car(make="Nissan")
print(car1.model)
