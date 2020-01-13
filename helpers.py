import sqlite3


def select(search):
	print ('****************************************************************************************************')
	print('Attempting to get data for an existing plate')
	
	conn = sqlite3.connect('dmv2u.sqlite')
	cursor = conn.cursor()
	print("Opened database successfully")

	cursor.execute('''SELECT EXISTS (SELECT 1 FROM DMV2U WHERE 
							STRING=? LIMIT 1)''', 
							(search.upper(),))
	conn.commit()
	exists = cursor.fetchone()

	if (exists[0] == 0): 
		print('License Plate doesn\'t exist in the database')
		error = "License Plate doesn\'t exist in the database"
		return error
	else:
		print('License plate record for string ' + search + ' does exists. Returning data.')
		cursor.execute('''SELECT STATUS, LAST FROM DMV2U WHERE 
							STRING=?''', 
							(search.upper(),))
		record = cursor.fetchone()
		print("helper record: " + str(record))
		result = []
		#result.status = record[0]
		#result.last = record[1]

	conn.commit()
	conn.close()
	return record

