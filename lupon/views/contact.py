import logging
from flask import render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from lupon import app, db
from lupon.models import Contact, Location
from lupon.forms import ContactForm, LocationForm

@app.route('/api/v1.0/contact', methods=["GET", "POST"])
@login_required
def contact_api():
    return Contact.tojson(current_user.get_id())

@app.route('/contact')
@login_required
def contact_dashbaord():
    contacts = Contact.get_all(current_user.get_id())
    return render_template('contact/contact.html', contacts=contacts)

@app.route('/contact/<int:contact_id>/edit', methods=["GET", "POST"])
@login_required
def edit_contact(contact_id):
    logging.info('edit_contact with ID: '+ str(contact_id))
    contact = Contact.query.filter_by(id=contact_id).first()
    contactform = ContactForm(obj=contact)
    contactform.location.query = Location.query.filter_by(contact_id=contact_id)

    location = contact.get_primary_location()
    
    locationform = LocationForm(obj=location)

    contacts = Contact.get_all(current_user.get_id())
    locations = Location.query.filter_by(contact_id=contact_id).all()

    if contactform.validate_on_submit():
        logging.info('edit_contact, form validation successfull for ID: '+ str(contact_id))
        contactform.populate_obj(contact)
        locationform.populate_obj(location)

        if contact.update_contact is True:
            logging.info('edit_contact, action Update contact with ID: '+ str(contact_id))
            contact.modify_by = current_user.get_id()
            db.session.commit()
            flash("Contact: "+contact.firstname +" "+ contact.lastname +" sucessfully Updated",  'success')

            return redirect(url_for('edit_contact', contact_id=contact_id))
        
        elif contact.del_contact is True:

            logging.info('edit_contact, action Delete contact with ID: '+ str(contact_id))
            for addr in contact.address:
                logging.info('edit_contact, action Delete contact with ID location removed: '+ str(addr))
                db.session.delete(addr)

            db.session.delete(contact)
            db.session.commit()
            flash("Contact: "+contact.firstname +" "+ contact.lastname +" sucessfully deleted",  'success')

            return redirect(url_for("contact_dashboard"))

    return render_template('contact/edit_contact.html', contactform=contactform, contacts=contacts, locationform=locationform, locations=locations)


@app.route('/contact/add', methods=['GET','POST'])
@login_required
def add_contact():
    # create forms
    contactform = ContactForm()
    locationform = LocationForm()
    # get all contacts from current_user
    contacts = Contact.get_all(current_user.get_id())

    if contactform.validate_on_submit():
        # Create location object
        location = Location(is_primary=True,
                            user_id=current_user.get_id())
        locationform.populate_obj(location)
        location.id = None
        # Create contact
        contact = Contact(user_id=current_user.get_id(),
                          create_by=current_user.get_name(),
                          address=[location])
        contactform.populate_obj(contact)
        contact.id = None
        # Add & Commit transacton
        db.session.add(contact)
        db.session.add(location)
        db.session.commit()

        return redirect(url_for('edit_contact', contact_id=contact.id))

    return render_template('contact/add_contact.html', contactform=contactform, contacts=contacts, locationform=locationform)
