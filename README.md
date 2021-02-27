# Altran_assignment

Steps to Deploy/Start Application

Note - Make sure you have Python 3.5+ and MySQL installed

1. Clone the project
2. Execute requirements.txt to install dependencies.\
	pip install -r requirements.txt
3. Edit config.py -> dbName and flaskPort variables as per your requirement
4. Now run the flask server.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python main.py
	
5. Application supports below API's:
a. GET /users\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns all the registered users
b. POST /users\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Body->\
		{\
			"name" : "<Value>",\
			"email": "<Value>",\
			"password": "<Value>", \
			"profile_pic_url" : "<Value>", \
			"mobile" : "<Value>",\
			"address": {\
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"house_num" : "<Value>", \
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"address_1": "<Value>",\
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"address_2": "<Value>", \
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"city": "<Value>", \
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"state": "<Value>",\
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"pincode": <Value Int>\
			}\
		}
