from repositories import TaskRepository

class CreateTaskUseCase():
   def __init__(self):
       self.repo = TaskRepository()
   def execute(self, userId, title, desc):
       return self.repo.create_task(userId, title, desc)