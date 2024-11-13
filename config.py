import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://assignment4_4vxh_user:FbmomyXbQ5PSow0HtrFSZPVD3Bu8FRaT@dpg-csq6cjhu0jms73fo8if0-a.frankfurt-postgres.render.com/assignment4_4vxh")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "not-set")