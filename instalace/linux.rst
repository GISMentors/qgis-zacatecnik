.. |aplikace_ikona| image:: images/aplikace_ikona.png
   :width: 1.5em

.. _label: instalace-linux

.. index::
   single: Linux
   see: Linux; Instalace


Instalace pod GNU/Linux - Ubuntu
--------------------------------

Instalace programů v systému Ubuntu je založená na tzv. balíčcích, které jsou k
dispozici v repozitářích.
Některé repozitáře můžou obsahovat starší verze systému QGIS, proto je nutné
dbát na způsob instalace. Instalace v Ubuntu je popsána ve dvou základních
způsobech - instalace přes *Terminál* a pomocí *Centra softweru pro Ubuntu*.

Terminál
========

Instalace v terminálu, která je níže podrobně rozepsaná, se skládá ze tří
základních částí. První krok přidá konkrétní repozitář pro získání systému QGIS.
Druhý krok slouží k aktualizaci seznamu repozitářu a jejich obsahu. Třetí krok
je samotná instalace programu.
 
.. notecmd:: Instalace QGIS
               
   .. code-block:: bash

      sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
      sudo apt-get update
      sudo apt-get install qgis


Centrum softwaru pro Ubuntu
===========================

Jedná se o jednoduchého grafického správce balíčků pro instalaci. Je dostupný z
menu přes ikonu |aplikace_ikona|. Ve vyhledávacím okně lze zadat "QGIS" a
následně se vypíše dostupná aplikace. Pomocí tlačítka :item:`Další informace`
lze otevřít detailní popis nabízeného systému. Hlavní informací je zejména verze
QGIS systému, kteou instalací získáme. Samotnou instalaci lze provést tlačítkem
:item:`Nainstalovat`.

.. figure:: images/centrum_soft.png

   Výběr QGISu přes Centrum softwaru pro Ubuntu.

.. todo:: opravit ikonku a pridat screenshot
