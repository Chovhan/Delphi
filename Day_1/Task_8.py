import os


def volume_up(value):
    os.system("nircmd.exe changesysvolume %d" %value)


def volume_down(value):
    os.system("nircmd.exe changesysvolume -%d" %value)


choice = input("Up/down").lower()
volume = int(input("Enter volume: "))*650
if choice == "up":
    volume_up(volume)
else:
    volume_down(volume)