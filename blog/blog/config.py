import os

# Configuration variables for Flask database
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful"
    DEBUG = True