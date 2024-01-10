import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    user_name = Column(String(50), nullable=False)
    password = Column(String(200))

class Pokemons(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(String(100))
    energy = Column(Integer)
    Type = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Habilities(Base):
    __tablename__ = 'habilities'
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(String(250))
    damage = Column(Integer)
    user_id = Column(Integer, ForeignKey('pokemons.id'))
    user = relationship(Pokemons)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(String)
    user_id = Column(Integer, ForeignKey('pokemons.id'))
    user = relationship(Pokemons)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
