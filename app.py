import os
import re
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
	"""Render map"""
	return render_template('index.html')
