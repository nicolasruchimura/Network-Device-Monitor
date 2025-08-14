import requests
from ping3 import ping
import time

def check_device(ip):
    response_time = ping(ip, timeout=2)
    is_online = response_time is not None

    api_url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(api_url).json()
        country = response.get('country', 'Unknown')
        isp = response.get('isp', 'Unknown')
    
    except:
        country = isp = "API Error"
    
    return {
        "IP": ip, 
        "Status": "Online" if is_online else "Offline",
        "Response Time (ms)": round(response_time * 1000, 2) if is_online else "N/A",
        "Country": country,
        "ISP": isp
    }

devices = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]
for device in devices:
    result = check_device(device)
    print(result)