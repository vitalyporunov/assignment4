import os

SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://assignment4_user:v1pTJeflTALxlefLsFd9onobHNu7ce6f@dpg-cspr2htds78s738s0ngg-a/assignment4'