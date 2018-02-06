import decorator
import os
import json
import pytest

from pprint import pprint

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

def test_builder_01(json_loader):
    obj = json_loader('data/example_01.json')
    # pprint(json)
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    schema = builder.to_graphql_schema()
    # print(json.dumps(schema))
    assert True

def test_builder_02(json_loader):
    # obj = json_loader('data/example_02.json')
    # pprint(json)
    # builder = Builder(root_model_name='user')
    # builder.add_object(obj)
    # schema = builder.to_graphql_schema()
    # pprint(schema)
    # print(json.dumps(schema))
    assert True

