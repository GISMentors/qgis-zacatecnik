Vlastnosti vrstvy
=================

Atributová tabulka
------------------

Vektorová data se skládájí ze dvou základních složek -- geometrie (body,
linie, polygony) a informací o jednotlivých prvcích tzv. atributů.

Atributovou tabulku otevřeme pomocí ikony |mActionOpenTable| :sup:`Otevřít
atributovou tabulku` (klávesová zkratka :kbd:`F6`), nebo pravým kliknutím 
vyvoláme kontextové menu a zvolíme :item:`Otevřít atributovou tabulku`. 
Tabulka slouží k prohlížení a editaci atributové složky dat. V názvu 
okna je vypsaný název vrstvy, celkový počet prvků (`Features total`), 
počet odfiltrovaných prvků (`filtered`) a počet prvků ve výběru 
(`selected`).

.. figure:: images/at_table.png
   :scale-latex: 60

   Atributová tabulka vrstvy.

Okno atributové tabulky lze otevírat ve dvou režimech, a to buď v 
samostatném okně, nebo jako panel. Přepínat tyto režimy lze  v liště 
atributové tabulky pomocí funkce|mDockify|:sup:`Atributová tabulka jako panel`. 
Výchozí chování lze nastavit v hlavním nastavení QGISu
(:menuselection:`Nastavení -> Nastavení...` záložka :item:`Zdroje dat`).

V okně atributové tabulky můžeme zobrazit jak atributovou tabulku (výchozí),
tak i formulář atributů. Tato zobrazení se přepínají pomocí tlačítek v pravém dolním rohu: |attributes|:sup:`Přepnout na zobrazení tabulky` a |mActionFormView|:sup:`Přepnout na zobrazení formuláře`.

**Základní funkce atributové tabulky**

- kliknutím na název pole, lze hodnoty seřadit.

- kliknutím na číslo řádku můžeme označit jednotlivé prvky do výběru

- pomocí tlačítka |mActionSelectedToTop| :sup:`Přesunout výběr nahoru`
  lze zobrazit vybrané prvky na prvním místě tabulky, což nám vybraná
  data zpřehlední.

- lze použít funkce výběru, které jsou dostupné i v hlavním okně:

    - |mIconExpressionSelect| :sup:`Vybrat prvky pomocí vzorce`
    - |mActionSelectAll| :sup:`Vybrat prvky pomocí vzorce`
    - |mActionInvertSelection| :sup:`Převrátit výběr prvků`
    - |mActionUnselectAttributes|:sup:`Zrušit výběr ve všech vrstvách` 
    - |mActionPanToSelected| :sup:`Posunout mapu na výběr`
    - |mActionZoomToSelected| :sup:`Přiblížit na výběr`

- tlačítko |mActionFilter2|:sup:`Vybrat/filtrovat prvky pomocí formuláře (Ctrl+F)` umožňuje vytvářet výběr nebo fltrovat prvky za pomocí formuláře (viz :ref:`vybrat-prvky` ). Pro návrat do atributové tabulky stiskněte tlačítko |attributes|:sup:`Přepnout na zobrazení tabulky`.

- pomocí tlačítka |organiseColumns|:sup:`Uspořádat sloupce tabulky` lze 
  měnit pořadí sloupců, nebo jednotlivé sloupce skrýt.

.. figure:: images/at_table_sort.png
   :scale-latex: 60

   Možnost uspořádání sloupců.


.. tip:: Pomocí nabídky |mActionFilter2| v levém dolním rohu lze zvolit filtr 
   zobrazených prvků. Ve výchozím nastavení filtr zobrazuje všechny 
   prvky ve vrstvě, tedy hodnota: |mActionFilter2| :item:`Zobrazit všechny 
   prvky`

   Pomocí funkce |mActionConditionalFormatting| :sup:`Pravidla`
   podmíněného formátování lze pole v atributové tabulce  stylizovat na 
   podle námi definovaných pravidel



Vlastnosti
----------

Vlastnosti vyvoláme dvojklikem na vrstvu nebo pravým tlačítkem myši
kontextové menu a zvolíme :item:`Vlastnosti`.

.. _vektor-informace:

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



..  Metadata
    ^^^^^^^^

    V záložce :item:`Metadata` je možné získat základní metadata vektorové vrstvy.

    .. figure:: images/vector_metadata.png
       :scale-latex: 65

       Příklad výpisu metadat vrstvy ve formátu ESRI shapefile.

    .. figure:: images/postgis_metadata.png
       :scale-latex: 65

       Příklad výpisu metadat vrstvy ve formátu PostGIS.


Panel stylování
---------------

Pro pohodlnější práci se stylováním, slouží panel stylování 
:item:`Stylování vrstvy`, který lze aktivovat pravým kliknutím na 
prázdné místo v hlavním panelu a výběrem z nabídky nebo mocí klávesové 
zkratky :item:`F7`. Výhodou panelu stylování je, že  lze rychle, bez 
znovuotevírání okna, přepínat mezi vrstvyami,veškeré provedené změny v 
symbologii se vykreslí ihned, a také je zde možnost kroku zpět na 
předchozí symbologii, nebo přímo procházení historie všech změn.

.. figure:: images/styl_panel.png 
   :class: small 
   :scale-latex: 40 

   Panel stylování


Práce se styly
--------------


Více stylů u vrstvy
^^^^^^^^^^^^^^^^^^^

V rámci projektu lze vytvořit různé "verze" nastylování u konkrétní 
vrstvy. Takto přednastavený styl můžeme potom podle potřeby měnit. Tato 
funkce může být užitečná např. při vytváření mapových výstupů 
jednoho zdroje dat s různou symbologií. Styly lze ovládat 
(přídání, smazání, přejmenování, zvolení, export) pomocí 
tlačítka ve spodní části okna vlastností, nebo z kontextového 
menu vrstvy (pravý klik na vrstvu v panelu vrstev), zde je 
přepínání jednotlivých stylů rychlejší. V panelu stylování se 
styly ovládají v samostatné záložce |stylepreset|:sup:`Správce 
stylů`.

.. figure:: images/styl_kat.png 
   :class: middle 
   :scale-latex: 40 

   Výběr stylu pomocí kontextového menu z panelu vrstev

.. figure:: images/styl_kont.png 
   :class: middle 
   :scale-latex: 40 

   Výběr stylu pomocí kontextového menu z panelu vrstev

..  Kopírování stylů
    ^^^^^^^^^^^^^^^^


Uložení a načtení nastavení vrstvy pomocí souboru
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Celé nastavení (styl, formuláře, atd.) vrstvy lze také uložit do 
samostatného souboru (*.qml, *.sld), což můžeme využít pro sdílení mezi 
kolegy, nebo pro pozdější použití nastavení vrstvy v jiném projektu.

Možnost uložení a načtení najdeme v okně `Vlastnoti vrstvy`
kliknutím na tlačítko :item:`Styl`. První dvě možnosti v 
nabídce umožní :item:`Načíst styl...` a :item:`Uložit styl...`.

.. figure:: images/styl_soubor_menu.png 
   :class: small 
   :scale-latex: 40 

   Možnosti práce se styly 


U QML souboru můžeme zvolit (stejně jako při kopírování stylů), které 
součásti nastavení se budou ukládat popř. načítat.

.. figure:: images/styl_soubor_nacteni.png 
   :class: small 
   :scale-latex: 40 

   Načítání nastavení vrstvy ze souboru
