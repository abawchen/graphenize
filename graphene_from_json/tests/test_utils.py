from graphene import ID, String

from ..utils import (ClassFactory, merge_two_dicts,
                     to_camel_case, to_singular)


def test_to_singular_dogs():
    assert to_singular('dogs') == 'dog'


def test_to_singular_all_dogs():
    assert to_singular('all_dogs') == 'all_dog'


def test_to_camel_case():
    assert to_camel_case('camel_case') == 'CamelCase'


def test_merge_two_dicts():
    x = {'x': 'x'}
    y = {'y': 1}
    expected = {
        'x': 'x',
        'y': 1
    }
    assert dict(merge_two_dicts(x, y)) == expected


def test_class_factory_generation():
    fields = {
        'id': ID(),
        'first_name': String()
    }
    User = ClassFactory("User", fields)
    assert isinstance(User.id, ID)
    assert isinstance(User.first_name, String)

