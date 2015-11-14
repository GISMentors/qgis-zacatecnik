.. |mActionZoomIn| image:: ../images/icon/mActionZoomIn.png
   :width: 1.5em

Terénne analýzy
---------------

Digitálny výškový model terénu je užitočný typ dát, z ktorého
je možné odvodiť ďalšie informácie o danom území a tak lepšie
vystihnúť charakter skúmaného územia. Nástroje pre terénne analýzy
a vizualizácie terénu sú dostupné z menu :menuselection:`Raster -->
Analýza --> DEM (modely reliéfu)`, viď. :num:`#menudem`. S týmito
nástrojmi môžeme odvodiť dátové sady, ktoré neboli úplne evidentné
z pôvodného rastra výškopisu. Môže ísť o odvodenie sklonu reliéfu
či orientáciu svahu voči svetovým stranám.

    .. _menudem:

    .. figure:: images/menudem.png

       Nástroje pre terénne analýzy dostupné z menu

.. note:: Nástrojová lišta :item:`Raster` obsahuje okrem možnosti
vykonávať terénne analýzy aj nástroje týkajúce sa mapovej algebry,
súradnicových systémov, konverzie do iných formátov, orezávanie rastrov,
generovanie vrstevníc a iné.

Tieňovaný reliéf (*Hillshade*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ako bolo spomenuté už v časti o nastaveniach transparentnosti rastrových
dát, tieňovaný reliéf je využívanou rastrovou vrstvou pri zobrazovaní 2D
dát reprezentujúcich 3D javy, pretože s jeho pomocou sa dá dosiahnuť
priestorový efekt. Abstraktné informácie o výške terénu v rasti
:map:`dmt.tiff` znázorníme pomocou rastrovej vrstvy tieňovaného
reliéfu, tzv. *hillshade*. Ten vytvoríme tak, že z ponuky menu vyberieme
:menuselection:`Raster --> Analýza --> DEM (modely reliéfu)`. V dialógovom
okne nastavíme názov a cestu k vstupnej (:map:`dmt.tiff`) a výstupnej
rastrovej vrstve (:map:`hillshade.tif`), zvolíme režim :item:`Tieňovaný
reliéf`, predvolené možnosti režimu ponecháme, zaškrtneme |checkbox|
:sup:`Po dokončení načítať do mapového okna` a potvrdíme tlačítkom
:item:`OK`.

.. noteadvanced:: V rámci možností režimu vytvárania tieňovaného
reliéfu je možné nastaviť hodnotu zvislého prevýšenia, pomer zvislých
a vodorovných jednotiek, azimut či nadmorskú výšku svetla.

Po skončení výpočtu sa v paneli so zoznamom vrstiev objaví novovytvorený
tieňovaný reliéf :map:`hillshade`. Aby sme lepšie videli detaily,
pomocou |mActionZoomIn| :sup:`Priblížiť` si ohraničíme časť
územia. Následne spôsobom, ktorý bol opísaný vyššie nastavíme
všeobecnú transparentnosť rastrovej vrstvy :map:`hillshade` na hodnotu
:item:`60%`. Dostaneme výsledok znázornený na :num:`#rsthillshade`.

    .. _rsthillshade:

    .. figure:: images/rst_hillshade.png
       :class: middle

       Vytvorenie priestorového efektu dát vďaka tieňovanému reliéfu

.. note:: Rastrová vrstva tieňovaného reliéfu je v menu :item:`Vrstvy`
nad vrstvou :map:`dmt.tiff`. Je možné urobiť to opačne, t.j. vrstvu
:map:`hillshade` nechať ako podklad a nastaviť transparentnosť digitálneho
výškového modelu terénu.

Sklon (*Slope*)
^^^^^^^^^^^^^^^

Jednou z užitočných informácií o teréne je aj sklon, ktorý predstavuje
maximálnu zmenu (gradient) výšky medzi susednými bunkami rastra. Rastrovú
vrstvu sklonu vygenerujeme obdobne ako tieňovaný reliéf, no použijeme
režim :item:`Sklon`. Na :num:`#rstsklon` je znázornený výsledok s farebnou
paletou *BrBG*, pričom je použité rozdelenie do 10 rovnakých intervalov.

    .. _rstsklon:

    .. figure:: images/rst_sklon.png
       :class: middle

       Rastrová vrstva sklonov reliéfu

Orientácia voči svetovým stranám (*Aspect*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Na vytvorenie mapy orientácie svahu na svetové strany použijeme režim
:item:`Aspekt`.

