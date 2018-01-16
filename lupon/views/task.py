import logging
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from lupon import app, db
from lupon.models import Task
from lupon.forms import TaskForm


@app.route('/task_db', methods=['GET','POST'])
@login_required
def task_dashboard():
    tasks = Task.get_all(current_user.get_id())
    return render_template("task/task.html", tasks=tasks)

@app.route('/task', methods=['GET','POST'])
@login_required
def task():

    # Prepoulate Form if task id is present in URL
    if request.args.get('task_id'):
        obj = Task.query.get(int(request.args['task_id']))
        taskform = TaskForm(obj=obj)

    else:
        taskform = TaskForm()

    # ToDo: only display where user_id = current_user
    tasks = Task.get_all(current_user.get_id())
    
    if taskform.validate_on_submit():
        logging.info('task from validated')
        task = Task()
        taskform.populate_obj(task)

        if task.update_task is True:
            tmp_task = Task.query.filter_by(id=task.id).first()
            taskform.populate_obj(tmp_task)
            tmp_task.modify_by = current_user.get_id()
            db.session.commit()
            flash("Task Updated! "+ str(task.update_task) , 'success')
            
        elif task.add_task is True:
            task.user_id = current_user.get_id()
            task.create_by = current_user.get_name()
            task.id = None
            db.session.add(task)
            db.session.commit()
            flash("Task created! "+ str(task.add_task), 'success')

        elif task.del_task is True:
            tmp_task = Task.query.filter_by(id=task.id).first()
            db.session.delete(tmp_task)
            db.session.commit()
            flash("Task deleted "+ str(task.del_task), 'warning')
        
        return redirect(url_for('task'))
    return render_template("task.html", taskform=taskform, tasks=tasks)


@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    logging.info('post success')
    task_add = Task(name=request.values.get('name'),
                amount=request.values.get('amount'),
                value=request.values.get('value'),
                unit=request.values.get('unit'),
                description=request.values.get('description'),
                user_id=current_user.get_id())
    task_add.create_by = current_user.get_name()
    db.session.add(task_add)
    db.session.commit()
    # flash("Task created! "+ str(task.add_task), 'success')
    t = task_add.serialize
    return jsonify(t)

