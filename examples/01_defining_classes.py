# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""01 - Define a class in Python."""


class Person:
    """A person has a name and likes to do things."""

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def go_to_the_movies(self) -> None:
        print(f"{self} goes to the movies. 🍿")

    def go_hiking(self) -> None:
        print(f"{self} goes hiking. ⛰")

    def build_a_robot(self) -> None:
        print(f"{self} builds a robot. 🤖")


if __name__ == "__main__":
    simone = Person("Simone")
    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()
