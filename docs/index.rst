##########################
OBP-Plotter V4 Information
##########################
Letzte Aktualisierung |today|

.. image:: https://readthedocs.org/projects/obp-plotter-v4-info/badge/?version=latest
    :target: https://obp-plotter-v4-info.readthedocs.io/de/latest/?badge=latest
    :alt: Documentation Status

.. note::   Diese Seiten sind noch in Bearbeitung.

.. image:: /pics/Display.jpg
             :scale: 20%

Der OBP-Plotter V4 wurde von Open Boat Projects entwickelt, um eine offene Navigationsplattform zur Verfügung zu stellen. Im Gegensatz ist bei kommerziellen Navigationssystemen die Funktionalität fest vom Hersteller vorgegeben und kann nachträglich vom Endanwender nicht verändert werden. Die Lebenszykluszeit solcher Geräte ist auf wenige Jahre beschränkt. Nach dem Verkaufsende werden alte Navigationssysteme meistens nicht mehr unterstützt und eine Weiterverwendung ist nicht mehr sinnvoll möglich, sofern Kartenbestände nicht mehr aktualisiert werden können. Das zwingt viele Anwender dazu neue Systeme zu kaufen, obwohl das alte System physisch noch funktionsfähig ist.

Oft ist es so, dass im DIY-Bereich individuelle eigene Lösungen existieren, die aber in vielen Dingen nicht perfekt an die Umgebungsbedingungen im Segelalltag angepasst sind. Das liegt teilweise an den begrenzten technischen Möglichkeiten und dem Erfahrungswissen bei der Umsetzung solcher Projekte. Open Boat Project hat sich zum Ziel gesetzt, eine stabile Navigations-Hardware zur Verfügung zu stellen, die an marine Umgebungsbedingungen angepasst ist und als Basis für eigene Projekte verwendet werden kann.

Die Hardwarefunktionalität orientiert sich an den Erfordernissen im rauen Alltagseinsatz.

	* Wetterfestes und wasserdichtes Gehäuse
	* Touch ist regenfest und handschuhtauglich
	* 10" TFT Touch-Display mit 1000 nits
	* Sensortasten
	* Leistungsstarke Hardware auf Basis eines Raspi CM5 Moduls
	* 4 GB RAM Arbeitsspeicher
	* 512 GB SSD Programmspeicher
	* WiFi 2.5 GHz und 5 GHz
	* Bluetooth 5.0
	* GPS-Empfänger
	* AIS-Empfänger
	* NMEA2000-Gateway
	* Unterstützt Linux, Android und Windows als Betriebssystem
	* Offene Schnittstelle für Erweiterungen

Der Grundgedanke beim OBP-Plotter V4 liegt in der Offenheit des gesamten Projektes. Wir nutzen die Community des Segeln-Forums und haben uns von den Iden inspirieren lassen wie eine ideale offene Hardware aussieht und tauschen uns mit Interessierten im Entwicklungsprozess darüber aus. Wir unterstützen die Idee hinter **Open Hardware, Open Source und Open Data**. Jeder Interessierte soll nachvollziehen und verstehen können, wie das Navigationssystem funktioniert. Es soll sich individuell durch die Offenheit an eigene Bedürfnisse anpassen lassen und eignet sich hervorragend bestehende ältere Systeme mit einzubeziehen, die bereits an Bord verfügbar sind. Wir veröffentlichen folgende Daten, die jeder einsehen und nutzen kann:

	* CAD-Unterlagen
	* Quell-Codes
	* Schaltpläne
	* Komponentenunterlagen
	* Vorbereitete Betriebssystem-Images
	
Die Hardware wurde von uns so konstruiert, dass sie wirtschaftlich und kosteneffizient von Zulieferern gefertigt werden kann. Die Entwicklung wird hauptsächlich durch Open Boat Projects verantwortet. Wir kümmern uns um Konzepterstellung, Entwicklung, Komponentenbeschaffung- und Validierung, Prototypenbau und eine erste Nullserie. Darüber hinaus suchen wir nach Fertigungspartnern, die das Gerät später fertigen werden. Wir werden auch nötige Zulassungen und Tests wie z.B. eine CE-Zertifizierung veranlassen, so dass die Navigationssysteme im öffentlichen Handel verkauft werden können. Die Themen Fertigung, Test, Qualitätskontrolle, Verpackung, Lagerung, Logistik, Marketing und Vertrieb werden wir an Dienstleiter übergeben. So können wir uns auf die Kernkompetenzen konzentrieren und die Produktausrichtung nach unseren Wünschen und Erfordernissen gestalten und kontrollieren.

Der OBP-Plotter V4 ist das bisher beste Hardwarekonzept, das wir bis jetzt erstellt haben. Es basiert auf einer Reihe von Erkenntnissen, die wir aus vorhergehenden Projekten gewonnen haben. So basiert das Hardwarekonzept auf einem Rasverry Pi Compute Modul CM5, bei dem alle Hardwareabhängigkeiten zu Betriebssystemen aufgehoben sind. Es werden keine speziellen GPIO-Pins für Hardwarekomponenten benutzt. Alle Komponenten werden über standardisierte Schnittstellen wie USB, I2C angebunden. So kann die Basisplatine mit verschiedenen Compute Modulen verschiedener Hersteller unter verschiedenen Betriebssystemen verwendet werden. So wären z.B. neben dem Compute Modul CM4, CM5 der Raspberry Pi Fondation auch der Einsatz der Compute Module  CM4, CM5 von Banana Pi oder von Radxa möglich. Alle genannten Module verfügen über die gleichen standardisierten Schnittstellen und sind gegenseitig austauschbar. Bei den verwendeten Betriebssystemen ist es ähnlich. Alle Modulhersteller bieten entsprechende Betriebssystem-Images für verschiedene Anwendungen an.

Ziel der ganzen Entwicklung ist es, dem Maker eine verlässliche, geprüfte und einsatztaugliche offene Hardwareplattform zu bieten, so dass das DIY-Betätigungsfeld überwiegend im Softwarebereich liegt oder bei der Erstellung von Erweiterungsmodulen.  

Im ersten Schritt werden wir neben der Hardware auch ein Betriebssystem auf Android 15 anbieten, so dass auch Maker ohne Erfahrungen die Hardware sinnvoll im Marinebereich nutzen können. Es werden eine Reihe von nützlichen Anwendungen vorinstalliert und einsatzfertig konfiguriert sein. Mit Android 15 werden die meisten Anwender sich schnell zu Recht finden. Durch die universelle Erweiterbarkeit über Apps aus dem Google PlayStore können auch etablierte kommerzielle Navigationsanwendungen wie Navionics und andere genutzt werden.

Der große Vorteil der offenen Plattform liegt in der Wandelbarkeit und Erweiterbarkeit. So lassen sich auch Anwendungen außerhalb des Marineumfeldes wie z.B. der Homeautomation erschließen. Durch die Offenheit besteht kein Zwang ein bestimmtes Betriebssystem zu nutzen. Die Updatefähigkeit ist immer gegeben, soweit die Hardware den Anforderungen genügt. Im Fehlerfall steht eine umfassende Dokumentation zur Verfügung, so dass man Probleme lokalisieren und selbst lösen kann. Durch die Offenheit wird die Community angeregt weitere Ideen beizusteuern, die von Makern umgesetzt werden können oder in spätere Versionen mit einfließen können. Open Boat Project bietet einen Plotter an, der von Wassersportlern für Wassersportler erstellt worden ist. Die Community und wir wissen sehr genau was nützlich und sinnvoll ist.


.. toctree::
   :maxdepth: 3
   :caption: Eigenschaften
   :name: sec-intro

   Übersicht <intro/historie>
   Technische Daten <intro/specification>
   Erweiterungen <intro/variants>
    
.. toctree::
   :maxdepth: 3
   :caption: Hilfe
   :name: sec-help   

   Fragen und Antworten <help/faq>
   Meinungen und Tipps <help/opinions>
   Bekannte Fehler <help/errors>
   Technische Unterstützung <help/support>
   Service <help/service>
   Mitarbeit <help/cooperation>
   Spenden <help/donation>
   Glossar <help/glossar>
