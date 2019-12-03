"""04 - Inject functionality into a class in Python.

Use multiple inheritance to override functionality on base classes.
"""

import contextlib
import typing


class Person:
    """A person has a name and likes to do things."""

    def __init__(self, *, name: str, **kwargs: typing.Any):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}"

    def stay_hydrated(self):
        print(f"{self} drinks some water. 🚰")

    def go_to_the_movies(self):
        print(f"{self} goes to the movies. 🍿")

    def go_hiking(self):
        print(f"{self} goes hiking. ⛰")

    def build_a_robot(self):
        print(f"{self} builds a robot. 🤖")


class TeaPerson(Person):
    def stay_hydrated(self):
        print(f"{self} drinks tea. 🍵")


class Project:
    """A project has a board_name and a description."""

    def __init__(self, board_name: str, description: str):
        self.board_name = board_name
        self.description = description

    def __repr__(self) -> str:
        return f"Project '{self.board_name}'"


class TeamMember(Person):
    """A team member is a person, who works on projects, and may have
    specialized in a specific field.
    """

    expertise: typing.Optional[str] = None

    def __repr__(self) -> str:
        # Get default repr from super class
        default = super().__repr__()

        if self.expertise is None:
            return f"{default}"

        return f"{self.expertise} {default}"

    @contextlib.contextmanager
    def commute(self):
        """Commute to the office and back."""
        print(f"{self} commutes to the office. 🏢")
        yield
        print(f"{self} commutes home. 🏡")

    def work_on_project(self, project):
        """Start working on the given project."""
        with self.commute():
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


class RemoteTeamMember(TeamMember):
    def __init__(self, *, workplace: str, **kwargs: typing.Any):
        self.workplace = workplace
        # Forward kwargs to super class
        super().__init__(**kwargs)

    @contextlib.contextmanager
    def commute(self):
        """Stay at home or commute to the workplace and back."""

        if self.workplace == "home":
            print(f"{self} works from home. 🏡")
            yield
            return

        print(f"{self} commutes to {self.workplace}. 🚌")
        yield
        print(f"{self} commutes home. 🏡")


class DataScientistWhoLikesTea(DataScientist, TeaPerson):
    """Data scientist who prefers tea over water."""


class ProjectManagerWhoWorksRemotely(ProjectManager, RemoteTeamMember):
    """Project manager who works remotely."""


class MobileEngineerWhoWorksRemotelyAndLikesTea(
    MobileEngineer, RemoteTeamMember, TeaPerson
):
    """Mobile engineer who works remotely and prefers tea over water."""


if __name__ == "__main__":
    simone = OperationsEngineer(name="Simone")
    simone.go_to_the_movies()
    simone.build_a_robot()
    simone.go_hiking()

    chelsea = DataScientistWhoLikesTea(name="Chelsea")
    dave = ProjectManagerWhoWorksRemotely(name="Dave", workplace="a local coffee shop")
    marlene = MobileEngineerWhoWorksRemotelyAndLikesTea(
        name="Marlene", workplace="home"
    )

    data_platform = Project(
        board_name="Data Platform",
        description="Platform providing datasets and data viewing tools.",
    )
    simone.work_on_project(data_platform)
    chelsea.work_on_project(data_platform)
    dave.work_on_project(data_platform)
    marlene.work_on_project(data_platform)
