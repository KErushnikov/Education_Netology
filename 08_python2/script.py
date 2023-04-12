import nmap3
scan = nmap3.Nmap()
result = scan.nmap_version_detection("192.168.0.10")

for i in result['192.168.0.10']['ports']:
    serv = dict(i['service'])
    k = serv.get('product')
    v = serv.get('version')
    print(f"Product: {k}, Version: {v}, Port: {i['portid']}")