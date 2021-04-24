import graphene
from ModelBindingWithGraohQL.models.firds import *
from ModelBindingWithGraohQL.models.fitrs import *
from ModelBindingWithGraohQL.resolver import *

class Query(graphene.ObjectType):

    firdsdata = graphene.Field(graphene.List(Firds))

    fitrsdata = graphene.Field(graphene.List(Fitrs))

    def resolve_firdsdata(root, info):

        return Demo().firdsData()
    
    def resolve_fitrsdata(root, info):

        return Demo().fitrsdData()
