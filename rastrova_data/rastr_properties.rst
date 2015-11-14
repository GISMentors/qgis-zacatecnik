.. |mActionFullHistogramStretch| image:: ../images/icon/mActionFullHistogramStretch.png
   :width: 1.5em
.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |CRS| image:: ../images/icon/CRS.png
   :width: 1.5em
.. |mActionLocalCumulativeCutStretch| image:: ../images/icon/mActionLocalCumulativeCutStretch.png
   :width: 1.5em
.. |mIconZoom| image:: ../images/icon/mIconZoom.png
   :width: 1.5em
.. |symbologyAdd| image:: ../images/icon/symbologyAdd.png
   :width: 1.5em
.. |mActionContextHelp| image:: ../images/icon/mActionContextHelp.png
   :width: 1.5em
.. |mActionFileOpen| image:: ../images/icon/mActionFileOpen.png
   :width: 1.5em
.. |symbologyRemove| image:: ../images/icon/symbologyRemove.png
   :width: 1.5em
.. |mActionFileSave| image:: ../images/icon/mActionFileSave.png
   :width: 1.5em

Vlastnosti rastrovej vrstvy
---------------------------

Na to, aby sme videli a nastavili vlastnosti danej rastrovej vrstvy,
použijeme buď ľavý dvojklik na meno vrstvy alebo pravým kliknutím
zvolíme z kontextového menu položku :item:`Vlastnosti`. Dialógové
okno obsahuje šesť záložiek: *Všeobecné*, *Štýl*, *Priehľadnosť*,
*Pyramídy*, *Histogram* a *Metadáta*.

Všeobecné
^^^^^^^^^

Prvá záložka poskytuje základné informácie o vrstve ako názov súboru,
názov vrstvy v legende s možnosťou editácie, zdroj vrstvy, počet stĺpcov
a riadkov, súradnicový referenčný systém, ktorý možno zmeniť kliknutím
na tlačítko |CRS| :sup:`Vyberte SRS`. V tejto záložke je možné nastaviť
aj viditeľnosť v závislosti na mierke, viď. :num:`#obecneraster`.

.. _obecneraster:

.. figure:: images/obecne_raster.png

   Vlastnosti rastovej vrstvy

Štýl
^^^^

Táto záložka slúži na nastavenie farebnosti rastrových dát v mapovom
okne. Je možné nastaviť vykresľovanie pásma, farby či prevzorkovanie. V
danej vrstve môžu byť farby invertované, dá sa vylepšovať kontrast,
sýtosť, jas, rozsah vykresľovaných hodnôt (:num:`#stylraster`).

.. _stylraster:

.. figure:: images/styl_raster.png
   :class: middle

   Rôzne štýly tej istej rastovej vrstvy: šedé pásmo (vľavo),
   pseudofarby (vpravo)

.. note:: Po nastavení farebnej palety je potrebné nezabudnúť na tlačítko
:item:`Klasifikovat`, ktoré vygeneruje farby pre konkrétny režim, v našom
prípade lineárna farebná interpolácia a invertovaná spojitá paleta
*RdYIGn*. Nastavenie hodnoty smerodajnej odchýlky dokáže zabezpečiť, aby
hodnoty, ktoré sa príliš líšia od priemeru pre vrstvu, neboli zobrazené.

.. noteadvanced:: Ďalšie možnosti štýlovania ponúka lišta
:item:`Raster`, ktorá sa zapína cez :menuselection:`Zobraziť -->
Nástrojové lišty --> Raster`. Napríklad prvá položka zľava
|mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut Stretch`
automaticky vylepší kontrast na základe minimálnej a maximálnej
hodnoty bunky v aktuálnej lokálnej časti rastra, pričom berie do úvahy
východzie limity a odhadnuté hodnoty. Výsledok je na :num:`#stylrstpanel`
vľavo. Voľba |mActionFullHistogramStretch| :sup:`Roztiahnuť histogram
na celý dataset` nástrojovej lišty vráti zmeny späť ako boli
na :num:`#stylraster`, t.j. vyrovná kontrast vzhľadom na celý raster
podľa skutočných hodnôt. Ak pravým kliknutím na meno vrstvy zvolíme z
kontextového menu :item:`ZOOM na najvhodnejšie merítko (100%)`, klikneme
na |mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut Stretch`
a zvolíme |mIconZoom| :sup:`Priblížiť na vrstvu` čím vytvoríme štýl
znázornený na :num:`#stylrstpanel` vpravo.

.. _stylrstpanel:

.. figure:: images/styl_rst_panel.png
   :class: middle

   Vylepšenie štýlu rastrovej vrstvy pomocou nástrojovej lišty :item:`Raster`

Priehľadnosť
^^^^^^^^^^^^

QGIS umožňuje zobrazovať každú vrstvu v mapovom okne s rôznym stupňom
priehľadnosti. Má to veľkú výhodu napríklad keď chceme, aby okrem
aktuálnej rastrovej vrstvy bola viditeľná aj iná. Typickým príkladom
je prekrývanie tieňovaného reliéfu s akoukoľvek farebnou rastrovou
vrstvou. Prekrytie a vhodné nastavenie priehľadnosti spôsobí priestorový
vzhľad 2D vrstvy. Konkrétnejšie si to ukážeme neskôr.

Záložka umožňuje nastaviť všeobecnú priehľadnosť, ale taktiež
priehľadnosť pre každý pixel. V časti o užívateľských nastaveniach
transparentnosti (viď. :num:`#rsttransparency` s paletovaným typom
vykreslenia pásma pre raster) je možné nastaviť hodnoty pomocou tlačidiel
|symbologyAdd| :sup:`Zadať hodnoty ručne` alebo |mActionContextHelp|
:sup:`Pridať hodnoty z obrazovky`, ďalej možno |symbologyRemove|
:sup:`Odstrániť vybrané riadky`, hodnoty |mActionFileOpen| :sup:`Importovať
z` alebo |mActionFileSave| :sup:`Exportovať do` súboru, čo má zmysel
hlavne pri detailnejších, časovo náročných prácach. Táto záložka
taktiež umožňuje nastavenia pre *no data*.

.. _rsttransparency:

.. figure:: images/rst_transparency.png

   Možnosti nastavenia priehľadnosti rastrovej vrstvy

Pyramídy
^^^^^^^^

Pyramídy sú dátové štruktúry, ktoré typicky obsahujú menšie
množstvo dát. Cieľom je znížiť výpočtovú náročnosť pri práci
s dátami. Ide o to, že okrem pôvodného rastra v plnom rozlíšení
sa vytvorí zjednodušená verzia (kópia s nižším rozlíšením). Na
prevzorkovanie sa používajú rôzne metódy, najčastejšie ide o metódu
priemerov (*Average*) alebo metódu najbližšieho suseda (Nearest Neighbour).

.. note:: Oprávnený na takéto úkony je len ten, kto má právo zápisu
do adresára s pôvodnými dátami.

.. important:: Je potrebné vedieť, že vytváranie pyramíd môže
pozmeniť orginálny raster a preto sa odporúča vytvorenie zálohy pôvodnej
bezpyramídovej verzie dát.


Histogram
^^^^^^^^^

QGIS ponúka nástroj na generovanie histogramu rastrovej vrstvy
(:num:`#rsthistogram`). Je vytvorený automaticky po kliknutí na voľbu
:item:`Vypočítať histogram`.

.. _rsthistogram:

.. figure:: images/rst_histogram.png
   :class: middle

   Výpočet histogramu rastrovej vrstvy digitálneho výškového modelu terénu

Metaúdaje
^^^^^^^^^
Táto záložky by mala poskytovať informácie o danej rastrovej vrstve
(ak existujú).  Ide najmä o základný popis dát (nadpis, abstrakt, zoznam
kľúčových slov), Url metadát a legendy či iné vlastnosti (ovládač,
popis datasetu, veľkosť pixela, súradnicové systémy, rozsah vrstvy,
atď.).

