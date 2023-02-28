import graphene

import equipos.schema


class Query(equipos.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
