import ctypes
import time
import os
import sys
import shutil
executable_name = "main.exe"
def start_screensaver():
    # Call the Windows API to start the screensaver
    ctypes.windll.user32.SystemParametersInfoW(16, 0, 0, 2)

def add_to_startup():

    startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    print(startup_folder)

    if os.path.abspath(sys.argv[0]) != os.path.abspath(os.path.join(startup_folder, executable_name)):
        shutil.copy(sys.argv[0], os.path.join(startup_folder, executable_name))

def main():
   

    add_to_startup()

    while True:
        # Check if the system is idle for the specified time
        if (ctypes.windll.user32.GetTickCount() - ctypes.windll.user32.GetLastInputInfo()) / 1000 >= idle_time:
            start_screensaver()

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    # Check for administrator privileges and request if necessary
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        main()
