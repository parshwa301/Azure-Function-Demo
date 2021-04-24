import graphene

class Base(graphene.Interface):
    id = graphene.ID()
    name = graphene.String()

    # @classmethod
    # def resolve_type(cls, instance, info):
    #     if instance.type == 'Firds':
    #         return Firds


class Firds(graphene.ObjectType):
    class Meta:
        interfaces = (Base, )

    department = graphene.String()


class Fitrs(graphene.ObjectType):
    class Meta:
        interfaces = (Base, )

    fileType = graphene.String()


