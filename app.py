import os

from flask import Flask, session, request, render_template, jsonify
from flask_session import Session
import sqlite3
import helpers

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
conn = sqlite3.connect('dmv2u.sqlite')
cursor = conn.cursor()

# Route to landing page
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("index.html")

# Searches for plate status
@app.route("/quick-search/", methods=['POST'])
def checkPlate():
	search = request.form.get("quick-search")
	search = search.upper()
	print("search: " + search)
	record = helpers.select(search)
	print("app record: " + str(record))
	if record == "License Plate doesn\'t exist in the database":
		return render_template("index.html", record=record)
	else:
		status = record[0].lower()
		last = record[1]
		print("status and last: " + status + " + " + last)
		return render_template("index.html", search=search, status=status, last=last)
		clear(search, status, last)
		print("search, status, last: " + search + status + last)

# Loads page with search tool
@app.route("/search/", methods=['GET', 'POST'])
def interactiveSearch():	
	if request.method == 'GET':
		print("SEARCH PLATES")
		return render_template("search.html")
	# Returns table of matching search results
	else:
		search = request.form.get("plateSearchInput")
		search = search.upper()
		print("search: " + search)
		records = helpers.interactiveSearch(search)
		# for record in records:
		# 	plate = record[1]
		# 	status = record[2]
		# 	last = record[3]
		# 	data = {"plate": plate, "status": status, "last": last}
		# 	records.append(data)
		# 	print("record: " + str(record[1]))
			

		return render_template("search.html", records=records)
	

# Returns table of available plates
@app.route("/available/", methods=['POST'])
def availablePlates():
	print("AVAILABLE PLATES!")
	return render_template("search.html")

# Returns table of restricted plates
@app.route("/restricted/", methods=['POST'])
def restrictedPlates():
	print("RESTRICTED PLATES!")
	return render_template("search.html")

# Returns table of assigned plates
@app.route("/assigned/", methods=['POST'])
def assignedPlates():
	print("ASSIGNED PLATES!")
	return render_template("search.html")
