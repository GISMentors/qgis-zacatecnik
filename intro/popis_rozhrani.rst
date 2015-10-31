.. |extents| image:: ../images/icon/extents.png
   :width: 1.5em
.. |tracking| image:: ../images/icon/tracking.png
   :width: 1.5em
.. |addscale| image:: ../images/icon/symbologyAdd.png
   :width: 1.5em
.. |removescale| image:: ../images/icon/symbologyRemove.png
   :width: 1.5em
.. |geographic| image:: ../images/icon/geographic.png
   :width: 1.5em
.. |log| image:: ../images/icon/mIconInfo.png
   :width: 1.5em
   
Popis rozhraní
--------------
Po zpuštění systému QGIS se zobrazí standardní rozhraní. 
Na obrázku níže jsou označeny základní části sytému.

.. tip:: Vzhled sysytému QGIS je možné jednoduše měnit dle potřeb. Zobrazování jednotlivých nástrojů je možné upravit a přizpůsobit si tak pracovní prostředí. Pokud budete rozšiřovat funkčnost systému, tak je dobré si vhodně umístit nové nástroje.

.. figure:: images/menu_description.png
   :class: large
   :scale-latex: 80

   Základní části systému QGIS (detailní popis částí je níže).
   
Mapové okno (1)
===============
V tomto okně se vykreslují všechny mapové vrstvy.

Přepínač vrstev / Panel prohlížeče (2)
======================================
Přepínač vrstev zobrazuje všechny přidané vrstvy. Jejich zobrazení poskytuje rychlou  informaci o jejich pozici a grafickém zobrazení v mapovém okně. Kliknutím pravého tlačítka na vybranou vrstvu se vyvolá kontextové menu k dané vrstvě. V tomto menu je možné najít vše od stylování vrstvy až po exportdat.

Panel prohlížeče slouží k zjedodušení přístupu ke geodatám. Umožňuje přistupovat k různým typům dat, např. vektorovým, rastrovým, databázím, službám.


Postranní menu (3)
==================
Menu s nástroji pro přidávání vrstev, nebo vytváření nových.  

Stavový řádek (4)
=================
Obsahuje základní informace o nastavení mapového okna. 
Jednotlivé části jsou posány níže.

.. figure:: images/status_bar.png
   :class: large
   :scale-latex: 80
   
   Stavový řádek systému QGIS.
   
Sořadnice
^^^^^^^^^ 
První část stavového řádku slouží pro orientaci v mapovém okně. Zde se zobrazuje buď aktuální souřadnice ukazatele myši v mapovém okně, nebo tzv. extent (rozsah území aktuálně zobrazeného v mapovém okně). Ukázka obou možností je zobrazena na náseldujícím obrázku. Jako přepínač mezi uvedenými fukcemi slouží ikona |extents|, resp. |tracking|.
   
    .. figure:: images/coordinates_extent.png
    
       Možnosti zobrazení souřadnic ukazatele myši nebo rozsahu mapového okna.
  
Měřítko
^^^^^^^   
Další funkcí je měřítko. Tato funkce zobrazuje aktuální měřítko mapového okna. Umožňuje také překreslení mapového okna do jiného měřítka pomocí výběru z předdefinovaného seznamu měřítek.

    .. tip:: Seznam předdefinovaných měřítek je možné upravit. V :menuselection:`Settings --> Options...` záložka :item:`Map Tools` je část Predefined scales. Nové měřítko je možné přidat pomocí ikonky |addscale| a nebo odstránit pomocí |removescale|. 

        .. figure:: images/predefined_scales.png
 
           Menu pro upravení předdefinovaných měřítek.

Překreslování mapového okna
^^^^^^^^^^^^^^^^^^^^^^^^^^^           
Vykreslování v mapovém okně je možné nastavit různým způsobem. Standardně se kresba v mapovém okně překresluje při následujících akcích:
    * přidání nové vrstvy
    * posun nebo zoomování mapového okna
    * změna velikosti QGIS okna
    * změna viditelnosti vrsty
    
V některých případech může překreslování mapového okna trvat déle než je vhodné. V takovýchto případech je možné upravit nastavení vykreslování a :ref:`stylování <styl-vrstvy>` jednotlivých vrstev.
V případě, že překreslování není potřebné, tak je možné jej potlačit - mapové okno se nebude překreslovat. Pro takovéto nastavení je v stavovém menu položka s checkboxem :item:`Render`.

    .. tip:: Pokud potřebujete přerušit vykreslování jednorázově, tak je to možné udělat stisknutím klávesy :item:`Esc`.

Souřadnicový systém
^^^^^^^^^^^^^^^^^^^        
Mezi nejdůležitější nastavení patří nastavení souřadnicového systému mapového okna. Aktuální EPSG kód souřadnicového systému je vidět přímo ve stavovém řádku vedle ikony |geographic|.


    .. tip:: Souřadnicové systémy je možné vybírat podle EPSG kódu. Po instalaci je defaultně nastaven souřadnicový systém WGS 84. Pro potřeby zpracování geodat na území ČR se však většinou používá souřadnicový systém s EPSG kódem 5514 (S-JTSK). Nastavení přes stavový řádek je však platné jenom pro aktuální projekt. Po opětovném spuštění se systém spustí v defaultním souřadnicovém systému. Jak nastavit defaultní souřadnicový systém je popsáno v :ref:`nastavení souřadnicového systému <sour-system>`.

.. noteadvanced:: V případě, že uživatel potřebuje zjistit detaily o jakékoli aktivitě systému, tak je možné prohlídnout si všechny informace. Záložku s jednotlivými logovacími zprávami je možné otevřít pomocí ikonky |log|. Tyto zprávy jsou podstatné zejména v případě neočekávaného chování.

Hlavní menu (5)
===============
Hlavní menu pozůstává z dvou základních částí. První je standardní menu v liště a druhou je nástrojová lišta.

V menu se nachází zejména nástroje pro správu systému a jeho nastavení.

    .. tip:: Nastavení systému je možné změnit přes :menuselection:`Settings --> Options...`. Prvním důležitým nastavením je volba souřadnicového systému - záložka :item:`CRS`. Zde se nastaví souřadnicový systém  pro nový projekt a zvlášť pro novou vrstvu.
    
Nástrojová lišta obsahuje základní nástroje pro práci s projektem a vrstvami.
    
