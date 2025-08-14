# Network Device Monitor

A Python tool to monitor network devices' availability and fetch their geolocation/ISP details using APIs.

## Features
- **Ping Monitoring**: Check if devices are online/offline
- **IP Geolocation**: Fetch country, city and ISP details using [ip-api.com](https://ip-api.com)
- **Simple Dashboard**: Web interface to view results (Flask)
- **Lightweight**: Only 3 dependencies
- **Extensible**: Easy to add email alerts or logging
- 
- ##  Tech Stack
- **Python 3** (Core)
- Libraries:
  - `ping3` - For ICMP ping checks
  - `requests` - For API calls
  - `Flask` - For web dashboard
    
## Installation
1. Clone the repo:
```bash
git clone https://github.com/nicolasruchimura/Network-Device-Monitor.git
cd network-device-monitor

