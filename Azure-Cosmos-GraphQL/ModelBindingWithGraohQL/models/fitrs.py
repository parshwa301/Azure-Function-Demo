import graphene
from ModelBindingWithGraohQL.models.base import * 

class Fitrs(graphene.ObjectType):
    class Meta:
        interfaces = (Base, )

    fileType = graphene.String()