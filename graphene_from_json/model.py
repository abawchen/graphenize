from .registry import get_global_registry

registry = get_global_registry()

class Model(object):

    def __init__(self, name, json_schema):
        self.name = name
        self.fields = {}

        root_type = json_schema.get('type')
        if root_type == 'object':
            map(self._add_field, json_schema.get('properties').items())
        # elif root_type == 'array':
        #    pass
        registry.models.append(self)

    def _add_field(self, field):
        # TODO: Refactor
        (field_name, field_schema) = field
        field_type = field_schema.get('type')
        if field_type == 'object':
            self.fields[field_name] = Model(field_name, field_schema)
        elif field_type == 'array':
            items = field_schema.get('items')
            items_type = items.get('type')
            if items_type == 'object':
                self.fields[field_name] = [Model(field_name, items)]
            else:
                self.fields[field_name] = [items_type]
        else:
            self.fields[field_name] = field_type


