Übersicht
=========

Den OBP-Plotter V4 besteht aus verschiedenen Komponenten die auf einer gemeinsamen Hauptplatine untergebracht sind.

.. image:: /pics/Plotter_Block_Schematic.png
             :scale: 60%

Abb.: Blockschaltbild Hauptplatine

**10" TFT-Display**
	* Auflösung 1280 x 800 pix
	* Helligkeit 1000 nits
	* Helligkeit automatisch über Umgebungslichtsensor anpassbar
	* Kapazitives Multi-Touch mit 5 Fingern
	* Touch ist regensicher und mit Handschuhen bedienbar
	* Kratzfestes, entspiegeltes, sonnenlichtfestes Deckglas 3 mm

.. image:: /pics/OBP_Plotter_PCB_Side_View_t.png
             :scale: 10%

**Hauptplatine**
	* Enthält alle wesentlichen Komponenten
	* 2x USB 2.0 für Useranwendungen
	* 1x Erweiterungsport mit: USB 3.0, I2C, ISP, RS232, Power
	* 1x PCI M.2 SATA für NVMe SSD, 2230, 2242, bis 2 TB bestückbar
	* 1x HDMI (Second Port)
	
**Stromversorgung**
	* Für Comute Modul und Peripherie
	* Eingangsspannung 10...30V DC, 5A
	* Eingangssicherung 5A
	* Kurzschlusssicher
	* Verpolungssicher
	* Eingangsfilter und Überspannungsschutz

**Comput Modul Steckplatz**
	* Geeignet für CM4, CM5 von Raspberry Pi (getestet)
	* Geeignet für CM4, CM5 von Banana Pi (ungetestet)
	
.. image:: /pics/RPI-CM4_t.png
             :scale: 10%

**Compute Modul CM5**
	* Quade-Core CPU Broadcom BCM2712
	* 4x 64bit Arm Cortex-A76, 2.4 GHz
	* 32 GB eMMC Flash-Speicher (Backup Betriebssystem)
	* WiFi 2.4 GHz, 5 GHz, 802.11 b/g/n/ac
	* Bluetooth 5.0, BLE
	* Gigabit Ethernet
	* 1x USB 2.0 (High Speed)
	* 2x USB 3.0 (5 Gbps)
	* 1 x PCIe x1 root complex, Gen 2 (5Gbps)
	* 2x HDMI 4K, 60 Hz
	* OpenGL ES 3.1
	* Vulcan 1.2
	* Betriebstemperaturbereich: -20°C bis +85°C

**USB-C OTG**
	* Dient zum Flashen des Betriebssystems und des Bootloaders für das Compute Modul
	* Umschaltbar über S2
	
**USB 2.0-Hub**
	* 2x USB 2.0 für Usererweiterungen
	* 5V, 1A
	* Kurzschlusssicher
	
.. image:: /pics/Sensor_PCB_t.png
             :scale: 10%

**Touch-Sensorplatine**
	* 3x Touch-Tasten
	* 2x LED-Signalisierung
	* 1x Umgebungslichtsensor
	* 1x IR-Sensor für Fernbedienungen
	
**HDMI-Controller**
	* Ansteuerung für TFT-Display
	* Enthält einen Upscaler für 1920 x 1080 pix
	* Auflösung Umschaltbar über Compute Modul
	
**PIC 1**
	* Enthält Funktionslogik für Touch-Sensorplatine und das Power Management
	* Flashbar und Updatebar über Dateisystem
	
**PIC 2**
	* Enthält Funktionslogik für HDMI-Chip
