import json

from genson import SchemaBuilder
from graphene import Field
from graphene.utils.str_converters import to_snake_case

from .converter import convert
from .model import Model
from .utils import ClassFactory, to_camel_case
from .registry import get_global_registry

registry = get_global_registry()

class Builder(SchemaBuilder):

    def __init__(self,
                 root_model_name,
                 registry=get_global_registry(),
                 schema_uri='DEFAULT'):
        super(Builder, self).__init__(schema_uri)
        self.root_model_name = root_model_name
        self.registry = registry

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
            classname = to_camel_case(model.name)
            fields = dict(
                (to_snake_case(kv[0]), convert(kv[1], registry)) for kv in model.fields.items()
            )
            Class = ClassFactory(classname, fields)
            registry.register(model, Class)
            klasses[classname] = Class

        return klasses

    def serialize(self):
        pass

