from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.task_repository as task_repository
import repositories.user_repository as users_repository
from models.task import Task


tasks_blueprint = Blueprint("tasks", __name__)
# combo of address and method creates unique url
@tasks_blueprint.route("/tasks", methods=['GET'])
def tasks():
    tasks_list = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks = tasks_list)

@tasks_blueprint.route("/tasks/new", methods = ['GET'])
def new_task():
    users_list = users_repository.select_all()
    return render_template('tasks/new.html', all_users = users_list)

@tasks_blueprint.route('/tasks', methods = ['POST'])
def create_task():
    description = request.form['description']
    user_id = request.form['user_id']
    duration = request.form['duration']
    completed = request.form['completed']
    user = users_repository.select(user_id)
    # assumes there is matching user
    task = Task(description, user, duration, completed)
    task_repository.save(task)
    return redirect('/tasks')

#accepts both post and delete
@tasks_blueprint.route('/tasks/<id>/delete', methods =['POST', 'DELETE'])
def whack_task(id):
    task_repository.delete(id)
    return redirect('/tasks')

@tasks_blueprint.route('/tasks/<id>/update', methods = ['GET'])
def REEEEEEE(id):
    task_object = task_repository.select(id)
    users = users_repository.select_all()
    return render_template('/tasks/edit.html', task=task_object, all_users = users)

@tasks_blueprint.route('/tasks/<id>', methods = ['GET'])
def CIAO_BUONGIORNO(id):
    task_object = task_repository.select(id)
    return render_template('tasks/show.html', task = task_object)
    
@tasks_blueprint.route('/tasks/<id>', methods = ['POST'])
def lebron_james(id):
    description = request.form['description']
    user_id = request.form['user_id']
    duration = request.form['duration']
    completed = request.form['completed']
    user = users_repository.select(user_id)
    task = Task(description, user, duration, completed, id)
    task_repository.update(task)
    return redirect('/tasks')