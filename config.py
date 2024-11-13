import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://assignment4_user:v1pTJeflTALxlefLsFd9onobHNu7ce6f@dpg-cspr2htds78s738s0ngg-a/assignment4")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "not-set")