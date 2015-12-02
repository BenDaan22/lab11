#this is a python code to verify the keys

import boto

print boto.Version
import urllib2

url = 'http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read().split(":")
print the_page[0]
print the_page[1]

