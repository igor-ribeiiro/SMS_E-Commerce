import urllib.request   
import urllib.parse      

url = "http://localhost:5000/sms"   
params = {"Body": "5 coca, 3 guarana, 7 refri",
            "From": "from who?"   
}      

query_string = urllib.parse.urlencode(params)   
data = query_string.encode( "ascii" ) 

with urllib.request.urlopen(url, data) as response:        
    response_text = response.read()        
    print(response_text)
