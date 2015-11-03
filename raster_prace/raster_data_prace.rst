.. |mActionAddRasterLayer| image:: ../images/icon/mActionAddRasterLayer.png
   :width: 1.5em

.. |mIconZoom| image:: ../images/icon/mIconZoom.png
   :width: 1.5em

.. |CRS| image:: ../images/icon/CRS.png
   :width: 1.5em

.. |mActionLocalCumulativeCutStretch| image:: ../images/icon/mActionLocalCumulativeCutStretch.png
   :width: 1.5em

.. |mActionFullHistogramStretch| image:: ../images/icon/mActionFullHistogramStretch.png
   :width: 1.5em

.. |symbologyAdd| image:: ../images/icon/symbologyAdd.png
   :width: 1.5em

.. |mActionContextHelp| image:: ../images/icon/mActionContextHelp.png
   :width: 1.5em

.. |symbologyRemove| image:: ../images/icon/symbologyRemove.png
   :width: 1.5em

.. |mActionFileOpen| image:: ../images/icon/mActionFileOpen.png
   :width: 1.5em

.. |mActionFileSave| image:: ../images/icon/mActionFileSave.png
   :width: 1.5em


Práca s rastrovými dátami
==========================

Rastrové dáta reprezentujú objekty a javy rozdelením priestoru do matice diskrétnych buniek (pixelov). Tie sú súčasťou pravidelnej mriežky (gridu), pričom každá z buniek gridu má hodnotu, ktorá reprezentuje nejakú vlastnosť charakteristickú pre dané miesto. Zväčša ide o spojité javy akou je napríklad nadmorská výška reliéfu, teplota ovzdušia či letecké a satelitné snímky. 

Táto časť školenia opisuje ako pracovať s takýmito dátami v prostredí QGIS. Ten totiž podporuje množstvo rozličných rastrových formátov vďaka knižnici GDAL.

Nahratie rastrových údajov
^^^^^^^^^^^^^^^^^^^^^^^^^^

Rastrové dáta možno do prostredia QGIS pridať kliknutím na tlačítko |mActionAddRasterLayer| :sup:`Pridať rastrovú vrstvu`, výberom z lišty menu pomocou :menuselection:`Vrstva --> Pridať vrstvu --> Pridať rastrovú vrstvu` alebo súčasným stlačením kláves :kbd:`Ctrl+Shift+R`. Na :num:`obr. #addraster` je znázornenie rastrovej vrstvy :map:`dmt.tiff` z datasetu :data:`EU-DEM (GeoTIFF)`.

    .. _addraster:

    .. figure:: images/add_raster.png

        Nahratie rastrovej vrstvy do QGIS  

.. note:: Ak by sa vrstva nezobrazila v mapovom okne ako je to na :num:`obr. #addraster`, je potrebné kliknúť pravým tlačítkom na meno vrstvy a zvoliť |mIconZoom| :sup:`Priblížiť na vrstvu`.

.. tip:: V prípade potreby pridržaním klávesy :kbd:`Ctrl` v dialógu vyberania súborov možno súčasne nahrať viacero vrstiev naraz.

Vlastnosti rastrovej vrstvy
---------------------------

Na to, aby sme videli a nastavili vlastnosti danej rastrovej vrstvy, použijeme buď ľavý dvojklik na meno vrstvy alebo pravým kliknutím zvolíme z kontextového menu položku :item:`Vlastnosti`. Dialógové okno obsahuje šesť záložiek: *Všeobecné*, *Štýl*, *Priehľadnosť*, *Pyramídy*, *Histogram* a *Metadáta*.

Všeobecné
^^^^^^^^^

Prvá záložka poskytuje základné informácie o vrstve ako názov súboru, názov vrstvy v legende s možnosťou editácie, zdroj vrstvy, počet stĺpcov a riadkov, súradnicový referenčný systém, ktorý možno zmeniť kliknutím na tlačítko |CRS| :sup:`Vyberte SRS`. V tejto záložke je možné nastaviť aj viditeľnosť v závislosti na mierke, viď. :num:`obr. #obecneraster`.

    .. _obecneraster:

    .. figure:: images/obecne_raster.png

        Vlastnosti rastovej vrstvy

Štýl
^^^^

Táto záložka slúži na nastavenie farebnosti rastrových dát v mapovom okne. Je možné nastaviť vykresľovanie pásma, farby či prevzorkovanie. V danej vrstve môžu byť farby invertované, dá sa vylepšovať kontrast, sýtosť, jas, rozsah vykresľovaných hodnôt (:num:`obr. #stylraster`). 

    .. _stylraster:

    .. figure:: images/styl_raster.png
       :class: large

       Rôzne štýly tej istej rastovej vrstvy: šedé pásmo (vľavo), pseudofarby (vpravo)
    
.. note:: Po nastavení  farebnej palety je potrebné nezabudnúť na tlačítko :item:`Klasifikovat`, ktoré  vygeneruje farby pre konkrétny režim, v našom prípade lineárna farebná interpolácia a invertovaná spojitá paleta *RdYIGn*. Nastavenie hodnoty smerodajnej odchýlky dokáže zabezpečiť, aby hodnoty, ktoré sa príliš líšia od priemeru pre vrstvu, neboli zobrazené.

.. noteadvanced:: Ďalšie možnosti štýlovania ponúka lišta :item:`Raster`, ktorá sa zapína cez :menuselection:`Zobraziť --> Nástrojové lišty --> Raster`. Napríklad prvá položka zľava |mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut Stretch` automaticky vylepší kontrast na základe minimálnej a maximálnej hodnoty bunky v aktuálnej lokálnej časti rastra, pričom berie do úvahy východzie limity a odhadnuté hodnoty. Výsledok je na :num:`obr. #stylrstpanel` vľavo. Voľba |mActionFullHistogramStretch| :sup:`Roztiahnuť histogram na celý dataset` nástrojovej lišty vráti zmeny späť ako boli na :num:`obr. #stylraster`, t.j. vyrovná kontrast vzhľadom na celý raster podľa skutočných hodnôt. Ak pravým kliknutím na meno vrstvy zvolíme z kontextového menu :item:`ZOOM na najvhodnejšie merítko (100%)`, klikneme na |mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut Stretch` a zvolíme |mIconZoom| :sup:`Priblížiť na vrstvu` čím vytvoríme štýl znázornený na :num:`obr. #stylrstpanel` vpravo.

    .. _stylrstpanel:

    .. figure:: images/styl_rst_panel.png
       :class: large

       Vylepšenie štýlu rastrovej vrstvy pomocou nástrojovej lišty :item:`Raster`

Priehľadnosť
^^^^^^^^^^^^

QGIS umožňuje zobrazovať každú vrstvu v mapovom okne s rôznym stupňom priehľadnosti. Má to veľkú výhodu napríklad keď chceme, aby okrem aktuálnej rastrovej vrstvy bola viditeľná aj iná. Typickým príkladom je prekrývanie tieňovaného reliéfu s akoukoľvek farebnou rastrovou vrstvou. Prekrytie a vhodné nastavenie priehľadnosti spôsobí priestorový vzhľad 2D vrstvy. Konkrétnejšie si to ukážeme neskôr.

Záložka umožňuje nastaviť všeobecnú priehľadnosť, ale taktiež priehľadnosť pre každý pixel. V časti o užívateľských nastaveniach transparentnosti (viď. :num:`obr. #rsttransparency` s paletovaným typom vykreslenia pásma pre raster) je možné nastaviť hodnoty pomocou tlačidiel |symbologyAdd| :sup:`Zadať hodnoty ručne` alebo |mActionContextHelp| :sup:`Pridať hodnoty z obrazovky`, ďalej možno |symbologyRemove| :sup:`Odstrániť vybrané riadky`, hodnoty |mActionFileOpen| :sup:`Importovať z` alebo |mActionFileSave| :sup:`Exportovať do` súboru, čo má zmysel hlavne pri detailnejších, časovo náročných prácach. Táto záložka taktiež umožňuje nastavenia pre *no data*.

    .. _rsttransparency:

    .. figure:: images/rst_transparency.png

       Možnosti nastavenia priehľadnosti rastrovej vrstvy

Pyramidy
^^^^^^^^



Histogram
^^^^^^^^^

Metadata
^^^^^^^^

Terénne analýzy
---------------

Z digitálneho výškového modelu je možné odvodiť ďalšie informácie o danom území. Ide hlavne o sklon reliéfu a orientáciu svahu voči svetovým stranám.

Hillshade (použitie, význam)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slope (nastavenie sklonu)
^^^^^^^^^^^^^^^^^^^^^^^^^

Aspect (orientácia na svetové strany)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reklasifikácia dát
------------------

Mapová algebra
--------------

Jednoduchý praktický príklad
----------------------------

Zobrazovanie v 3D
-----------------




