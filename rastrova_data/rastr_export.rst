.. |gdal| image:: ../images/icon/gdal.png
   :width: 1.5em


Export rastrových údajov
^^^^^^^^^^^^^^^^^^^^^^^^

Vďaka knižnici |gdal| :sup:`GDAL` (Geospatial Data Abstraction Library) je možné čítanie a zápis rastrových GIS formátov v prostredí QGIS. Pre všetky podporované dátové formáty využíva knižnica jednoduchý dátový model. 

Existuje množstvo rastrových formátov, ktoré sú zvyčajne odlíšené podľa prípony súborov. QGIS umožňuje export do veľkého množstva rôznych bežne používaných formátov.  

Dáta možno exportovať dvomi spôsobmi. Ak potrebujeme vrstvu uložiť (exportovať) v tom istom formáte, lebo pracujeme napríklad len s časťou záujmového územia, použijeme voľbu :item:`Uložiť ako`. Nájdeme ju pravým kliknutím myši na mapu v paneli vrstiev. Objaví sa dialógové okno, kde sa dá nastaviť režim výstupu (surové dáta alebo vykreslený obrázok), názov, súradnicový systém, rozsah, rozlíšenie, možnosti vytvorenia a ďalšie parametre novej exportovanej vrstvy. Po spustení sa nová vrstva pridá do mapového okna (:num:`#saveas`). 

    .. _saveas:

    .. figure:: images/saveas.png
       :class: middle
   
       Export rastrovej vrstvy pomocou :item:`Uložiť rastrovú vrstvu ako ... `

Ak potrebujeme rastrovú vrstvu uložiť v inom formáte, použijeme :menuselection:`Raster --> Prevod --> Previesť na iný formát` (:num:`#menu-prevod`). V dialógovom okne nastavíme vstupnú a výstupnú vrstvu, cieľový súradnicový systém, atď.

    .. _menu-prevod:

    .. figure:: images/menu_prevod.png
       :class: small
   
       Export rastrovej vrstvy do iného formátu

