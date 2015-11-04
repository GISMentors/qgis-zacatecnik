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
.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |mActionZoomIn| image:: ../images/icon/mActionZoomIn.png
   :width: 1.5em
.. |mActionShowRasterCalculator| image:: ../images/icon/mActionShowRasterCalculator.png
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
       :class: middle

       Rôzne štýly tej istej rastovej vrstvy: šedé pásmo (vľavo), pseudofarby (vpravo)
    
.. note:: Po nastavení  farebnej palety je potrebné nezabudnúť na tlačítko :item:`Klasifikovat`, ktoré  vygeneruje farby pre konkrétny režim, v našom prípade lineárna farebná interpolácia a invertovaná spojitá paleta *RdYIGn*. Nastavenie hodnoty smerodajnej odchýlky dokáže zabezpečiť, aby hodnoty, ktoré sa príliš líšia od priemeru pre vrstvu, neboli zobrazené.

.. noteadvanced:: Ďalšie možnosti štýlovania ponúka lišta :item:`Raster`, ktorá sa zapína cez :menuselection:`Zobraziť --> Nástrojové lišty --> Raster`. Napríklad prvá položka zľava |mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut Stretch` automaticky vylepší kontrast na základe minimálnej a maximálnej hodnoty bunky v aktuálnej lokálnej časti rastra, pričom berie do úvahy východzie limity a odhadnuté hodnoty. Výsledok je na :num:`obr. #stylrstpanel` vľavo. Voľba |mActionFullHistogramStretch| :sup:`Roztiahnuť histogram na celý dataset` nástrojovej lišty vráti zmeny späť ako boli na :num:`obr. #stylraster`, t.j. vyrovná kontrast vzhľadom na celý raster podľa skutočných hodnôt. Ak pravým kliknutím na meno vrstvy zvolíme z kontextového menu :item:`ZOOM na najvhodnejšie merítko (100%)`, klikneme na |mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut Stretch` a zvolíme |mIconZoom| :sup:`Priblížiť na vrstvu` čím vytvoríme štýl znázornený na :num:`obr. #stylrstpanel` vpravo.

    .. _stylrstpanel:

    .. figure:: images/styl_rst_panel.png
       :class: middle

       Vylepšenie štýlu rastrovej vrstvy pomocou nástrojovej lišty :item:`Raster`

Priehľadnosť
^^^^^^^^^^^^

QGIS umožňuje zobrazovať každú vrstvu v mapovom okne s rôznym stupňom priehľadnosti. Má to veľkú výhodu napríklad keď chceme, aby okrem aktuálnej rastrovej vrstvy bola viditeľná aj iná. Typickým príkladom je prekrývanie tieňovaného reliéfu s akoukoľvek farebnou rastrovou vrstvou. Prekrytie a vhodné nastavenie priehľadnosti spôsobí priestorový vzhľad 2D vrstvy. Konkrétnejšie si to ukážeme neskôr.

Záložka umožňuje nastaviť všeobecnú priehľadnosť, ale taktiež priehľadnosť pre každý pixel. V časti o užívateľských nastaveniach transparentnosti (viď. :num:`obr. #rsttransparency` s paletovaným typom vykreslenia pásma pre raster) je možné nastaviť hodnoty pomocou tlačidiel |symbologyAdd| :sup:`Zadať hodnoty ručne` alebo |mActionContextHelp| :sup:`Pridať hodnoty z obrazovky`, ďalej možno |symbologyRemove| :sup:`Odstrániť vybrané riadky`, hodnoty |mActionFileOpen| :sup:`Importovať z` alebo |mActionFileSave| :sup:`Exportovať do` súboru, čo má zmysel hlavne pri detailnejších, časovo náročných prácach. Táto záložka taktiež umožňuje nastavenia pre *no data*.

    .. _rsttransparency:

    .. figure:: images/rst_transparency.png

        Možnosti nastavenia priehľadnosti rastrovej vrstvy

Pyramídy
^^^^^^^^

Pyramídy sú dátové štruktúry, ktoré typicky obsahujú menšie množstvo dát. Cieľom je znížiť výpočtovú náročnosť pri práci s dátami. Ide o to, že okrem pôvodného rastra v plnom rozlíšení sa vytvorí zjednodušená verzia (kópia s nižším rozlíšením). Na prevzorkovanie sa používajú rôzne metódy, najčastejšie ide o metódu priemerov (*Average*) alebo metódu najbližšieho suseda (Nearest Neighbour). 

.. note:: Oprávnený na takéto úkony je len ten, kto má právo zápisu do adresára s pôvodnými dátami.

.. important:: Je potrebné vedieť, že vytváranie pyramíd môže pozmeniť orginálny raster a preto sa odporúča vytvorenie zálohy pôvodnej bezpyramídovej verzie dát. 


Histogram
^^^^^^^^^

QGIS ponúka nástroj na generovanie histogramu rastrovej vrstvy (:num:`obr. #rsthistogram`). Je vytvorený automaticky po kliknutí na voľbu :item:`Vypočítať histogram`. 

    .. _rsthistogram:

    .. figure:: images/rst_histogram.png
       :class: middle

       Výpočet histogramu rastrovej vrstvy digitálneho výškového modelu terénu

Metaúdaje
^^^^^^^^^
Táto záložky by mala poskytovať informácie o danej rastrovej vrstve (ak existujú).  Ide najmä o základný popis dát (nadpis, abstrakt, zoznam kľúčových slov), Url metadát a legendy či iné vlastnosti (ovládač, popis datasetu, veľkosť pixela, súradnicové systémy, rozsah vrstvy, atď.). 

Terénne analýzy
---------------

Digitálny výškový model terénu je užitočný typ dát, z ktorého je možné odvodiť ďalšie informácie o danom území a tak lepšie vystihnúť charakter skúmaného územia. Nástroje pre terénne analýzy a vizualizácie terénu sú dostupné z menu :menuselection:`Raster --> Analýza --> DEM (modely reliéfu)`, viď. :num:`obr. #menudem`. S týmito nástrojmi môžeme odvodiť dátové sady, ktoré neboli úplne evidentné z pôvodného rastra výškopisu. Môže ísť o odvodenie sklonu reliéfu či orientáciu svahu voči svetovým stranám. 

    .. _menudem:

    .. figure:: images/menudem.png

       Nástroje pre terénne analýzy dostupné z menu

.. note:: Nástrojová lišta :item:`Raster` obsahuje okrem možnosti vykonávať terénne analýzy aj nástroje týkajúce sa mapovej algebry, súradnicových systémov, konverzie do iných formátov, orezávanie rastrov, generovanie vrstevníc a iné.

Tieňovaný reliéf (*Hillshade*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ako bolo spomenuté už v časti o nastaveniach transparentnosti rastrových dát, tieňovaný reliéf je využívanou rastrovou vrstvou pri zobrazovaní 2D dát reprezentujúcich 3D javy, pretože s jeho pomocou sa dá dosiahnuť priestorový efekt. Abstraktné informácie o výške terénu v rasti :map:`dmt.tiff` znázorníme  pomocou rastrovej vrstvy tieňovaného reliéfu, tzv. *hillshade*. Ten vytvoríme tak, že z ponuky menu vyberieme :menuselection:`Raster --> Analýza --> DEM (modely reliéfu)`. V dialógovom okne nastavíme názov a cestu k vstupnej (:map:`dmt.tiff`) a výstupnej rastrovej vrstve (:map:`hillshade.tif`), zvolíme režim :item:`Tieňovaný reliéf`, predvolené možnosti režimu ponecháme, zaškrtneme |checkbox| :sup:`Po dokončení načítať do mapového okna` a potvrdíme tlačítkom :item:`OK`. 

.. noteadvanced:: V rámci možností režimu vytvárania tieňovaného reliéfu je možné nastaviť hodnotu zvislého prevýšenia, pomer zvislých a vodorovných jednotiek, azimut či nadmorskú výšku svetla.

Po skončení výpočtu sa v paneli so zoznamom vrstiev objaví novovytvorený tieňovaný reliéf :map:`hillshade`. Aby sme lepšie videli detaily, pomocou |mActionZoomIn| :sup:`Priblížiť` si ohraničíme časť územia. Následne spôsobom, ktorý bol opísaný vyššie nastavíme všeobecnú transparentnosť rastrovej vrstvy :map:`hillshade` na hodnotu :item:`60%`. Dostaneme výsledok znázornený na :num:`obr. #rsthillshade`.

    .. _rsthillshade:

    .. figure:: images/rst_hillshade.png
       :class: middle

       Vytvorenie priestorového efektu dát vďaka tieňovanému reliéfu

.. note:: Rastrová vrstva tieňovaného reliéfu je v menu :item:`Vrstvy` nad vrstvou :map:`dmt.tiff`. Je možné urobiť to opačne, t.j. vrstvu :map:`hillshade` nechať ako podklad a nastaviť transparentnosť digitálneho výškového modelu terénu.

Sklon (*Slope*)
^^^^^^^^^^^^^^^

Jednou z užitočných informácií o teréne je aj sklon, ktorý predstavuje maximálnu zmenu (gradient) výšky medzi susednými bunkami rastra. Rastrovú vrstvu sklonu vygenerujeme obdobne ako tieňovaný reliéf, no použijeme režim :item:`Sklon`. Na :num:`obr. #rstsklon` je znázornený výsledok s farebnou paletou *BrBG*, pričom je použité rozdelenie do 10 rovnakých intervalov.

    .. _rstsklon:

    .. figure:: images/rst_sklon.png

       Rastrová vrstva sklonov reliéfu

Orientácia voči svetovým stranám (*Aspect*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Na vytvorenie mapy orientácie svahu na svetové strany použijeme režim :item:`Aspekt`.

Použitie rastrovej kalkulačky
-----------------------------

Pri tvorbe mapy orientácie na svetové strany je lepšie reklasifikovať (rozdeliť) rozsah hodnôt do kategórií sever (1), východ (2), juh (3) a západ (4), pričom sever znamená :item:`0°` a východ :item:`90°`. Jednou z možností je využitie tzv. rastrovej kalkulačky, konkrétne |mActionShowRasterCalculator| :sup:`Raster kalkulátor`. 

Rastrová kalkulačka súvisí s mapovou algebrou. Ide o matematické operácie s rastrovými mapami, ktoré sú akoby matice čísel s priestorovým umiestnením. Pomocou mapovej algebry je možné matematickými, ale i inými operáciami kombinovať viaceré rastrové vrstvy a tým vytvárať nové vrstvy. 

    .. _rstcalculator:

    .. figure:: images/rstcalculator.png
       :scale: 70%

       Mapová algebra

Ak sme mapu orientácií nazvali :map:`aspect`, výraz bude vyzerať nasledovne: :code:`(("aspect@1"  >= 315)  AND  ("aspect@1" < 45)) * 1 + (("aspect@1"  >= 45)  AND  ("aspect@1" < 135)) * 2 + (("aspect@1"  >= 135)  AND  ("aspect@1" < 225)) * 3 + (("aspect@1"  >= 225)  AND  ("aspect@1" < 315)) * 4`. Reklasifikovanej vrstve následne nastavíme farebnosť a popisy (:num:`obr. #nesw` a :num:`obr. #aspectrecl`).

    .. _nesw:

    .. figure:: images/nesw.png
       :class: middle

       Reklasifikácia orientácií svahu na svetové strany pomocou mapovej kalkulačky

    .. _aspectrecl:

    .. figure:: images/aspect_recl.png

       Reklasifikovaná mapa orientácií svahu na svetové strany

.. note:: Pri reklasifikáciách sa zvyčajne používa modul GRASS-u :grasscmd:`r.reclass`. Na to je však potrebné nainštalovať zásuvný modul :item:`grass`, ktorý nie je dostupný v každej verzii *QGIS*. Cieľom bolo ukázať, že reklasifikovať sa dá aj bez bez pluginov.

Jednoduchý praktický príklad
----------------------------

Zobrazovanie v 3D
-----------------




