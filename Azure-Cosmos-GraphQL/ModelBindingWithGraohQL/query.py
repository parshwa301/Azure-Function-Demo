import graphene
from models.model import *
from resolver import *

class Query(graphene.ObjectType):

    firdsdata = graphene.Field(graphene.List(Firds))

    fitrsdata = graphene.Field(graphene.List(Fitrs))

    def resolve_firdsdata(root, info):

        return Demo().firdsData()
    
    def resolve_fitrsdata(root, info):

        return Demo().fitrsdData()
