.. |mActionZoomIn| image:: ../images/icon/mActionZoomIn.png
   :width: 1.5em
.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em


Terénní analýzy
---------------

Digitální výškový model terénu je užitečný typ dat, ze kterého je možné odvodit
další informace o daném území a tak lépe vystihnout charakter zkoumaného území.
Nástroje pro terénní analýzy a vizualizace terénu jsou dostupné z menu
:menuselection:`Raster --> Analýza --> DEM (modely reliéfu)`, viz
:num:`#menudem`. S těmito nástroji můžeme odvodit datové sady, které nebyli
úplně evidentní z původního rastru výškopisu. Může jít například o odvození 
sklonu reliéfu nebo orientaci svahu vůči světovým stranám.

.. _menudem:

.. figure:: images/menudem.png

   Nástroje pro terénní analýzy dostupné z menu.

.. note:: 

   Nástrojová lišta :item:`Rastr` obsahuje kromě možnosti vykonávat terénní
   analýzy i nástroje týkajíci se mapové algebry, souřadnicových systémů,
   konverze do jiných formátů, ořezávání rastrů, generování vrstevnic a jiné.

Stínovaný reliéf (*Hillshade*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jak již bylo uvedeno v části o nastavení transparentnosti rastrových dat,
stínovaný reliéf je využívanou rastrovou vrstvou při zobrazování 2D dat
reprezentujících 3D jevy, protože s jeho pomocí se dá dosáhnout prostorový
efekt. Abstraktní informace o výšce terénu v rastru :map:`dmt.tiff` znázorníme
pomocí rastrové vrstvy stínovaného reliéfu, tzv. *hillshade*. Ten vytvoříme tak,
že z nabídky menu vybereme :menuselection:`Rastr --> Analýza --> DEM (modely 
reliéfu)`. V dialogovém okně nastavíme název a cestu ke vstupní
(:map:`dmt.tiff`) a výstupní  rastrové vrstvě (:map:`hillshade.tif`), zvolíme
režim :item:`Stínovaný reliéf`, předvolené možnosti režimu ponecháme, zaškrtneme
|checkbox| :sup:`Po dokončení načíst do mapového okna` a potvrdíme tlačítkem
:item:`OK`.

.. noteadvanced:: 

   V rámci možností režimu vytváření stínovaného reliéfu je možné nastavit
   hodnotu svislého převýšení, poměr svislých a vodorovných jednotek, azimut či
   nadmořskou výšku světla.

Po ukončení výpočtu se v panelu vrstev objeví nově vytvořený
stínovaný reliéf :map:`hillshade`. Abychom lépe viděli detaily, pomocí
|mActionZoomIn| :sup:`Přiblížit` si ohraničíme část území. Následně způsobem,
který byl popsaný výše nastavíme všeobecnou transparentnost rastrové vrstvy
:map:`hillshade` na hodnotu :item:`60%`. Dostaneme výsledek znázorněný na
:num:`#rsthillshade`.

.. _rsthillshade:

.. figure:: images/rst_hillshade.png
   :class: middle
   :scale-latex: 65
   
   Vytvoření prostorového efektu dat díky stínovanému reliéfu.

.. note::

   Rastrová vrstva stínovaného reliéfu je v menu :item:`Vrstvy` nad vrstvou
   :map:`dmt.tiff`. Je možné udělat i opačné pořadí vrstev - :map:`hillshade`
   ponechat jako podklad a nastavit transparentnost digitálního výškového modelu
   terénu. 

Sklon (*Slope*)
^^^^^^^^^^^^^^^

Jednou z užitečných informací o terénu je i sklon, který představuje maximální
změnu (gradient) výšky mezi sousedními buňky rastru. Rastrovou vrstvu sklonu
vygenerujeme obdobně jako stínovaný reliéf, pouze použijeme režim :item:`Sklon`. Na
:num:`#rstsklon` je znázorněný výsledek s barevnou paletou *BrBG*, přičemž je
použité  rozdělení do 10 stejných intervalů.

.. _rstsklon:

.. figure:: images/rst_sklon.png
   :class: middle

   Rastrová vrstva sklonu reliéfu.

Orientace vůči světovým stranám (*Aspect*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pro vytvoření mapy orientace svahu vůči světovým stranám použijeme režim
:item:`Aspekt` a postupujeme obdobně jako při předchozích analýzách.

.. _rstaspekt:

.. figure:: images/aspekt.png
   :class: middle

   Rastrová vrstva orientace svahu.

