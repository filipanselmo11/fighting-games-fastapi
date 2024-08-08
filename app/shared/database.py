from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "postgresql://admin:kPPeCR42zp6c38WIDXDY92L35BLbso9F@dpg-cqqjvirv2p9s73b8q9jg-a.oregon-postgres.render.com/fg_games_db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()