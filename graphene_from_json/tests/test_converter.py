from ..converter import convert


def test_convert_camel_case():
    assert convert('CamelCase') == 'camel_case'


def test_convert_plural():
    assert convert('dogs') == 'dog'


def test_convert_camel_case_plural():
    assert convert('allDogs') == 'all_dog'

