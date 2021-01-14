from flask import Flask,jsonify,make_response
import os
import boto3
import awsgi


app = Flask(__name__)
VISITORS_TABLE = os.environ['VISITORS_TABLE']

@app.route("/mainpage")
def mainpage():
  return 'working'

@app.route("/getcount")
def returncount():
  dynamodbclient=boto3.resource('dynamodb')
  table = dynamodbclient.Table(VISITORS_TABLE)
  response = table.scan()
  data = response['Items']
  resp=make_response(jsonify(count=len(data)),200)
  return resp

def lambda_handler(event, context):
    return awsgi.response(app,event,context)

