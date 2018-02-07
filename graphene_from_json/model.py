from graphene import Field, Int, List, String
from graphene.utils.str_converters import to_snake_case

from .registry import get_global_registry
from .utils import ClassFactory, to_camel_case, to_singular

registry = get_global_registry()

native_type = {
    'integer': Int,
    'string': String
}


def convert(field_type, registry):
    # TODO: Refactor
    if isinstance(field_type, list):
        if field_type[0] in native_type:
            return List(type(convert(field_type[0], registry)))

        if isinstance(field_type[0], Model):
            return List(registry.get_type(field_type[0]))

    if field_type in native_type:
        return native_type.get(field_type)()

    if isinstance(field_type, Model):
        return Field(registry.get_type(field_type))

    return registry.get_type(field_type)


class Model(object):

    def __init__(self, name, json_schema):
        self.name = str(name)
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
                self.fields[field_name] = [Model(to_singular(field_name), items)]
            else:
                self.fields[field_name] = [items_type]
        else:
            self.fields[field_name] = field_type

    def graphenize(self):
        klassname = to_camel_case(self.name)
        fields = dict(
            (to_snake_case(kv[0]), convert(kv[1], registry)) for kv in self.fields.items()
        )
        self.klass = ClassFactory(klassname, fields)
        registry.register(self, self.klass)

    def persist(self):
        declaration = 'class {}(graphene.ObjectType):\n\n'.format(self.klass._meta.name)
        for name in self.fields.keys():
            declaration += self.persist_attribute(name, getattr(self.klass, name))
        print(declaration)

    def persist_attribute(self, name, graphene_type):
        declaration = '\t{} = graphene.{}()\n'.format(name, type(graphene_type))
        return declaration

