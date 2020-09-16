from repositories import TaskRepository

class PerformTaskUseCase():
   def __init__(self):
       self.repo = TaskRepository()
   def execute(self, taskId, userId):
       self.repo.update_task_performed(taskId, userId)