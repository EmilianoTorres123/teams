import graphene
from graphene_django import DjangoObjectType

from .models import Equipo
from users.schema import UserType

from equipos.models import Equipo, Vote
from graphql import GraphQLError
from django.db.models import Q



# ...code
# Add after the LinkType
class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class EquipoType(DjangoObjectType):
    class Meta:
        model = Equipo


class Query(graphene.ObjectType):
    equipos = graphene.List(EquipoType, search=graphene.String())
    votes = graphene.List(VoteType)


    def resolve_equipos(self, info, search=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if search:
            filter = (
                Q(nombre__icontains=search) |
                Q(continente__icontains=search)
            )
            return Equipo.objects.filter(filter)

        return Equipo.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

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
    posted_by = graphene.Field(UserType)


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
        user = info.context.user or None
        equipo = Equipo(nombre=nombre, fundacion=fundacion, continente=continente, trofeos=trofeos, presidente=presidente, pais=pais, liga=liga, trofeosinte=trofeosinte, trofeosloca=trofeosloca, numerojuga=numerojuga, posted_by=user,)
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
            posted_by=equipo.posted_by,
        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    equipo = graphene.Field(EquipoType)

    class Arguments:
        equipo_id = graphene.Int()

    def mutate(self, info, equipo_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')


        equipo = Equipo.objects.filter(id=equipo_id).first()
        if not equipo:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            equipo=equipo,
        )

        return CreateVote(user=user, equipo=equipo)
    

# ...code
# Add the mutation to the Mutation class
class Mutation(graphene.ObjectType):
    create_equipo = CreateEquipo.Field()
    create_vote = CreateVote.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)



