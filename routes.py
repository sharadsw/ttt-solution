from flask import render_template, request, flash

from app import app
from forms import nForm
from freq import get_file, clean_text, parse_text

@app.route("/")
def index():
    form = nForm()
    return render_template("index.html", form=form)

@app.route("/", methods=["GET", "POST"])
def result():
    URL = "https://terriblytinytales.com/test.txt"
    form = nForm()
    if request.method == "POST" and form.validate_on_submit():
        num = form.num.data
        text = get_file(URL)
        clean = clean_text(text)
        nfreq, flag = parse_text(clean, num)

        if flag:
            flash("Warning: N higher than total unique words, displaying all words instead")

        return render_template("index.html", form=form, result=nfreq)
    
    return render_template("index.html", form=form)



