Erweiterungen
=============

Software
--------

**Android 15** (Standard)
	Als Standard-Betriebssystem wird Android 15 AOSP verwendet. AOSP basiert auf der freien Android Open Source Platform und nutzt die aktuellen Entwicklungen, die in Google Android verwendet werden. Android 15 AOSP enthält im Original keine Google-Services. Für das Plotter-Image wurden einige Google-Services eingefügt, wie PlayStore, Maps, GMail und Files. Zur Nutzung der Google Serices muss man sich mit einem Google-Account anmelden. Standardmäßig sind alle Sicherungsaktivitäten deaktiviert, die Daten zu Google auslagern.

**Android 14** (getestet)
	Android 14 AOSP kann als alternatives Betriebssystem genutzt werden. Es ist in gleicher Weise konfiguriert wie Android 15.

**Raspbian mit AVnav** (in Vorbereitung)
	Das AVnav Rasbian Image ist aktuell in Vorbereitung. Es stellt Raspian als Linux-Betriebssystem in der Version xxx bereit. AVnav und SignalK und einige andere wichtige Komponenten sind vorinstalliert. Das System ist headless und benutzt keine Tastatur oder Maus. Die Bedienung erfolgt ausschließlich über die Weboberfläche per Touch.

**Raspbian mit Open Plotter** (in Vorbereitung)
	Das Open Plotter Image ist aktuell in Vorbereitung. Open Plotter benutzt einen gewöhnlichen Linux-Desktop als Bedienoberfläche. Die Bedienung erfolgt haupsächlich über Tastatur und Maus. Einige Programme sind auch über ein Webinterface bedienbar wie z.B. SignalK. Open Plotter unterstützt AVnav und OpenCPN als Plugin.

**O-Charts Seekarten**
	O-Charts Seekarten sind kommerzielle Seekarten, die in AVnav oder OpenCPN verwendet werden können. Die oeSENC Vektorkarten sind recht preisgünstig und decken die wichtigsten Seegebiete für Wassersportler ab. Sie können online über den `Store von O-Charts`_ bezogen werden. Die Seekarten werden über einen Software-Token geschützt, der Ihnen nach dem Kauf per Mail übergeben wird. Die Karte kann auf einem Gerät benutzt werden. Nach Ablauf der Gültigkeit ist die Seekarte weiterhin nutzbar, jedoch nicht mehr aktualisierbar. Der Token kann auch auf einen USB-Dongle übertragen werden. So lassen sich die Seekarten auf mehreren Geräten nutzen, wenn der USB-Dongle im jeweiligen Gerät benutzt wird.
	
.. _Store von O-Charts: https://o-charts.org/shop/de/8-oesenc

Hardware
--------

**Gehäuseschalen**
	.. image:: /pics/OBP_Plotter_Case_t.png
             :scale: 10%
			 
	Die Gehäuseschalen sind bearbeitet und verfügen über die nötigen Ausbrüche im Gehäuse. Eine Gehäusedichtung und die notwendigen Schrauben gehören ebenfalls dazu.

**Mainboard**
	.. image:: /pics/OBP_Plotter_PCB_Side_View_t.png
             :scale: 10%
			 
	Auf dem Mainboard sind alle funktionswichtigen Hardwarekomponenten vereinigt. Mit nur wenigen Kabelverbindungen und einem zusätzlichen Raspberry Pi CM5 Modul kann ein lauffähiges System bereit gestellt werden. Das Mainboard ist an das Gehäuse angepasst und wird an vier Domen im Gehäuse mit Schrauben befestigt. Das Mainboard lässt sich auch in anderen Gehäusen verwenden. Das Raspberry Pi CM5 Modul ist nicht Bestandteil des Mainboards.
	
**HDMI-Controller**
	Der HDMI-Controller ist ein Zusatzbord, das verwendet wird, wenn keine Mainbord eingesetzt wird und das Plottergehäuse mit integriertem Display als Monitor verwendet werden soll. Der Controller verfügt über einen Anschluss für den Streifenleiter zum Display. Über einne Keyboard-Platine lassen sich die Grundeinstellungen, wie Auflösung, Helligkeit, Kontrast und Farbe des HDMI-Controllers vornehmen, wie man es von einem Monitor gewohnt ist. Der HDMI-Controller dient nur zur Bildübertragung. Die Touchfunktion des Displays und der IR-Fernbedinung werden nicht unterstützt.

	* HDMI-Controller-Platine für 10" TFT-Display
	* Auflösung: VGA, SVGA, HD, 2K, 4K
	* Funktionen: Upscaler, PIP
	* Eingang: HDMI, VGA
	* Stromversorgung: 12V 1.5A, Hohlklinkenstecker

**HDMI-Connector-Board**
	Das HDMI-Connector-Board wird anstelle des Compute Moduls im Mainboard eingesteckt. Dadurch kann die Plotter-Hardware wie in normaler Monitor benutzt werden. Zusätzlich können über USB unabhängig vom verwendeten Betriebssystem die Touchfunktion des 10" TFT-Displays und die Funktionen der IR-Fernbedienung genutzt werden. Der so entstandene Monitor lässt sich unter Linux, Mac OS und Windows nutzen.
	

**Compute Modul CM5** (Standard)
	.. image:: /pics/RPI-CM4_t.png
             :scale: 10%
			 
	Das Raspberry Pi Compute Modul CM5 ist die zentrale Recheneinheit des OBP-Plotters. Es ist das derzeit leistungsfähigste Modul der Raspberry Fondation. Als Standard-Modul wird eine Modul mit folgenden Komponeneten eingesetzt:
	
	* CPU: BCM2712, Quad Core, 64 Bit
	* CPU-Speed: 2.5 GHz, Auto-Speedstepping
	* RAM: 4 GB, fix
	* eMMC: 0 GB
	* WiFi, BT
	* Angepasster Bootloader für SSD NVMe
	
**Compute Modul CM5 Extended**
	.. image:: /pics/RPI-CM4_t.png
             :scale: 10%
			 
	Das Compute Modul CM5 Extended verfügt über mehr RAM und über einen eMMC Flash-Speicher. Alle weiteren Daten sind identisch zum Standard-Modul. Der Bootloader wurde an die Verwendung einer SSD NVMe angepasst. Die Bootreihenfolge wurde verändert, so dass automatisch zwischen dem Betriebssystem der SSD und des eMMC umgeschaltet wird. Beim Fehlen einer SSD wird das Betriebssystem des eMMC verwendet.
	
	* CPU: BCM2712, Quad Core, 64 Bit
	* CPU-Speed: 2.5 GHz, Auto-Speedstepping
	* RAM: 8 GB, fix
	* eMMC: 32 GB (Bootfähiges Backupmedium mit Android 15)
	* WiFi, BT
	* Angepasster Bootloader für SSD NVMe und Bootreihenfolge 

**Compute Modul CM4** (getestet)
	.. image:: /pics/RPI-CM4_t.png
             :scale: 10%
			 
	Das Raspberry Pi Compute Modul CM4 kann als alternative Recheneinheit des OBP-Plotters verwendet werden. Das Modul hat folgende Komponeneten:
	
	* CPU: BCM2711, Quad Core, 64 Bit
	* CPU-Speed: 1.5 GHz, Auto-Speedstepping
	* RAM: 4 GB, fix
	* eMMC: 0 GB
	* WiFi, BT
	* Angepasster Bootloader für SSD NVMe

**SSD NVMe 1 TB**
	.. image:: /pics/SSD_M.2_2242_t.png
             :scale: 10%
			 
	Die SSD NVMe 1 TB ist mit Android 15 vorinstalliert und verfügt über deutlich mehr Speicher als die Standard-SSD mit 512 GB.

**NMEA2000-Erweiterung**
	.. image:: /pics/Sensor_PCB_t.png
             :scale: 10%
	
	Die NMEA2000-Erweiterung dient zur Bereitstellung der NMEA2000-Funktionalität. Sie wird als kleine Zusatzplatine im Mainbord aufgesteckt. Der NMEA2000-Bus wird über Kabelverbindungen mit einer M12 Einbaubuchse verbunden. Zusätzlich gibt es Anschlüsse für I2C- und 1Wire-Sensorik. Das Erweiterungsmodul enthält folgende Komponenten:
	
	* ESP32-S3
	* NMEA2000-Gateway-Firmware
	* NMEA2000-Port
	* NMEA0183-Port
	* Unterstützung von I2C- und 1Wire-Sensorik
	* M12-Buche mit Verbindungskabel
	* 2 Befestigungsschrauben

**U-Mount**
	.. image:: /pics/U-Mount_t.png
             :scale: 10%
			 
	Der U-Mount ist ein Befestigungsbügel für den OBP-Plotter. Der Plotter lässt sich einhängen und mit zwei Knäufen arretieren. Der Betrachtungswinkel kann vertikal eingestellt werden. Der Befestigungsbügel ist aus mattem Edelstahl hergestellt. Der Befestigungsbügel kann an horizontalen oder vertikalen Flächen angebracht werden. Eine Deckenmontage ist ebenfalls möglich. Das Kit besteht aus:
	
	* 1x Befestigungsbügel
	* 2x Haltewinkel für Plotter
	* 2x Knäufe mit Unterlegscheiben und Federn
	* 4x Selbstsichernde Mutter mit Unterlkegscheibe und Dichtung
	* 3x Befestigungsschrauben für Bügel
	* 1x Bohrschablone

**RAM-Mount**
	.. image:: /pics/RAM-Mount_t.png
             :scale: 10%
			 
	Der RAM-Mount ist eine universelle Befestigungsmöglichkeit für den OBP-Plotter. DDer RAM-Mount besteht aus einem witterungsbeständigen Kunststoff und wird über die VESA-Halterung mit der Rückseite des OBP-Plotters verbunden. Über zwei Kugelgelenke lässt sich der Plotter beliebig im Hoch- oder Querformat in beliebigen Winkeln positionieren. Mit einer zentralen Klemmschraube lässt sioch die Position fixieren. Das Kit besteht aus:
	
	* RAM-Mount mit 2 Kugelplatten und 2 Verbindungsstegen
	* Fixierschraube
	* 4x Befestigungtsschrauben für VESA-Halterung
	* 4x Befestigungschrauben für Untergrund

**IR-Fernbedienung**
	.. image:: /pics/RAM-Mount_t.png
             :scale: 10%
			 
	Mit der leistungsstarken IR-Fernbedienung kann der OBP-Plotter auch unter Sonnenlicht über eine Entfernung mit bis zu 8 m bedient werden. Über 15 Tasten lassen sich die wichtigsten Funktionen des Plotters erreichen. Die Fernbedienung ist an AVnav angepasst und besteht aus einem spritzwassergeschützen Kunststoffgehäuse mit Folientastatur. Eine Kordel als universelle Befestigungsmöglichkeit gehört zum Lieferumfang. Mit einer CR2032 Batterie ist die Fernbedienung über mehrere Jahre einsatzbereit.
	
	* Gehäuse: ABS, spritzwassergeschützt
	* Tastenanzahl: 15, Folientastatur
	* Übertragungsart: IR
	* Reichweite: bis zu 8 man
	* Sonnentauglich
	* Stromversorgung: 1x CR2032, 3V
	* Einsatzdauer: mehr als 1 Jahr (nutzungsabhängig)
	