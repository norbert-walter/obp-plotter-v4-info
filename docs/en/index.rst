######################
OBP-Plotter V4 documentation
######################
Letzte Aktualisierung |today|

.. note::   These sites are still in progress

.. image:: /pics/Display.jpg
             :scale: 20%

The OBP Plotter V4, developed by Christian Hartz, is used for displaying marine charts and data on leisure boats. The target group is recreational boaters all over the world. 

The OBP plotter is equipped with a daylight-compatible 10-inch touch display. Compute modules versions 4 and 5 from the Raspberry Foundation serve as the hardware basis. The plotter communicates with the outside world primarily via USB or WLAN. This makes it extremely flexible when using a wide range of navigation systems on board. 

Integration into existing NMEA networks is of course also possible, whether NMEA-0183 or NMEA2k. The operating system is based on a current Android (14 or 15), on which the “AvNav” navigation app is pre-installed. Alternatively, users can also use a Raspbian to install OpenCPN, for example.



.. toctree::
   :maxdepth: 3
   :caption: Intro
   :name: sec-intro

   overview <en/intro/historie>
   technical data <intro/specification>
   variants <intro/variants>
   
.. toctree::
   :maxdepth: 3
   :caption: installation
   :name: sec-usermanual

   start-up <usermanual/start>
   installation android <usermanual/android_install>
   configuration android <usermanual/android_configuration>
   installation raspbian <usermanual/raspbian_install>
   configuration raspbian <usermanual/raspbian_configuration>
   interfaces <usermanual/dataexchange>
   sensors <usermanual/sensors>
   example configuration <usermanual/samples>
   safety hints <usermanual/safety>

.. toctree::
   :maxdepth: 3
   :caption: assembling
   :name: sec-assembling
   
   device design <assembling/device>
   preparation <assembling/preparation>
   part list <assembling/partlist>
   implementation <assembling/actionsteps>
   functional test <assembling/tests>
   
    
.. toctree::
   :maxdepth: 3
   :caption: support
   :name: sec-help   

   F & Q <help/faq>
   feedback and hints <help/opinions>
   known errors <help/errors>
   technical support <help/support>
   service <help/service>
   cooperation <help/cooperation>
   donate <help/donation>
   glossar <help/glossar>
