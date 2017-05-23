import NetworkManager

def getFingerPrint():
    devs=NetworkManager.NetworkManager.Devices

    fingerPrint={}

    for dev in devs:
        if isinstance(dev,NetworkManager.Wireless):
            apList={}
            for ap in dev.AccessPoints:
                apList[ap.HwAddress]=ap.Strength
            fingerPrint[dev.Interface]=apList
    
    return fingerPrint
