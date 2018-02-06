from graphene import ID, String

from ..utils import (ClassFactory, to_singular_camel_case,
                     to_singular_underscore, merge_two_dicts)


def test_convert_name_camel_case():
    assert to_singular_underscore('CamelCase') == 'camel_case'


def test_to_singular_underscore_plural():
    assert to_singular_underscore('dogs') == 'dog'


def test_to_singular_underscore_camel_case_plural():
    assert to_singular_underscore('allDogs') == 'all_dog'


def test_to_singular_camel_case():
    assert to_singular_camel_case('camel_case') == 'CamelCase'


def test_to_singular_camel_case_plural():
    assert to_singular_camel_case('all_dogs') == 'AllDog'


def test_convert_type_integer():
    pass

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

