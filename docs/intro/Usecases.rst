Einsatzmöglichkeiten
====================

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

Als weitere Variante besteht die Möglichkeit, den OBP-Plotter auch direkt mit den Bussystemen an Bord zu verbinden. Dazu benötigt man eine Zusatzplatine die in den Erweiterungsport im Plotter installiert wird. Folgende Funktionen lassen sich über die Zusatzplatine nutzen:

	* GPS-Empfänger (GPS, Glonas, Beidu, Galileo)
	* 1x NMEA200-Port (isoliert)
	* 1x NMEA0183-Port (isoliert, unidirektional)
	* 1x I2C-Port (isoliert)
	* 11x Wire-Port
	* NMEA2000-Gateway

Neben den Daten aus den Bussystemen lassen sich auch Daten über WiFi in den Plotter einbinden, wie z.B. von einem Windsensor Yachta.

.. note::
	Die Zusatzplatine bedindet sich aktuell noch in Entwicklung und wird demnächst verfügbar sein.


.. image:: /pics/Use_Case_2.png
		 :scale: 50%