from flask import Flask, request, render_template,redirect, url_for

from forms  import MyLibrary
from models import mybooks

import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
app.config["UPLOAD_FOLDER"] = "static/covers"


@app.route("/mybooks/", methods=["GET", "POST"])
def mybooks_list():
    form = MyLibrary()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            mybooks.create(form.data)
            mybooks.save_all()
        
        return redirect(url_for("mybooks_list"))
    return render_template("mybooks.html", form=form, mybooks=mybooks.all(), error=error)

@app.route("/mybooks/<int:mybook_id>/", methods=["GET", "POST"])
def mybooks_details(mybook_id):
    mybook = mybooks.get(mybook_id -1)
    form = MyLibrary(data=mybook)

    if request.method == "POST":
        if form.validate_on_submit():
            mybooks.update(mybook_id -1, form.data)
        return redirect(url_for("mybooks_list"))
    return render_template("mybook.html", form=form, mybook_id=mybook_id)

if __name__ == "__main__":
    app.run(debug=True)