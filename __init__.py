from flask import Flask, render_template,request
from app import fb_api as api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images', methods=['POST'])
def disp_images():
    url = request.form['url']
    images = api.get_images(_id=url)
    return render_template('show_images.html', images=images)


if __name__ == '__main__':
    app.run()

