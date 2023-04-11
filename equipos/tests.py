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

CREATE_Equipo_MUTATION = '''
 mutation createEquipoMutation($continente: String, $fundacion: Int, $liga: String, $nombre: String, $numerojuga: Int, $pais: String, $presidente: String, $trofeos:Int, $trofeosinte: Int, $trofeosloca: Int) {
     createEquipo(continente: $continente, fundacion: $fundacion, liga: $liga, nombre: $nombre, numerojuga: $numerojuga, pais: $pais, presidente: $presidente, trofeos: $trofeos, trofeosinte: $trofeosinte, trofeosloca: $trofeosloca) {
         continente
         fundacion
         liga
         nombre
         numerojuga
         pais
         presidente
         trofeos
         trofeosinte
         trofeosloca
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

    def test_createEquipo_mutation(self):

        response = self.query(
            CREATE_Equipo_MUTATION,
            variables={'continente': 'europa', 'fundacion': 1934, 'liga': 'premier league', 'nombre': 'arsenal', 'numerojuga': 25, 'pais': 'inglaterra', 'presidente': 'fermin', 'trofeos': 24, 'trofeosinte': 12, 'trofeosloca': 21 }
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createEquipo": {"continente": "europa", "fundacion": 1934, "liga": "premier league", "nombre": "arsenal", "numerojuga": 25, "pais": "inglaterra", "presidente": "fermin", "trofeos": 24, "trofeosinte": 12,  "trofeosloca": 21 }}, content['data']) 

