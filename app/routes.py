from flask import render_template, flash
from app import app, db
from app.forms import DestinationForm
from app.models import Destination


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DestinationForm()

    if form.validate_on_submit():
        dest = Destination()
        form.populate_obj(dest)

        db.session.add(dest)
        db.session.commit()

        flash(f'Destination successfully added for {form.city_name.data}')

    return render_template('index.html', title='Home', form=form)
