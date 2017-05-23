import NetworkManager

def getFingerPrint():
    devs=NetworkManager.NetworkManager.Devices

    fingerPrint={}

    for dev in devs:
        if isinstance(dev,NetworkManager.Wireless):
            for ap in dev.AccessPoints:
                fingerPrint[dev.Interface+" "+ap.HwAddress]=ap.Strength
    
    return fingerPrint
