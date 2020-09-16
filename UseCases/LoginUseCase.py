from repositories import UserRepository
from werkzeug.security import check_password_hash

class LoginUseCase():
   def __init__(self):
       self.repo = UserRepository()
   def execute(self, name, password):
       user = self.repo.get_user_by_name(name)
       if check_password_hash(user.password, password):
           return {'ok':True, 'user':user}

       return {'ok': False}