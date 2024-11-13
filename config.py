import os

SECRET_KEY = os.getenv('SECRET_KEY', '1584ffa92daae1b64584c6812331f392f03d780f4e69ced2290b75b94fd23e97')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://assignment4_user:v1pTJeflTALxlefLsFd9onobHNu7ce6f@dpg-cspr2htds78s738s0ngg-a/assignment4')