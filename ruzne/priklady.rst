.. |srs| image:: ../images/icon/mActionSetProjection.png
   :width: 1.5em
.. |box_yes| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |box_no| image:: ../images/icon/checkbox_unchecked.png
   :width: 1.5em
.. |mIconVectorLayer| image:: ../images/icon/mIconVectorLayer.png
   :width: 1.5em
.. |mActionSelect| image:: ../images/icon/mActionSelect.png
   :width: 1.5em
.. |buffer| image:: ../images/icon/buffer.png
   :width: 1.5em
.. |dissolve| image:: ../images/icon/dissolve.png
   :width: 1.5em
.. |mIconSelectRemove| image:: ../images/icon/mIconSelectRemove.png
   :width: 1.5em
.. |mIconEditable| image:: ../images/icon/mIconEditable.png
   :width: 1.5em
.. |mActionDeleteAttribute| image:: ../images/icon/mActionDeleteAttribute.png
   :width: 1.5em
.. |mActionCalculateField| image:: ../images/icon/mActionCalculateField.png
   :width: 1.5em
.. |intersect| image:: ../images/icon/intersect.png
   :width: 1.5em
.. |mActionSaveEdits| image:: ../images/icon/mActionSaveEdits.png
   :width: 1.5em
.. |mIconExpressionSelect| image:: ../images/icon/mIconExpressionSelect.png
   :width: 1.5em
.. |union| image:: ../images/icon/union.png
   :width: 1.5em
.. |select_location| image:: ../images/icon/select_location.png
   :width: 1.5em
.. |mActionZoomToLayer| image:: ../images/icon/mActionZoomToLayer.png
   :width: 1.5em
.. |clipper| image:: ../images/icon/clip.png
   :width: 1.5em

Příklady GIS analýz
-------------------

Příklad 1
=========

Kolik procent území ČR je ve vzdálenosti do 100 km od hranice Hlavního města Prahy?

Data
^^^^

:map:`kraje.shp`

Řešení
^^^^^^

1. Nástrojem *Buffer* vytvoříme obalovou zónu 100 km kolem Prahy.
2. Nástrojem *Dissolve* sloučíme kraje a vytvoříme hranici ČR.
3. Vypočteme plochu ČR.
4. Nástrojem *Intersect* vytvoříme průnik obalové zóny s hranicí ČR.
5. Vypočteme plochu průniku a procenta vybrané plochy k původní ploše.

.. note:: Postup řešení v programu ArcGIS Desktop je dostupný `zde 
   <http://maps.fsv.cvut.cz/frvsgis/web.html>`_. S Open Source programem QGIS
   však lze dosáhnout stejný výsledek.

Postup v QGIS
^^^^^^^^^^^^^

Po spuštění programu QGIS se zobrazí standardní rozhraní, viz
:ref:`Popis rozhraní <popisrozhrani>`. Souřadnicový systém projektu je
přednastavený na WGS 84 (:epsg:`4236`), což lze zkontrolovat ve
stavovém řádku vpravo dole. Budeme pracovat s daty České republiky,
kde se obvykle používá souřadnicový systém S-JTSK (:epsg:`5514`).

V prvním kroku proto nastavíme souřadnicový systém projektu. Z menu lišty
vybereme :menuselection:`Nastavení --> Možnosti`. Otevře se dialogové okno, kde
v záložce :item:`SRS` nastavíme ``Vždy začít nové projekty s tímto SRS`` na
``EPSG:5514 - S-JTSK (Greenwich)/Křovak East North`` a to kliknutím na ikonku 
|srs| :sup:`Vyberte SRS`. Tento souřadnicový systém nastavíme i pro nové vrstvy
v položce ``SRS pro nové vrstvy`` a ``Použít výchozí SRS``. Na závěr povolíme 
|box_yes| ``"on-the-fly" SRS transformaci`` pro případ, že by jsme v projektu
pracovali s vrstvami v souřadnicovém systému, který je odlišný od systému
projektu. Postup je popsaný v kapitole :ref:`Souřadnicový systém<sour-system>`.
    
V dalším kroku kliknutím na |mIconVectorLayer| :sup:`Přidat vektorovou vrstvu`
do mapového okna přidáme vrstvu :map:`kraje.shp`. Tlačítkem |mActionSelect| 
:sup:`Vybrat prvky oblastí nebo jednoklikem` klikneme do mapy na místo, kde se
nachází kraj Hlavního města Prahy (:num:`#u-select-praha`).


.. note:: V případě, že by šlo o složitější výběr, použijeme 
	  |mIconExpressionSelect| :sup:`Vybrat prvky pomocí vzorce` a prvky 
	  vybereme atributovým dotazem.


.. _u-select-praha:

.. figure:: images/u-select-praha.png
   :class: middle
        
   Výběr území Prahy kliknutím do mapového okna.

Následně vytvoříme obalovou zónu 100 km od hranice Prahy. Použijeme prostorovou
analýzu |buffer| :sup:`Buffer`. Z menu lišty vybereme :menuselection:`Vektor 
--> Nástroje geoprocessingu --> Obalové zóny`. V dialogovém okně nastavíme
vstupní vrstvu, t.j. :map:`kraje`, zaklikneme |box_yes| :sup:`Použít pouze 
vybrané prvky`, protože chceme obalovou zónu jen kolem konkrétního vybraného
kraje. Míru aproximace zvýšíme na ``70``, protože předvolená hodnota ``5``
segmentů je málo na to, aby obalová zóna odpovídala kruhu. Dále nastavíme
velikost obalové zóny v metrech, název výstupního souboru a povolíme |box_yes| 
:sup:`Přidat výsledek do mapového okna` a potvrdíme  ``OK`` (:num:`#u-p100km`).  


.. note:: Maximální možný počet segmentů na aproximaci je ``99``. Výhodou je 
	  sice přesnější výsledek, nicméně výpočty budou trvat delší dobu.

.. _u-p100km:

.. figure:: images/u-p100km.png
   :class: small
      
   Tvorba obalové zóny velikosti 100 km kolem hranice Prahy.

Do mapového okna se přidá nová vektorová vrstva :map:`P100km`. Nastavíme jí styl
:menuselection:`pravým tlačítkem myši --> Vlastnosti --> Styl`, například jako
na :num:`#u-p100km-styl` transparentní výplň, červené ohraničení široké 1 mm.

.. _u-p100km-styl:

.. figure:: images/u-p100km-styl.png
   :class: middle
   
   Nastavení stylu obalové zóny.

Dále provedeme sjednocení všech krajů, resp. vrstvu České republiky. Budeme ji
potřebovat na určení plochy ČR. Využijeme nástroj geoprocessingu 
|dissolve| :sup:`Rozpustit`. 
Před touto funkcí ještě zrušíme výběr kraje Prahy pomocí |mIconSelectRemove| 
:sup:`Zrušit výber prvků ve všech vrstvách`. Výstupní vektorovou vrstvu
pojmenujeme :map:`hraniceCR`, viz :num:`#u-dissolve`.

.. _u-dissolve:

.. figure:: images/u-dissolve.png
   :class: small
   
   Spojení všech krajů do jednoho polygonu pomocí nástroje *Dissolve*.

Otevřeme atributovou tabulku vrstvy :map:`hraniceCR` (pravým ``Otevřít
atributovou tabulku``) a pak použijeme kalkulačku polí - ikona v horní
liště atributové tabulky |mActionCalculateField| :sup:`Otevřít
kalkulátor polí`.  Vytvoříme nový atribut (pole) s názvem
:dbcolumn:`area_sum` (desetinné číslo), do kterého vložíme hodnotu
plochy polygonu. Datový typ nastavíme tedy jako ``real``, šířka
např. ``15`` a jako výraz napíšeme ``$area`` (:num:`#u-area`).  Změny
uložíme ikonou |mActionSaveEdits| a editovací režim vypneme opětovným
stisknutím |mIconEditable|.

.. note:: Výraz nemusíme psát ručně. V středném poli dialogového okna kalkulačky
	  je množství položek. V našem případě vybereme 
          :menuselection:`Geometrie --> $area (dvojklik)`.

.. _u-area:

.. figure:: images/u-hraniceCR-area.png
        
   Vytvoření atributu s výměrou České republiky.

Pak použijeme nástroj |intersect| :sup:`Průsečník`, kde vstupem budou vrstvy 
:map:`hraniceCR` a :map:`P100km`. Výsledek je zobrazen na :num:`#intersect-map`.     

.. _intersect-map:

.. figure:: images/u_intersect-map.png
   :class: middle
        
   Výsledek nástroje *Intersect*, území České republiky ve vzdálenosti 100 km 
   od hranic Prahy.

Posledním krokem je určení procentuálního zastoupení plochy republiky do 100 km
od Prahy. Nejdřív vypočteme plochu průniku :map:`hraniceCR_intersect`, přičemž
postupujeme obdobně jako při ploše vrstvy :map:`hraniceCR` (vytvoříme sloupec s
názvem :dbcolumn:`area`). 

.. tip:: Kvůli přehlednosti vymažeme všechny nepotřebné sloupce v atributové
   tabulce vrstvy :map:`hraniceCR_intersect` tak, že nejdříve zapneme editovací
   mód kliknutím na |mIconEditable| :sup:`Prepnout režim editaci`, potom zvolíme
   |mActionDeleteAttribute| :sup:`Smazat sloupec` a označíme názvy těch
   atributů, které chceme vymazat. Ponecháme jenom pole :dbcolumn:`area_sum` a 
   :dbcolumn:`area`.

Pak přidáme nový atribut :dbcolumn:`procento`, do kterého pomocí mapové
kalkulačky vložíme výsledek ``"area"/"area_sum * 100"``.  Ten je na 
:num:`#vysledok-u1` (48,6% území České republiky je ve vzdálenosti do 100 km od
hranic Prahy). 

.. _vysledok-u1:

.. figure:: images/u-vysledok-u1.png
        
   Výpočet procentuálního zastoupení území ve vzdálenosti do 100 km od Prahy.

Příklad 2
=========

Najděte vhodné parcely na území Hlavního města Prahy pro výstavbu
nového stavebního objektu. Kvůli připadnému hluku musí být vzdálené
alespoň 500 m od železnic, jejich výměra musí být minimálně 20 ha a
měli by se nacházet mimo městské části Praha 6, 7 a Praha 8.

.. _data-ul2:

Data
^^^^
:map:`spravniobvody.shp, parcely.shp, zeleznice.shp`

.. _reseni-ul2:

Řešení
^^^^^^

1. Nástrojem *Dissolve* sloučíme správní obvody a vytvoříme polygonovou vrstvu Prahy.
2. Nástrojem *Clip* ořežeme vrstvu železnic podle polygonu Prahy.
3. Nástrojem *Buffer* vytvoříme obalovou zónu 500 m kolem pražských železnic.
4. Vybereme správní obvody Praha 6, 7 a 8 a nástrojem *Union* je sjednotíme s
   obalovou zónou kolem železnic (negativní oblasti).
5. Vybereme všechny parcely s rozlohou větší než 20 ha.
6. Z vybraných parcel vybereme ty, které nejsou v negativní oblasti.
7. Výsledek zobrazíme.   

Postup v QGIS
^^^^^^^^^^^^^

Do mapového okna pomocí |mIconVectorLayer| :sup:`Přidat vektorovou
vrstvu` přidáme potřebná :ref:`data <data-ul2>`. Vidíme, že vrstva
železnic je pro celou Českou republiku. Části mimo Prahy ale nebudeme
potřebovat, proto vrstvu ořežeme. Musíme si vytvořit hranici města. Z
menu :menuselection:`Vektor --> Nástroje geoprocessingu` vybereme
nástroj |dissolve| :sup:`Rozpustit`, kde jako vstupní vektorovou
vrstvu nastavíme :map:`spravniobvody`, pole rozpuštění na ``---
Rozpustit vše ---`` a výstup uložíme jako :map:`praha`.  Potom
použijeme nástroj na ořezání |clipper| :sup:`Ořezávač`. Vstupem bude
vektor železnic České republiky, ořezávat budeme podle nově vytvořené
polygonové vrstvy :map:`Praha` a výsledek uložíme jako
:map:`zeleznice_p`, teda železnice pouze na území Prahy. Dialogová okna
nástrojů *Dissolve* a *Clip* jsou zobrazeny na :num:`#dissolve-clip`. Následně
můžeme každé vrstvě :ref:`nastavit styl<styl-vrstvy>`, čím si vstupní
data přehledně zobrazíme (:num:`#vstup-ul2`).

.. _dissolve-clip:

.. figure:: images/u-dissolve-clip.png
   :class: middle

   Použití nástrojů *Dissolve* a *Clip*.

.. note:: Na :num:`#vstup-ul2` je pro vektorovou vrstvu :map:`parcely` nastavena
   jednoduchá průhledná výplň a šedé ohraničení s transparentností ``10%``, 
   symbol vrstvy :map:`zeleznice_p` je nastavený na ``Resident``, správní obvody
   jsou barevně kategorizované dle pole :dbcolumn:`nazev`, pričemž hodnoty tohto
   atributu jsou vykresleny.


.. _vstup-ul2:

.. figure:: images/u-vstup-ul2.png
   :class: middle
        
   Správní obvody, parcely a železnice Prahy.

.. tip:: V tomto kroku je dobré si projekt uložit, a to pomocí 
	 :menuselection:`Projekt --> Uložit`. 

Teď přistoupíme k tvorbě obalové zóny kolem pražských železnic, na to využijeme
nástroj |buffer| :sup:`Buffer`. V jednom dialogovém okně nastavíme vstup, míru
aproximace na ``70``,  velikost obalové zóny na ``500 m``, zaklikneme |box_yes| 
:sup:`Rozpustit výsledky obalové zóny`, aby byla obalová zóna celistvá a výstup
uložíme jako :map:`zeleznice_pb`, povolíme |box_yes| :sup:`Přidat výsledek do 
mapového okna` a spustíme ``OK``, viz. :num:`#zeleznice-buffer`.
 
.. _zeleznice-buffer:

.. figure:: images/u-zeleznice-buffer.png
   :class: small
   
   Obalová zóna 500 m kolem vektorové vrstvy pražských železnic.

Pokračujeme výběrem správních obvodů, kde se parcela pro nový stavební
objekt nemá nacházet. V okně vrstev označíme vektor
:map:`spravniobvody` a v menu klikneme na |mIconExpressionSelect|
:sup:`Vybrat prvky pomocí vzorce`.  V střední části dialogového okna
najdeme položku ``Pole a hodnoty``, dvouklikem zvolíme ``nazev``, v
pravé části klikneme na ``všechny jedinečné hodnoty`` a tímto způsobem
napíšeme do levého okna výraz (:num:`#vyraz678`), kterým z vrstvy
správních obvodů vybereme Prahu 6, 7 a 8.

.. code-block:: sql

   "nazev" = 'Praha 6' OR "nazev" = 'Praha 7' OR "nazev" = 'Praha 8'

Pak přes pravé tlačítko myši nad vrstvou :map:`spravniobvody` výběr
uložíme pomocí `Uložit jako`, nazveme jej :map:`praha_neg`. Dbáme na
to, aby políčko |box_no| :sup:`Uložit pouze vybrané prvky` bylo
zaškrtnuté |box_yes| a zkontrolujeme i souřadnicový systém
:epsg:`5514`.


.. note:: Operátor ``OR`` se nachází v položce ``Operátory``.

.. _vyraz678:

.. figure:: images/u-vyraz678.png
   :class: middle
   
   Výběr správních obvodů, kde budeme hledat vhodné parcely.

.. note:: Po exportu zrušíme vybrané obvody Prahy pomocí |mIconSelectRemove| 
	  :sup:`Zrušit výběr prvků ve všech vrstvách`.

Následuje spojení "negativních" zón. Cílem je dostat vektorovou vrstvu, která je
sjednocením obalové zóny železnic a nepožadovaných správních obvodů. Využijeme
nástroj |union| :sup:`Sjednotit`. Vznikne výstup (například 
:map:`oblasti_neg1`), na který opět použijeme  |dissolve| :sup:`Rozpustit`.
Výsledek pojmenujeme :map:`oblasti_neg` (:num:`#neg`).

.. _neg:

.. figure:: images/u-neg.png
   :class: large
        
   Sjednocení negativních oblastí :fignote:`(1)`, spojení do souvislého 
   vektoru :fignote:`(2)` a zobrazení v mapovém okně :fignote:`(3)`.

Pak pokračujeme krokem č. 5, viz :ref:`Řešení<reseni-ul2>`. Postup je obdobný
jako při výběru správních obvodů pomocí |mIconExpressionSelect| 
:sup:`Vybrat prvky pomocí vzorce`. Výraz ``"vymeraparc" > 200000`` je ten,
kterým vybereme parcely  s výměrou nad 20 ha (:num:`#parcely20ha`). Vybrané
prvky uložíme jako nový vektor :map:`parcely_20ha` a výběr zrušíme ikonkou 
|mIconSelectRemove|.
  

.. _parcely20ha:

.. figure:: images/u-parcely20ha.png
        
   Výběr parcel s výměrou nad 20 hektarů.

Z těchto parcel je potřebné vybrat ty, které nejsou v negativní oblasti.
Nejdříve označíme všechny prvky vrstvy :map:`parcely_25ha`, například vybereme
všechny ``gml_id`` pomocí |mIconExpressionSelect| 
:sup:`Vybrat prvky pomocí vzorce`. Následně z hlavní lišty spustíme dialogové
okno |select_location| :sup:`Vybrat podle umíštění`. Najdeme jej v položce 
:menuselection:`Vektor --> Výzkumné nástroje`. Zaškrtneme |box_yes| 
:sup:`Include input features that intersect the selection features`, |box_yes| 
:sup:`Zahrnout vstupní prvky, které překrývají/protínají prvky výběru` a jelikož
chceme právě ty parcely, které zadané podmínky nesplňují, zvolíme možnost 
``odstraněním z aktuálneho výběru`` (:num:`#vybrat-umisteni`).
  

.. _vybrat-umisteni:

.. figure:: images/u-vybrat-umisteni.png
        
   Výběr parcel podle umístění metodou odstranění z aktuálního výběru.

Výsledek (podmnožina :map:`parcely_20ha`) uložíme pomocí ``Uložit jako``, a
zobrazíme na podkladě původního zájmového území (:num:`#vysledok-ul2`).
Pro lepší detail použijeme |mActionZoomToLayer| :sup:`Přiblížit na vrstvu`. 

.. note:: Pro zvýraznění výsledku je průhlednost vrstvy správních celků 
	  nastavena na ``70`` 
	  (:menuselection:`Vlastnosti --> Styl --> Průhlednost vrstvy`).

.. _vysledok-ul2:

.. figure:: images/u-vysledok-u2.png
   :class: middle
        
   Vhodné parcely pro výstavbu nového stavebního objektu.
