.. |add_map| image:: ../images/icon/mActionAddMap.png
   :width: 1.5em
.. |add_label| image:: ../images/icon/mActionLabel.png
   :width: 1.5em
.. |add_legend| image:: ../images/icon/mActionAddLegend.png
   :width: 1.5em
.. |add_scale| image:: ../images/icon/mActionScaleBar.png
   :width: 1.5em
.. |add_image| image:: ../images/icon/mActionAddImage.png
   :width: 1.5em 
.. |add_arrow| image:: ../images/icon/mActionAddArrow.png
   :width: 1.5em
.. |add_attributes| image:: ../images/icon/grass_edit_attributes.png
   :width: 1.5em
.. |up| image:: ../images/icon/mActionArrowUp.png
   :width: 1.5em
.. |down| image:: ../images/icon/mActionArrowDown.png
   :width: 1.5em
.. |add| image:: ../images/icon/symbologyAdd.png
   :width: 1.5em  
.. |remove| image:: ../images/icon/symbologyRemove.png
   :width: 1.5em 
.. |add_nodes| image:: ../images/icon/mActionAddNodesShape.png
   :width: 1.5em 
.. |add_html| image:: ../images/icon/mActionAddHtml.png
   :width: 1.5em 
.. |add_shape| image:: ../images/icon/mActionAddBasicShape.png
   :width: 1.5em 
.. |mActionMoveItemContent| image:: ../images/icon/mActionMoveItemContent.png
   :width: 1.5em 

.. index::
   single: mapové elementy

Prvky mapového výstupu
----------------------

Mapový výstup může obsahovat různé součásti (mapové pole, legenda,
titulek, měřítko a jiné). Nastavení celého výstupu je popsáno krok po
kroku až po export výstupu.

.. index::
   pair: tvůrce map; nastavení pracovních panelů


Zobrazení pracovních panelů
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pro příjemnou práci při tvorbě výsledků je vhodné mít nastavené 
zobrazování jednotlivých panelů. *Vypnout/zapnout* panel je možné v menu
:menuselection:`Zobrazit --> Panely`, kde se nastaví viditelnost 
jednotlivým panelům. Na obrázku :numref:`panels` je zobrazeno doporučené 
nastavení zobrazených panelů.

.. raw:: latex

   \newpage

.. _panels:
   
.. figure:: images/panels.png
   :scale-latex: 45
   
   Nastavení zobrazení a skrytí jednotlivých panelů.
 
.. index::
   pair: mapové elementy; obsah mapového okna


Obsah mapového okna
^^^^^^^^^^^^^^^^^^^

Pomocí ikony |add_map| :sup:`Přidat novou mapu` se aktivuje funkce pro 
přidání výřezu s mapovým oknem. Dalším krokem je umístění výřezu pro 
mapové okno do pracovní plochy pomocí tažení myši.  Po umístění se do 
výřezu načte obsah mapového okna.

.. figure:: images/map_input.png
   :class: large
   :scale-latex: 80
 
   Výřez s obsahem mapového okna a jeho detailní nastavení.
       
Velikost výřezu a jeho polohu lze měnit pomocí tahání za jeho hrany
nebo uchopení za jeho obsah a posun. Pokud potřebujeme posunout obsah mapy,
pak použijeme nástroj |mActionMoveItemContent| :sup:`Posunout obsah položky`
a interaktivně změníme rozsah pomocí tažení.

.. raw:: latex

   \newpage

.. tip:: Výřez s mapovým oknem má vícero dalších nastavení. Rozšířené
   nastavení je dostupné pro každý prvek přidaný do mapového
   výstupu. V části :item:`Položky` se nachází přehled všech
   prvků přidaných v mapovém výstupu. Označením vybraného prvku
   se v části :item:`Vlastnosti položky` otevře detailní
   nastavení konkrétního mapového prvku.
        
   .. figure:: images/map_items.png
      :class: small
      :scale-latex: 30
 
      Dostupné položky u nastavení mapového okna.
           
Obsah výřezu byl při jeho umístění vygenerován dle aktuálního rozsahu
mapového okna. Manipulace obashu mapy a jeho překreslování je možné ovládat pomocí sady tlačítek v horní části detailu prvku :item:`Vlastnosti položky`.

- |mActionRefresh| :sup:`Aktualizovat náhled mapy` - aktualizace obsahu mapového okna
- |mActionSetToCanvasExtent| :sup:`Nastavit rozsah mapy tak, aby odpovídal hlavnímu rozsahu plátna`
- |mActionViewExtentInCanvas| :sup:`Zobrazit aktuální rozsah mapy na hlavním plátně`
- |mActionSetToCanvasScale| :sup:`Nastavit měřítko mapy tak, aby odpovídalo měřítku hlavního plátna`
- |mActionViewScaleInCanvas| :sup:`Nastavit hlavní plátno tak, aby odpovídalo aktuálnímu měřítku mapy`
- |mActionShowBookmarks| :sup:`Záložky` nastavení mapového okna dle existujících záložek
- |mActionMoveItemContent| :sup:`Interaktivně upravit rozsah mapy` totožná funkcionalita pro změnu rosahu tažením
- |labels| :sup:`Nastavení tvorby popisků` speciální chování popisků v mapovém výstupu - jejich posun na okrajích, blokování popisků


V první sekci nastavení lze nastavit přesné měřítko mapového okna, 
jeho natočení, nebo specifický souřadnicový systém.

V části :item:`Rozsahy` lze přesně nadefinovat rozsah mapového okna v
souřadnicovém systému mapového projektu. 

.. figure:: images/map_main_properties.png
   :class: small
   :scale-latex: 30
 
   Hlavní nastavení položky mapového okna.

.. raw:: latex

   \newpage

.. index::
   pair: mapové elementy; souřadnicová mřížka 

Častou součástí mapového výřezu je i souřadnicová mřížka - grid s
popisem souřadnic. Grid lze přidat a nastavit v položce
:item:`Mřížky`. Lze nastavit styl gridu (linie, křížky, jiné symboly,
jenom rám se souřadnicemi) a dále nastavit interval a styl
vykreslování.

.. tip:: Pro grid lze definovat souřadnicový systém odlišný od
             projektu.

.. figure:: images/map_coordinates.png
   :scale-latex: 70
   
   Mapové okno s gridem a souřadnicemi.
       
.. figure:: images/map_grids.png
   :class: small
   :scale-latex: 35
        
   Nastavení gridu pro mapové okno.
 
Nastavení popisků gridu je umístěno v části :item:`Vykreslit
souřadnice`. Lze nastavit formát vystupu, počet desetinných míst font
i barvu.  Popisky jsou rozděleny do jednotlivých částí mapového okna
(levá, pravá, horní, dolní). Každou stranu lze nastavit samostatně -
zda se zobrazuje, pozici vůči rámu, orientaci a řazení.

.. figure:: images/map_decoration.png
   :class: small
   :scale-latex: 45

   Nastavení zobrazování popisových souřadnic gridu.

.. index::
   pair: mapové elementy; titulek
   
Text (titulek, tiráž, doprovodný text)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Obvyklým požadavkem pro mapový výstup je textové pole s titulkem.
Textové pole se přidá pomocí ikonky |add_label| :sup:`Přidat nový 
popísek`. Umístění textového pole probíhá stejně jako je popsané 
u mapového výřezu.

Jednotlivá nastavení pro obsah tohoto pole jsou opět dostupná přes
záložku :item:`Vlastnosti položky`. Lze zde nastavit samotný text, jeho
font, zarovnání, orámování, pozadí a další různé. Textové pole se dále využivá 
např. pro vložení tiráže či dalšího doprovodného textu

.. index::
   pair: mapové elementy; legenda

Legenda
^^^^^^^
Další obvyklou součástí mapového výstupu je legenda. Ta má popisovat
jednotlivé prvky, které jsou zobrazovány.  Přidání legendy do mapového
výstupu je možné pomocí ikonky |add_legend| :sup:`Přidat novou legendu`.
Umístění položky legendy do mapového okna je provedeno stejně jako u 
předchozích položek.

Obsah legendy je vygenerován v momentě jejího umístění a na základě
nastavení stylů jednotlivých vrstev zobrazovaných v mapovém okně.
V ideálním případě se všechny úpravy provádí v nastavení vrstev tak, 
aby byl minimalizovaný počet ručních úprav v tomto kroku.

Obsah legendy je možné upravovat podobným způsobem jako ostatní prvky
(:item:`Vlastnosti položky`). Lze upravit název, zarovnání, odsazování
a další vizuální nastavení pro zobrazování legendy. 

Dále lze upravit i jednotlivé položky legendy, ubrat, přidat novou,
změnit text i zařazení jednotlivých položek v rámci legendy samotné.

.. figure:: images/composer_legend.png
   :class: large
   :scale-latex: 55
 
   Přidaná legenda a úprava jejích položek.


.. tip:: Pokud upravujete legendu, tak se může stát, že se změnami nebudete 
   spokojeni. V případě, že nechcete změny v nastavení provést ručně, můžete 
   legendu vygenerovat z dat znova pomocí tlačítka :item:`Aktualizovat vše`.

.. index::
   pair: mapové elementy; atributová tabulka

Atributová tabulka
^^^^^^^^^^^^^^^^^^

V některých případech je vhodné umístit do mapového výstupu i část
atributové tabulky. Tuto lze přidat pomocí tlačítka |add_attributes| 
:sup:`Přidat atributovou tabulku`.

Všeobecná nastavení tabulky a jejího vzhledu se nachází v části
:item:`Vlastnosti položky`. Pokud je v projektu přidáno vícero vrstev,
které mají atributovou tabulku, tak se nastaví zdrojová vrstva pro
atributovou tabulku do mapového výstupu.

.. figure:: images/composer_table.png
   :class: large
   :scale-latex: 55
 
   Atributová tabulka vybrané vrstvy přidaná v mapovém výstupu.
       
Úprava samotné tabulky se nachází pod tlačítkem
:item:`Atributy...`. V tomto menu jsou 2 základní části. V první
části se manipuluje s atributy. Zde se vyberou všechny atributy, které
se v tabulce mají zobrazit |add| |remove|, jejich pořadí |up| |down|,
může se zde nastavit titulek pro atribut, ale i zarovnávání hodnot.

V druhé části se nastavuje řazení dat v tabulce. Řazení se řídí
definovanými pravidly. Každé pravidlo musí obsahovat atribut, podle
kterého se tabulka bude řadit, a typ řazení (sestupně nebo
vzestupně). Takto nadefinované pravidlo se pak tlačítkem |add| přidá
do seznamu pravidel. Jednotlivá pravidla se vypisují do pole pod
sebe. Jejich pořadí je možné měnit a ovlivnit tak přesné vypsání
tabulky do mapového výstupu.
       
.. figure:: images/attribute_setting.png

   Nastavení zobrazení atributové tabulky v mapovém výstupu.

.. index::
   pair: mapové elementy; měřítko

Měřítko
^^^^^^^

Běžnou součástí výstupu je také měřítko. To lze přidat pomocí ikony |add_scale|
:sup:`Přidat nové grafické měřítko` a vložením prvku do výstupu. Výběr stylu a
další nastavení je dostupné v záložce :item:`Vlastnosti položky` viz
:numref:`legenda-nastaveni`. Nejdůležitější je výběr stylu legendy v položce :item:`Styl`. 
Lze vybrat z grafických měřítek nebo zvolit číselné měřítko. Dále lze nastavit
jednotky a jejich popisek. Dále jsou pak ostatní nastavení pro vzhled měřítka.

.. _legenda-nastaveni:

.. figure:: images/legenda_nastaveni.png
   :class: small
   :scale-latex: 30 
 
   Detailní nastavení měřítka.
 
.. index::
   pair: mapové elementy; směrová růžice

Směrová růžice
^^^^^^^^^^^^^^

Do mapového výstupu lze přidat také směrovou růžici - pomocí ikony |north_arrow| 
:sup:`Přidat směrovou růžici`. Pokud nemáme žádný obrázek růžice, najdeme několik typů růžic v základní QGIS SVG knihovně. Zdrojový obrázek zvolíme v 
záložce :item:`Vlastnosti položky`, zde jsou dostupná také další nastavení, 
např. rotace, která je za určitých okolností u směrové růžice nutná a lze ji
nastavit automaticky.

Na obrázku :numref:`arrow` je vidět nastavení synchornizace s vybraným mapovým oknem a nastevní na *skutečný sever*, které nastaví rotaci růžice automaticky.

.. _arrow:

.. figure:: images/composer_arrow.png
   :class: large
   :scale-latex: 55
 
   Nastavení směrové růžice.

Obrázek
^^^^^^^

Tento nástroj je totožný s nástrojem pro přidání směrové růžice. Je dobré si
uvědomit, že obsah přidaného obrázku je pouze na uživateli a do mapového výstupu
může přidat různý obsah.



Šipka
^^^^^

Alternativní možností vytvoření směrové ružice může být pomocí ikony |add_arrow| 
:sup:`Přidat šipku`. Tato funkce je primárně určena ke kreslení šipek ve smyslu 
znázornění vztahů mezi jednotlivými součástmi mapové kompozice. Držením klávesy 
:item:`Shift` při kreslení šipky se nám kurzor bude přichytávat po 45°. 
Směrová růžice může být vykreslena různou symbologií. Výběr symbologie a další 
nastavení jsou dostupné v záložce :item:`Vlastnosti položky`. Lze zde ponechat 
defaultní styl prvku, kdy se vykresluje jednoduchá šipka. Je možné použít i 
složitější nastavení - například použít vlastní svg symboly pro začátek a konec 
šipky.

.. raw:: latex

   \newpage

.. figure:: images/arrow.png
   :class: small
   :scale-latex: 35
 
   Detailní nastavení směrové šipky.

.. index::
   pair: mapové elementy; další prvky mapového výstupu

Další prvky
^^^^^^^^^^^
Do mapového výstupu můžeme také přidat základní geometrické tvary |add_shape| :sup:`Přidat tvar`, rýsovat polygony a linie |add_nodes| :sup:`Add Node item`, nebo přidat HTML kód |add_html| :sup:`Přidat HTML rám`.
