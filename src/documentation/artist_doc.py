from flask_restx import fields
from src.common.utils import api

artist_doc = api.model('ArtistDocumentation',{
    'name':fields.String(required=True, example='José José'),
    'birthdate':fields.Date(required=False, example='1948-08-17')
})