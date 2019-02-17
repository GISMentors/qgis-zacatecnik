.. |mActionFullHistogramStretch| image:: 
   ../images/icon/mActionFullHistogramStretch.png
   :width: 1.5em
.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |CRS| image:: ../images/icon/CRS.png
   :width: 1.5em
.. |mActionLocalCumulativeCutStretch| image:: 
   ../images/icon/mActionLocalCumulativeCutStretch.png
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

Vlastnosti rastrové vrstvy
--------------------------

Dialog pro nastavení vlastností dané rastrové vrstvy vyvoláme buď
levým dvouklikem nad danou vrstvou, nebo pravým klikem z kontextového
menu zvolíme položku :item:`Vlastnosti`.

Dialogové okno obsahuje šest záložek : *Všeobecné*, *Styl*,
*Průhlednost*, *Pyramidy*, *Histogram* a *Metadata*.


Informace
^^^^^^^^^
Tato záložka by měla poskytovat informace o dané rastrové vrstvě. Jedná se
zejména o technické parametry dat - počet sloupců a řádků, rozsah, způsob
uložení hodnot, místo uložení, souřadnicový systém, velikost pixelu,
počet pásem a jejich statistiky. 
Metadata popisující obsah, poskytovatele a další infromace jsou v samostatné
záložce :item:`Metadata`. 


Zdroj
^^^^^

První záložka poskytuje základní informace o vrstvě jako je název souboru, název
vrstvy v legendě s možností editace a
souřadnicový referenční systém (ten je možno nastavit kliknutím na tlačítko
|CRS| :sup:`Vyberte SRS`). 

V této záložce je možné nastavit i viditelnost v
závislosti na měřítku (:numref:`obecneraster`).

.. _obecneraster:

.. figure:: images/obecne_raster.png
   :scale-latex: 60
   
   Vlastnosti rastrové vrstvy.

Symbologie
^^^^^^^^^^

Tato záložka slouží na nastavení barevnosti rastrových dat v mapovém okně. Je
možné nastavit vykreslování pásma, barvy nebo převzorkování. V dané vrstvě mohou
být barvy invertované, dá se vylepšit kontrast, sytost, jas, rozsah
vykreslovaných hodnot (:numref:`stylraster`).

.. _stylraster:

.. figure:: images/styl_raster.png
   :class: large
   :scale-latex: 75
       
   Různé styly té samé rastrové vrstvy: šedé pásmo (vlevo), pseudobarvy (vpravo).
    
.. note:: 

   Nastavení hodnoty směrodatné odchylky dokáže zabezpečit, aby hodnoty, které
   se příliš liší od průměru pro vrstvu, nebyly zobrazené.     
  
.. noteadvanced:: 

   Další možnosti stylování nabízí lišta :item:`Rastr`, která se zapíná přes
   :menuselection:`Zobrazit --> Nástrojové lišty --> Rastr`. Například první
   položka zleva |mActionLocalCumulativeCutStretch| :sup:`Local Cumulative Cut
   Stretch` automaticky vylepší kontrast na základě minimální a maximální
   hodnoty buňky v aktuální lokální části rastru, přičemž bere do úvahy výchozí
   limity a odhadnuté hodnoty. Výsledek je na :numref:`stylrstpanel` vlevo. Volba
   |mActionFullHistogramStretch| :sup:`Roztáhnout histogram na celý dataset`
   nástrojové lišty vrátí změny zpět jak byly na :numref:`stylraster`, t.j. vyrovná
   kontrast vzhledem na celý rastr dle skutečných hodnot. Pokud pravým
   kliknutím na název vrstvy zvolíme z kontextového menu :item:`Zoom na
   nejvhodnější měřítko (100%)`, klikneme na |mActionLocalCumulativeCutStretch|
   :sup:`Local Cumulative Cut Stretch` a zvolíme |mIconZoom| :sup:`Přiblížit na
   vrstvu`, čímž vytvoříme styl znázorněný na :numref:`stylrstpanel` vpravo. 

   .. _stylrstpanel:

   .. figure:: images/styl_rst_panel.png
      :class: middle
      :scale-latex: 60

      Změna stylu rastrové vrstvy pomocí nástrojové lišty :item:`Rastr`.
      
Pokud potřebujeme používat opakovaně stejné nastavení symbologie, nebo jen
poskytnout nastavení i jiným uživatelům, tak je možné styl uložit stejným
způsobem jako u vektorových dat. Ve spodní části záložky :item:`Symbologie`
se nachází talčítko :item:`Styl`. Zde se nachází jak možnost uložit aktulání
styl do souboru, tak možnost načíst styl ze souboru a nastavit ho tak danému
rastru. Styly se ukládají v souboru s přídponou :file:`.qml`.
Tento soubor je v podstatě :file:`.xml` soubor, takže je možné ho případně
editovat podle potřeb.

.. figure:: images/save_style.png
   :class: small
 

Průhlednost
^^^^^^^^^^^

QGIS umožňuje zobrazovat každou vrstvu v mapovém okně s různým stupněm
průhlednosti. To je velmi výhodné, pokud například chceme, aby kromě aktuální
rastrové vrstvy byla viditelná i jiná vrstva. Typickým příkladem je překryv
stínovaného reliéfu jakoukoli barevnou rastrovou vrstvou. Překryv a vhodné
nastavení průhlednosti způsobí prostorový vzhled 2D vrstvy. Konkrétní příklad je
uveden později. 

Záložka umožňuje nastavit všeobecnou průhlednost, ale taktéž průhlednost pro
každý pixel. V části o uživatelských nastaveních transparentnosti (viz
:numref:`rsttransparency` s paletovým typem vykreslení pásma pro rastr) je možné
nastavit hodnoty pomocí tlačítek |symbologyAdd| :sup:`Zadat hodnoty ručně` nebo
|mActionContextHelp| :sup:`Přidat hodnoty z obrazovky`, dále možno
|symbologyRemove| :sup:`Odstranit vybrané řádky`, hodnoty |mActionFileOpen|
:sup:`Importovat z` nebo |mActionFileSave| :sup:`Exportovat do` souboru. To má
smysl hlavně u detailnějších, časově náročných prací. Tato záložka umožňuje
taky nastavení *no data* hodnoty (tzv. žádná data). 

.. _rsttransparency:

.. figure:: images/rst_transparency.png
   :class: middle
   :scale-latex: 65

   Možnosti nastavení průhlednosti rastrové vrstvy.

Některé rastry můžou obsahovat samostatný kanál, ve kterém je zapsán předpis pro průhlednost jednotlivých buněk. Pokud takovýto kanál data obsahují, tak je možné nastavit průhlednost přímo pomocí nastavení tohoto kanálu. 

Histogram
^^^^^^^^^
QGIS nabízí nástroj pro generování histogramu rastrové vrstvy
(:numref:`rsthistogram`). Je vytvořen automaticky po kliknutí na volbu
:item:`Vypočítat histogram`.

.. _rsthistogram:

.. figure:: images/rst_histogram.png
   :class: middle

   Výpočet histogramu rastrové vrstvy digitálního výškového modelu terénu.

Vykreslování
^^^^^^^^^^^^

U některých vrstev, rastrových i vektorových, se může stát, že jejich
vykreslování v mapovém okně má smysl pouze v rozmezí určitých měřítek.
Toto nastavení je možné provést v záložce :item:`Vykreslování`. 
Typickým příkladem může být rastrové vykreslení druhů pozemků v kontextu
celé republiky

Toto nastavení se často používá při WMS.

.. figure:: images/scale_visibility.png
   :class: middle

   Nastavení měřítkového rozsahu ve které se vrstva bude vykreslovat.


Pyramidy
^^^^^^^^

Pyramidy jsou datové struktury, které typicky obsahují menší množství dat.
Cílem je snížit výpočetní náročnost při práci s daty. Podstatou je, že se kromě
původního rastru v plném rozlišení vytvoří zjednodušená verze (kopie s nižším
rozlišením pro konkrétní přiblížení). Na převzorkování se použijí různé metody, 
nejčastěji jde o metodu průměru (*Average*) nebo metodu nejbližšího souseda 
(*Nearest Neighbour*).

.. figure:: images/pyramids.png
   :class: small

   Schéma vzniku pyramid jako zjednodušených náhledových vrstev.

.. note::

   Pro vytvoření pyramid musíte mít právo zápisu do adresáře s
   původními daty.

.. important::

   Je potřebné vědět, že vytvoření pyramid může pozměnit originální rastr, a
   proto se doporučuje vytvoření zálohy původní bezpyramidové verze dat.


Metadata
^^^^^^^^

Zde je možné  číst a editovat metadatové údaje o vrstvě. Uvádění těchto 
definic je nutné zejména v případě, že se jedná o oficiálně poskytovaná data
a je dobré u nich uvádět detaily o poskytovateli, jako i o datech samotných. 

.. figure:: images/raster_metadata.png
   :class: middle

   Metadatové položky u rastrové vrstvy.   


