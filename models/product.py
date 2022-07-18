from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, Text
from config.db import meta, engine
#from .user import users

products = Table(
            "products", meta, 
            Column('id', Integer, primary_key=True), 
            Column('name', String(255)),
            Column('description', Text),
            Column('price', Float)
            )

meta.create_all(engine)
