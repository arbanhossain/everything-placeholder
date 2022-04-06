### Imports
from flask import Flask, render_template, request, Response, jsonify, send_file
from utils.image import get_image
from utils.text import gen_text
from io import BytesIO

app = Flask(__name__)

### Global Functions & Constants ###

LOREM = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam consequat justo nec vestibulum commodo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum sodales ligula tellus, nec posuere leo lacinia aliquet. Nam mattis, odio at tincidunt imperdiet, velit nisi cursus magna, at elementum odio leo eu risus. Quisque fermentum libero vel dapibus tincidunt. Maecenas vel risus lobortis, blandit risus quis, laoreet lorem. In at finibus dolor, a vehicula ante. Pellentesque nunc purus, varius eget enim nec, imperdiet dignissim quam. Curabitur ornare dapibus convallis. Curabitur vehicula tortor nec enim lacinia auctor. Praesent venenatis, metus dictum tincidunt pharetra, arcu sapien sollicitudin massa, ac rutrum nulla diam sed ante. Aliquam vel finibus magna.
'''

def serve_pil_image(pil_img):
  img_io = BytesIO()
  pil_img.save(img_io, 'JPEG', quality=70)
  img_io.seek(0)
  return send_file(img_io, mimetype='image/jpeg')

### Routes

@app.route("/")
def index():
  return "Hello"


@app.route("/image")
def image():
  width = request.args.get('width')
  height = request.args.get('height')
  color = request.args.get('color')
  if width is None: width = 300
  if height is None: height = 300
  if color is None: color = 'red'
  img = get_image(int(width), int(height), color)
  return serve_pil_image(img)

@app.route("/text")
def text():
  paragraphs = request.args.get('paragraphs')
  words = request.args.get('words')

  if paragraphs is None: paragraphs = 1
  return gen_text(LOREM, int(paragraphs), words)

### dunder main
if __name__ == "__main__":
  app.run()