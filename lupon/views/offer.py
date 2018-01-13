import logging
import json
from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user
from lupon import app, db
from lupon.models import Workpackage, Location, Contact, Task
from lupon.forms import OfferForm, OfferEditForm


@app.route('/offer', methods=['GET','POST'])
@login_required
def offer_dashboard():
    offers = Workpackage.get_all(current_user.get_id())
    return render_template('offer/dashboard.html', offers=offers)


@app.route('/offer/add', methods=['GET','POST'])
@login_required
def add_offer():
    offerform = OfferForm()
    offerform.location.query = Location.query.filter_by(user_id=current_user.get_id())
    offerform.contact.query = Contact.query.filter_by(user_id=current_user.get_id())

    if offerform.validate_on_submit():
        # Create offer
        offer = Workpackage(user_id=current_user.get_id(),
                            create_by=current_user.get_name(),
                            location_id=offerform.location.data.id,
                            contact_id=offerform.location.data.id)
        offerform.populate_obj(offer)
        offer.id = None
        # Add & Commit transacton
        db.session.add(offer)
        db.session.commit()
        return redirect(url_for('offer_dashboard'))

    return render_template('offer/add_offer.html', offerform=offerform)

@app.route('/offer/edit/<int:offer_id>', methods=['GET','POST'])
@login_required
def edit_offer(offer_id):
    offer = Workpackage.query.filter_by(id=offer_id).first()
    form = OfferEditForm(obj=offer)
    form.task.query = Task.query.filter_by(user_id=current_user.get_id())
    offers = Workpackage.get_all(current_user.get_id())
    logging.info('edit_offer with ID: '+ str(offer_id))
    tasks = offer.get_tasks()
    
    if form.validate_on_submit():
        logging.info('edit_offer, form validation successfull for ID: '+ str(offer_id))
        form.populate_obj(offer)
        if offer.add_task is True:
            task = Task.query.get(form.task.data.id)
            offer.tasks.append(task)
            db.session.commit()
            return redirect(url_for('edit_offer', offer_id=offer_id))
        
    return render_template('offer/edit_offer.html', offers=offers, form=form, tasks=tasks)


@app.route('/api/v1.0/offer/get/<int:offer_id>', methods=["GET"])
@login_required
def offer_api_get(offer_id):
    if request.method == 'GET':
        return Workpackage.query.filter_by(id=offer_id).first().get_tasks()
    
    return json.dumps({'success':False}), 500, {'ContentType':'application/json'} 

@app.route('/api/v1.0/offer/edit/<int:offer_id>/<int:task_id>', methods=["GET", "POST"])
@login_required
def offer_api_edit(offer_id, task_id):

    if request.method == 'PUT':
        task = Task.query.get(task_id)
        offer = Workpackage.query.get(offer_id)
        offer.tasks.append(task)
        db.session.commit()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

    elif request.method == 'DELETE':
        task = Task.query.get(task_id)
        offer = Workpackage.query.get(offer_id)
        offer.tasks.remove(task)
        db.session.commit()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

    return json.dumps({'success':False}), 500, {'ContentType':'application/json'} 