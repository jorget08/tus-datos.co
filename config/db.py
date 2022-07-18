from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:lolazolol@localhost:5432/product")

meta = MetaData()

conn = engine.connect()