class SmartPlug:


    def __init__(self, consumptionRate):
        self.switchedOn = False
        self.consumptionRate = consumptionRate


    def toggleSwitch(self):
        if self.switchedOn == False:
            self.switchedOn = True
        else:
            self.switchedOn = False


    def getSwitchedOn(self):
        if self.switchedOn == True:
            return "on"
        else:
            return "off"


    def getConsumptionRate(self):
        if self.consumptionRate >= 0 and self.consumptionRate <= 150:
            return self.consumptionRate
        else:
            return f"ERROR: Consumption rate outside of normal range: {self.consumptionRate}"


    def setConsumptionRate(self, rate):
        if rate >= 0 and rate <= 150:
            self.consumptionRate = rate
        else:
            print(f"ERROR: Cannot set consumption rate outside normal range: {rate}")


    def __str__(self):
        status = self.getSwitchedOn()
        return f"Plug: {status}, Consumption: {self.consumptionRate}"


def testSmartPlug():
    plug = SmartPlug(45)
    plug.toggleSwitch()
    print(plug.switchedOn)
    print(plug.getConsumptionRate)
    plug.setConsumptionRate(100)
    print(plug.getConsumptionRate)
    print(plug)

#testSmartPlug()


class SmartFridge:


    def __init__(self):
        self.switchedOn = False
        self.temperature = 3
        self.acceptableTemps = [1,3,5]


    def toggleSwitch(self):
        if self.switchedOn == True:
            self.switchedOn = False
        else:
            self.switchedOn = True


    def getSwitchedOn(self):
        if self.switchedOn == True:
            return "on"
        else:
            return "off"


    def getTemperature(self):
        if self.temperature in self.acceptableTemps:
            return self.temperature
        else:
            return None


    def setTemperature(self, temperature):
        if temperature in self.acceptableTemps:
            self.temperature = temperature
        else:
            pass


    def __str__(self):
        status = self.getSwitchedOn()
        return f"Fridge: {status}, Temperature: {self.temperature}"


def testSmartFridge():
    fridge = SmartFridge()
    fridge.toggleSwitch()
    print(fridge.getSwitchedOn)
    print(fridge.getTemperature)
    fridge.setTemperature(5)
    print(fridge.getTemperature)
    print(fridge)

#testSmartFridge()


class SmartHome:


    def __init__(self):
        self.devices = []
        self.deviceCount = 0


    def getDevices(self):
        if len(self.devices) != 0:
            return self.devices
        else:
            return None


    def getDeviceAt(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            return None


    def removeDeviceAt(self, index):
        if index >= 0 and index <= len(self.devices)-1:
            del self.devices[index]
        else:
            pass
    

    def addDevice(self, device):
        self.devices.append(device)


    def toggleSwitch(self, index):
        device = self.devices[index]
        device.toggleSwitch()


    def turnOnAll(self):
        for device in self.devices:
            if device.getSwitchedOn() == "off":
                device.toggleSwitch()
    

    def turnOffAll(self):
        for device in self.devices:
            if device.getSwitchedOn() == "on":
                device.toggleSwitch()

            
    def updateDevice(self, index, device):
        if 0 <= index < len(self.devices):
            self.devices[index] = device
    

    def __str__(self):
        output = "Smart Home devices:\n"
        for device in self.devices:
            output += str(device) + '\n'
        return output


def testSmartHome():
    home = SmartHome()
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    fridge1 = SmartFridge()
    plug1.toggleSwitch()
    plug1.setConsumptionRate(150)
    plug2.setConsumptionRate(25)
    fridge1.setTemperature(5)
    home.addDevice(plug1)
    home.addDevice(plug2)
    home.addDevice(fridge1)
    home.toggleSwitch(1)
    print(home)
    home.turnOnAll()
    print(home)
    home.removeDeviceAt(0)
    print(home)

#testSmartHome()