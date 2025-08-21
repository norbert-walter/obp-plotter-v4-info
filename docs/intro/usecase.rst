Einsatzmöglichkeiten
====================

Basisgerät
----------

Der OBP-Plotter als Basisgerät ist ein einatztaugliches Gerät für den Außeneinsatz. Das Gerät verfügt über keine eigene Sensorik. Sensorsignale können über das WiFi-Nertzwerk als NMEA0183 Datenstrom empfangen und gesendet werden. Als Sensor-Datenquellen können folgende Geräte verwendet werden:

    * Android Handy mit NetGPS-App (Position, Fahrtrichtung, Geschwindigkeit, Kompass)
    * M5Stack mit NMEA2000-Gateway
    * Marine Control Server mit Open Plotter (kompelette Sensorid, die mit einem MCS verwendet werden kann)
    
Das Basisgerät richtet sich an Leute, die schon über Sensorsysteme erfügen und diese über WiFi übertragen können.

Android Handy mit NetGPS-App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Im einfachsten Fall kann dafür ein gewöhnliches Handy benutzt werden, das über einen GPS-Empfänger verfügt. Mit der NetGPS-App lassen sich folgende Daten des GPS-Empfängers über Wifi an den OBP-Plotter übertragen:

    * Latutude
    * Longitude
    * Wahrer Kurs
    * Geschwindigkeit über Grund
    * Höhe über NN
    * Positionsgenauigkeit
    
Die Positionsdaten, die Geschwindigkeit und der Kurs werden in AVnav in die Seekarte übernommen und angezeigt. AIS-Daten können aus dem Internet vom AIS Catcher Server bezogen und in der Seekarte angeziegt werden, wenn die eigene Position zum Server übertragen wird.

M5Stack mit NMEA2000-Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wer bereits Bordsnetze im eigenen Boot zur Verfügung hat, kann die Sensordaten mit dem NMEA2000-Gateway auf Basis eines M5Stack über Wifi in den OBP-Plotter einlesen. Das NMEA2000-Gateway ist ein Open Source Projekt, das einen einfachen M5Stack als Hardwarebasis nutzt und mit einer speziellen Firmware versehen wird. Über Zusatzmodule lassen sich folgende Bussysteme einbinden:

    * NMEA2000
    * NMEA0183
    * I2C
    * 1Wire
    
Nähere Informationen zum Open Source Projekt finden Sie hier:

Das Gateway ermöglicht es, auch Daten zwischen dem NMEA2000-Bus und dem NMEA0183-Bus bidirektional auszutauschen. Mit dem Gateway können alle Daten aus dem Bussystem an AVnav übertragen und angezeigt werden:

    * Latutude
    * Longitude
    * Wahrer Kurs
    * Magnetkurs
    * Geschwindigkeit über Grund
    * Geschwindigkeit durchs Wasser
    * Wassertiefe
    * Roll und Pitch
    * Windrichtung
    * Windgescwindigkeit
    * Positionsgenauigkeit
    * Tankinhalte
    * Motordrehzahl
    * Batteriespannung
    * Temperaturwerte

**O-Charts Seekarten**
	.. image:: /pics/AVnav_Chart.webp
             :scale: 10%
             

			 
	O-Charts Seekarten sind kommerzielle Seekarten, die in AVnav oder OpenCPN verwendet werden können. Die oeSENC Vektorkarten sind recht preisgünstig und decken die wichtigsten Seegebiete für Wassersportler ab. Sie können online über den `Store von O-Charts`_ bezogen werden. Die Seekarten werden über einen Software-Token geschützt, der Ihnen nach dem Kauf per Mail übergeben wird. Die Karte kann auf einem Gerät benutzt werden. Nach Ablauf der Gültigkeit ist die Seekarte weiterhin nutzbar, jedoch nicht mehr aktualisierbar. Der Token kann nicht auf einen USB-Dongle übertragen werden. Bereits gekaufte Seekarten, die einem USB-Dongle sind können nicht unter Android genutzt werden.
	
.. _Store von O-Charts: https://o-charts.org/shop/de/8-oesenc

Basisgerät mit GPS und AIS
--------------------------

**Gehäuseschalen**
	.. image:: /pics/OBP_Plotter_Case_t.png
             :scale: 10%
			 
	Die Gehäuseschalen sind bearbeitet und verfügen über die nötigen Ausbrüche im Gehäuse. Eine Gehäusedichtung und die notwendigen Schrauben gehören ebenfalls dazu.

Nachfolgend werden einige Einsatzmöglichkeiten für den OBP-Plotter gezeigt. 

Variante WiFi
-------------

Bei der WiFi-Variante werden alle externen Informationen über WiFi dem OBP-Plotter zugeführt. Die unterschiedlichen Geräte wie Windsensor, Kamera oder Busdaten werden dabei über WiFi-Verbindungen hergestellt. Der OBP-Plotter ist dabei der WiFi-Hotspot und das Bedien- und Anzeigegerät so ähnlich wie man das vom Handy her gewohnt ist. Ein Handy kann z.B. als GPS-Datenquelle dienen und dem Plotter die GPS-Daten zur Verfügung stellen..

.. hint::
	Für die Bereitstellung eines WiFi-Hotspots ist es praktischer, wenn man im Boot einen dedizierten internetfähigen 4G/5G-WiFi-Router benutzt. So können sich alle Geräte und Besatzungsmitglieder mit dem Internet verbinden.

.. image:: /pics/Use_Case_3.png
		 :scale: 50%

Variante Bussystem
------------------

Als weitere Variante besteht die Möglichkeit, den OBP-Plotter auch direkt mit den Bussystemen an Bord zu verbinden. Dazu benötigt man eine Zusatzplatine die in den Erweiterungsport im Plotter installiert wird. Die Zusatzplatine enthällt einen ESP32-S3 mit ähnlicher Funktionalität wie ein M5Stack ATOM. Folgende Funktionen lassen sich über die Zusatzplatine nutzen:

	* GPS-Empfänger (GPS, Glonas, Beidu, Galileo)
	* 1x NMEA200-Port (isoliert)
	* 1x NMEA0183-Port (isoliert, unidirektional)
	* 1x I2C-Port (isoliert)
	* 11x Wire-Port
	* NMEA2000-Gateway
	* Firmware-Update des Gateways über USB
	* Parametrierung des Gateways webbasiert

Neben den Daten aus den Bussystemen lassen sich auch Daten über WiFi in den Plotter einbinden, wie z.B. von einem Windsensor Yachta.

.. note::
	Die Zusatzplatine bedindet sich aktuell noch in Entwicklung und wird demnächst verfügbar sein.


.. image:: /pics/Use_Case_2.png
		 :scale: 50%
