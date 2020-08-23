# using flask_restful 
from flask import Flask, jsonify,request,render_template,redirect, url_for
from flask_restful import Resource, Api 
import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('revised_measurements_new.csv')#, sep='\t', names=['user_id','item_id','rating','titmestamp'])

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class Hello(Resource): 

	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
	def get(self): 

		return jsonify({'message': 'hello world'}) 

	# Corresponds to POST request 
	def post(self): 
		
		data = request.get_json()	 # status code 
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number 
class Square(Resource): 

	def get(self, num): 

		return jsonify({'square': num**2}) 



def dress_suggestions(body_shape):
    dress=df[df['body type']==body_shape]['category'].unique()
    #dress=pd.DataFrame(dress)
    a=df.groupby('category')['rating'].describe()
    #Gives the threshold for the number of reviewers
    a=a[a['count']>5]
    a=(a.index.values)
    #a=pd.DataFrame(a)
    shortlisted_dress=set(a)-(set(a)-set(dress))
    return list(shortlisted_dress)
    #return jsonify({'recommendation':list(shortlisted_dress)})


class Dress_suggestions(Resource):
    def post(self,colour,occasion,body_shape):
        body_shape=body_shape
        occasion=occasion
        occasion_dress=list(df[(df['body type']==body_shape) & (df['rented for']==occasion)]['category'].unique())
        j=dress_suggestions(body_shape)
        custom_dress=set(occasion_dress)-(set(occasion_dress)-set(j))
        #return list(custom_dress)
        f=list(custom_dress)
        return jsonify({'custom_recommendation':f})

    def get(self,colour,occasion,body_shape):
        body_shape=body_shape
        occasion=occasion
        occasion_dress=list(df[(df['body type']==body_shape) & (df['rented for']==occasion)]['category'].unique())
        j=dress_suggestions(body_shape)
        custom_dress=set(occasion_dress)-(set(occasion_dress)-set(j))
        #return list(custom_dress)
        f=list(custom_dress)
        return jsonify({'custom_recommendation':f})


# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 
api.add_resource(Dress_suggestions, '/cust_sugg/<string:colour>/<string:occasion>/<string:body_shape>') 


# driver function 
if __name__ == '__main__': 

	app.run(host='0.0.0.0',debug = False) 
