import random
import click


@click.command()
@click.version_option(version="0.1")
def main():
    click.echo("Hello, world!")


def foo(
    name: str,
    age: int,
    admin: bool,
    is_as_cool_as_chris: bool,
) -> float:
    total: float = sum([random.random() for _ in range(5)])
    return total


def eh() -> bool:
    print("...")

    return True


class Rectagle:
    def __init__(self, width: float, length: float) -> None:
        self.width = width
        self.length = length

    @property
    def area(self) -> float:
        return self.width * self.area


def give_me_a_rectangle() -> Rectagle:
    return Rectagle(1, 2)
