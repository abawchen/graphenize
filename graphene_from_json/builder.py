import json

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

    def to_graphene_klasses(self):
        json_schema = super(Builder, self).to_schema()
        root_type = json_schema.get('type')
        if root_type == 'array':
            Model(self.root_model_name, json_schema.get('items'))
        else:
            Model(self.root_model_name, json_schema)

        # TODO: Refactor
        klasses = {}
        for model in registry.models:
            model.klassilize()
            klasses[model.klass._meta.name] = model.klass

        return klasses
