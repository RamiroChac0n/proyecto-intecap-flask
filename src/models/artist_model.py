from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from src.common.utils import db

class ArtistModel(db.Model):
    __tablename__='artist'
    id_artist:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(String(45), nullable=False)
    birthdate:Mapped[date]=mapped_column(Date, default=date.today)