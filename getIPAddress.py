#import get function from the requests library
#requests library in order to get API from the website 
from requests import get

#run API from ipify.org and convert results to text
#API takes Public IPv4 Address of Computer
ip = get('https://api.ipify.org').text

#print Public IPv4 Address
print('My public IP address is: {}'.format(ip))

#run API from ipapi.co
#API takes an input of an IPv4 Address and gets information
#based off of it
loc = get('https://ipapi.co/'+ip+'/json/')
print (loc.json())