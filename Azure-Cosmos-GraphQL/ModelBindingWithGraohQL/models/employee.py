import graphene
from ModelBindingWithGraohQL.models.address import * 

class Employee(graphene.ObjectType):

    salary = graphene.Float()
    address = graphene.List(Address)