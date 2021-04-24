import graphene
from ModelBindingWithGraohQL.models.base import * 
from ModelBindingWithGraohQL.models.employee import * 

class Firds(graphene.ObjectType):
    class Meta:
        interfaces = (Base, )

    department = graphene.String()
    employeeDetail = graphene.List(Employee)