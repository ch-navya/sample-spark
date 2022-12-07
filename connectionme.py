import os

db_user = os.environ.get('DB_USER')

db_password=os.environ.get('DB_PASS')

db_database=os.environ.get('DB_DATABASE')

db_host=os.environ.get('DB_HOST')

db_port=os.environ.get("DB_PORT")

print(db_user)

print(db_password)

print(db_host)

print(db_database)

print(db_port)