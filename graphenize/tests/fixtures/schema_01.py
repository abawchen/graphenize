import graphene


class Job(graphene.ObjectType):

    type = graphene.String()
    years = graphene.Int()


class Cat(graphene.ObjectType):

    age = graphene.Int()
    name = graphene.String()


class User(graphene.ObjectType):

    cats = graphene.List(Cat)
    dogs = graphene.List(String)
    favorite_color = graphene.String()
    id = graphene.Int()
    job = graphene.Field(Job)
    name = graphene.String()

class Query(graphene.ObjectType):

    user = graphene.Field(User)

    def resolve_user(self, *args, **kwargs):
        pass

