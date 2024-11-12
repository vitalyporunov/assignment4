import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/pet_shelter'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

**Note: Replace 'postgresql://username:password@localhost/pet_shelter' with your actual PostgreSQL connection URI. Set up environment variables for production with a real secret key and database URI.**