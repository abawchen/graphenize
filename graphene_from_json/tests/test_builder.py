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

@pytest.fixture
def file_loader():

    def _loader(folder, filename):
        filename = os.path.join(dir_path, folder, filename)
        with open(filename, 'r') as f:
            return f.read()

    return _loader


def get_build_filepath(filename):
    return os.path.join(dir_path, 'build', filename)


def test_builder_to_model_complex_object(json_loader, file_loader):
    obj = json_loader('example_01.json')
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    models = builder.to_models()

    job = models.get('Job')
    JobType = job.klass
    assert isinstance(JobType.type, String)
    assert isinstance(JobType.years, Int)

    job.persist(get_build_filepath('job.py'))
    expected_py = file_loader('fixtures', 'job.py')
    built_py = file_loader('build', 'job.py')
    assert built_py == expected_py

    cat = models.get('Cat')
    CatType = cat.klass
    assert isinstance(CatType.name, String)
    assert isinstance(CatType.age, Int)

    cat.persist(get_build_filepath('cat.py'))
    expected_py = file_loader('fixtures', 'cat.py')
    built_py = file_loader('build', 'cat.py')
    assert built_py == expected_py

    user = models.get('User')
    UserType = user.klass
    assert isinstance(UserType.id, Int)
    assert isinstance(UserType.name, String)
    assert isinstance(UserType.favorite_color, String)
    assert isinstance(UserType.job, Field)
    assert UserType.job._type == JobType
    assert isinstance(UserType.dogs, List)
    assert UserType.dogs._of_type == String
    assert isinstance(UserType.cats, List)
    assert UserType.cats._of_type == CatType

    user.persist(get_build_filepath('user.py'))
    expected_py = file_loader('fixtures', 'user.py')
    built_py = file_loader('build', 'user.py')
    assert built_py == expected_py


def test_builder_to_model_array_root(json_loader):
    obj = json_loader('example_02.json')
    builder = Builder(root_model_name='user')
    builder.add_object(obj)
    models = builder.to_models()

    CompanyType = models.get('Company').klass
    assert isinstance(CompanyType.name, String)
    assert isinstance(CompanyType.catch_phrase, String)
    assert isinstance(CompanyType.bs, String)

    GeoType = models.get('Geo').klass
    assert isinstance(GeoType.lat, String)
    assert isinstance(GeoType.lng, String)

    AddressType = models.get('Address').klass
    assert isinstance(AddressType.street, String)
    assert isinstance(AddressType.suite, String)
    assert isinstance(AddressType.city, String)
    assert isinstance(AddressType.city, String)
    assert isinstance(AddressType.zipcode, String)
    assert isinstance(AddressType.geo, Field)
    assert AddressType.geo._type == GeoType

    UserType = models.get('User').klass
    assert isinstance(UserType.id, Int)
    assert isinstance(UserType.username, String)
    assert isinstance(UserType.email, String)
    assert isinstance(UserType.phone, String)
    assert isinstance(UserType.website, String)
    assert isinstance(UserType.address, Field)
    assert UserType.address._type == AddressType
    assert isinstance(UserType.company, Field)
    assert UserType.company._type == CompanyType
