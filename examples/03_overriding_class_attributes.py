"""03 - Overriding class attributes in Python.

Use inheritance to override a class attribute of the Person class and call
method of base class.
"""

import typing


class Person:
    """A person has a name and likes to do things."""

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def stay_hydrated(self) -> None:
        print(f"{self} drinks some water. 🚰")

    def go_to_the_movies(self) -> None:
        print(f"{self} goes to the movies. 🍿")

    def go_hiking(self) -> None:
        print(f"{self} goes hiking. ⛰")

    def build_a_robot(self) -> None:
        print(f"{self} builds a robot. 🤖")


class Project:
    """A project has a board_name and a description."""

    def __init__(self, board_name: str, description: str):
        self.board_name = board_name
        self.description = description

    def __str__(self) -> str:
        return f"Project '{self.board_name}'"


class TeamMember(Person):
    """A team member is a person, who works on projects, and may have
    specialized in a specific field.
    """

    expertise: typing.Optional[str] = None

    def __str__(self) -> str:
        # Get default string representation from the super class
        default = super().__str__()

        if self.expertise is None:
            return f"{default}"

        return f"{self.expertise} {default}"

    def work_on_project(self, project: Project) -> None:
        """Start working on the given project."""
        print(f"{self} is now working on {project}. 📋")
        self.stay_hydrated()


class MobileEngineer(TeamMember):
    """Team member specialized in developing for mobile platforms."""

    expertise = "📱"


class DataScientist(TeamMember):
    """Team member specialized in data science."""

    expertise = "📈"


class ProjectManager(TeamMember):
    """Team member specialized in project management."""

    expertise = "📝"


class OperationsEngineer(TeamMember):
    """Team member specialized in running cloud infrastructure."""

    expertise = "📦"


if __name__ == "__main__":
    simone = OperationsEngineer("Simone")
    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()

    chelsea = DataScientist("Chelsea")
    dave = ProjectManager("Dave")
    marlene = MobileEngineer("Marlene")

    data_platform = Project(
        board_name="Data Platform",
        description="Platform providing datasets and data viewing tools.",
    )
    simone.work_on_project(data_platform)
    chelsea.work_on_project(data_platform)
    dave.work_on_project(data_platform)
    marlene.work_on_project(data_platform)
