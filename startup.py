from bluepy.btle import DefaultDelegate, Scanner, Peripheral, ADDR_TYPE_PUBLIC, AssignedNumbers, UUID

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        self.device = None

    def handleDiscovery(self, scanEntry, isNewDev, isNewData):
        print("Discovered device", scanEntry.addr)


class PeripheralDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        parsed = list(data)
        if len(parsed) > 1:
            print(f"{parsed[1]} bpm")

scanner = Scanner().withDelegate(ScanDelegate())
scanEntries = scanner.scan(10)

device = None
device2 = None

for entry in scanEntries:
    name = entry.getValueText(9) 
    if name == "poxi_0.9":
        print(f"Found proxy - address={entry.addr}")
        device = Peripheral(entry.addr, ADDR_TYPE_PUBLIC)
    if name == "P2PSRV1":
        print(f"Found stm dev board - address={entry.addr}")
        device2 = Peripheral(entry.addr, ADDR_TYPE_PUBLIC)

if device:
    device.setDelegate(PeripheralDelegate())
    hrService = device.getServiceByUUID(AssignedNumbers.heartRate)
    hrChar = hrService.getCharacteristics(AssignedNumbers.heart_rate_measurement)[0]
    desc = hrChar.getDescriptors(AssignedNumbers.client_characteristic_configuration);
    device.writeCharacteristic(desc[0].handle, b"\x01\x00")

    while True:
        if device.waitForNotifications(1.0):
            # handleNotification() was called
            continue

        print("Waiting for notification")


if device2:
    char = device2.getCharacteristics(uuid="0000fe41-8e22-4541-9d4c-21edae82ed19")[0]
    char.write(b"\x00\x01")