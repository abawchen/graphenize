from graphene import Field, Int, List, String

from .model import Model

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

