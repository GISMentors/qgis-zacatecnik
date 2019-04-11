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

- pomocí tlačítka |mActionSelectedToTop| :sup:`Přesunout výběr nahoru`
lze zobrazit vybrané prvky na prvním místě tabulky, což nám vybraná
data zpřehlední.

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

.. tip:: Pomocí nabídky |mActionFilter2| v levém dolním rohu lze zvolit filtr 
   zobrazených prvků. Ve výchozím nastavení filtr zobrazuje všechny 
   prvky ve vrstvě, tedy hodnota: |mActionFilter2| :item:`Zobrazit všechny 
   prvky`

   Pomocí funkce |mActionConditionalFormatting| :sup:`Pravidla`
   podmíněného formátování` lze pole v atributové tabulce  stylizovat na 
   podle námi definovaných pravidel


Vlastnosti
----------

Vlastnosti vyvoláme dvojklikem na vrstvu nebo pravým tlačítkem myši
kontextové menu a zvolíme :item:`Vlastnosti`.

Informace
^^^^^^^^^

Jako první vidíme ve vlastnostech vrstvy záložku informace. Zde najdeme
základní popis zdrojových dat - cesta k souboru, kódování, souřadnicový systém,
ale i počet prvků a seznam atributů

.. figure:: images/info.png

    Informace vektorové vrstvy.

Zdroj
^^^^^

Zde nalezneme základní nastavení ke zdroji vrstvy -
název vrstvy, kódování textu, souřadnicový systém (SRS) a
nastavení filtru.

.. figure:: images/properties.png

    Zdroj vektorové vrstvy.

.. _styl-vrstvy:

Styl
^^^^

|symbology| Symbologie
**********************

Pomocí rolovací nabídky |selectstring| vybereme typ symbologie:

- |rendererSingleSymbol|:sup:`Jednoduchý symbol` - zde máme na výběr z
  uložených symbolů. V levém sloupci máme zobrazený typ symbolu a jeho
  jednotlivé části. Při kliknutí na konkrétní složku symbolu můžeme měnit
  její vlastnosti (barvy, typ výplně, šířka ohraničení atd.).

.. figure:: images/symbol_simple.png

    Jednoduchá symbologie. V levé části vlastnosti označené
    složky symbolu.

.. tip:: Pomocí tlačítek můžeme další složky symbolu přidávat 
         |symbologyAdd|, odebírat |symbologyRemove|, zamykat |locked| nebo 
         měnit jejich pořadí |mActionArrowUp|, |mActionArrowDown|. Tímto způsobem 
         si můžeme vytvořit vlastní symbologii.

- |rendererCategorizedSymbol|:sup:`Kategorizovaný` - vhodný pro kategoriální
  proměnné

    - :guilabel:`sloupec` - pro výběr atributu
    - :guilabel:`barevný rozsah` - výběr barev
    - pro vytvoření kategorii kliknout na :guilabel:`klasifikovat`

.. figure:: images/symbol_kat.png
   :scale-latex: 60

   Kategorizovaná symbologie.

- |rendererGraduatedSymbol|:sup:`Odstupňovaný` - vhodný pro spojité proměnné

    - nastavení obdobné jako u možnosti
      |rendererCategorizedSymbol|:sup:`Kategorizovaný`
    - možnost režimu intervalů a počet tříd
    - možnost zobrazení histogramu

.. figure:: images/symbol_odst.png
   :scale-latex: 60

   Odstupňovaná symbologie.
    
|mActionLabeling| Popisky
*************************

Kromě rozlišení prvků pomocí symbologie lze také přidat k jednotlivým
prvkům popisek na základě jednoho z atributů.

.. figure:: images/labels.png
   :scale-latex: 60

   Vlastnosti popisků vrstvy.

Na této záložce je nejdříve nutné vybrat z rolovací nabídky |selectstring| 
položku |mActionLabeling|:sup:`Single labels`. Tím se nám otevřou 
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

Pro pohodlnější práci se stylováním, slouží panel stylování :item:`Stylování vrstvy`, který lze aktivovat pravým kliknutím na prázdné místo v hlavním panelu a výběrem z nabídky nebo mocí klávesové zkratky :item:`F7`. Výhodou panelu stylování je, že  lze rychle, bez znovuotevírání okna, přepínat mezi vrstvyami,veškeré provedené změny v symbologii se vykreslí ihned, a také je zde možnost kroku zpět na předchozí symbologii, nebo přímo procházení historie všech změn.

.. figure:: images/styl_panel.png 
   :class: small 
   :scale-latex: 40 

   Panel stylování

.. tip:: V rámci vrstvy lze vytvořit různé "verze" nastylování, které 
        můžeme podle potřeby měnit. Tato funkce může být užitečná 
        např. při vytváření mapových výstupů jednoho zdroje dat s různou 
        symbologií. Styly lze ovládat (přídání, smazání, přejmenování, 
        zvolení, export) pomocí tlačítka ve spodní části okna vlastností, 
        nebo z kontextového menu vrstvy (pravý klik na vrstvu v panelu 
        vrstev), zde je přepínání jednotlivých stylů rychlejší. V panelu 
        stylování se styly ovládají v samostatné záložce
        stylepreset|:sup:`Správce stylů`.

	.. figure:: images/styl_kat.png 
	   :class: middle 
	   :scale-latex: 40 

	   Výběr stylu pomocí kontextového menu z panelu vrstev

	.. figure:: images/styl_kont.png 
	   :class: middle 
	   :scale-latex: 40 

	   Výběr stylu pomocí kontextového menu z panelu vrstev

..  Metadata
    ^^^^^^^^

    V záložce :item:`Metadata` je možné získat základní metadata vektorové vrstvy.

    .. figure:: images/vector_metadata.png
       :scale-latex: 65

       Příklad výpisu metadat vrstvy ve formátu ESRI shapefile.

    .. figure:: images/postgis_metadata.png
       :scale-latex: 65

       Příklad výpisu metadat vrstvy ve formátu PostGIS.

