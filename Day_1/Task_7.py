from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def change_volume(speakers_volume):

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(speakers_volume*(-1), None)
    print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())


change_volume(int(input("Enter volume level (65 min, 0 max)")))
