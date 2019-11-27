# FEW 1.1 Flask Serve JSON

This is a short tutorial that will show you how to serve static files with Python Flask. 

## Install Python Flask

`pip install Flask`

Run your server with: 

`flask run`

## Create Directory structure

Create the following files and folders. 

- my-project
  - static
    - index.html
    - styles 
    - images
  - app.py

the static directory will host static files. These are files that are not rendered, that is their content is not dynamic. 

## Set up app.py

```python
from flask import Flask, render_template, request, jsonify

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
  return app.send_static_file('index.html')

if __name__ == "__main__":
  # app.config["TEMPLATES_AUTO_RELOAD"] = True
  app.run(debug=True)
```

Here you imported some packages to be used by your app. 

Defined the app with a static url path. 

The defined a single route. This route will send the single static file `index.html`. This file is in the static directory. 

Last, you started your server on port 5000. 

## Serve JSON from a route

```python
# This route serves the dictionary d at the route /date
@app.route("/data")
def data():
  # define some data
  d = {
    "name": "foo",
    "rank": "bar"
  }
  return jsonify(d) # convert your data to JSON and return
```

This new route serves JSON data from the route `/data`. 

The data starts as a dictionary. 

Use `jsonify()` to convert the dictionary into a JSON string and return this to the client that made the request. 

## Loading JSON from your route with JS

```JS
// Loads data from the route /data (see app.py)
fetch('/data').then(function(res) {
  return res.json()
}).then(function(json) {
  const h1 = document.querySelector('h1')
  const h2 = document.querySelector('h2')
  // Use the JSON data to populate these elements
  h1.innerHTML = json.name 
  h2.innerHTML = json.rank
}).catch(function(err) {
  console.log(err.message)
})
```

The JavaScript above would be used in your static page (`index.html`)

The first line uses `fetch()` to make a request to the route `/data`. 

We handle the request by assigning some of the values returned as part of the JSON object to HTML elements in the DOM. 

Try this on your own: 

- Add some new fields to the dictionary in app.py
- Get those new field from the JSON object in your JS and assign it an element in the DOM. 
- Generate serverside data dynamically and return that by attaching it to the dictionary in the `/data` route. 

## Receiveing at a Route

```Python
# This route receives data via POST at /send-data
@app.route("/send-data", methods=["POST"])
def sendData():
  d = request.get_json()
  print(d) 
  return jsonify(d)
```

The route above receives data via the POST method. 

Converts that data from JSON to a Python Dict (d). 

Then converts the dict to JSON and sends this back as a reply. 

In short this route receives JSON and then sends that same JSON back. This is just an example to show the process. You would apply some code to shape a custom response before the return statement. 

## Sending JSON Data with Fetch

```JS
const str = sendInput.value

const options = {
  method: 'post',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ data: str })
}

// Query the /send-data route with fetch
fetch('/send-data', options)
  .then(function(res){
    return res.json()
  }).then(function(json){
    // Handle the response and display the data received
    sendResults.innerHTML = json.data
  }).catch(function(err) {
    console.log(err.message)
  })
```

The first get a string to send to the server. This comes from the input in the form in the example. 

Next define some options to send the data using POST as JSON. We need to create an options object with a method: POST, headers: defines the type of data we're sending, and body: this is content we are sending. 

Use fetch to send and receive data. This fucntion expects a JSON response with a data property. Which it displays a DOM element. 



