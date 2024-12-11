Technische Daten
================

.. image:: /pics/Display.jpg
	:scale: 20%

Funktionen
----------

* 10-Zoll Touch-Display (tageslichttauglich)
* 3 Sensor-Tasten (u.a. geeignet für Android Buttons)
* Akustischer Signalgeber (Lautsprecher)
* NMEA2000 (vollduplex, isoliert)
* NMEA0183 (RX oder TX, konfigurierbar, isoliert)
* NMEA2000/NMEA0183 Gateway (bidirektional)
* I2C (isoliert)
* USB-C (OTG, Debug, NMEA0183)
* GPS-Empfäger (GPS, Glonas, Baidu, interne oder externe GPS-Antenne)
* WiFi 2.4GHz (HTTP, TCP, UDP)
* Bluetooth (aktuell ungenutzt)
* Low Power Modus


Aufbau
------

.. image:: ../pics/OBP60_Explode_View.png
   :scale: 45%


Spezifikation
-------------

+----------------------+-----------------------------+
| Versorgungsspannung  | 10...28 V, verpolungssicher |
+----------------------+-----------------------------+
| Stromverbrauch       | 7...18 W, typisch 12 W      |
+----------------------+-----------------------------+
| Prozessor            | BCM2712, Quad Core          |
+----------------------+-----------------------------+
| Clock Speed          | 2.5 GHz, Auto-Speedstepping |
+----------------------+-----------------------------+
| RAM                  | 4 GB                        |
+----------------------+-----------------------------+
| Flash                | 512 GB, SSD NVMe            |
+----------------------+-----------------------------+
| Flash-Format         | m.2, 2230, 2242             |
+----------------------+-----------------------------+
| Displaygröße         | 1250 x 800 pix, 60 Hz       |
+----------------------+-----------------------------+
| Bedienung            | 5-Finger-Touch, regensicher |
+----------------------+-----------------------------+
| Sensortasten         | 3x kapazitiv                |
+----------------------+-----------------------------+
| Fernbedinung         | IR, 8 m                     |
+----------------------+-----------------------------+
| Kommunikation        | WiFi, 802.11 bgnac, 50 m    |
+----------------------+-----------------------------+
| WiFi Frequenzen      | 2.4 GHz, 5.0 GHz            |
+----------------------+-----------------------------+
| Erweiterungsport     | USB 3.0, I2C, SPI           |
+----------------------+-----------------------------+
| Schnittstellen       | 1x USB 3.0, 2x USB 2.0, Pwr |
+----------------------+-----------------------------+
| ESD-Schutz           | 8 kV                        |
+----------------------+-----------------------------+
| Schutzgrad           | IP65                        |
+----------------------+-----------------------------+
| Abmessungen          | 285 x 198 x 46 mm           |
+----------------------+-----------------------------+
| Gewicht              | 1280 g                      |
+----------------------+-----------------------------+

Anschlussbelegung
-----------------
.. image:: ../pics/Bus_Systems.png
   :scale: 50%
   
Schaltplan
----------

* `Schaltplan V2.1 [PDF] <../_static/files/Schematic_OBP60_V2.1.pdf>`_


Maßbilder
---------

* `Maßbild [PDF] <../_static/files/Drawing_OBP60_V2.pdf>`_

   
Nutzbare und konvertierbare Telegramme
--------------------------------------

**NMEA0183**
    * AIVDM, AIVDO, DBK, DBS, DBT, DPT, GGA, GLL, GSA, GSV, HDG, HDM, HDT, MTW, MWD, MWV, RMB, RMC, ROT, RSA, VHW, VTG, VWR, XDR, XTE, ZDA
    
**NMEA2000**
    * 126992, 127245, 127250, 127251, 127257, 127258, 127488, 127489, 127505, 127508, 128259, 128267, 128275, 129025, 129026, 129029, 129033, 129038, 129039, 129283, 129284, 129539, 129540, 129794, 129809, 129810, 130306, 130310, 130311, 130312, 130313, 130314, 130316
	
Nutzbare I2C-Sensorik
---------------------

**Umgebungssensoren**
	* BMP085, BMP180, BMP280, BME280, SHT20, HTU21
	
**Spannungs- und Stromsensoren**
	* INA226, INA219 (in Vorbereitung)
	
**Winkelsensoren**
	* AS5600, MT6701 (in Vorbereitung)
	
**Port-Erweiterungen**
	* PCF8574 (in Vorbereitung)
	
**Echtzeit-Uhren**
	* DS1388
	
Nutzbare 1Wire-Sensorik
-----------------------

**Temperatursensoren**
	* DS18B20
