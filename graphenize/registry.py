class Registry(object):

    def __init__(self):
        self.models = []
        self._registry = {}

    def register(self, field_type, graphene_type):
        self._registry[field_type] = graphene_type

    def get_type(self, field_type):
        return self._registry.get(field_type)


registry = None


def get_global_registry():
    global registry
    if not registry:
        registry = Registry()
    return registry


def reset_global_registry():
    global registry
    registry = None
