"""New engine which will connect to database.
"""
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

metadata = MetaData()


class DBStorage():
    """Database management
    """
    USER = getenv('HBNB_MYSQL_USER')
    HOST = getenv('HBNB_MYSQL_HOST')
    PWD = getenv('HBNB_MYSQL_PWD')
    DB = getenv('HBNB_MYSQL_DB')
    env = getenv('HBNB_ENV')
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

    __engine = None
    __session = None

    def __init__(self):
        """Starts the engine and database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:5432/{}'.
                                      format(self.USER, self.PWD,
                                             self.HOST, self.DB),
                                      pool_pre_ping=True)
        if self.env == 'test':
            self.__session.drop_all()

    def reload(self):
        """Creates tables and scoped session"""
        Base.metadata.create_all(self.__engine)
        Session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Ses = scoped_session(Session_fac)
        self.__session = Ses()

    def all(self, cls=None):
        """ All returns a dic with class instances
        """
        dic = {}
        if cls:
            if isinstance(cls, str):
                for ins in self.__session.query(eval(cls)).all():
                    dic[ins.__class__.__name__ + '.' + ins.id] = ins
            else:
                for ins in self.__session.query(cls).all():
                    dic[ins.__class__.__name__ + '.' + ins.id] = ins
        else:
            holder_list = [State, City]
            for clas in holder_list:
                for ins in self.__session.query(clas).all():
                    dic[ins.__class__.__name__ + '.' + ins.id] = ins
        return dic

    def delete(self, obj=None):
        """Deletes provided object from database"""
        if obj is None:
            return
        else:
            self.__session.delete()

    def new(self, obj):
        """Adds object to the current database"""
        if obj is None:
            return
        else:
            self.__session.add(obj)
            return

    def save(self):
        """Commit all changes of the current database"""
        self.__session.commit()
