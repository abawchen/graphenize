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
        filename = os.path.join(dir_path, 'fixtures', filename)
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    return _loader

def test_builder_complex_object(json_loader):
    obj = json_loader('example_01.json')
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    klasses = builder.to_graphene_klasses()

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
    obj = json_loader('example_02.json')
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    klasses = builder.to_graphene_klasses()

    CompanyType = klasses.get('Company')
    assert isinstance(CompanyType.name, String)
    assert isinstance(CompanyType.catch_phrase, String)
    assert isinstance(CompanyType.bs, String)

    GeoType = klasses.get('Geo')
    assert isinstance(GeoType.lat, String)
    assert isinstance(GeoType.lng, String)

    AddressType = klasses.get('Address')
    assert isinstance(AddressType.street, String)
    assert isinstance(AddressType.suite, String)
    assert isinstance(AddressType.city, String)
    assert isinstance(AddressType.city, String)
    assert isinstance(AddressType.zipcode, String)
    assert isinstance(AddressType.geo, Field)
    assert AddressType.geo._type == GeoType

    UserType = klasses.get('User')
    assert isinstance(UserType.id, Int)
    assert isinstance(UserType.username, String)
    assert isinstance(UserType.email, String)
    assert isinstance(UserType.phone, String)
    assert isinstance(UserType.website, String)
    assert isinstance(UserType.address, Field)
    assert UserType.address._type == AddressType
    assert isinstance(UserType.company, Field)
    assert UserType.company._type == CompanyType

