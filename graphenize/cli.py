import click
import json

from .builder import Builder


@click.command()
@click.option('--input', required=True, help='input path of json data')
@click.option('--output', default='models.py', help='file path of output models')
@click.option('--root', default='obj', help='root model name')
def cli(input, output, root):
    """Generate Graphene models from json data"""

    with open(input, 'r') as f:
        obj = json.load(f)

    builder = Builder(root_model_name=root)
    builder.add_object(obj)
    builder.to_models(output)


if __name__ == '__main__':
    cli()
