import csv
import os
import psutil
import time


def get_process_name():
    return input("Enter process name: ")


def find_process_pid(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return process.pid


def get_info(process_name, process):
    return [process_name, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), str(process.cpu_percent(interval=5)), str(process.memory_full_info().rss),
            str(psutil.virtual_memory().free),
            str(100-psutil.cpu_percent(interval=5))]


def record_data(data):
    dir = os.path.abspath(os.curdir)
    timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
    timestr = str(dir) + '\\' + timestr
    with open(timestr + '.csv', 'w', newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(data)


process_name = get_process_name()
record_data(get_info(process_name, psutil.Process(find_process_pid(process_name))))
