import json
from cryptography.fernet import Fernet
from json.decoder import JSONDecodeError

from autherrors import NullFile
from validators import DataRequired, Length
from formfield import StringField, PasswordField


class SetUp:
    # <!-- this class will be used for redundant task like for housing global variables -->
    def __init__(self):
        self.database_path = 'database.json'
    
    def __createDb(self, data=None):
        pass

    def __getDb(self):
        pass


class LoginForm:
    database = "database.json"

    def __init__(self):
        pass

    @property
    def __getDb(self):
            try:
                with open(self.database) as db_obj:
                    data = json.load(db_obj)
            except (FileNotFoundError, JSONDecodeError) as err:
                # print(err)
                return {}
            else:
                return data
            
    def __createDb(self, data=None):
        if data and isinstance(data, dict):
            with open(self.database, 'w') as db_obj:
                json.dump(data, db_obj, indent=2)
            self.db = self.__getUserInfo()
        else:
            raise NullFile('DataBase cannot be Empty')
        

    def login(self):
        username = StringField('Username', validators=[DataRequired(), Length(max=20)]).entry

        if not username:
            self.login()
        else:
            password = PasswordField('Password').entry

            if self.valid(username, password):
                print('Success!')
            else:
                print('Failure')
        # Validate and return info

    def valid(self, username: str, password: str):
        
        if db := self.__getDb.get(username):
            userDb = db
            if password == self.__getHash(userDb): 
                print('Logged in!')
                return True
            else:
                print('PassWord Invalid!')
        else:
            print('Username InValid')
        return False
    
    def __getHash(self, userDb) -> str:
        password = userDb['password'].encode()
        key = userDb['key'].encode()
        fernet = Fernet(key)
        unhashed = fernet.decrypt(password).decode()
        # print(unhashed)
        return unhashed
    
class RegistrationForm:

    def __init__(self) -> None:
        pass
    
    def __updateDb(self, user_data):
        pass

    def register(self):
        username = StringField('Username', validators=[DataRequired, Length(min=5, max=20)])
        email = StringField('Email', validators=[DataRequired])
        password = PasswordField('Password', validators=[DataRequired])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired, EqualTo('password')])

    
login = LoginForm()
# print(login.valid('Divine', 'mainkey'))

login.login()

# <-- Next Up Sign UP Page and More Validators 
# ... then You can Make it Gui and Push to Git then You Can Be Confident Enough
# ... to now focus on Flask. Learn Html And CSS in the Main time, Launch Your Agency after one Web Project,
# ... Reach out to Businesses Locally Use em to build your portfolio but not totally free, build
# ... linkedin connects grow your network and get high ticket clients and start working on your saas take cs50, ai/ml, maths,js--> 