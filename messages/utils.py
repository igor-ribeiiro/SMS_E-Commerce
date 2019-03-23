import urllib.request   
import urllib.parse      

from messages.db import DB


url = "http://localhost:5000/sms"   

gambi = 2

body = "error"
if gambi == 1:
    body = "5 coca, 3 deterjente, 7 aros"
if gambi == 2:
    body = "Pegar na loja"
if gambi == 3:
    body = "Rua H8A 121"
if gambi == 4:
    body = "Igor Ribeiro"

params = {"Body": body,
            "From": "+5585999911065"   
}      

query_string = urllib.parse.urlencode(params)   
data = query_string.encode( "ascii" ) 

with urllib.request.urlopen(url, data) as response:        
    response_text = response.read()        
    print(response_text)
