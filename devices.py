import nmap
import os

# def is_device_present(ip_range, device_ip):
#     nm = nmap.PortScanner()
#     nm.scan(hosts=ip_range, arguments='-sn')

#     for host in nm.all_hosts():
#         if host == device_ip:
#             return True
#     return False

# def lock_if_device_not_present(ip_range, device_ip):
#     if not is_device_present(ip_range, device_ip):
#         # Add a delay or prompt for confirmation before locking (optional)
#         os.system("rundll32.exe user32.dll, LockWorkStation")  # This line locks the PC
#     else:
#         print("Device is present on the network.")

# # Example usage
# network_range = '192.168.1.0/24'
# specific_device_ip = '192.168.1.100'  # Change this to the IP address of the specific device you want to check for
# lock_if_device_not_present(network_range, specific_device_ip)


def scan_network(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')

    for host in nm.all_hosts():
        print(f"Host: {host} {'(' + nm[host].hostname() + ')' if 'hostname' in nm[host] else ''} is {'up' if nm[host].state() == 'up' else 'down'}")

# Example usage
scan_network('192.168.1.1/24')  # Replace with your network range
