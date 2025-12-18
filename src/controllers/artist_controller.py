from flask import request
from flask_restx import Resource
from src.common.utils import db, api
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError
from src.schemas.artist_schema import ArtistSchema
from src.documentation.artist_doc import artist_doc
from src.models.artist_model import ArtistModel

class ArtistController(Resource):
    
    @api.expect(artist_doc)
    def post(self):
        try:
            artist_json=request.json
            artist_schema=ArtistSchema(exclude=['id_artist'])
            artist_validated = artist_schema.load(artist_json)
            db.session.add(artist_validated)
            db.session.commit()
            return ArtistSchema().dump(artist_validated), 200
            
        except ValidationError as err:
            print(err)
            mensajes_concatenados = " ".join([f"{clave}: {' '.join(mensajes)}" for clave, mensajes in err.messages_dict.items()])
            return {'message':mensajes_concatenados}, 422
        except Exception as err:
            print(err)
            return {'message':'Something went wrong, please try again.'},503 
        
    def get(self):
        try:
            artist=db.session.execute(
                db.select(ArtistModel)
            ).scalars().all()
            list_json=ArtistSchema(many=True).dump(artist)
            return list_json, 200
            
        except Exception as err:
            return {'message':'Something went wrong, please try again.'},503
        
    @api.expect(artist_doc)
    def put(self):
        try:
            
            artist_json=request.json
            artist_schema=ArtistSchema()
            artist_validated = artist_schema.load(artist_json)
            
            print(artist_validated)
            print('hola')
                        
            artist_db=db.session.execute(
                db.select(ArtistModel).where(ArtistModel.id_artist==1)
            ).scalar_one()
            artist_db.name = artist_validated.name
            artist_db.birthdate = artist_validated.birthdate
            db.session.commit()
            return ArtistSchema().dump(artist_db), 200
            
        except ValidationError as err:
            print(err)
            mensajes_concatenados = " ".join([f"{clave}: {' '.join(mensajes)}" for clave, mensajes in err.messages_dict.items()])
            return {"message":mensajes_concatenados}, 422            
        except NoResultFound as err:
            return {'message':'The Artist you are trying to update does not exist'},404
        except Exception as err:
            print(err)
            return {'message':'Something went wrong, please try again.'},503     
        
    def delete(self):
        try:
            artist_db =db.session.execute(
                db.select(ArtistModel).where(ArtistModel.id_artist == 1)
            ).scalar_one()
            db.session.delete(artist_db)
            db.session.commit()
            return True, 204
            
        except NoResultFound as err:
            print(err)
            return {'message':'The Artist you want to delete does not exist'},404
        except Exception as err:
            print(err)
            return {'message':'Something went wrong, please try again.'},503 