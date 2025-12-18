from src.common.utils import ma
from marshmallow import fields, validate
from src.models.artist_model import ArtistModel

class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=ArtistModel
        load_instance=True
        
    id_artist =fields.Integer(
        required=True,
        validate=validate.Range(min=1),
        error_messages={
            'required':'This field is required.'
        }
    )
    
    name =fields.String(
        required=True,
        validate=validate.Length(
            min=1,
            max=45,
            error='The field must be between 1 and 200 characters long.',
        ),
        error_messages={
            'required':'This field is required.'
        }
    )    