#upload this to github before you go to beaminster, as well as any other work you've done
#that hasn't been uploaded yet#


from backend import *
from tkinter import *


def setUpHome():

    home = SmartHome()

    for count in range(1,6):

        device = input(f"Choose device {count}: Plug (1) or Fridge (2)\n")

        if device == "1":
            consumption_rate = input("Enter consumption rate (0-150): ")
            smart_device = SmartPlug(consumption_rate)
            home.addDevice(smart_device)

        elif device == "2":
            smart_device = SmartFridge()
            home.addDevice(smart_device)

    return home

home = setUpHome()
devices = home.getDevices()


class SmartHomeSystem:


    def __init__(self, deviceList, backend):
        self.root = Tk()
        self.backend = backend

        self.primaryColor = "#37474F"
        self.secondaryColor = "#FF8B3D"
        self.textColor = "#FFFFFF"
        self.borderType = "solid"

        self.root.title("Smart Home")
        self.root.configure(background=self.primaryColor)

        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(row=0, column=0)
        self.mainFrame.configure(background=self.primaryColor)

        self.deviceInfo = StringVar()
        self.deviceList = deviceList

        self.widgets = []


    def run(self):
        self.createWidgets()
        self.root.mainloop()


    def createWidgets(self):
        self.deleteAllWidgets()

        switchOnAllButton = Button(
            self.mainFrame,
            text="Switch on all",
            font=("Segoe UI", 13),
            width=20,
            relief=self.borderType,
            background=self.secondaryColor,
            foreground=self.textColor,
            command=self.switchOnAll
        )
        switchOnAllButton.grid(row=0, column=0, columnspan=3, padx=50, pady=10)

        switchOffAllButton = Button(
            self.mainFrame,
            text="Switch off all",
            font=("Segoe UI", 13),
            width=20,
            relief=self.borderType,
            background=self.secondaryColor,
            foreground=self.textColor,
            command=self.switchOffAll
        )
        switchOffAllButton.grid(row=0, column=3, columnspan=3, padx=50, pady=10)

        for i, device in enumerate(self.deviceList):
            devInfo = str(device)

            deviceLabel = Label(
                self.mainFrame,
                font=("Segoe UI", 13),
                width=25,
                height=2,
                relief=self.borderType,
                background=self.secondaryColor,
                foreground=self.textColor,
                text=devInfo
            )
            deviceLabel.grid(row=i+1, column=0, columnspan=3, padx=10, pady=10)

            deviceToggleButton = Button(
                self.mainFrame,
                text="Toggle",
                font=("Segoe UI", 13),
                width=10,
                relief=self.borderType,
                background=self.secondaryColor,
                foreground=self.textColor,
                command=lambda index=i: self.deviceToggle(index)
            )
            deviceToggleButton.grid(row=i+1, column=3, padx=10, pady=10)

            deviceEditButton = Button(
                self.mainFrame,
                text="Edit",
                font=("Segoe UI", 13),
                width=10,
                relief=self.borderType,
                background=self.secondaryColor,
                foreground=self.textColor,
                command=lambda index=i: self.deviceEdit()
            )
            deviceEditButton.grid(row=i+1, column=4, padx=10, pady=10)

            deviceDeleteButton = Button(
                self.mainFrame,
                text="Delete",
                font=("Segoe UI", 13),
                width=10,
                relief=self.borderType,
                background=self.secondaryColor,
                foreground=self.textColor,
                command=lambda index=i: self.deviceDelete(index)
            )
            deviceDeleteButton.grid(row=i+1, column=5, padx=15, pady=10)

            self.widgets.append((deviceLabel, deviceToggleButton, deviceEditButton, deviceDeleteButton))

        addDeviceButton = Button(
            self.mainFrame,
            text="Add",
            font=("Segoe UI", 13),
            width=20,
            relief=self.borderType,
            background=self.secondaryColor,
            foreground=self.textColor,
            command=self.addDevice
        )
        addDeviceButton.grid(row=len(self.deviceList)+1, column=0, columnspan=3, padx=10, pady=10)

        self.widgets.append((addDeviceButton, addDeviceButton))

    
    def switchOnAll(self):
        self.backend.turnOnAll()
        self.createWidgets()


    def switchOffAll(self):
        self.backend.turnOffAll()
        self.createWidgets()


    def deviceToggle(self, index):
        self.backend.toggleSwitch(index)
        self.createWidgets()
    

    def deviceEdit(self): #this should launch a new window where the user enters new value, dependent on device type#
        pass


    def deviceDelete(self, index):
        self.backend.removeDeviceAt(index)
        self.createWidgets()

    
    def addDevice(self): #this should launch a new window where the user selects the device type#
        pass


    def deleteAllWidgets(self):
        for widgetlist in self.widgets:
            for widget in widgetlist:
                widget.destroy()
        self.widgets = []


def main(devices, home):
    smarthomesys = SmartHomeSystem(devices, home)
    smarthomesys.run()

main(devices, home)