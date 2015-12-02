# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#

import boto.sqs
import argparse
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys

import boto

import urllib2

url = 'http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read().split(":")

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = the_page[0]
secret_access_key = the_page[1]

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

parser = argparse.ArgumentParser()
parser.add_argument("qname")
parser.add_argument("qmessage")
the_page = parser.parse_args()

# Get a list of the queues that exists and then print the list out
rs = conn.get_all_queues()
q = conn.get_queue(the_page.qname)

try:
	message = the_page.qmessage
	m = Message()
	m.set_body(message)
	status = q.write(m)
	print "Message: " + the_page.qmessage + " - written to " + the_page.qname

except:
	print "Could not write message"
