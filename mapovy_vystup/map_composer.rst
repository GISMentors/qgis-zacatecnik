
   
   
Map composer
============
Systém QGIS dokáže pracovat s různými formáty a také je zobrazovat v mapovém okně. V případě, že je zapotřebí obrazový výstup, který zachová nastavení zobrazování vrstev, tak je nutné využít samostatný nástroj *Map Composer*. Důvodem je, že všechna nastavení -  reference na vrstvy, stylování, popisky a další, se sice ukládají do *.qgs* projektu, ale ten je přenositelný pouze do QGIS systému.

    .. figure:: images/map_window.png
       :class: large
       :scale-latex: 80
 
       Mapové okno zobrazující vrstvy dle jejich stylování.
       
    .. figure:: images/composer_output.png
       :class: large
       :scale-latex: 80
 
       Ukázka výstupu z Map Composeru.

Map Composer umožňuje vytvořit z dat výstup v běžně používaných formátech, jakými jsou např. \*.pdf, \*.png, \*.jpeg* a další. Takovýmto způsobem je možné prezentovat jednotlivá data, jejich kombinaci, nebo výsledky různých analýz i bez potřeby speciálních systémů.


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
        
        
    .. tip:: Existující mapový výstup lze zkopírovat pomocí tlačítka :item:`Duplicate`. Mapový výstup ke zkopírování se označí a pak se stiskne zmíněné tlačítko. V otevřeném okně se pak nastaví nový název mapového výstupu.

Pokud chcete otevřít existující mapový výstup, tak se v seznamu *Composer manageru* vybere a tlačítkem :item:`Show` se otevře.
Všechny existující mapové výstupy jsou přístupné také z :menuselection:`Project --> Print Composers`.

Nastavení pracovní plochy
-------------------------
Jako první je nutné nastavit vlastnosti pracovní plochy. Toto nastavení najdeme v práve části v záložce :item:`Composition` část :item:`Paper and Quality`.

    .. figure:: images/paper_settings.png
 
       Zakládání nového mapového výstupu

Zde se nastaví velikost "papíru", jeho orientaci, barvu pozadí a rozlišení v DPI při exportu.
Tyto hodnoty lze přenastavit i v průběhu práce. Do takto nastavené pracovní plochy lze začít přidávat jednotlivé prvky.

    .. tip:: Při tvorbě profesionálních mapových výstupů se doporučuje používat DPI = 400. Pro běžné použití je vhodné ponechat původní nastavení 300 DPI.
    
     V některých případech je nutné najít vhodnou kombinaci měřítka zobrazovaného mapového výřezu, velikosti podkladového papíru a příslušného DPI. 


    

