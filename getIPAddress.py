from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))

#loc = get('https://ipapi.co/'+ip+'/json/')
loc = get('https://ipapi.co/112.207.104.99/json/')
print (loc.json())