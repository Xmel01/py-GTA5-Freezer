import time
import sys


import psutil
import wmi

def main(process_name: str, freeze_time):

    print(f"freezing {process_name} on {freeze_time} seconds ...")

    conn = wmi.WMI()
    id_mas = list()
    for process in conn.Win32_Process(name=process_name):
        id_mas.append(process.ProcessID)
        print(process.ProcessID, process.name)

    if len(id_mas) != 0:
        for id in id_mas:
            p = psutil.Process(id)
            p.suspend()

        time.sleep(freeze_time)

        for id in id_mas:
            p = psutil.Process(id)
            p.resume()

        print('successful')
    else:
        print("GTA5 is not working")

if __name__ == '__main__':
    main('GTA5.exe', 10)
    #main(sys.argv[1] + '.exe', sys.argv[2]) if you want to freeze some another process