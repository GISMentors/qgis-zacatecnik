.. |gdal| image:: ../images/icon/gdal.png
   :width: 1.5em

.. index::
   pair: rastrová data; export dat

Export rastrových údajů
^^^^^^^^^^^^^^^^^^^^^^^

.. Díky knihovně |gdal| :sup:`GDAL` (Geospatial Data Abstraction Library) je možné
   čtení a zápis rastrových GIS formátů v prostředí QGIS. Pro všechny podporované
   datové formáty využívá knihovna jednoduchý datový model.

Existuje množství rastrových formátů, které jsou obvykle odlišené dle
přípony souborů. Díky knihovně GDAL umožňuje QGIS export do velkého
množství různých běžně používaných formátů.

Data je možné exportovat dvěma způsoby. Pokud potřebujeme vrstvu
uložit (exportovat) v tom samém formátu, protože pracujeme například
jenom s částí zájmového území, použijeme volbu :item:`Uložit
jako`. Tato volba je dostupná z kontextového menu na vybranou
vrstvou. Objeví se dialogové okno, kde se dá nastavit režim výstupu
(surová data nebo vykreslený obrázek), název, souřadnicový systém,
rozsah, rozlišení, možnosti vytvoření a další parametry nově
exportované vrstvy. Po spuštění se nová vrstva přidá do mapového okna
(:num:`#saveas`).

.. _saveas:

.. figure:: images/saveas.png
   :class: large
   :scale-latex: 85
   
   Export rastrové vrstvy pomocí :item:`Uložit rastrovou vrstvu jako ...`.

Pokud potřebujeme rastrovou vrstvu uložit v jiném formátu, použijeme
:menuselection:`Raster --> Převod --> Převíst na jiný formát` 
(:num:`#menu-prevod`). V dialogovém okně nastavíme vstupní vrstvu, cílový
souřadnicový systém a ostatní dle potřeby.

.. _menu-prevod:

.. figure:: images/menu_prevod.png
   :scale-latex: 45
   
   Export rastrové vrstvy do jiného formátu.


