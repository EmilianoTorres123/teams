from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
# Create your tests here.
from equipos.schema import schema
from equipos.models import Equipo

Equipos_QUERY = '''
 {
   equipos {
     nombre
     fundacion
     continente
     trofeos
     presidente
     pais
     liga
     trofeosinte
     trofeosloca
     numerojuga
   }
 }
'''

class EquipoTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.equipo1 = mixer.blend(Equipo)
        self.equipo2 = mixer.blend(Equipo)

    def test_equipos_query(self):
        response = self.query(
            Equipos_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query equipo results ")
        print (content)
        assert len(content['data']['equipos']) == 2
