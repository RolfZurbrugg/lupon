import logging
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from lupon import app, db
from lupon.models import Contact, Location
from lupon.forms import ContactForm, LocationForm

@app.route('/contact/<int:contact_id>', methods=["GET", "POST"])
@login_required
def edit_contact(contact_id):

    contact = Contact.query.filter_by(id=contact_id).first()
    contactform = ContactForm(obj=contact)
    contactform.location.query = Location.query.filter_by(contact_id=contact_id)

    location = contact.get_primary_location()
    
    locationform = LocationForm(obj=location)

    contacts = Contact.get_all(current_user.get_id())
    locations = Location.query.filter_by(contact_id=contact_id).all()

    if contactform.validate_on_submit():
        contactform.populate_obj(contact)
        locationform.populate_obj(location)

        if contact.update_contact is True:
            contact.modify_by = current_user.get_id()
            db.session.commit()
            flash("contact Updated! "+ str(contact.update_contact), 'success')

            return redirect(url_for('edit_contact', contact_id=contact_id))
        
        elif contact.del_contact is True:
            for addr in contact.address:
                db.session.delete(addr)

            db.session.delete(contact)
            db.session.commit()
            return redirect(url_for("contact"))

    return render_template('contact/edit_contact.html', contactform=contactform, contacts=contacts, locationform=locationform, locations=locations)


@app.route('/contact', methods=['GET','POST'])
@login_required
def add_contact():
    # create forms
    contactform = ContactForm()
    locationform = LocationForm()
    # get all contacts from current_user
    contacts = Contact.get_all(current_user.get_id())

    if contactform.validate_on_submit():
        # Create location object
        location = Location(is_primary=True)
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

        return redirect(url_for('edit_contact', contact_id=contact.get_id()))

    return render_template('contact/add_contact.html', contactform=contactform, contacts=contacts, locationform=locationform)