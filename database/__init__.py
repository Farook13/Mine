# Initializes the database module
from .mongo import db
from .users import add_user, get_user, get_all_users, total_users
from .files import insert_file, get_file, search_files, total_files
