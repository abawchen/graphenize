import decorator
import os
import json
import pytest

from graphene import Field, Int, List, String

from ..builder import Builder

dir_path = os.path.dirname(os.path.realpath(__file__))

@pytest.fixture
def json_loader():
    def _loader(filename):
        filename = os.path.join(dir_path, filename)
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    return _loader

def test_builder_complex_object(json_loader):
    obj = json_loader('data/example_01.json')
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    klasses = builder.to_graphql_schema()

    JobType = klasses.get('Job')
    assert isinstance(JobType.type, String)
    assert isinstance(JobType.years, Int)

    CatType = klasses.get('Cat')
    assert isinstance(CatType.name, String)
    assert isinstance(CatType.age, Int)

    UserType = klasses.get('User')
    assert isinstance(UserType.id, Int)
    assert isinstance(UserType.name, String)
    assert isinstance(UserType.favorite_color, String)
    assert isinstance(UserType.job, Field)
    assert UserType.job._type == JobType
    assert isinstance(UserType.dogs, List)
    assert UserType.dogs._of_type == String
    assert isinstance(UserType.cats, List)
    assert UserType.cats._of_type == CatType


def test_builder_array_root(json_loader):
    obj = json_loader('data/example_02.json')
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    schema = builder.to_graphql_schema()
    # pprint(schema)
    print(json.dumps(schema))
    assert True

