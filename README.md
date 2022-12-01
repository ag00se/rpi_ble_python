# BLE Setup:

Auf dem Raspberry per Remote VS-Code

```shell
sudo pip3 install bluepy
```

Damit der Zugriff auf die BLE Hardware möglich ist muss der Python-Code als superuser ausgeführt werden.
Dafür muss eine 'launch.json' Datei erstellt werden und in dieser Datei die Konfiguration "sudo" auf "true" stellen.
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