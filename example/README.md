Example Graphenize Usage
================================


Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the
whole Graphene repository:

```bash
# Get the example project code
git clone git@github.com:abawchen/graphenize.git
cd graphene-mongo/example
```

It is good idea (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to keep things simple,
but you may also find something like
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to be useful:

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

Now the following command will generate corresponding models from sample.json:

```bash
graphenize --input sample.json --root user
```

Then you will get `models.py` as follows:

```python
import graphene


class Job(graphene.ObjectType):

    type = graphene.String()
    years = graphene.Int()


class Cat(graphene.ObjectType):

    age = graphene.Int()
    name = graphene.String()


class User(graphene.ObjectType):

    cats = graphene.List(Cat)
    dogs = graphene.List(graphene.String)
    favorite_color = graphene.String()
    id = graphene.Int()
    job = graphene.Field(Job)
    name = graphene.String()
```
