import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}


app = Flask(__name__)




def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        print("This is a POST request")
        # check if the post request has the file part
        if "img" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["img"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print(file.filename)
            filename = secure_filename(file.filename)
            response = [
                {"id": 1, "payload_url": "http://placekitten.com/200/300", "more_info": "blablabl"},
                {"id": 2, "payload_url": "http://placekitten.com/200/300", "more_info": "blablabl"},
                {"id": 3, "payload_url": "http://placekitten.com/200/300", "more_info": "blablabl"}
            ]
            headers = {
                'Access-Control-Allow-Origin': '*'
            }
            return (response, 200, headers)
          
        
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=img>
      <input type=submit value=Upload>
    </form>
    """


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
