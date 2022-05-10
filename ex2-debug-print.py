proxies={
    "192.168.1": "172.16.1.1",
    "192.168.2": "172.16.2.1",
    "192.168.3": "172.16.3.1",
    "192.168.4": "172.16.4.1",
    "192.168.5": "172.16.5.1",
    "192.168.6": "172.16.6.1",
    "192.168.7": "172.16.7.1",
    "192.168.8": "172.16.8.1",
    "192.168.9": "172.16.9.1",
    "192.168.10": "172.16.10.1"
}

devices={
    "router1-1": "192.168.1.1",
    "router1-2": "192.168.1.2",
    "router2-1": "192.168.2.1",
    "router2-2": "192.168.2.2",
    "router3-1": "192.168.3.1",
    "router3-2": "192.168.3.2",
    "router4-1": "192.168.4.1",
    "router4-2": "192.168.4.2",
    "router5-1": "192.168.5.1",
    "router5-2": "192.168.5.2",
    "router6-1": "192.168.6.1",
    "router6-2": "192.168.6.2",
    "router7-1": "192.168.7.1",
    "router7-2": "192.168.7.2",
    "router8-1": "192.168.8.1",
    "router8-2": "192.168.8.2",
    "router9-1": "192.168.9.1",
    "router9-2": "192.168.9.2",
    "router10-1": "192.168.10.1",
    "router10-2": "192.168.10.2",
}

def get_proxy(ip):
    #return proxy based on the subnet
    print(f"DEBUG. Requested ip: {ip}")
    print(f"DEBUG. Subnet for ip: {ip[:9]}")
    print(f"DEBUG. Returning proxy: {proxies[ip[:9]]}")
    return(proxies[ip[:9]])

for device in devices:
    proxy=get_proxy(devices[device])
    print(f"To reach {device} use {proxy}")