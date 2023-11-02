from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:example_password@database/mydb'
db = SQLAlchemy(app)

# Défini les classes
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)

# Défini les routes et leurs fonctions attribué
@app.route('/')
def index():
    try:
        new_user = User(username='john_doe')
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()

    users = User.query.all()
    user_list = [user.username for user in users]

    return 'Users in the database: {}'.format(user_list)

@app.route('/clear_users', methods=['DELETE'])
def clear_users():
    try:
        db.session.query(User).delete()
        db.session.commit()

        return jsonify({"message": "The 'users' table has been cleared successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'task': task.task} for task in tasks]
    return jsonify({'tasks': task_list})

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json.get('task')
    if new_task:
        task = Task(task=new_task)
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully'})
    else:
        return jsonify({'error': 'Task cannot be empty'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task =  db.session.get(Task, task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': f'Task {task.task} deleted successfully'})
    else:
        return jsonify({'error': 'Invalid task ID'})

# Récupère le name de Flask et on run l'app sur l'IP localhost
if __name__ == '__main__':
    app.run(host='0.0.0.0')
