import urllib.request   
import urllib.parse      

url = "http://localhost:5000/sms"   
params = {"param1": "arg1",
            "param2": "arg2",       
            "param3": "arg3"   
}      

query_string = urllib.parse.urlencode(params)   
data = query_string.encode( "ascii" ) 

with urllib.request.urlopen(url, data) as response:        
    response_text = response.read()        
    print(response_text)
