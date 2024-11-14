import pychromecast
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # pychromecast.get_chromecasts() returns a tuple(list, pychromecast.discovery.CastBrowser)
    (chromecasts, castBrowser) = pychromecast.get_chromecasts()

    return f"<p>{chromecasts[0].cast_info.friendly_name}</p>"