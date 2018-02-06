from graphene import ID, String

from ..converter import ClassFactory, convert, merge_two_dicts


def test_convert_camel_case():
    assert convert('CamelCase') == 'camel_case'


def test_convert_plural():
    assert convert('dogs') == 'dog'


def test_convert_camel_case_plural():
    assert convert('allDogs') == 'all_dog'



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

