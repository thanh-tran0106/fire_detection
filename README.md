# fire_detection

Before running install_packages.sh,
```
chmod +x install_packages.sh
sh install_packages.sh
```
Then to run the run.py
```
python3 run.py
```
In the run.py you can change the number of ledred, ledbl base on the sensors you use.<br>



In the index.html, it will read the temp and humidity value from the sensor. Then it will check the the led status, if the led is currently on, it will display the TURN OFF button to turn it off. If the led is currently off, it will display the TURN ON button.
