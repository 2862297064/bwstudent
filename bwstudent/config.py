HOSTNAME = "127.0.0.1"
POST = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "bwstudent"


db_url = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, POST, DATABASE)


SQLALCHEMY_DATABASE_URI = db_url
SQLALCHEMY_TRACK_MODIFICATIONS = True