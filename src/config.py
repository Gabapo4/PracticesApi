
from os import getenv
from dotenv import load_dotenv

class DevelopmentConfig():
    load_dotenv()

    key=getenv("SECRETKEY")
    dbUser=getenv("DBUSER")
    dbPass=getenv("DBPASS")
    dbHost=getenv("DBHOST")
    dbName=getenv("DBNAME")

    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql://'+dbUser+':'+dbPass+'@'+dbHost+'/'+dbName+''
    SQLALCHEMY_TRACK_MODIFICATIONS=False

config={
    'development':DevelopmentConfig
}
