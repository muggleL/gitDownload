from flask import Flask
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import url_for
from flask import render_template
from flask import flash
from config import FILE_PATH

from service.download import get_all_files, gitClone
import os
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        status = gitClone(url)
        if status:
            return redirect(url_for("get_file"))
        flash("下载失败！请检查链接")
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/d/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        return send_from_directory(FILE_PATH, filename, as_attachment=True)

@app.route("/d/")
def get_file():
    files = get_all_files()
    if files:
        return render_template("d_page.html", files=files)
    flash("这里没有文件哟！")
    return render_template("d_page.html")

@app.route("/r/<filename>")
def rmfile(filename):
    file = FILE_PATH + filename
    os.remove(file)
    return redirect(url_for("get_file"))


if __name__ == '__main__':
    app.run()