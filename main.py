import psutil
import os
import time
# Function to check if KDE Connect process is running
def is_kde_connect_running():
  for process in psutil.process_iter():
    if process.name() == "kdeconnect-kdeconnectd.exe":
      return True
  return False

# Continuously check for KDE Connect and lock if disconnected
while True:
  time.sleep(10)  
  if not is_kde_connect_running():
    # Add a delay or prompt for confirmation before locking (optional)
    os.system("rundll32.exe user32.dll, LockWorkStation")  # This line locks the PC
  else :
    print("KDE Connect is running")