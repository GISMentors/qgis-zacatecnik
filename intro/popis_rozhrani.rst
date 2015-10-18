Popis rozhraní
--------------
Po zpuštění systému QGIS se zobrazí standardní rozhraní. 
Na obrázku níže jsou označeny základní části sytému.

.. tip:: Vzhled sysytému QGIS je možné jednoduše měnit dle potřeb. Zobrazování jednotlivých nástrojů je možné upravit a přizpůsobit si tak pracovní prostředí. Pokud budete rozšiřovat funkčnost systému, tak je dobré si vhodně umístit nové nástroje.

.. figure:: images/menu_description.png

   Základní části systému QGIS (detailní popis částí je níže).
   
Mapové okno - :fignote:`1`
==========================
V tomto okně se vykreslují všechny mapové vrstvy.

Přepínač vrstev / Panel prohlížeče - :fignote:`2`
=================================================
Přepínač vrstev zobrazuje všechny přidané vrstvy. Jejich zobrazení poskytuje rychlou  informaci o jejich pozici a grafickém zobrazení v mapovém okně. Kliknutím pravého tlačítka na vybranou vrstvu se vyvolá kontextové menu k dané vrstvě. V tomto menu je možné najít vše od stylování vrstvy až po exportdat.

Panel prohlížeče slouží k zjedodušení přístupu ke geodatám. Umožňuje přistupovat k různým typům dat, např. vektorovým, rastrovým, databázím, službám.


Postranní menu - :fignote:`3`
=============================
Menu s nástroji pro přidávání vrstev, nebo vytváření nových.  

Stavový řádek - :fignote:`4`
============================
Obsahuje základní informace o nastavení mapového okna. 
Mezi nejdůležitější patří informace o souřadnicovém systému, který se zde dá i přenastavit. 

    .. tip:: Souřadnicové systémy je možné vybírat podle EPSG kódu. Po instalaci je defaultně nastaven souřadnicový systém WGS 84. Pro potřeby zpracování geodat na území ČR se však většinou používá souřadnicový systém s EPSG kódem 5514 (S-JTSK). Nastavení přes stavový řádek je však platné jenom pro aktuální projekt. Po opětovném spuštění se systém spustí v defaultním souřadnicovém systému. Jak nastavit defaultní souřadnicový systém je popsáno v náseldující části.

Hlavní menu - :fignote:`5`
==========================
Hlavní menu pozůstává z dvou základních částí. První je standardní menu v liště a druhou je nástrojová lišta.

V menu se nachází zejména nástroje pro správu systému a jeho nastavení.

    .. tip:: Nastavení systému je možné změnit přes :menuselection:`Settings --> Options...`. Prvním důležitým nastavením je volba souřadnicového systému - záložka :item:`CRS`. Zde se nastaví souřadnicový systém  pro nový projekt a zvlášť pro novou vrstvu.
    
Nástrojová lišta obsahuje základní nástroje pro práci s projektem a vrstvami.
    
