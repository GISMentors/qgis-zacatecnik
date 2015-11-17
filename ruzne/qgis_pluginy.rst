.. |plug1| image:: ../images/icon/mActionShowPluginManager.png
   :width: 1.5em
.. |checkbox_unchecked| image:: ../images/icon/checkbox_unchecked.png
   :width: 1.5em
.. |plugin| image:: ../images/icon/plugin.png
   :width: 1.5em
.. |plugin-installed| image:: ../images/icon/plugin-installed.png
   :width: 1.5em
.. |q2t| image:: ../images/icon/q2t.png
   :width: 1.5em
.. |plugin-upgrade| image:: ../images/icon/plugin-upgrade.png
   :width: 1.5em
.. |mActionTransformSettings| image:: ../images/icon/mActionTransformSettings.png
   :width: 1.5em
.. |star| image:: ../images/icon/osm_star.png
   :width: 1.5em
.. |1| image:: ../images/icon/dxf2shp_converter.png
   :width: 1.5em
.. |3| image:: ../images/icon/roadgraph.png
   :width: 1.5em
.. |2| image:: ../images/icon/coordinate_capture.png
   :width: 1.5em
.. |4| image:: ../images/icon/spatialquery.png
   :width: 1.5em
.. |5| image:: ../images/icon/olp.png
   :width: 1.5em
.. |6| image:: ../images/icon/mGeorefRun.png
   :width: 1.5em
.. |7| image:: ../images/icon/evis_icon.png
   :width: 1.5em
.. |8| image:: ../images/icon/gps_importer.png
   :width: 1.5em
.. |9| image:: ../images/icon/dem.png
   :width: 1.5em
.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |geographic| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |reticle| image:: ../ruzne/images/p_reticle.png
   :width: 1.5em
.. |askcor| image:: ../ruzne/images/p_askcor.png
   :width: 1.5em
.. |askcorcopy| image:: ../ruzne/images/p_askcorcopy.png
   :width: 1.5em
.. |mActionNewVectorLayer| image:: ../images/icon/mActionNewVectorLayer.png
   :width: 1.5em
.. |selectcreatelayer| image:: ../images/icon/selectcreatelayer.png
   :width: 1.5em





QGIS pluginy
------------

QGIS umožňuje práci se zásuvnými moduly, tzv. :wikipedia:`plugin
<https://en.wikipedia.org/wiki/Plug-in_(computing)>` -mi. Ve všeobecnosti se
jedná o softvéry, které nepracují samostatně, ale jako doplňkové moduly jiné
aplikace a tím rozšiřujú její funkčnost. V současnosti existuje pro QGIS víc než
300 zásuvných modulů. Všechny jsou napsané v programovacím jazyku `Python 
<https://www.python.org/>`_ nebo `C++ <https://isocpp.org/>`_. Mnohé z nich jsou
stále ve vývoji. Jejich kompletní seznam spolu s příslušnou charakteristikou,
informacemi například o použití, potřebné minimální verzi QGISu, domovské
stránce, autorech, o počtu stáhnutí, o tom, které jsou označené jako
nejoblíbenější je dostupný `zde <https://plugins.qgis.org/plugins/>`_.
    

Moduly jsou udržované vývojovým týmem QGISu (`QGIS Development Team 
<http://qgis-development-team.software.informer.com/>`_) a jsou automaticky
součástí každé jeho distribuce. Všechny externí pluginy jsou napsané v
programovacím jazce Python a jsou udržovány příslušnými autory. Chyby (angl.
*bugy*) by měli být zveřejnovány  a dostupné na stránkách `projektu 
<http://hub.qgis.org/projects/qgis-user-plugins>`_.


.. _spravca-plugin:

Správce zásuvných modulů
========================

V prvník kroku v menu zvolíme :menuselection:`Zásuvné moduly --> Spravovat a instalovat
zásuvné moduly` (|plug1| :sup:`Spravovat a instalovat zásuvné moduly`).
Spustí se dialogové okno (:num:`#vse`), které slouží na prohlížení, vypínání a
zapínání  dostupných modulů příslušné verze QGISu.

.. _vse:

.. figure:: images/p_vse.png
   :scale: 55%

   Správce zásuvných modulů v prostředí QGIS

Pod položkou |plugin-installed| :sup:`Instalované` najdeme ty, které byli
nainstalované automaticky při instalaci QGISu. Z nich jsou některé načtené, jiné
lze dočasně povolit nebo zakázat zaškrtnutím ikonky |checkbox_unchecked|.
V případě, že klikneme na některý z modulů, zobrazí se jeho charakteristika nebo
účel, spolu s dalšími informacemi jako je název, popis, počet hodnocení a
stáhnutí modulu,reprezentující ikona, kategorie, instalovaná nebo dostupná
verze, autor, seznam změn a další. Na :num:`plugininfo`  je znázorněný příklad
zásuvného modulu s názvem |q2t| :sup:`Qgis2threejs`.

.. _plugininfo:

.. figure:: images/p_info.png
   :scale: 55%

   Charakteristika zásuvného modulu na prohlížení 3D objektů ve webovém
   prohlížeči.

Seznam všech dostupných pluginů možno zobrazit a konkrétní modul načíst zvolením
|plugin| :sup:`Nenainstalováno` a spuštěním :item:`Instalovat zásuvný modul`.
Následně se dá tento modul přeinstalovat nebo úplně odinstalovat 
(:num:`#p-instal`).  


.. _p-instal:

.. figure:: images/p_instal.png
   :scale: 55%

   Seznam nenainstalovaných modulů :fignote:`(1)`, instalace :fignote:`(2)`,
   možnost odinstalování :fignote:`(3)` nebo přeinstalování :fignote:`(4)`
   kteréhokoli z modulů

Pod záložkou |plugin-upgrade| :sup:`Aktualizovatelný` se nachází zásuvné moduly,
které jsou dostupné i v novější verzi. Záložka |mActionTransformSettings| 
:sup:`Nastavení` obsahuje nastavení týkající se kontroly aktualizací modulů,
experimentálních a neschválených modulů a zobrazuje i seznam repozitářů, které
lze přidávat editovat nebo mazat, viz :num:`#akt-nast`.
Po zaškrtnutí políček |checkbox_unchecked|  při položkách :item:`Zobrazit také 
experimentální` a :item:`neschválené moduly` je k dispozici téměř 500 zásuvných
modulů.


.. _akt-nast:

.. figure:: images/p_akt_nast.png
   :scale: 55%

   Záložky svisející s aktualizacemi a nastavením zásuvných modulov

.. tip:: Seznam zásuvních modulů může uživatel uspořádat dle svých potřeb.
   Po stisknutí pravého tlačítka myši v seznamu modulů jek dispozici jejich
   uspořádání dle abecedy, počtu stáhnutí, hlasů nebo stavu (:num:`#rad`).

    .. _rad:

    .. figure:: images/p_rad.png
       :scale: 55%

       Možnosti seřazení zásuvných modulů

.. note:: Je zapotřebí připomenout, že zásuvné moduly v oficiálních repozitářech
   byli testovány, no jednotlivé repozitáře mohou obsahovat i méně ověřené
   moduly různé kvality a stádia vývoje. Proto je dobrou pomůckou zobrazení
   hodnocení či počtu  |star| |star| |star|.  

.. tip:: Pokud známe alespoň přibližný název konkrétního modulu, při vyhledávání
   může vyplnění políčka :item:`Hledat` v dialogovém okně.   

 

Příklady zásuvních modulů
=========================

V další části si částečně ukážeme některé z užitečných a často používaných
zásuvních modulů programu QGIS: 

.. only:: latex
          
   .. tabularcolumns:: |p{5cm}|p{10cm}|
                       
.. only:: html
                                 
   .. cssclass:: border

+------------------------------------------------+-------------------------------------------------+
| Zásuvný modul                			 | Charakteristika  	  	                   |
+================================================+=================================================+
| |1| :sup:`Konvertor Dxf2Shp` 			 | konvertuje formát ``*.dxf`` do formátu ``*.shp``|
+------------------------------------------------+-------------------------------------------------+
| |2| :sup:`Získání souřadnic`     		 | získáva souřadnice myši                         |
+------------------------------------------------+-------------------------------------------------+
| |3| :sup:`Zásuvný modul silničního grafu` 	 | řeší problém nejkratší cesty                    |
+------------------------------------------------+-------------------------------------------------+
| |4| :sup:`Zásuvný modul prostorových dotazů`   | tvorba prostorových dotazů			   |
+------------------------------------------------+-------------------------------------------------+
| |5| :sup:`OpenLayers Plugin`                   | OpenLayers vrstvy			           |
+------------------------------------------------+-------------------------------------------------+
| |6| :sup:`Georeferencovač GDAL`		 | georeferencování rastrů pomocí GDAL             |
+------------------------------------------------+-------------------------------------------------+
| |7| :sup:`eVis`             			 | nástroj vizualizace událostí                    |
+------------------------------------------------+-------------------------------------------------+
| |8| :sup:`GPS nástroje`      			 | nástroje pro načtení a import dat GPS           |
+------------------------------------------------+-------------------------------------------------+
| |9| :sup:`Zásuvný modul analýzy terénu rastru` | nástroj pro analýzu terénu 		           |
+------------------------------------------------+-------------------------------------------------+


|1| :sup:`Konvertor Dxf2Shp`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

V případě, že máme k dispozici soubor AutoCAD DXF (`Drawing Exchange Format 
<https://en.wikipedia.org/wiki/AutoCAD_DXF>`_), do prostředí programu QGIS ho
umíme načíst díky zásuvnému modulu *Konvertor Dxf2Shp*. Již z názvu vyplývá, že
soubor je převeden do formátu *Shapefile*.

Po načítaní modulu pomocou :ref:`správcu zásuvných modulov <spravca-plugin>`
sa po kliknutí na ikonu |1| objaví dialógové okno, kde je potrebné nastaviť
vstupný ``*.dxf`` súbor, názov, cestu a typ nového ``*.shp`` súboru, 
viď. :num:`#dxf2shp`. Povolenie |checkbox| :sup:`Exportovat textové značky`
vytvorí extra bodovú vrstvu s označeniami a príslušná ``*.dbf`` tabuľka bude
obsahovať "textové" informácie zo súboru ``*.dxf``. 

.. note:: Když se po spuštění modulu tlačítkem :item:`OK` zobrazí dialogové
   okno související se souřadnicovými systémy, systém nastavíme.

.. _dxf2shp:

.. figure:: images/p_dxf2shp.png
   :scale: 70%

   Dialogové okno modulu na převod AutoCAD DXF souboru na soubor Shapefile

|2| :sup:`Získání souřadnic`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tento zásuvný modul se používá velmi jednoduše a umožňuje zobrazení souřadnic
myši pro dva vybrané souřadnicové systémy. Dialogové okno je na :num:`#zis-sur`.
Kliknutím na ikonu |geographic| nastavíme požadovaný souřadnicový systém,
zvolením |2| :sup:`Zapnout získávání` se symbol myši změní na |reticle|. Po
kliknutí do mapového okna se objeví malá červená tečka. Její souřadnice v souř.
systému projektu se zobrazí v okně vedle symbolu |askcor|. Na :num:`#zis-sur`
jsou na ukázku zobrazené  souřadnice vybraného bodu v souřadnicových systémech
S-JTSK (Greenwich) Krovak a S-JTSK (Greenwich) Krovak East North. Ikona
|askcorcopy| umožňuje souřadnice kopírovat do schránky v podobě čtyř hodnot (pro
:num:`#zis-sur`  by to bylo ``4494520.158,-2880372.147,
4746310.700,2931421.671``). 

.. _zis-sur:

.. figure:: images/p_zis_sur.png
   :scale: 55%

   Dialogové okno modulu na zobrazení souřadnic z mapového okna

|3| :sup:`Zásuvný modul silničního grafu`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ve vrstvě polylinií modul vypočte a následně vykreslí nejkratší cestu mezi dvěma
zvolenými body. Je napsaný v programovacím jazyku C++. Umožňuje určit
nejoptimálnější trasu  na základě délky nebo času. Výsledek je automaticky
exportován jako nová vektorová vrstva. 

.. note:: Při výpočtu nejkratší cesty se doporučuje nastavit souřadnicový systém
   projektu dle souřadnicového systému vrstvy polylínií. 

Zásuvný modul cestného grafu aktivujeme v :ref:`panelu správce zásuvných modulů 
<spravca-plugin>`. V liště menu přejdeme na :menuselection:`Vektor --> 
Silniční graf --> Nastavení`. Zobrazí se okno, kde vyplníme základní nastavení
jako jednotku času, vzdálenosti, topologickou toleranci a další, viz. 
:num:`#path-nast`. Na nastavení modulu použijeme vektorovou vrstvu cest České
republiky zobrazenou na :num:`path-vector` dle typu.

.. _path-nast:

.. figure:: images/p_path_nast.png
   :scale: 55%

   Nastavení zásuvného modulu cestného grafu

.. _path-vector:

.. figure:: images/p_path_vector.png
   :scale: 60%

   Cesty České republiky zobrazené dle jejich typu.

V panelu :item:`Nejkratší cesta` použijeme |2| a v mapovém okně kliknutím zvolíme
počáteční a koncový bod cesty. Zobrazí se jako zelená, resp. červená tečka.
Následně nastavíme kritérium, t.j. délku nebo čas a potvrdíme stisknutím 
:item:`Vypočítat`. Po proběhnutí výpočtu  se v mapovém okně zobrazí výsledek v
podobě polylinie, která se dá exportovat jako nová vektorová vrstva (použitím 
:item:`Export`).Tlačítko :item:`Vyčistit` slouží na smazání obsahu políček.
Postup je znázorněný na :num:`#path`.

.. _path:

.. figure:: images/p_path.png
   :scale: 60%

   Použití zásuvného modulu cestného grafu a výpočet nejoptimálnější cesty

.. tip:: Pokud nevidíme panel :item:`Nejkratší cesta`, přidáme ho z menu lišty 
   :item:`Zobrazit` (:menuselection:`Zobrazit --> Panely --> Nejkratší cesta`),
   jak je to znázorněno na :num:`#path-menu`.
  
    .. _path-menu:
    
    .. figure:: images/p_path_menu.png
       :scale: 55%

       Zobrazení dialogového okna na výpočet nejkratší cesty

|4| :sup:`Zásuvný modul prostorových dotazů`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pomocí tohoto zásuvného modulu lze vykonávat různé prostorové dotazy. Mezi dostupné
prostorové  vztahy patří vztah dotyku, rozpojení, křížení, protínání nebo
překryvu. Funkcionalita je založená na knihovně 
`GEOS <https://en.wikipedia.org/w/index.php?title=JTS_Topology_Suite&redirect=no#GEOS_Library>`_.
Vždy je nutné pracovat s vrstvou obsahující zdrojové prvky a vrstvou s
referenčními prvky. 

Se zásuvným modulem začneme pracovat tak, že klikneme na ikonu modulu |4| nebo z
menu jako :menuselection:`Vektor --> Prostorový dotaz --> Prostorový dotaz`.
Potom v dialogovém okně s názvem *Prostorový dotaz* nastavíme zdrojové a
referenční vrstvy, prostorový vztah (operátor) a zvolíme zda se jedná o nový
výběr, nebo vybíráme z již existujícího výběru.

Ukážeme si to na příkladě výběru všech obcí v České republice (:map:`obce`), ve
kterých se nachází požární stanice (:map:`pozarni_stanice`).Použití je znázorněné
na :num:`#p-pr-dot`. Po proběhnutí výběru zvolením :item:`Použít` se otevře
další okno (na :num:`#p-pr-dot` vpravo). V tomto kroku můžeme tlačítkem 
|mActionNewVectorLayer| vytvořit vektorovou vrstvu z výběru, |selectcreatelayer|
můžeme pokračovat s výběrem a provádět dalším podvýběry, volbou |checkbox|
se dokážeme přibližovat k výsledným objektům, případně zapisovat zprávy.  

.. _p-pr-dot:

.. figure:: images/p_pd_menu.png
   :scale: 60%

   Použití zásuvného modulu prostorových dotazů (prvek obsahuje ...)

.. _p-pr-vysl:

.. figure:: images/p_pd_vysl.png
   :scale: 70%

   Obce České republiky s požární stanicí

|5| :sup:`OpenLayers Plugin` 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*OpenLayers Plugin* (:menuselection:`Web --> OpenLayers Plugin`)  umožňuje
přidávat do mapového okna množství obrazových služeb z Google, Bing, Yahoo a
OpenStreetMap (:num:`#plp`). Satelitní snímky těchto služeb se mohou lišit jak
datumem, tak kvalitou v závislosti od lokality nebo poskytovatele. Podmínkou pro
použití zásuvného modulu je dobrý přístup k internetu. Na :num:`p-olm`  je
příklad načtení čtyř různých vrstev s detailem pro určitou oblast.

.. _plp:

.. figure:: images/olp.png
   :scale: 70%

   OpenLayers Plugin z lišty menu

.. _p-olm:

.. figure:: images/p_olm.png
   :class: large

   Ukážka vrstev OpenStreetMap :fignote:`(1)`, OpenCycleMap :fignote:`(2)`, Bing
   Road :fignote:`(3)` a MapQuest-OSM :fignote:`(4)` pro vybranou část Prahy.

.. note:: Další ze zmíněných modulů jsou (budou) obsahem Školení pro pokročilé.
