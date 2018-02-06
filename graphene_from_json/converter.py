import re

from graphene import (ID, Boolean, Dynamic, Enum, Field, Float, Int, List,
                      NonNull, String, UUID, is_node)
from textblob import Word


mapper = {
    'integer': Int(),
    'string': String()
}

def convert(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    word = Word(re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower())
    return word.singularize()

