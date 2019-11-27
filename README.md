# FEW 1.1 Flask Serve JSON

This is a short tutorial that will show you how to serve static files with Python Flask. 

## Install Python Flask



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
from flask import Flask, render_template, request

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

