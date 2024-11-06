######################
OBP-Plotter V4 Dokumentation
######################
Letzte Aktualisierung |today|

.. note::   Diese Seiten sind noch in Bearbeitung.

.. image:: /pics/Display.jpg
             :scale: 20%

NEU
Der OBP-Plotter V4, entwickelt von Christian Hartz,  wird für die Darstellung von marinen Karten und Daten auf Freizeit-Booten verwendet. Zielgruppe sind Sportbootfahrende in aller Welt. 

Der OBP-Plotter ist ausgestattet mit einem tageslichttauglichen 10-Zoll-Touch-Display. Als Hardwarebasis dienen Compute Module der Versionen 4 und 5 der Raspberry Foundation. Mit der Außenwelt kommuniziert der Plotter vor allem per USB oder WLAN. Das macht ihn maximal flexibel im Einsatz unterschiedlichster Navigationssysteme an Bord. 

Eine Einbindung in bestehende NMEA-Netzwerke ist selbstverständlich ebenso möglich, egal ob NMEA-0183 oder NMEA2k. Die Betriebssystembasis bildet ein aktuelles Android (14 oder 15), auf dem die Navigations-App "AvNav" vorinstalliert ist. Alternativ lässt sich von Anwendern auch ein Raspbian einsetzen, um dort zum Beispiel OpenCPN zu installieren.

.. toctree::
   :maxdepth: 3
   :caption: Einführung
   :name: sec-intro

   Übersicht <intro/historie>
   Technische Daten <intro/specification>
   Varianten <intro/variants>
   
.. toctree::
   :maxdepth: 3
   :caption: Installation
   :name: sec-usermanual

   Inbetriebnahme <usermanual/start>
   Installation Android <usermanual/android_install>
   Konfiguration Android <usermanual/android_configuration>
   Installation Raspbian <usermanual/raspbian_install>
   Konfiguration Raspbian <usermanual/raspbian_configuration>
   Schnittstellen <usermanual/dataexchange>
   Sensorik <usermanual/sensors>
   Beispielkonfiguration <usermanual/samples>
   Sicherheitshinweise <usermanual/safety>

.. toctree::
   :maxdepth: 3
   :caption: Zusammenbau
   :name: sec-assembling
   
   Geräteaufbau <assembling/device>
   Vorbereitung <assembling/preparation>
   Bauteilliste <assembling/partlist>
   Durchführung <assembling/actionsteps>
   Funktionstest <assembling/tests>
   
    
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
