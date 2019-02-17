.. |symbology image:: ../images/icon/symbology.png
   :width: 2em
.. |selectstring| image:: ../images/icon/selectstring.png
   :width: 2.5em
.. |symbologyAdd| image:: ../images/icon/symbologyAdd.png
   :width: 1.5em
.. |symbologyRemove| image:: ../images/icon/symbologyRemove.png
   :width: 1.5em
.. |mActionOpenTable| image:: ../images/icon/mActionOpenTable.png
   :width: 1.5em
.. |mIconExpressionSelect| image:: ../images/icon/mIconExpressionSelect.png
    :width: 1.5em
.. |mActionUnselectAttributes| image:: ../images/icon/mActionUnselectAttributes.png
    :width: 1.5em
.. |mActionInvertSelection| image:: ../images/icon/mActionInvertSelection.png
   :width: 1.5em
.. |mActionSelectAll| image:: ../images/icon/mActionSelectAll.png
   :width: 1.5em
.. |mActionSelectedToTop| image:: ../images/icon/mActionSelectedToTop.png
   :width: 1.5em
.. |symbologyUp| image:: ../images/icon/symbologyUp.png
   :width: 1.5em
.. |symbologyDown| image:: ../images/icon/symbologyDown.png
   :width: 1.5em
.. |locked| image:: ../images/icon/locked.png
   :width: 1.5em
.. |mActionFilterMap| image:: ../images/icon/mActionFilterMap.png
   :width: 1.5em
.. |mIconExpression| image:: ../images/icon/mIconExpression.png
   :width: 1.5em
.. |mActionConditionalFormatting| image:: ../images/icon/mActionConditionalFormatting.png
   :width: 1.5em
.. |mDockify| image:: ../images/icon/mDockify.png
   :width: 1.5em
.. |mActionPanToSelected| image:: ../images/icon/mActionPanToSelected.png
   :width: 1.5em
.. |mActionZoomToSelected| image:: ../images/icon/mActionZoomToSelected.png
   :width: 1.5em



Vlastnosti vrstvy
=================
Atributová tabulka
------------------

Vektorová data se skládájí ze dvou základních složek -- geometrie (body,
linie, polygony) a informací o jednotlivých prvcích tzv. atributů.

Atributovou tabulku otevřeme pomocí ikony |mActionOpenTable| :sup:`Otevřít
atributovou tabulku` nebo pravým kliknutím vyvoláme kontextové menu
a zvolíme :item:`Otevřít atributovou tabulku`. Tabulka slouží
k prohlížení a editaci atributové složky dat. V názvu okna je vypsaný název
vrstvy, celkový počet prvků (`Features total`), počet odfiltrovaných prvků
(`filtered`) a počet prvků ve výběru (`selected`).

.. figure:: images/at_table.png
   :scale-latex: 60

   Atributová tabulka vrstvy.

**Zákaldní funkce attributové tabulky**

- kliknutím na název pole, lze hodnoty seřadit.

- kliknutím na číslo řádku můžeme označit jednotlivé prvky do výběru

- pomocí tlačítka |mActionSelectedToTop| :sup:`Přesunout výběr 
nahoru` lze zobrazit vybrané prvky na prvním místě tabulky, což nám 
vybraná data zpřehlední.

- lze použít funkce výběru, které jsou dostupné i v hlavním okně:

    - |mIconExpressionSelect| :sup:`Vybrat prvky pomocí vzorce`
    - |mActionSelectAll| :sup:`Vybrat prvky pomocí vzorce`
    - |mActionUnselectAttributes|:sup:`Zrušit výběr ve všech vrstvách` 
    - |mActionInvertSelection| :sup:`Převrátit výběr prvků`
    - |mActionZoomToSelected| :sup:`Přiblížit na výběr`
    - |mActionPanToSelected| :sup:`Posunout mapu na výběr`


Okno atributové tabulky lze otevírat ve dvou režimech buď v samostatném okně,
nebo jako panel. Přepínat tyto režimy lze pomocí funkce
|mDockify|:sup:`Dock Attribute Panel`.

.. tip:: Pomocí nabídky |mActionFilterMap| v levém dolním rohu lze zvolit filtr 
   zobrazených prvků. Ve výchozím nastavení filtr zobrazuje všechny 
   prvky ve vrstvě, tedy hodnota: |mActionFilterMap| :item:`Zobrazit všechny 
   prvky`

   Pomocí funkce |mActionConditionalFormatting| :sup:`Pravidla 
   podmíněného formátování` lze pole v atributové tabulce  stylizovat na 
   podle námi definovaných pravidel


Vlastnosti
----------

Vlastnosti vyvoláme dvojklikem na vrstvu nebo pravým tlačítkem myši
kontextové menu a zvolíme :item:`Vlastnosti`.

Obecné
^^^^^^

V první záložce nalezneme základní informace o nahrané vrstvě jako
název vrstvy, zdroj, kódování znaků, souřadnicový systém (SRS) a
další.

.. figure:: images/properties.png

    Vlastnosti vektorové vrstvy.

.. _styl-vrstvy:

Styl
^^^^

Styl (symbologie)
*****************
Pomocí rolovací nabídky |selectstring| vybereme typ symbologie:

- :guilabel:`jednoduchý symbol` - zde máme na výběr z uložených
  symbolů. V levém sloupci máme zobrazený typ symbolu a jeho jednotlivé
  části. Při kliknutí na konkrétní složku symbolu můžeme měnit
  její vlastnosti (Barvy, Typ výplně, Šířka ohraničení atd.).


.. figure:: images/symbol_simple.png

    Jednoduchá symbologie. V levé části vlastnosti označené
    složky symbolu.

.. tip:: Pomocí tlačítek můžeme další složky symbolu přidávat 
         |symbologyAdd|, odebírat |symbologyRemove|, zamykat |locked| nebo 
         měnit jejich pořadí |symbologyUp|, |symbologyDown|. Tímto způsobem 
         si můžeme vytvořit vlastní symbologii.

- :guilabel:`kategorizovaný` - vhodný pro kategoriální proměnné

    - :guilabel:`sloupec` - pro výběr atributu
    - :guilabel:`barevný rozsah` - výběr barev
    - pro vytvoření kategorii kliknout na :guilabel:`klasifikovat`

.. figure:: images/symbol_kat.png
   :scale-latex: 60

   Kategorizovaná symbologie.

- :guilabel:`odstupňovaný` - vhodný pro spojité proměnné

    - nastavení obdobné jako u možnosti :guilabel:`kategorizovaný`
    - možnost režimu intervalů a počet tříd

.. figure:: images/symbol_odst.png
   :scale-latex: 60

   Odstupňovaná symbologie.
    
Popisky
*******

Kromě rozlišení prvků pomocí symbologie lze také přidat k jednotlivým
prvkům popisek na základě jednoho z atributů.

.. figure:: images/labels.png
   :scale-latex: 60

   Vlastnosti popisků vrstvy.

Na této záložce je nejdříve nutné vybrat z rolovací nabídky |selectstring| 
polužku  :guilabel:`Zobrazit popisky pro tuto vrstvu`. Tím se nám otevřou 
možnosti stylizace popisků, kde můžeme nastavit formát textu, obalovou zónu 
kolem textu, pozadí, stínování, možnosti umístění a vykreslování. Nejdříve je 
ale nutné nastavit zdroj popisku. Pomocí rolovací nabídky :guilabel:`Popisky z` 
vybreme zdrojový atribut popisku.

.. figure:: images/labels_sample.png
   :scale-latex: 47

   Příklad popisků s použitím obalové zóny textu.

.. noteadvanced:: Jako zdroj popisků lze použít i vzorec, a to buď
    přímým vepsáním do nabídky, nebo vytvořením vzorce pomocí kalkulátoru 
    |mIconExpression|.

Práce se styly
**************

Pro pohodlnější práci se stylováním, slouží panel stylování :item:`Layer styling`, který lze aktivovat pravým kliknutím na prázdné místo v hlavním panelu a výběrem z nabídky nebo mocí klávesové zkratky :item:`F7`. Výhodou panelu stylování je, že  lze rychle, bez znovuotevírání okna, přepínat mezi vrstvyami,veškeré provedené změny v symbologii se vykreslí ihned, a také je zde možnost kroku zpět na předchozí symbologii, nebo přímo procházení historie všech změn.

.. figure:: images/styl_panel.png 
   :class: small 
   :scale-latex: 40 

   Panel stylování

.. noteadvanced:: V rámci vrstvy lze vytvořit různé "verze" nastylování,
	které můžeme podle potřeby měnit. Tato funkce může být užitečná 
	např. při vytváření mapových výstupů jednoho zdroje dat s různou 
	symbologií. Styly lze ovládat (přídání, smazání, přejmenování, 
	zvolení, export) pomocí tlačítka ve spodní části okna vlastností, 
	nebo z kontextového menu vrstvy (pravý klik na vrstvu v panelu 
	vrstev), zde je přepínání jednotlivých stylů rychlejší. V panelu 
	stylování se styly ovládají v samostatné záložce :guilabel:`Správce 
	stylů`.

	.. figure:: images/styl_kat.png 
	   :class: middle 
	   :scale-latex: 40 

	   Výběr stylu pomocí kontextového menu z panelu vrstev

	.. figure:: images/styl_kont.png 
	   :class: middle 
	   :scale-latex: 40 

	   Výběr stylu pomocí kontextového menu z panelu vrstev

Metadata
^^^^^^^^

V záložce :item:`Metadata` je možné získat základní metadata vektorové vrstvy.

.. figure:: images/vector_metadata.png
   :scale-latex: 65

   Příklad výpisu metadat vrstvy ve formátu ESRI shapefile.

.. figure:: images/postgis_metadata.png
   :scale-latex: 65

   Příklad výpisu metadat vrstvy ve formátu PostGIS.
   
