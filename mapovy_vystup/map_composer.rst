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
.. |print| image:: ../images/icon/mActionFilePrint.png
   :width: 1.5em   
.. |as_image| image:: ../images/icon/mActionSaveMapAsImage.png
   :width: 1.5em
.. |as_pdf| image:: ../images/icon/mActionSaveAsPDF.png
   :width: 1.5em
.. |as_svg| image:: ../images/icon/mActionSaveAsSVG.png
   :width: 1.5em
   
Tvorba mapového výstupu
=======================
Systém QGIS dokáže pracovat s různými formáty a také je zobrazovat v mapovém okně. V případě, že je zapotřebí obrazový výstup, který zachová nastavení zobrazování vrstev, tak jenutné využít samostatný nástroj Map Composer. Důvodem je, že všechna nastavení -  reference na vrstvy, stylování, popisky a další, se sice ukládají do *.qgs* projektu, ale ten je přenosisetlný pouze do QGIS systému.

    .. figure:: images/map_window.png
       :class: large
       :scale-latex: 80
 
       Mapové okno zobrazující vícero vrstev a popisky.
       
    .. figure:: images/composer_output.png
       :class: large
       :scale-latex: 80
 
       Ukázka výstupu z Map Composeru.
       
TODO: udělat hezčí výstup.

Map Composer umožňuje vytvořit z dat výstup v běžně používaných formátech. Takovýmto způsobem je možné prezentovat jednotlivá data, jejich kombinaci, nebo výseldky různých analýz i bez potřeby speciálních systémů.

Composer manager
----------------
Systém QGIS umožňuje vytvářet víc než jeden mapový výstup pro projekt. Zpravování jednotlivých mapových výstupů umožňuje *Composer manager*, dostupný v :menuselection:`Project --> Composer Manager...`. 

    .. figure:: images/composer_manager.png
       :class: large
       :scale-latex: 80
 
       Otevření Composer Manageru z Menu.

Zde se nachází okno, kde jsou všechny mapové výstupy. Pokud není doposud žádný vytvořený, tak je seznam prázdný a pomocí talčítka :item:`Add` se vytvoří nový.

    .. figure:: images/add_new_composer.png
       :class: small
       :scale-latex: 30
 
       Zakládání nového mapového výstupu

Vyskočí okno pro zadání názvu nově vytvářeného mapového výstupu. Po zadání názvu a potvrzení tlačítkem :item:`OK` se tento vytvoří a následně se otevře okno pro editaci a úpravu samotného mapového výstupu.

Pokud chcete použít existující mapový výstup, tak se v seznamu *Composer manageru* vybere a tlačítkem :item:`Show` se otevře.


Tvorba mapového výstupu
-----------------------
Mapový výstup může obsahovat různé součásti (mapové pole, legenda, titulek, měřítko a jiné). Nastavení celého výstupu je popsáno kro po kroku až po export výstupu.

    .. figure:: images/composer_plain.png
       :class: large
       :scale-latex: 80
 
       Okno nového mapového výstupu.
       
Nastavení pracovní plochy
^^^^^^^^^^^^^^^^^^^^^^^^^
Jako první je nutné nastavit vlastnosti pracovní plochy. Toto nastavení najdeme v práve části v záložce :item:`Composition` část :item:`Paper and Quality`.

Zde se nastaví velikost "papíru", jeho orientaci, barvu pozadí a rozlišení v DPI při exportu.
Tyto hodnoty lze přenastavit i v průběhu práce. Do takto nastavené pracovní plochy lze začít přidávat jednotlivé prvky. 

Přidání obsahu mapového okna
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pomocí ikony |add_map| se aktivuje funkce pro přidání výřezu s mapovým oknem. Dalším krokem je umístění výřezu pro mapové okno do pracovní plochy pomocí tažení myši. 
Po umístění se do výřezu načte obsah mapového okna.

    .. figure:: images/map_input.png
       :class: large
       :scale-latex: 80
 
       Výřez s obsahem mapového okna a jeho detailní nastavení.
       
Velikost výřezu a jeho polohu lze měnit pomocí tahání za jeho hrany nebo uchopení za jeho obsah a posun.

    .. tip:: Výřez s mapovým oknem má vícero dalších nastavení. Rozšířené nastavení je dostupné pro každý prvek přidaný do mapového výstupu. V části :item:`Items` se nachází přehled všech prvků přidaných v mapovém výstupu. Označením vybraného prvku se v části :item:`Item properties` otevře detailní nastevní konkrétního prvku.
        
        .. figure:: images/map_items.png
           :class: small
           :scale-latex: 30
 
           Výřez s obsahem mapového okna a jeho detailní nastavení.
           
Obsah výřezu byl při jeho umístění vygenerován dle aktuálního rozsahu mapového okna. Překreslení dle pozměněného mapového oknaje možné v detailu prvku :item:`Item properties` v části :item:`Main properties` pomocí tlačítka :item:`Update preview`. Lze použít také další nástroje.

TODO: překreslení jinými funkcemi


Přidání titulku
^^^^^^^^^^^^^^^
Obvyklým požadavkem pro mapový výstup je textové pole s titulkem.
Textové pole se přidá pomocí ikonky |add_label|. Umístění textového pole probíhá stejně jako je popsané u mapového výřezu.

Jednotlivá nastavení  pro obsah tohoto pole jsou opět dostupná přes záložku :item:`Item properties`. Lze zde nastavit samotný text, jeho font, zarovnání, orámování, pozadí a další různé.


Přidání legendy
^^^^^^^^^^^^^^^
Další obvyklou součástí mapového výstupu je legenda. Ta má popisovat jednotlivé prvky, které jsou zbrazovány.
Přidání legendy do mapového výstupu je možné pomocí ikonky |add_legend|. Umístění položky legendy do mapového okna se proveden stejně jako u předchozích položek.

Obsah legendy je vygenerován v momentě jejího umístění a je vygenerován z nastavení stylů jednotlivých vrstev zobrazovaných v mapovém okně.

Obsah legendy je možné upravovat podobným způsobem jako  ostatní prvky (:item:`Item properties`). Lze zde upravit název, zarovnání, odsazování a další vizuální nastavení pro zobrazování legendy.

Lze zde však upravit i jednotlivé položky legendy, ubrat, přidat novou, změnit text i zařazení jednotlivých položek v rámci  legendy samotné. 

 TODO: přidat obrazek k nastavování položek legendy

    .. tip:: Pokud upravujete legendu, tak se může stát, že se změnami nebudete spokojeni. V případě, že nechcete změny opravovat nazpátek ručně, můžete legendu vygenerovat z dat znova pomocí tlačítka :item:`Update all`
 
Další prvky
^^^^^^^^^^^
Jako součást mapového výstupu se běžně používají i další prvky.

Měřítko je možné přidat pomocí ikony |add_scale|, dále lze přidat směrovou šipku |add_arrow|, obrázek |add_image| nebo atributovou tabulku |add_attributes|.

    
Export mapového výstupu
-----------------------
Všechna nastavení mapového výstupu jsou součástí mapového projektu. S uložením projektu se tedy uloží i nastavení mapového výstupu.

Pokud máte mapový výstup upraven, lze tento výstup uložit nebo vytisknout.

Tisk je možný pres ikonu |print|. Při tisku je nutné zkontrolovat všechna nastavení tisku pro konkrétní tiskárnu.

Často požadovaným výstupem je také výstup do souboru. V tomto případě lze volit mezi 3 základními typy výstupního souboru - obrázek |as_image|, PDF |as_pdf| nebo SVG |as_svg|.

    .. tip:: Při exportu mapového výstupu do obrázku je k dispozici široká škála formátů. Z hlediska kvality výstupu, nebo možnosti jeho úpravy je lepší použít PDF nebo SVG.
