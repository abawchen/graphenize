from genson import SchemaBuilder

from .model import Model
from .registry import get_global_registry

registry = get_global_registry()


class Builder(SchemaBuilder):

    def __init__(self,
                 root_model_name,
                 registry=get_global_registry(),
                 schema_uri='DEFAULT'):
        super(Builder, self).__init__(schema_uri)
        self.root_model_name = root_model_name

    def to_models(self, filename=None):
        json_schema = super(Builder, self).to_schema()
        root_type = json_schema.get('type')
        if root_type == 'array':
            Model(self.root_model_name, json_schema.get('items'))
        else:
            Model(self.root_model_name, json_schema)

        # TODO: Refactor
        models = {}
        for model in registry.models:
            model.graphenize()
            models[model.klass._meta.name] = model

        if filename is not None:
            declaration = 'import graphene{}'.format('\n' * 3)
            declaration += '\n\n'.join(map(lambda m: m.persist(), registry.models))
            with open(filename, 'w') as f:
                f.write(declaration)

        return models
