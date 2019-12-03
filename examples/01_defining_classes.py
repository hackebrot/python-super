"""01 - Define a class in Python."""


class Person:
    """A person has a name and likes to do things."""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}"

    def go_to_the_movies(self):
        print(f"{self} goes to the movies. 🍿")

    def go_hiking(self):
        print(f"{self} goes hiking. ⛰")

    def build_a_robot(self):
        print(f"{self} builds a robot. 🤖")


if __name__ == "__main__":
    simone = Person("Simone")
    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()
