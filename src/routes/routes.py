from flask_restx import Namespace, Api
from src.routes.artist_routes import ArtistRoutes

def General_Routes(api:Api):
    
    ArtistRoutes(api)