'''Config file'''

# run.py
jwt_secret = 'Key'

# *_app.py
user_name = 'postgres'
database_name = 'database'
host_name = 'localhost'
table_name = 'messages'
query = f'select id from {table_name} limit 500000;'
