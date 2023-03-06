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

class CreateEquipo(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    fundacion = graphene.Int()
    continente = graphene.String()
    trofeos = graphene.Int()
    presidente = graphene.String()
    pais = graphene.String()
    liga = graphene.String()    
    trofeosinte = graphene.Int()
    trofeosloca = graphene.Int()
    numerojuga = graphene.Int()


    #2
    class Arguments:
        nombre = graphene.String()
        fundacion = graphene.Int()
        continente = graphene.String()
        trofeos = graphene.Int()
        presidente = graphene.String()
        pais = graphene.String()
        liga = graphene.String()
        trofeosinte = graphene.Int()
        trofeosloca = graphene.Int()
        numerojuga = graphene.Int()

    #3
    def mutate(self, info, nombre, fundacion, continente, trofeos, presidente, pais, liga, trofeosinte, trofeosloca, numerojuga):
        equipo = Equipo(nombre=nombre, fundacion=fundacion, continente=continente, trofeos=trofeos, presidente=presidente, pais=pais, liga=liga, trofeosinte=trofeosinte, trofeosloca=trofeosloca, numerojuga=numerojuga)
        equipo.save()

        return CreateEquipo(
            id=equipo.id,
            nombre=equipo.nombre,
            fundacion=equipo.fundacion,
            continente=equipo.continente,
            trofeos=equipo.trofeos,
            presidente=equipo.presidente,
            pais=equipo.pais,
            liga=equipo.liga,
            trofeosinte=equipo.trofeosinte,
            trofeosloca=equipo.trofeosloca,
            numerojuga=equipo.numerojuga,
        )


#4
class Mutation(graphene.ObjectType):
    create_equipo = CreateEquipo.Field()
