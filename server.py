from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)


@app.route("/")
def read_story():
    data = data_handler.read_data()
    return render_template("index.html", content=data, headers=data_handler.DATA_HEADER)


@app.route("/story", methods=["GET", "POST"])
def add_story():
    if request.method == "POST":
        story = request.form.to_dict()
        story["user_story"] = " ".join(story["user_story"].split("\r\n"))
        story["acceptance_criteria"] = " ".join(story["acceptance_criteria"].split("\r\n"))
        data_handler.save_user_story(story)
        return redirect("/")
    return render_template("add.html")


@app.route("/story/<int:id>", methods=["GET", "POST"])
def update_story(id):
    data = data_handler.read_data()
    story = list(data[id].values())
    if request.method == "POST":
        updated_story = request.form.to_dict()
        updated_story["id"] = id
        updated_story["user_story"] = " ".join(updated_story["user_story"].split("\r\n"))
        updated_story["acceptance_criteria"] = " ".join(updated_story["acceptance_criteria"].split("\r\n"))
        data_handler.update_user_story(updated_story)
        return redirect("/")
    return render_template("update.html", content=story, statuses=data_handler.STATUSES)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_story(id):
    data_handler.delete_user_story(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
