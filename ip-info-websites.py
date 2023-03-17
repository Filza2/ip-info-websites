from requests import get
user_agent={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}
# By @TweakPY - @vv1ck
# 

def ip_info():
  
    # ip info websites #
   
    r=get('https://api.ipify.org/?format=json',headers=user_agent).json()['ip'] # request to get the ip
    
    ip=r # Define the IP to be the result of the above request

    r1=get(f'https://ipapi.co/{ip}/json/',headers=user_agent) # request 1 to get ip info 
    
    r2=get(f'http://demo.ip-api.com/json/{ip}?fields=66842623',headers=user_agent) # request 2 to get ip info 
    
    r3=get(f'https://ipinfo.io/widget/demo/{ip}',headers={'Host': 'ipinfo.io','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://ipinfo.io/','Content-Type': 'application/json','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'}) # request 3 to get ip info 
    
    return r1.text+r2.text+r3.text

print(ip_info())
