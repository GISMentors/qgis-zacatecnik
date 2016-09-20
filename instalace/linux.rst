.. |aplikace_ikona| image:: images/aplikace_ikona.png
   :width: 1.5em

.. _label: instalace-linux

.. index::
   single: Linux
   see: Linux; Instalace


GNU/Linux - Ubuntu
------------------

Instalace programů v systému Ubuntu je založená na tzv. balíčcích, které jsou k
dispozici v repozitářích.
Některé repozitáře můžou obsahovat starší verze systému QGIS, proto je nutné
dbát na způsob instalace. Instalace v Ubuntu je popsána ve dvou základních
způsobech - instalace přes *Terminál* a pomocí *Centra softweru pro Ubuntu*.

Terminál
========

Podrobný postup jak nainstalovat požadovanou verzi (Latest/Long Term) lze 
nálezt v instalační příručce v 
`QGIS dokumentaci <https://www.qgis.org/en/site/forusers/alldownloads.html#linux>`_. 
Zde také naleznete odkazy na repozitáře těchto verzí.

Instalaci můžeme provézt dvěma základními způsoby, a to buď se závislostmi na 
repozitáři *ubuntugis* či nikoliv. V obou případech musíme přidat repozitář do 
zdroju softwaru systému (přes aplikaci :item:`software-sources` nebo editací 
souboru :item:`/etc/apt/sources.list`. Zdoje přidáme v následujícím tvaru:

.. notecmd:: Přidání repozitářů pro instalaci QGIS
               
   .. code-block:: bash

      deb     *repository* *codename* main
      deb-src *repository* *codename* main

V případě, že chcete instalovat QGIS se závislostmi na repozitáři *ubuntugis*, 
ale ještě jej nemáte ve zdrojích, je nutné přidat:

.. notecmd:: Přidání repozitářů pro instalaci QGIS
               
   .. code-block:: bash

      deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu 
      *codename* main

nebo přímo v terminálu zadat příkaz:

.. notecmd:: Přidání repozitářů pro instalaci QGIS
               
   .. code-block:: bash

      sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable

Příklad pro případnou instalaci LTR verze na Ubuntu 16.04 (LTS) Xenial bez 
*ubuntugis*:

.. notecmd:: Instalace QGIS
               
   .. code-block:: bash

      deb     http://qgis.org/debian-ltr xenial main
      deb-src http://qgis.org/debian-ltr xenial main


Samotný příkaz k instalaci:

.. notecmd:: Instalace QGIS
               
   .. code-block:: bash

       sudo apt-get update
       sudo apt-get install qgis python-qgis qgis-plugin-grass

V některých pípadech je poro instalaci nutné přidat klíč:

.. notecmd:: Instalace QGIS
               
   .. code-block:: bash
      
      sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 
      073D307A618E5811


Centrum softwaru pro Ubuntu
===========================

Jedná se o jednoduchého grafického správce balíčků umožňující jejich
instalaci. Je dostupný z menu přes ikonu |aplikace_ikona|. Ve
vyhledávacím okně lze zadat "QGIS" a následně se vypíšou všechny
dostupné aplikace. Pomocí tlačítka :item:`Další informace` lze otevřít
detailní popis nabízeného systému. Hlavní informací je zejména verze
systému QGIS, kterou instalací získáme. Samotnou instalaci lze provést
tlačítkem :item:`Nainstalovat`.

.. figure:: images/centrum_soft.png
   :class: middle
        
   Výběr QGISu přes Centrum softwaru pro Ubuntu.
