import logging
from flask import render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from lupon import app, db
from lupon.models import Workpackage, Location, Contact
from lupon.forms import OfferForm


@app.route('/offer')
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
                            create_by=current_user.get_name())
        offerform.populate_obj(offer)
        offer.id = None
        # Add & Commit transacton
        db.session.add(offer)
        db.session.commit()
        return redirect(url_for('offer_dashbaord'))

    return render_template('offer/add_offer.html', offerform=offerform)
