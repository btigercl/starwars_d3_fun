from flask import Flask, render_template, redirect, request, session, flash, g, url_for, jsonify 
from api_calls import ALskillcall, ALlocation, CBskillcall
import jinja2
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.jinja_env.undefined = jinja2.StrictUndefined


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # print "port: " + str(port)
    app.run(debug=True, host="0.0.0.0", port=port)