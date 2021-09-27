import requests

def get_user(user_id):
	#import pdb;pdb.set_trace()
	print("GET USER CALLED")
	url = "https://reqres.in/api/users?page=2"
	response = requests.get(url)
	return response.status_code

def users():
	resp = get_user(23)
	return resp


def add(x,y):
	try:
		return x+y  
	except:
		return None

def sub(x,y):
	return x-y