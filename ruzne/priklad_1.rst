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

Ukázka jednoduchých prostorových funkcí
=======================================

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
   však lze dosáhnout stejného výsledku.

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
``EPSG:5514 - S-JTSK (Greenwich)/Krovak East North``, a to kliknutím na ikonku 
|srs| :sup:`Vyberte SRS`. Tento souřadnicový systém nastavíme i pro nové vrstvy
v položce ``SRS pro nové vrstvy`` a ``Použít výchozí SRS``. Na závěr povolíme 
|box_yes| ``"on-the-fly" SRS transformaci`` pro případ, že bychom v projektu
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
   :scale: 75
   
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

.. note:: Výraz nemusíme psát ručně. V středním poli dialogového okna kalkulačky
	  je množství položek. V našem případě vybereme 
          :menuselection:`Geometrie --> $area (dvojklik)`.

.. raw:: latex

   \newpage

.. _u-area:

.. figure:: images/u-hraniceCR-area.png
        
   Vytvoření atributu s výměrou České republiky.

Poté použijeme nástroj |intersect| :sup:`Průsečník`, kde vstupem budou vrstvy 
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
:num:`#vysledok-u1` (48,6 % území České republiky je ve vzdálenosti do 100 km od
hranic Prahy). 

.. _vysledok-u1:

.. figure:: images/u-vysledok-u1.png
   :scale-latex: 50
   
   Výpočet procentuálního zastoupení území ve vzdálenosti do 100 km od Prahy.
