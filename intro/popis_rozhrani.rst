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
.. |mActionZoomOut| image:: ../images/icon/mActionZoomOut.png
   :width: 1.5em
.. |mActionZoomIn| image:: ../images/icon/mActionZoomIn.png
   :width: 1.5em
.. |mActionZoomLast| image:: ../images/icon/mActionZoomLast.png
   :width: 1.5em
.. |mActionZoomNext| image:: ../images/icon/mActionZoomNext.png
   :width: 1.5em
.. |mActionZoomToLayer| image:: ../images/icon/mActionZoomToLayer.png
   :width: 1.5em
.. |mActionZoomFullExtent| image:: ../images/icon/mActionZoomFullExtent.png
   :width: 1.5em
.. |mActionPan| image:: ../images/icon/mActionPan.png
   :width: 1.5em
.. |mActionRefresh| image:: ../images/icon/mActionRefresh.png
    :width: 1.5em
Popis rozhraní
--------------
Po zpuštění systému QGIS se zobrazí standardní rozhraní. 
Na obrázku níže jsou označeny základní části systému.

.. tip:: Vzhled systému QGIS je možné jednoduše měnit dle potřeb. Zobrazování jednotlivých nástrojů je možné upravit a přizpůsobit si tak pracovní prostředí. Pokud budete rozšiřovat funkčnost systému, tak je dobré si vhodně umístit nové nástroje.

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

Souřadnice
^^^^^^^^^^ 
První část stavového řádku slouží pro orientaci v mapovém okně. Zde se zobrazuje buď aktuální souřadnice ukazatele myši v mapovém okně, nebo tzv. extent (rozsah území aktuálně zobrazeného v mapovém okně). Ukázka obou možností je zobrazena na následujícím obrázku. Jako přepínač mezi uvedenými fukcemi slouží ikona |extents|, resp. |tracking|.
   
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
    
Nástrojová lišta obsahuje základní nástroje pro práci s projektem a vrstvami. Vypínání a zapínání jednotlivých nástrojových lišt a oken lze provádět pravým kliknutím na panel a výběrem z nabídky

Základní nástroje pro pohyb v okně 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- |mActionZoomIn| :sup:`Přiblížit``, |mActionZoomOut| :sup:`Oddálit` - přiblíží/oddálí vybranou oblast, pro přibližovaní bez vybrání oblasti lze použít i kolečko myši
- |mActionZoomLast| :sup:`Zvětšit podle posledního výřezu`, |mActionZoomNext| :sup:`Přiblížit na další` - lze vrátit na předchozí stav přiblížení a zpět
- |mActionZoomToLayer| :sup:`Přiblížení na vrstvu` - přiblíží na rozsah vybrané vrstvy
- |mActionZoomFullExtent| :sup:`Přiblížení na všechny vrstvy` - přiblíží na všechny vrstvy v projektu
- |mActionPan| :sup:`Posun mapy` - umožňí posun v mapovém okně tažením, tato funkce lze nahradit stisknutím kolečka myši a následným tažením
        .. tip:: při posunu pomocí stiknutí kolečka myši můžeme mít aktivní jinou funkci např výběr, vytváření nových prvků atd.
- |mActionRefresh| :sup:`Obnovit` - obnoví zobrazení všech nahraných dat


    
