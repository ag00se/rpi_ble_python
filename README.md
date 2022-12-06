# BLE Setup:

Auf dem Raspberry per Remote VS-Code

```shell
sudo pip3 install bluepy
```
[Bluepy Dokumentation](https://ianharvey.github.io/bluepy-doc/)

Damit der Zugriff auf die BLE Hardware möglich ist muss der Python-Code als superuser ausgeführt werden.
Dafür muss eine 'launch.json' Datei erstellt werden und in dieser Datei die Konfiguration "sudo" auf "true" gestellt werden.
```json
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "sudo": true
        }
    ]
```


## BLE Debugging bei Problemen

Wenn die BLE-Kommunikation nicht korrekt funktioniert, kann die Kommunikation mitgeschnitten werden. Dafür kann das Tool "hcidump" verwendet werden.
```console
sudo hcidump -t
```

Sollte der Befehl nicht gefunden werde, kann das Tool mit folgendem Befehl installiert werden:

```console
sudo apt-get install bluez-hcidump
```
## Beispiel

Die grundlegende Verwendung des ```bluepy``` Modules wird in der Datei [startup.py]((https://github.com/ag00se/rpi_ble_python/blob/master/startup.py)) veranschaulicht. Die oben verlinkte [Dokumentation](https://ianharvey.github.io/bluepy-doc/) beschreibt die weitere Verwendung des Moduls.

Im Allgemeinen kann mit einem ```Scanner```-Objekt die Suche nach BLE-Geräten gestartet werden. (Zeile 21) Über eine eigene Klasse, welche von der Klasse ```DefaultDelegate``` erbt, kann durch Überschreiben der Methode ```def handleDiscovery(self, scanEntry, isNewDev, isNewData):``` benutzerdefiniertes Verhalten beim Auffinden eines neuen Geräts ausgeführt werden. (Zeilen 3-9) Ebenso werden die gefundenen Geräte direkt beim Aufruf der ```scan``` Methode des Scanners zurückgegeben. (Zeile 22)

Die Code-Zeilen 37-48 zeigen wie auf einen HeartRate-Service zugegriffen werden kann und wie die Notifications für die HeartRateMeasurements aktiviert werden. Für die Verarbeitung der Notification wird dem Device ein Objekt einer benutzerdefinierte Klasse, welche von der Klasse ```DefaultDelegate``` erbt, übergeben. (Zeile 37) In dieser benutzerdefinierte Klasse kann durch Überschreiben der Methode ```def handleNotification(self, cHandle, data):``` benutzerdefiniertes Verhalten beim Empfang einer Notification ausgeführt werden. (Zeilen 16-19)

