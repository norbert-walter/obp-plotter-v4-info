Technische Daten
================

.. image:: /pics/OBP_Plotter_Front_View_t.png
	:scale: 50%

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

.. image:: ../pics/OBP_Plotter_Exploded_t.png
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
| RAM                  | 4 GB, fix                   |
+----------------------+-----------------------------+
| Flash                | 512 GB, SSD NVMe, wechselbar|
+----------------------+-----------------------------+
| Freier User-Bereich  | 500 GB, erweiterbar bis 2 TB|
+----------------------+-----------------------------+
| Flash-Format         | m.2, 2230, 2242             |
+----------------------+-----------------------------+
| Displaygröße         | 1250 x 800 pix, 60 Hz       |
+----------------------+-----------------------------+
| Displayhelligkeit    | 1000 nits                   |
+----------------------+-----------------------------+
| Bedienung            | 5-Finger-Touch, regensicher |
+----------------------+-----------------------------+
| Sensortasten         | 3x kapazitiv                |
+----------------------+-----------------------------+
| Fernbedienung        | IR, 8 m                     |
+----------------------+-----------------------------+
| Kommunikation        | WiFi, 802.11 bgnac, 50 m    |
+----------------------+-----------------------------+
| WiFi Frequenzen      | 2.4 GHz, 5.0 GHz            |
+----------------------+-----------------------------+
| Ethernet-Protokolle  | HTTP, SSH, VNC, SMB, UDP    |
+----------------------+-----------------------------+
| Bluetooth            | BT 5.0, BLE                 |
+----------------------+-----------------------------+
| Bluetooth-Profile    | Heatset, A2DP, Fitness      |
+----------------------+-----------------------------+
| Erweiterungsport     | USB 3.0, I2C, SPI           |
+----------------------+-----------------------------+
| Schnittstellen       | 1x USB 3.0, 2x USB 2.0, Pwr |
+----------------------+-----------------------------+
| Signaleinrichtungen  | 2x LED, frontseitig         |
+----------------------+-----------------------------+
| Lautsprecher         | Mono, 10 W                  |
+----------------------+-----------------------------+
| Betriebssystem       | Android 15, AOSP            |
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
.. image:: ../pics/OBP_Plotter_Back_View_t.png
   :scale: 50%
   
Schaltplan
----------

* `Schaltplan V2.1 [PDF] <../_static/files/OBP_Plotter_Dimensions.pdf>`_


Maßbilder
---------

* `Maßbild [PDF] <../_static/files/OBP_Plotter_Dimensions.pdf>`_

   
Nutzbare Telegramme
-------------------

**NMEA0183 via WiFi**
    * AIVDM, AIVDO, DBK, DBS, DBT, DPT, GGA, GLL, GSA, GSV, HDG, HDM, HDT, MTW, MWD, MWV, RMB, RMC, ROT, RSA, VHW, VTG, VWR, XDR, XTE, ZDA
	
Nutzbare I2C-Sensorik
---------------------

**Umgebungssensoren**
	* Bewegung
	* Helligkeit
	* IR-Remote
	
**Echtzeit-Uhren**
	* Integriert in CM5