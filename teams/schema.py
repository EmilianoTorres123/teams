import graphene

import equipos.schema


class Query(equipos.schema.Query, graphene.ObjectType):
    pass

class Mutation(equipos.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
