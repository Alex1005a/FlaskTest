from models import User, Task

class UserRepository():
    def create_user(self, name, password):
        user = User(
            name=name,
            password=password
        ).save()

        return user.get_id()

    def get_user_by_id(self, id):
        return User.objects.get(id=id)

    def get_user_by_name(self, name):
        return User.objects.get(name=name)

class TaskRepository():
    def create_task(self, id, title, description):
        task = Task(
            userId=id,
            title=title,
            description=description
        ).save()

        return str(task.pk)

    def get_tasks_by_userId(self, userId):
        return Task.objects.filter(userId=userId)

    def update_task_performed(self, id, userId):
        task = Task.objects.get(id=id)
        if task.userId == userId:
            task.update(performed=True)