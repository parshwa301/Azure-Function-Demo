import graphene

class Base(graphene.Interface):
    id = graphene.ID()
    name = graphene.String()