import click

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')


if __name__ == '__main__':
    cli()

