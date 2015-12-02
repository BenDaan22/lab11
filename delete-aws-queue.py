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
the_page = parser.parse_args()

# Get a list of the queues that exists and then print the list out
rs = conn.get_all_queues()

try:
	q = conn.get_queue(the_page.qname)

except:
	print "Cannot find the desired queue", the_page.qname

try:
	conn.delete_queue(q,True)
	print the_page, "the desired queue is deleted"
except:
	print "Cannot delete desired queue, or doesnt exist"
