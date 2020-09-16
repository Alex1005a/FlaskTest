from repositories import TaskRepository

class GetTasksByUserId():
   def __init__(self):
       self.repo = TaskRepository()
   def execute(self, userId):
       return self.repo.get_tasks_by_userId(userId)