import random

class Code:
    def __init__(self, request, digit=6, save=False) -> None:
        self.request = request
        self.digit = digit
        self.code = None
        self.save = save

    def generator(self):
        code = int(random.random() * (10**self.digit))
        self.code = code
        if self.save:
            self.save_code()
        return code
    
    def save_code(self):
        self.request.session['code'] = self.code

    def delete_code(self):
        self.request.session['code'].delete()