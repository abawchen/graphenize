import json

from genson import SchemaBuilder
from textblob import Word


class Builder(SchemaBuilder):

    def __init__(self, root_model_name, schema_uri='DEFAULT'):
        super(Builder, self).__init__(schema_uri)
        self.models = []
        self.root_model_name = root_model_name

    def to_graphql_schema(self):
        json_schema = super(Builder, self).to_schema()
        # print(json.dumps(json_schema))
        root_type = json_schema.get('type')
        # print('root_type: ' + root_type)
        Model(self.root_model_name, json_schema, self.models)
        # print(model)
        return json_schema

class Model(object):

    def __init__(self, name, json_schema, models):
        self.name = name
        self.fields = {}

        root_type = json_schema.get('type')
        if root_type == 'object':
            map(self._add_field, json_schema.get('properties').items())
        elif root_type == 'array':

        models.append(self)

    def _add_field(self, field):
        (field_name, field_schema) = field
        field_type = field_schema.get('type')
        if field_type == 'object':
            self.fields[field_name] = Model(field_name, field_schema)
        elif field_type == 'array':
            items = field_schema.get('items')
            items_type = items.get('type')
            if items_type == 'object':
                field_name = Word(field_name).singularize()
                self.fields[field_name] = 'listof({})'.format(Model(field_name, items))
            else:
                self.fields[field_name] = 'listof({})'.format(items_type)
        else:
            self.fields[field_name] = field_type

    def serialize(self):
        pass

    def __str__(self):
        return '{name}:\n{fields}'.format(name=self.name, fields=self.fields)

