from peewee import *
import datetime

DATABASE = 'rest'
HOST = 'localhost'
USER = 'root'
PASSWORD = ''

DATABASE = MySQLDatabase(DATABASE, host=HOST, user=USER, password=PASSWORD)

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Task(BaseModel):
    title = CharField(max_length=250)
    description = TextField()
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now())

    @classmethod
    def get_element(cls, id):
        try:
            return Task.get(id=id)
        except DoesNotExist:
            return None

    @classmethod
    def get_all(cls):
        return [task.serialize for task in Task.select() ]

    @classmethod
    def create_element(cls, title, description, active=True):
        task = Task.create(title=title, description=description, active=active)
        return task

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title.strip(),
            'description': self.description.strip(),
            'active': str(self.active),
            'created_at': str(self.created_at)
        }

    def update_element(self, title='', description='', active=False):
        self.title = title
        self.description = description
        self.active = active

        self.save()

    def delete_element(self):
        self.delete_instance()

def load_data():
    Task.create(title='Tarea número uno', description='Descripción')
    Task.create(title='Tarea número dos', description='Descripción')

def initialize():
    if Task.table_exists():
        Task.drop_table()

    Task.create_table()
    load_data()
