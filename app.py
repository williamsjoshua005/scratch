import os
from pathlib import Path

import psycopg2
from flask import Flask
from playhouse.pool import PooledPostgresqlExtDatabase
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

app = Flask(__name__)
app.config['DB_USER'] = os.getenv('DB_USER', 'sa')
app.config['DB_PASSWD'] = os.getenv('DB_PASSWD', 'db_pass')
app.config['DB_HOST'] = os.getenv('DB_HOST', '127.0.0.1')
app.config['DB_PORT'] = os.getenv('DB_PORT', '5432')


db = PooledPostgresqlExtDatabase(database='scratch',
                                 user=app.config['DB_USER'], password=app.config['DB_PASSWD'],
                                 max_connections=32,
                                 stale_timeout=300,
                                 host=app.config['DB_HOST'],
                                 port=app.config['DB_PORT'])

import api.api
