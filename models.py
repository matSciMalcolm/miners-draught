import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        
    def create_to_do_table(self):
        
        query = '''
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean
            _is_delted boolean
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        '''

        self.conn.execute(query)

    def create_user_table(self):
        # create user table

        query = '''
        CREATE TABLE IF NOT EXISTS "User" (
            Name TEXT NOT NULL,
            Email TEXT,
            _id INTEGER PRIMARY KEY AUTOINCREMENT 
        );
        '''

        self.conn.execute(query)


class ToDoModel:
    """Binds common database actions to sql queries.
    """    

    TABLENAME = 'TODO'

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'insert into {TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        result = self.conn.execute(query)
        return result

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        self.model.create(params["text"], params["Description"])