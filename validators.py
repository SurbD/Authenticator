class DataRequired:

    @property
    def __name__(self):# <-- allows class instances to get the class name,
                                      # ... so it can be used to check if validator is in the name space -->
        return DataRequired.__name__

    def __init__(self):
        pass

    def __call__(self, class_instance):
        label = 'entry'
        class_args = class_instance.__dict__

        assert label in class_args
        if class_args[label] and self.__validator(class_args[label]):
            return True
        else:
            print('Error: Input Must Start with Alpha Character')

    def __validator(self, value):
        # print('VAlUE is -- ', value)
        if isinstance(value, str):
            return True if value[0].isalpha() else False
        

class Length:
    """ Checks if a User Input Length is Valid with the given/default min and max value. """

    @property
    def __name__(self):
        return DataRequired.__name__  # <-- allows class instances to get the class name,
                                      # ... so it can be used to check if validator is in the name space -->

    def __init__(self, min=2, max=50):
        self.min = min
        self.max = max

    def __call__(self, class_instance):
        label = 'label' 
        class_args = class_instance.__dict__

        assert label in class_args  # <-- check if value 'label' is a available in class attributes dict -->
        if self.__validator(class_args[label]): # <-- calls Validator method with label value and parameter -->
            return True
        else:
            print(f'Error!: User input must have a minimum value of {self.min} and a maximum value of {self.max}')

    def __validator(self, value): # <-- Validator function checks if condition is met for value in this case the length min and max  -->
        if isinstance(value, str):
           return True if self.min < len(value) <= self.max else False


class EqualTo:
    pass
#     @property
#     def __name__(self):
#         return DataRequired.__name__
    
#     def __init__(self, object: str) -> None:
#         self.object = eval(object)

#     def __call__(self, class_instance):
#         label = 'entry'
#         class_args = class_instance.__dict__

#         assert label in class_args
#         if self.__validated(class_args[label]):
#             return True
#         else:
#             print(f'Error: Password Does not Match')

#     def __validated(self, entry_value):
#         if value == self.object.entry

# # <-- More Validators to be Added -->
# <-- --> #Comment