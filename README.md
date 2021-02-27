# Altran_assignment

Steps to Deploy/Start Application

Note - Make sure you have Python 3.5+ and MySQL installed

1. Clone the project
2. Execute requirements.txt to install dependencies.\
	pip install -r requirements.txt
3. Edit config.py -> dbName and flaskPort variables as per your requirement
4. Now run the flask server.\
	python main.py
	
5. Application supports below API's:
a. GET /users\
	Returns all the registered users
b. POST /users\
	Body->\
		{\
			"name" : "<Value>",\
			"email": "<Value>",\
			"password": "<Value>", \
			"profile_pic_url" : "<Value>", \
			"mobile" : "<Value>",\
			"address": {\
				"house_num" : "<Value>", \
				"address_1": "<Value>",\
				"address_2": "<Value>", \
				"city": "<Value>", \
				"state": "<Value>",\
				"pincode": <Value Int>\
			}\
		}\
