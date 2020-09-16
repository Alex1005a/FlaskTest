from flask import Flask, request, Response, jsonify
from flask_login import LoginManager, logout_user, login_required, login_user, current_user
from repositories import UserRepository
from UseCases.RegisterUseCase import RegisterUseCase
from UseCases.LoginUseCase import LoginUseCase
from UseCases.CreateTaskUseCase import CreateTaskUseCase
from UseCases.GetTasksByUserId import GetTasksByUserId
from UseCases.PerformTaskUseCase import PerformTaskUseCase

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MONGODB_SETTINGS'] = {'db':'testing', 'alias':'default'}

from models import db
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return UserRepository().get_user_by_id(user_id)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register', methods=["POST"])
def register():
    content = request.json
    reg = RegisterUseCase()
    reg.execute(content["name"], content["pass"])
    return Response(status=200)

@app.route('/login', methods=["POST"])
def login():
    content = request.json

    login = LoginUseCase()
    result = login.execute(content["name"], content["pass"])

    if result['ok'] == False:
        return Response(status=404)

    login_user(result['user'], remember=True)

    return Response(status=200)


@app.route('/getCurrentUserId')
@login_required
def getCurrentUserId():
    return str(current_user.pk)

@app.route('/createTask', methods=["POST"])
@login_required
def createTask():
    content = request.json
    create_task_use_case = CreateTaskUseCase()
    return create_task_use_case.execute(str(current_user.pk), content["title"], content["desc"])

@app.route('/getTasks')
@login_required
def getTasks():
    content = request.json
    get_tasks_by_user_id = GetTasksByUserId()
    return jsonify(get_tasks_by_user_id.execute(str(current_user.pk)))

@app.route('/performTask', methods=["POST"])
@login_required
def performTask():
    content = request.json
    perform_task = PerformTaskUseCase()
    perform_task.execute(content["taskId"], str(current_user.pk))
    return Response(status=200)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logout'

if __name__ == '__main__':
    app.debug = True
    app.run()
