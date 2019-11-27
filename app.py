from flask import Flask, render_template, request, jsonify

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

# This route serves static/index.html at the route /
@app.route("/")
def index():
  return app.send_static_file('index.html')

# This route serves the dictionary d at the route /data
@app.route("/data")
def data():
  # define some data
  d = {
    "name": "foo",
    "rank": "bar"
  }
  return jsonify(d) # convert your data to JSON and return 


# This route receives data via POST at /send-data
@app.route("/send-data", methods=["POST"])
def sendData():
  d = request.get_json()
  print(d)
  return jsonify(d)



if __name__ == "__main__":
  # app.config["TEMPLATES_AUTO_RELOAD"] = True
  app.run(debug=True)

    