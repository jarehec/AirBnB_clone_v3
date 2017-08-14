from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""CNC - dictionary = { Class Name (string) : Class Type }"""
CNC = file_storage.FileStorage.CNC

if HBNB_TYPE_STORAGE == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
