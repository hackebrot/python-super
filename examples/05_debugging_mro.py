"""05 - Debug the Method Resolution Order of Python.

Use a metaclass to decorate methods of Person and its subclasses.
"""

import contextlib
import typing

import wrapt


@wrapt.decorator
def log_call(wrapped_method, instance, args, kwargs) -> typing.Any:
    """Print when the decorated method is called."""
    method_name = wrapped_method.__qualname__
    class_name = instance.__class__.__qualname__
    print(f"Calling method {method_name} for {class_name}.")
    return wrapped_method(*args, **kwargs)


class LogMethods(type):
    """Metaclass that decorates methods with log_call."""

    def __new__(cls, name, bases, attrs, **kwargs):
        for attr, value in attrs.items():
            if not callable(value):
                continue
            attrs[attr] = log_call(value)
        return super().__new__(cls, name, bases, attrs, **kwargs)


class Person(metaclass=LogMethods):
    """A person has a name and likes to do things."""

    def __init__(self, *, name: str, **kwargs: typing.Any):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}"

    def stay_hydrated(self) -> None:
        print(f"{self} drinks some water. 🚰")

    def go_to_the_movies(self) -> None:
        print(f"{self} goes to the movies. 🍿")

    def go_hiking(self) -> None:
        print(f"{self} goes hiking. ⛰")

    def build_a_robot(self) -> None:
        print(f"{self} builds a robot. 🤖")


class TeaPerson(Person):
    def stay_hydrated(self) -> None:
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
    def commute(self) -> typing.Generator:
        """Commute to the office and back."""
        print(f"{self} commutes to the office. 🏢")
        yield
        print(f"{self} commutes home. 🏡")

    def work_on_project(self, project) -> None:
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
