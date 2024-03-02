class SmartPlug:

    def __init__(self, consumption_rate):
        self.switched_on = False
        self.consumption_rate = consumption_rate

    def toggleSwitch(self):
        if self.switched_on == False:
            self.switched_on = True
        else:
            self.switched_on = False

    def getSwitchedOn(self):
        if self.switched_on == True:
            return "on"
        else:
            return "off"

    def getConsumptionRate(self):
        if self.consumption_rate >= 0 and self.consumption_rate <= 150:
            return self.consumption_rate
        else:
            return f"ERROR: Consumption rate outside of normal range: {self.consumption_rate}"

    def setConsumptionRate(self, rate):
        if rate >= 0 and rate <= 150:
            self.consumption_rate = rate
        else:
            print(f"ERROR: Cannot set consumption rate outside normal range: {rate}")

    def __str__(self):
        status = self.getSwitchedOn()
        return f"Plug: {status}, consumption = {self.consumption_rate}"


class SmartFridge:

    def __init__(self):
        self.switched_on = False
        self.temperature = 3
        self.acceptable_temps = [1,3,5]

    def toggleSwitch(self):
        if self.switched_on == True:
            self.switched_on = False
        else:
            self.switched_on = True

    def getSwitchedOn(self):
        if self.switched_on == True:
            return "on"
        else:
            return "off"

    def getTemperature(self):
        if self.temperature in self.acceptable_temps:
            return self.temperature
        else:
            return None

    def setTemperature(self, temperature):
        if temperature in self.acceptable_temps:
            self.temperature = temperature
        else:
            pass

    def __str__(self):
        status = self.getSwitchedOn()
        return f"Fridge: {status}, temperature = {self.temperature}"


class SmartHome:

    def __init__(self):
        self.devices = []
        self.device_count = 0

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
