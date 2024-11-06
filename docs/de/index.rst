######################
OBP-Plotter V4 Dokumentation
######################
Letzte Aktualisierung |today|

.. note::   Diese Seiten sind noch in Bearbeitung.

.. image:: /pics/Display.jpg
             :scale: 20%

Der OBP-Plotter V4, entwickelt von Christian Hartz,  wird für die Darstellung von marinen Karten und Daten auf Freizeit-Booten verwendet. Zielgruppe sind Sportbootfahrende in aller Welt. 

Der OBP-Plotter ist ausgestattet mit einem tageslichttauglichen 10-Zoll-Touch-Display. Als Hardwarebasis dienen Compute Module der Versionen 4 und 5 der Raspberry Foundation. Mit der Außenwelt kommuniziert der Plotter vor allem per USB oder WLAN. Das macht ihn maximal flexibel im Einsatz unterschiedlichster Navigationssysteme an Bord. 

Eine Einbindung in bestehende NMEA-Netzwerke ist selbstverständlich ebenso möglich, egal ob NMEA-0183 oder NMEA2k. Die Betriebssystembasis bildet ein aktuelles Android (14 oder 15), auf dem die Navigations-App "AvNav" vorinstalliert ist. Alternativ lässt sich von Anwendern auch ein Raspbian einsetzen, um dort zum Beispiel OpenCPN zu installieren.

.. toctree::
   :maxdepth: 3
   :caption: Einführung
   :name: sec-intro

   Übersicht <de/intro/historie>
   Technische Daten <de/intro/specification>
   Varianten <de/intro/variants>
   
.. toctree::
   :maxdepth: 3
   :caption: Installation
   :name: sec-usermanual

   Inbetriebnahme <de/usermanual/start>
   Installation Android <de/usermanual/android_install>
   Konfiguration Android <de/usermanual/android_configuration>
   Installation Raspbian <de/usermanual/raspbian_install>
   Konfiguration Raspbian <de/usermanual/raspbian_configuration>
   Schnittstellen <de/usermanual/dataexchange>
   Sensorik <de/usermanual/sensors>
   Beispielkonfiguration <de/usermanual/samples>
   Sicherheitshinweise <de/usermanual/safety>

.. toctree::
   :maxdepth: 3
   :caption: Zusammenbau
   :name: sec-assembling
   
   Geräteaufbau <de/assembling/device>
   Vorbereitung <de/assembling/preparation>
   Bauteilliste <de/assembling/partlist>
   Durchführung <de/assembling/actionsteps>
   Funktionstest <de/assembling/tests>
   
    
.. toctree::
   :maxdepth: 3
   :caption: Hilfe
   :name: sec-help   

   Fragen und Antworten <de/help/faq>
   Meinungen und Tipps <de/help/opinions>
   Bekannte Fehler <de/help/errors>
   Technische Unterstützung <de/help/support>
   Service <de/help/service>
   Mitarbeit <de/help/cooperation>
   Spenden <de/help/donation>
   Glossar <de/help/glossar>
