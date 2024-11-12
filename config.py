import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://assignment4_user:v1pTJeflTALxlefLsFd9onobHNu7ce6f@dpg-cspr2htds78s738s0ngg-a.oregon-postgres.render.com/assignment4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False