Erweiterungen
=============

Software
--------

**Android 15** (Standard)
	Als Standard-Betriebssystem wird Android 15 AOSP verwendet. AOSP basiert auf der freien Android Open Source Platform und nutzt die aktuellen Entwicklungen, die in Google Android verwendet werden. Android 15 AOSP enthält im Original keine Google-Services. Für das Plotter-Image wurden einige Google-Services eingefügt, wie PlayStore, Maps, GMail und Files. Zur Nutzung der Google Serices muss man sich mit einem Google-Account anmelden. Standardmäßig sind alle Sicherungsaktivitäten deaktiviert, die Daten zu Google auslagern.

**Android 14** (getestet)
	Android 14 AOSP kann als alternatives Betriebssystem genutzt werden. Es iost in gleicher Weise konfiguriert wie Android 15.

**Raspbian mit AVnav** (in Vorbereitung)
	Das AVnav Rasbian Image ist aktuell in Vorbereitung. Es stellt Raspian als Linux-Betriebssystem in der Version xxx bereit. AVnav und SignalK und einige andere wichtige Komponenten sind vorinstalliert. Das System ist headless und benutzt keine Tastatur oder Maus. Die Bedienung erfolgt ausschlißlich über die Weboberfläche per Touch.

**Raspbian mit Open Plotter** (in Vorbereitung)
	Das Open Plotter Image ist aktuell in Vorbereitung. Open Plotter benutzt einen gewöhnlichen Linux-Desktop als Bedienoberfläche. Die Bedienung erfolgt haupsächlich über Tastatur und Maus. Einige Programme sind auch über ein Webinterface bedienbar wie z.B. SignalK. Open Plotter unterstützt AVnav und OpenCPN als Plugin.

**O-Charts Seekarten**
	O-Charts Seekarten sind kommerzielle Seekarten, die in AVnav oder OpenCPN verwendet werden können. Die recht preisgünstigen Seekarten decken die wichtigsten Seegebiete für Wassersportler ab. Sie können online über den Store von O-Charts bezogen werden. Die Seekarten werden über einen Software-Token geschützt, der Ihnen nach dem Kauf per Mail übergeben wird. Die Karte kann auf einem Gerät benutzt werden. Nach Ablauf der Gültigkeit ist die Seekarte weiterhin nutzbar, jedoch nicht mehr aktualisierbar. Der Token kann auch auf einen USB-Dongle übertragen werden. So lassen sich die Seekarten auf mehreren Geräten nutzen, wenn der USB-Dongle im jeweiligen Gerät benutzt wird. 

Hardware
--------

**Gehäuseschalen**
	Die Gehäuseschalen sind bearbeitet und verfügen über die nötigen Ausbrüche im Gehäuse. Eine Gehäusedichtung und die notwendigen Schrauben gehören ebenfalls dazu.

**Mainboard**
	Auf dem Mainboard sind alle funktionswichtigen Hardwarekomponenten vereinigt. Mit nur wenigen Kabelverbindungen und einem zusätzlichen Raspberry Pi CM5 Modul kann ein lauffähiges System bereit gestellt werden. Das Mainboard ist an das Gehäuse angepasst und wird an vier Domen im Gehäuse mit Schrauben befestigt. Das Mainboard lässt sich auch in anderen Gehäusen verwenden. Das Raspberry Pi CM5 Modul ist nicht Bestandteil des Mainboards und muss separat besorgt werden.

**Compute Modul CM5** (Standard)
	Das Raspberry Pi Compute Modul CM5 ist die zentrale Recheneinheit des OBP-Plotters. Es ist das derzeit leistungsfähigste Modul der Raspberry Fondation. Als Standard-Modul wird eine Modul mit folgenden Komponeneten eingesetzt:
	* CPU: BCM2712, Quad Core, 64 Bit
	* CPU-Speed: 2.5 GHz, Auto-Speedstepping
	* RAM: 4 GB, fix
	* eMMC: 0 GB
	* Format: m.2, 2230, 2242
	* WiFi, BT
	* Angepasster Bootloader für SSD NVMe
	
**Compute Modul CM5 Extended**
	Das Compute Modul CM5 Extended verfügt über mehr RAM und über einen eMMC Flash-Speicher. Alle weiteren Daten sind identisch zum Standard-Modul. Der Bootloader wurde an die Verwendung einer SSD NVMe angepasst. Die Bootreihenfolge wurde verändert, so dass automatisch zwischen dem Betriebssystem der SSD und des eMMC umgeschaltet wird. Beim Feheln einer SSD wird das Betriebssystem des eMMC verwendet.
	* CPU: BCM2712, Quad Core, 64 Bit
	* CPU-Speed: 2.5 GHz, Auto-Speedstepping
	* RAM: 8 GB, fix
	* eMMC: 32 GB (Bootfähiges Backupmedium mit Android 15)
	* Format: m.2, 2230, 2242
	* WiFi, BT
	* Angepasster Bootloader für SSD NVMe und Bootreihenfolge 

**Compute Modul CM4** (getestet)

**SSD NVMe 1 TB**
	Die SSD NVMe 1 TB ist mit Android 15 vorinstalliert und verfügt über deutlich mehr Speicher als die Standard-SSD mit 512 GB.

**NMEA2000-Erweiterung**

**U-Mount**

**RAM-Mount**

**IR-Fernbedienung**
