from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

storage = file_storage.FileStorage()
storage.reload()

CLS = {
    'BaseModel': BaseModel,
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
    'User': User
    }
