from flask_restx import Api, Namespace
from src.controllers.artist_controller import ArtistController

def ArtistRoutes(api):
    ns_artist=Namespace(name='artist',description='Describe the set of endpoints for Artist.')
    ns_artist.add_resource(ArtistController,'')
    api.add_namespace(ns_artist)