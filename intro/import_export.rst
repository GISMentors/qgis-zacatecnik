.. |mActionZoomToLayer| image:: ../images/icon/mActionZoomToLayer.png
   :width: 1.5em
.. |mActionZoomFullExtent| image:: ../images/icon/mActionZoomToLayer.png
   :width: 1.5em

.. _importexport:

Přidávání a export geodat
=========================

QGIS podporuje široké spektrum geodat. Prostorová data můžeme
rozdělit podle způsobu uložení na lokální a distribuovaná (síťová).
V obou kategoriích se následně vyskytují data rastrová a vektorová.
V této kapitole jsou popsány základní principy připojení a exportu
prostorových
dat v prgramu QGIS. Práce s konkrétními formáty budou potom uvedeny v
samostatných kapitolách.

.. _vectorimport:

Přidávání dat
-------------

Data lze přidat pomocí hlavního menu :menuselection:`Vrstva --> Přidat
vrstvu-->...`. Na základě vybraného typu dat se nám zobrazí konkrétní
dialogové okno s nastavením importu dat.

.. _addlayer:

.. figure:: images/addlayer_menu.png

    Menu přidávání vrstev

.. noteadvanced:: Jak jde vidět na obrázku :num:`addlayer`, u většiny 
   typů dat lze pro přidání využít klávesové zkratky.

Stejného výsledku lze dosáhnout i pomocí ikon v nástrojovém panelu
:option:`Spravovat vrstvy`

.. figure:: images/addlayer.png

    Nástrojový panel pro přidávání vrstev :option:`Spravovat vrstvy`

Další možností je přidat data pomocí vestavěného datového
katalogu (prohlížeče souborů) a to buď dvojitým kliknutím nebo
jednoduchým přetažením souboru do mapového okna nebo okna vrstev
(:num:`#browser`). Pomocí kláves :kbd:`CTRL` nebo :kbd:`SHIFT` můžeme
vybrat a přidat přetažením více souborů najednou. Pomocí datového
katalogu lze také procházet a přidávat soubory přímo z archivu zip.

    .. tip:: Pomocí přetažení lze přidat data také přímo ze správce
       souborů v operačním systému.

.. _browser:

.. figure:: images/qgis_ogc_addbrowser.png

    Přidání vrstvy přetažením souboru do mapového okna nebo seznamu
    vrstev



Export dat
----------
Pro export vrstvy nebo její částí se používá funkce
:menuselection:`Uložit jako...`. Funkci můžeme spustit dvěma způsoby:

V seznamu vrstev označíme vrstvu, kterou chceme exportovat. Spustíme
funkci z hlavního menu :menuselection:`Vrstva --> Uložit jako...`

.. figure:: images/saveas.png

    Spuštění exportu z hlavního menu

Elegantnější a rychlejší způsob je spuštění exportu ze seznamu
vrstev. Pravým kliknutím na vrstvu vyvoláme kontextové menu a vybereme
:menuselection:`Uložit jako...`

.. figure:: images/layer_saveas.png
    :scale: 90%

    Spuštění exportu z kontextového menu v seznamu vrstev


Jak exportovat konkrétní data se dozvíme v jednotlivých kapitolách.

Výběr souřadnicového systému
----------------------------

Při vkládání rastrových nebo vektorových dat se může stát, že po
potvrzení výběru je vyžedována specifikace souřadnicového systému
vkládaných dat (:num:`#srs`). Okno se zobrazí v případě, pokud vkládaný
soubor neobsahuje vlastní specifikaci souřadnicového systému, jako
například ESRI Shapefile bez souboru končícího příponou \*.prj. V okně
výběru je možné vyhledat pomocí filtru požadovanou projekci. Zvolení
správné projekce je velice důležité pro překrývání více vrstev s
jinou projekcí, měření nebo pro připojování k webovým službám.

.. _srs:

.. figure:: images/qgis_ogc_set_proj.png

   Volba souřadnicového systému při vkládání dat


.. tip:: Po přidání dat můžeme zkontrolovat jejich pozici v prostoru
   pomocí funkce |mActionZoomToLayer| :sup:`Přiblížení na vrstvu`, nebo
   pomocí funkce |mActionZoomFullExtent| :sup:`Přiblížit na rozměry okna`
   pozici vůči ostatním vrstvám projektu. Změnu špatně zvoleného systému
   lze provést ve vlastnostech dané vrstvy v záložce :item:`Obecné`.

