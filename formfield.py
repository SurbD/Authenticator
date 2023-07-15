# <!-- Author: Divine Mukoro
#      Date: Friday, June 29, 2023 -->

class StringField:

    def __init__(self, label, validators=None):
        self.label = label
        self.entry = self.get_entry(self.label, validators)

    def validate(self, validators):
        for validator in validators:
            if not validator(self):
                break
        else:
            return True
        return False
    
    def get_entry(self, label, validators):
        user_entry = input(f'{label.title()}:\n>>> ')
        self.entry = user_entry

        if validators:
            if not self.validate(validators):
                user_entry = None
        
        return user_entry
    

class PasswordField:

    def __init__(self, label, validators=None):
        self.label = label
        self.entry = self.get_entry(self.label, validators)

    def get_entry(self, label, validators):
        user_entry = input(f'{label.title()}:\n>>> ')
        self.entry = user_entry

        if validators:
            if not self.validate(validators):
                user_entry = None
            # else:
                # user_entry = self.__gethash(user_entry)
        # print(self.entry, 'Password Field')
        return user_entry
    
    def validate(self, validators):
        for validator in validators:
            if not validator(self):
                break
        else:
            return True
        return False

    # def __gethash(self) -> bytes:
    #     from cryptography.fernet import Fernet
    # <-- No need to return hash because the Password Field will need access to 
    # ... the Username String Field to get the username personal key, the only other way, 
    # ... is using a general key for all users, but this is less secure, so hash it in
    # ... Sign Up and store key path in database.json -->


class BooleanField:
    pass

class SubmitField:
    pass

# <-- Most of the fields will not be functional until Tkinter -->