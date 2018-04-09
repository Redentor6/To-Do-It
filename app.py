from flask import Flask, render_template, request, jsonify
    from pusher import Pusher
    import json

    # creates flask app
    app = Flask(__name__)

    # configures pusher obj
    pusher = Pusher(
      app_id= "506177",
      key= "67e28f4a286cfbf553ba",
      secret= "53473f7d6ed44f05db83",
      cluster= "us2",
      ssl=True
    )

    # index route, shows index.html view
    @app.route('/')
    def index():
      return render_template('index.html')