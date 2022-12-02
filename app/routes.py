from app import app
from app.forms import MyForm
from flask import render_template, url_for, redirect


@app.route('/')
@app.route('/submit_file', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        print(form.name.data)
        
        return redirect('/result') 

    return render_template('submit_file.html', form=form) 

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html') 