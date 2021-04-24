import graphene

class Address(graphene.ObjectType):

    street = graphene.String()

    city = graphene.String()

    state = graphene.String()

    pincode = graphene.Int()