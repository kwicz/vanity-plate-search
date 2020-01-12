import os

from flask import Flask, session, request, render_template, jsonify
from flask_session import Session
import sqlite3

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
conn = sqlite3.connect('dmv2u.sqlite')
cursor = conn.cursor()

@app.route("/", methods=['GET'])
def home():
	
	if request.method == 'GET':
		return render_template("index.html")

	else: 
		return render_template("index.html")

@app.route("/results", methods=['GET'])
def searchResults():
	
	if request.method == 'GET':
		return render_template("results.html")

	else: 
		return render_template("results.html")

@app.route("/restricted", methods=['GET'])
def restrictedPlates():
	
	if request.method == 'GET':
		return render_template("restricted.html")

	else: 
		return render_template("restricted.html")

@app.route("/available", methods=['GET'])
def availablePlates():
	
	if request.method == 'GET':
		return render_template("available.html")

	else: 
		return render_template("available.html")

@app.route("/assigned", methods=['GET'])
def assignedPlates():
	
	if request.method == 'GET':
		return render_template("assigned.html")

	else: 
		return render_template("assigned.html")



