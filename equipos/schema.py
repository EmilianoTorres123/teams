import graphene
from graphene_django import DjangoObjectType

from .models import Equipo


class EquipoType(DjangoObjectType):
    class Meta:
        model = Equipo


class Query(graphene.ObjectType):
    equipos = graphene.List(EquipoType)

    def resolve_equipos(self, info, **kwargs):
        return Equipo.objects.all()
