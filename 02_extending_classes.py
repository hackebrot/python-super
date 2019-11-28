"""02 - Extending a class in Python.

Use inheritance to extend the Person class.
"""


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


class Project:
    """A project has a board_name and a description."""

    def __init__(self, board_name: str, description: str):
        self.board_name = board_name
        self.description = description

    def __repr__(self) -> str:
        return f"Project '{self.board_name}'"


class TeamMember(Person):
    """A team member is a person, who works on projects."""

    def work_on_project(self, project: Project):
        print(f"{self} is now working on {project}. 📋")


if __name__ == "__main__":
    simone = TeamMember("Simone")
    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()

    data_platform = Project(
        board_name="Data Platform",
        description="Platform providing datasets and data viewing tools.",
    )
    simone.work_on_project(data_platform)
