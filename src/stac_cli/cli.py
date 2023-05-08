import click


@click.group()
@click.version_option()
def stac() -> None:
    pass


@stac.command()
def hello() -> None:
    click.echo("Hello World!")


if __name__ == "__main__":
    stac()
