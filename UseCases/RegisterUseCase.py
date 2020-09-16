from repositories import UserRepository
from werkzeug.security import generate_password_hash

class RegisterUseCase():
   def __init__(self):
       self.repo = UserRepository()
   def execute(self, name, password):
       hash = generate_password_hash(password)
       return self.repo.create_user(name, hash)