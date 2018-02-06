import re

from graphene import (ID, Boolean, Dynamic, Enum, Field, Float, Int, List,
                      NonNull, ObjectType, String, UUID, is_node)
from textblob import Word


mapper = {
    'integer': Int(),
    'string': String()
}


def convert(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    word = Word(re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower())
    return word.singularize()


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def ClassFactory(name, fields, BaseClass=ObjectType):
    """
    https://stackoverflow.com/a/15247892/9041712
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s"
                    % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])
    newclass = type(name, (BaseClass,), merge_two_dicts({"__init__": __init__}, fields))
    return newclass

