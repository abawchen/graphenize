class User(graphene.ObjectType):

    cats = graphene.List(Cat)
    dogs = graphene.List(graphene.String)
    favorite_color = graphene.String()
    id = graphene.Int()
    job = graphene.Field(Job)
    name = graphene.String()
