from backend import *
from tkinter import *


def setUpHome():

    home = SmartHome()

    for count in range(1,6):

        device = input(f"Choose device {count}: Plug (1) or Fridge (2)\n")

        if device == "1":
            consumptionRate = input("Enter consumption rate (0-150): ")
            smartDevice = SmartPlug(consumptionRate)
            home.addDevice(smartDevice)

        elif device == "2":
            smartDevice = SmartFridge()
            home.addDevice(smartDevice)

        else:
            print("ERROR: Invalid input.")

    return home

home = setUpHome()
devices = home.getDevices()


class SmartHomeSystem:


    def __init__(self, deviceList):
        self.root = Tk()

        self.backgroundColor = "#102820"
        self.deviceButtonColor = "#838562"
        self.oButtonColor = "#525032"
        self.labelColor = "#8A6240"
        self.textColor = "#F4E4C9"

        self.buttonBorder = "raised"
        self.labelBorder = "solid"

        self.root.title("Smart Home")
        self.root.configure(background=self.backgroundColor)
        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(row=0, column=0)
        self.mainFrame.configure(background=self.backgroundColor)

        self.deviceInfo = StringVar()
        self.deviceList = deviceList

        self.widgets = []

        self.root.focus()


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
            relief=self.buttonBorder,
            background=self.oButtonColor,
            foreground=self.textColor,
            command=self.switchOnAll
        )
        switchOnAllButton.grid(row=0, column=0, columnspan=3, padx=50, pady=10)

        switchOffAllButton = Button(
            self.mainFrame,
            text="Switch off all",
            font=("Segoe UI", 13),
            width=20,
            relief=self.buttonBorder,
            background=self.oButtonColor,
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
                relief=self.labelBorder,
                background=self.labelColor,
                foreground=self.textColor,
                text=devInfo
            )
            deviceLabel.grid(row=i+1, column=0, columnspan=3, padx=10, pady=10)

            deviceToggleButton = Button(
                self.mainFrame,
                text="Toggle",
                font=("Segoe UI", 13),
                width=10,
                relief=self.buttonBorder,
                background=self.deviceButtonColor,
                foreground=self.textColor,
                command=lambda index=i: self.deviceToggle(index)
            )
            deviceToggleButton.grid(row=i+1, column=3, padx=10, pady=10)

            deviceEditButton = Button(
                self.mainFrame,
                text="Edit",
                font=("Segoe UI", 13),
                width=10,
                relief=self.buttonBorder,
                background=self.deviceButtonColor,
                foreground=self.textColor,
                command=lambda index=i: self.deviceEdit(index)
            )
            deviceEditButton.grid(row=i+1, column=4, padx=10, pady=10)

            deviceDeleteButton = Button(
                self.mainFrame,
                text="Delete",
                font=("Segoe UI", 13),
                width=10,
                relief=self.buttonBorder,
                background=self.deviceButtonColor,
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
            relief=self.buttonBorder,
            background=self.oButtonColor,
            foreground=self.textColor,
            command=self.addNewDevice
        )
        addDeviceButton.grid(row=len(self.deviceList)+1, column=0, columnspan=3, padx=10, pady=10)

        self.widgets.append((addDeviceButton, addDeviceButton))

    
    def switchOnAll(self):
        home.turnOnAll()
        self.createWidgets()


    def switchOffAll(self):
        home.turnOffAll()
        self.createWidgets()


    def deviceToggle(self, index):
        home.toggleSwitch(index)
        self.createWidgets()
    

    def deviceEdit(self, index):

        self.deviceEditWindow = Toplevel(self.root)
        self.deviceEditWindow.title("Edit Device")
        self.editWindowFrame = Frame(self.deviceEditWindow)
        self.editWindowFrame.grid(row=0, column=0)

        self.editWindowFrame.config(background=self.backgroundColor)
        self.deviceEditWindow.config(background=self.backgroundColor)

        self.deviceEditWindow.focus()
        self.deviceEditWindow.grab_set()

        self.newDeviceValue = StringVar()
        deviceParameters = StringVar()

        if isinstance(self.deviceList[index], SmartFridge):
            deviceParameters = "Edit temperature (1, 3, 5):" 
        elif isinstance(self.deviceList[index], SmartPlug):
            deviceParameters = "Edit consumption rate (0-150):"

        deviceEditLabel = Label(
            self.editWindowFrame,
            text=deviceParameters,
            font=("Segoe UI", 13),
            width=25,
            relief=self.labelBorder,
            background=self.labelColor,
            foreground=self.textColor
        )
        deviceEditLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        deviceEditEntry = Entry(
            self.editWindowFrame,
            textvariable=self.newDeviceValue,
            font=("Segoe UI", 13),
            width=20,
            relief=self.labelBorder,
            background=self.deviceButtonColor,
            foreground=self.textColor
        )
        deviceEditEntry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        deviceEditButton = Button(
            self.editWindowFrame,
            text="Confirm",
            font=("Segoe UI", 13),
            width=20,
            relief=self.buttonBorder,
            background=self.oButtonColor,
            foreground=self.textColor,
            command=lambda idx=index: self.deviceEditLink(idx)
        )
        deviceEditButton.grid(row=2, column=0, columnspan=3, padx=10, pady=10)


    def deviceEditLink(self, index):
        device = self.deviceList[index]

        try:
            newValue = int(self.newDeviceValue.get())
        except:
            self.errorDisplay("ERROR: Invalid input. Can only be positive integer.")

        if isinstance(device, SmartPlug):
            if newValue > 150 or newValue < 0:
                self.errorDisplay("ERROR: Invalid input. Plug consumption rate must be between 0-150.")
            else:
                device.setConsumptionRate(int(newValue))

        elif isinstance(device, SmartFridge):
            try:
                if newValue not in device.acceptableTemps:
                    self.errorDisplay("ERROR: Invalid input. Fridge temperature must be 1, 3 or 5 degrees.")
                else:
                    device.setTemperature(newValue)
            except UnboundLocalError:
                pass

        home.updateDevice(index, device)
        self.widgets[index][0].config(text=str(device))
        self.deviceEditWindow.destroy()


    def addNewDevice(self):

        self.addDeviceWindow = Toplevel(self.root)
        self.addDeviceWindow.title("Add a Device")
        self.addWindowFrame = Frame(self.addDeviceWindow)
        self.addWindowFrame.grid(row=0, column=0)

        self.addWindowFrame.config(background=self.backgroundColor)
        self.addDeviceWindow.config(background=self.backgroundColor)

        self.consumptionRate = StringVar()

        self.addDeviceWindow.focus()
        self.addDeviceWindow.grab_set()

        addFridgeButton = Button(
            self.addWindowFrame,
            text="Add a fridge",
            font=("Segoe UI", 13),
            width=20,
            relief=self.buttonBorder,
            background=self.oButtonColor,
            foreground=self.textColor,
            command=lambda: self.addFridge()
        )
        addFridgeButton.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        addPlugButton = Button(
            self.addWindowFrame,
            text="Add a plug",
            font=("Segoe UI", 13),
            width=20,
            relief=self.buttonBorder,
            background=self.oButtonColor,
            foreground=self.textColor,
            command=lambda: self.addPlug()
        )
        addPlugButton.grid(row=0, column=4, columnspan=3, padx=10, pady=10)

        consumptionRateEntry = Entry(
            self.addWindowFrame,
            textvariable=self.consumptionRate,
            font=("Segoe UI", 13),
            width=20,
            relief=self.labelBorder,
            background=self.labelColor,
            foreground=self.textColor
        )
        consumptionRateEntry.grid(row=1, column=4, columnspan=3, padx=10, pady=10)


    def addFridge(self):
        smartDevice = SmartFridge()
        home.addDevice(smartDevice)
        self.createWidgets()
        self.addDeviceWindow.destroy()


    def addPlug(self):
        try:
            consumptionRate = int(self.consumptionRate.get())
        except:
            self.errorDisplay("ERROR: Invalid input. Can only be a positive integer.")
            consumptionRate = 75 #default value if no input is given or input is invalid#

        if consumptionRate > 150 or consumptionRate < 0:
            self.errorDisplay("ERROR: Invalid input. Consumption rate must be between 0-150.")
            consumptionRate = 75 #default value if input is outside normal range#

        smartDevice = SmartPlug(int(consumptionRate))
        home.addDevice(smartDevice)
        self.createWidgets()
        self.addDeviceWindow.destroy()


    def deviceDelete(self, index):
        home.removeDeviceAt(index)
        self.createWidgets()


    def errorDisplay(self, errorMessage):
        self.errorWindow = Toplevel(self.root)
        self.errorWindow.title("")
        self.errorWindowFrame = Frame(self.errorWindow)
        self.errorWindowFrame.grid(row=0, column=0)

        self.errorWindow.configure(background=self.backgroundColor)
        self.errorWindowFrame.configure(background=self.backgroundColor)

        self.errorWindow.focus()
        self.errorWindow.grab_set()

        errorLabel = Label(
            self.errorWindowFrame,
            text=errorMessage,
            font=("Segoe UI", 13),
            relief=self.labelBorder,
            background=self.labelColor,
            foreground=self.textColor
        )
        errorLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        okButton = Button(
            self.errorWindowFrame,
            text="OK",
            font=("Segoe UI", 13),
            width=25,
            relief=self.buttonBorder,
            background=self.oButtonColor,
            foreground=self.textColor,
            command=lambda: self.errorWindow.destroy()
        )
        okButton.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


    def deleteAllWidgets(self):
        for widgetlist in self.widgets:
            for widget in widgetlist:
                widget.destroy()
        self.widgets = []


def main(devices):
    smarthomesys = SmartHomeSystem(devices)
    smarthomesys.run()

main(devices)