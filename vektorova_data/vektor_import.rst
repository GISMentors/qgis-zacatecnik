Přidání a export dat
====================

V této kapitole je popsán postup přidání a exportu vektorových
dat. Obecný princip přidávání a exportu dat v QGIS najdeme v kapitole
:ref:`importexport`.  Pro čtení a zápis vektorových formátů používá
QGIS knihovnu GDAL.

.. tip:: V režimu čtení lze vektorová data také načíst přímo z archivu
         *zip* a *gzip*.

Přidávání vektorových dat
-------------------------

Nabídka pro načtení vektorové vrstvy se aktivuje v záložce
:menuselection:`Vrstva --> Přidat vrstvu --> Přidat vektorovou vrstvu`,
ikonou |mActionAddOgrLayer| :sup:`přidání vektorové vrstvy` nebo pomocí
klávesové zkratky :kbd:`Ctrl+Shift+V`.

.. figure:: images/qgis_ogc_addvector_icons.png
   :scale-latex: 37
   
   Dialogové okno přidání vektorové vrstvy.

Nejčastější volbou vkládání dat je soubor nebo adresář. Vložení jedné
vrstvy je možné označením :item:`Typ zdroje` - |checkbox|
:option:`Soubor`. Kliknutím na tlačítko :item:`Procházet` se otevře
navigační okno s možností vybrat soubor s vektorovými daty. Po
potvrzení se označená vrstva načte do mapového okna.

Volba :item:`Adresář` umožňuje označit složku, ve které se nachází
vektorová data. Potvrzením tlačítkem :item:`Otevřít` QGIS připraví
všechna dostupná data uložená ve složce k načtení. Objeví se
potvrzující okno se všemi dostupnými vrstvami. Vrstvy lze buď označit
všechny, nebo podržením klávesy :kbd:`Ctrl` vybrat jen požadované
vrstvy (:numref:`vecfolder`). Další možností je přidat data pomocí
vestavěného datového katalogu (prohlížeče souborů)
viz kapitola :ref:`vectorimport`.

.. _vecfolder:

.. figure:: images/qgis_ogc_addvector_selectfromfolder.png

   Výběr jednotlivých vrstev při přidávání vektorových vrstev
   ze složky.

Export vektorových dat
----------------------

Pravým kliknutím na vrstvu vyvoláme kontextové menu, vybereme možnost
:menuselection:`Export -> Save Features As...` a zadáme parametry exportu.
Můžeme zde zvolit výstupní formát (např. ``*.kml``, ``*.shp``, ``*.gpx``), 
souřadnicový systém vrstvy a další volitelné parametry.

.. figure:: images/vector_saveas.png
   :scale-latex: 45

   Okno exportu vektorové vrstvy.

Pokud potřebujeme exportovat pouze část prvků vrstvy nebo
konkrétní zájmové prvky, musíme tyto prvky nejprve označit
výběrem (např. |mActionSelectRectangle| :sup:`Vybrat prvky oblastí
nebo jednoklikem` nebo |mIconExpressionSelect| :sup:`Vabrat prvky
pomocí vzorce`). Potom se nám v okně exportu aktivuje možnost
|checkbox| :sup:`Uložit pouze vybrané prvky`, nebo pro export použijeme
druhou volbu z kontextového menu
:menuselection:`Export --> Save Features As...`

.. tip:: Pro uložení pouze atributové tabulky vrstvy lze zvolit
    výstupní formát ``*.csv``.

