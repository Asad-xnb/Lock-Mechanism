import subprocess
import platform
import time
import os

# def is_device_present(device_ip):
#     command = f"ping -c 1 -w 1000 {device_ip}"
#     try:
#         result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print(result.returncode == 0)
#         return result.returncode == 0
#     except subprocess.CalledProcessError:
#         return False

def is_device_present(device_ip, timeout=1000):
    """Checks if a device is reachable on the network using ping.

    Args:
        device_ip (str): The IP address of the device to check.
        timeout (int, optional): The maximum time (in milliseconds) to wait for a response. Defaults to 1000.

    Returns:
        bool: True if the device is reachable, False otherwise.
    """
    command = ["ping", "-c", "1", "-W", str(timeout // 1000), device_ip]  # Adjust timeout to seconds
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=timeout/1000)
        if result.returncode == 0 and result.stdout.decode().startswith("PING"):
            return True
        else:
            return False
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return False
    except Exception:  
        return False



specific_device_ip = '192.168.1.9'

while True:
    if not is_device_present(specific_device_ip):
        if platform.system() == 'Windows':
            os.system("rundll32.exe user32.dll, LockWorkStation") 
            break
        elif platform.system() == 'Linux':
            os.system('xscreensaver-command -activate') # add -lock flag to lock the screen 
            print("Device is not present")
        else:
            print("Unsupported operating system.")
            break
    else:
        os.system('xscreensaver-command -deactivate')
        print("Device is present")
    time.sleep(1) 
