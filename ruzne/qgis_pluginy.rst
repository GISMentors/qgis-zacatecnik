.. |plug1| image:: ../images/icon/mActionShowRasterCalculator.png
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


QGIS pluginy
------------

QGIS umožňuje prácu so zásuvnými modulmi, tzv. :wikipedia:`plugin
<https://en.wikipedia.org/wiki/Plug-in>`-mi. Vo
všeobecnosti ide o softvéry, ktoré nepracujú samostatne, ale ako
doplnkové moduly inej aplikácie a tým rozširujú jej funkčnosť. V
súčasnosti existuje pre QGIS viac ako 300 zásuvných modulov. Všetky sú
napísané v programovacom jazyku `Python <https://www.python.org/>`_ alebo 
`C++ <https://isocpp.org/>`_. Mnohé z nich sú stále vo vývoji. 
Ich kompletný zoznam spolu s príslušnou charakteristikou, informáciami 
napríklad o použití, potrebnej minimálnej verzii QGISu, domovskej stránke, 
autoroch, o počte stiahnutí, o tom, ktoré sú označované ako najviac obľúbené 
či najmenej hodnotené je dostupný `tu <https://plugins.qgis.org/plugins/>`_.

Moduly sú udržiavané vývojovým tímom QGISu 
(`QGIS Development Team <http://qgis-development-team.software.informer.com/>`_) 
a sú automaticky súčasťou každej jeho distribúcie. Všetky externé pluginy sú 
napísané v programovom jazyku Python a udržiavajú ich príslušní autori.
Chyby (angl. *bugy*) by mali byť zverejnené a dostupné na stránkach 
`tu <http://hub.qgis.org/projects/qgis-user-plugins>`_.

.. _spravca-plugin:

Správca zásuvných modulov
=========================

V prvom kroku prejdeme na lištu menu a zobrazíme správcu zásuvných modulov 
v prostredí QGIS tým, že zvolíme položku |plug1| :sup:`Spravovat a instalovat 
zásuvné moduly` pomocou :menuselection:`Zásuvné moduly --> Spravovat a instalovat
zásuvné moduly`. Spustí sa dialógové okno (:num:`#vse`), ktoré slúži na
prehliadanie, zapínanie či vypínanie dostupných modulov príslušnej verzie QGISu. 

.. _vse:

.. figure:: images/p_vse.png
   :scale: 55%

   Správca zásuvných modulov v prostredí QGIS

Pod položkou |plugin-installed| :sup:`Instalované` nájdeme tie, ktoré boli 
nainštalované automaticky pri inštalácii QGISu. Z nich sú niektoré načítané,
iné možno dočasne povoliť alebo zakázať zaškrtnutím ikonky |checkbox_unchecked|. 
V prípade, že klikneme na niektorý z nich, zobrazí sa jeho charakteristika alebo 
účel spolu s ďalšími informáciami ako je názov, popis, počet hodnotení
a stiahnutí modulu, reprezentujúca ikonka, kategória, inštalovaná či
dostupná verzia, autor, zoznam zmien a iné. Na :num:`plugininfo` je znázornený 
príklad zásuvného modulu s názvom |q2t| :sup:`Qgis2threejs`.

.. _plugininfo:

.. figure:: images/p_info.png
   :scale: 55%

   Charakteristika zásuvného modulu na prehliadanie 3D objektov vo webovom prehliadači

Zoznam všetkých plugin-ov možno zobraziť a konkrétny modul načítať zvolením 
|plugin| :sup:`Nenainstalovano` a spustením :item:`Instalovat zásuvný modul`. 
Následne sa dá tento modul preinštalovať alebo úplne odinštalovať 
(:num:`#p-instal`). 

.. _p-instal:

.. figure:: images/p_instal.png
   :scale: 55%

   Zoznam nenainštalovaných modulov :fignote:`(1)`, inštalácia :fignote:`(2)`, možnosť odinštalovania :fignote:`(3)` alebo preinštalovania :fignote:`(4)` ktoréhokoľvek z nich

Pod záložkou |plugin-upgrade| :sup:`Aktualizovatelný` sa nachádzajú zásuvné 
moduly, ktoré sú dostupné aj v novšej verzii. Záložka |mActionTransformSettings| 
:sup:`Nastavení` obsahuje nastavenia týkajúce sa kontroly aktualizácií modulov,
experimentálnych a neschválených modulov a zobrazuje aj zoznam repozitárov, 
ktoré sa dajú pridávať, editovať alebo mazať, viď. :num:`#akt-nast`. 
Po zaškrtnutí políčok |checkbox_unchecked| pri položkách
:item:`Zobrazit také experimentální` a :item:`neschválené moduly` je 
k dispozícii takmer 500 zásuvných modulov.

.. _akt-nast:

.. figure:: images/p_akt_nast.png
   :scale: 55%

   Záložky súvisiace s aktualizáciami a nastaveniami zásuvných modulov

.. tip:: Zoznam zásuvných modulov môže užívateľ usporiadať ako mu vyhovuje. 
Po stlačení pravého tlačidla myši v zozname modulov je k dispozícii ich 
usporiadanie podľa abecedy, počtu stiahnutí, hlasov alebo stavu (:num:`#rad`).

    .. _rad:

    .. figure:: images/p_rad.png
       :scale: 55%

       Možnosti zoradenia zásuvných modulov
    
.. note:: Je potrebné pripomenúť, že zásuvné moduly v oficiálnych repozitároch 
boli testované, no jednotlivé repozitáre môžu obsahovať aj menej overené moduly 
rôznej kvality a štádia vývoja. Preto je dobrou pomôckou zobrazenie hodnotenia 
či počtu |star| |star| |star|.  

.. tip:: Ak poznáme aspoň približný názov konkrétneho modulu, pri vyhľadávaní 
môže pomôcť vyplnenie políčka :item:`Hledat` v dialógovom okne.

Príklady zásuvných modulov
==========================

V ďalšej časti si aspoň čiastočne ukážeme niektoré z užitočných a často 
používaných zásuvných modulov programu QGIS: 

.. only:: latex
          
   .. tabularcolumns:: |p{5cm}|p{10cm}|
                       
.. only:: html
                                 
   .. cssclass:: border

+------------------------------------------------+-------------------------------------------------+
| Zásuvný modul                			 | Charakteristika  	  	                   |
+================================================+=================================================+
| |1| :sup:`Konvertor Dxf2Shp` 			 | konvertuje formát ``*.dxf`` do formátu ``*.shp``|
+------------------------------------------------+-------------------------------------------------+
| |2| :sup:`Získání souřadnic`     		 | získáva souřadnic myši                          |
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^

V prípade, že máme k dispozícii súbor AutoCAD DXF 
(`Drawing Exchange Format <https://en.wikipedia.org/wiki/AutoCAD_DXF>`_), 
do prostredia programu QGIS ho vieme načítať vďaka zásuvnému 
modulu *Konvertor Dxf2Shp*. Ako intuitívne napovedá názov, prevedieme na 
*Shapefile*.

Po načítaní modulu pomocou :ref:`správcu zásuvných modulov <spravca-plugin>`
sa po kliknutí na ikonu |1| objaví dialógové okno, kde je potrebné nastaviť
vstupný ``*.dxf`` súbor, názov, cestu a typ nového ``*.shp`` súboru, 
viď. :num:`#dxf2shp`. Povolenie |checkbox| :sup:`Exportovat textové značky`
vytvorí extra bodovú vrstvu s označeniami a príslušná ``*.dbf`` tabuľka bude
obsahovať "textové" informácie zo súboru ``*.dxf``. 

.. note:: Ak sa po spustení modulu tlačidlom :item:`OK` zobrazí dialógové
okno súvisiace so súradnicovými systémami, systém nastavíme.

.. _dxf2shp:

.. figure:: images/p_dxf2shp.png
   :scale: 70%

   Dialógové okno modulu na prevod AutoCAD DXF súboru na súbor Shapefile

.. todo:: ??? Export inserts ??? + ??? výstup sa pridá do zoznamu vrstiev 
ako "Data layer" ???

|2| :sup:`Získání souřadnic`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tento zásuvný modul sa používa veľmi jednoducho a umožňuje zobrazenie súradníc
myši pre dva vybrané súradnicové systémy. Dialógové okno je na :num:`#zis-sur`.
Kliknutím na ikonu |geographic| nastavíme požadovaný súradnicový systém, 
zvolením |2| :sup:`Zapnout získávání` sa myš zmení na |reticle|. 
Po kliknutí do mapového okna sa objaví malá červená bodka. Jej súradnice 
v súradnicovom systéme projektu sa zobrazia v okne vedľa symbolu |askcor|. 
Na :num:`#zis-sur` sú na ukážku zobrazené súradnice vybraného bodu v 
súradnicových systémoch S-JTSK (Greenwich) Krovak a S-JTSK (Greenwich) Krovak 
East North. Ikona |askcorcopy| umožňuje súradnice kopírovať do schránky v podobe 
štyroch hodnôt (pre :num:`#zis-sur` by to bolo ``4494520.158,-2880372.147,
4746310.700,2931421.671``).

.. _zis-sur:

.. figure:: images/p_zis_sur.png
   :scale: 55%

   Dialógové okno modulu na zobrazenie súradníc z mapového okna

|3| :sup:`Zásuvný modul silničního grafu`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vo vstve polylínií modul vypočíta a následne vykreslí najkratšiu cestu medzi 
dvoma zvolenými bodmi. Je napísaný v programovacom jazyku C++. Umožňuje určiť 
najoptimálnejšiu trasu na základe dĺžky alebo času.  Výsledok je automaticky 
exportovaný ako nová vektorová vrstva. 

.. note:: Pri počítaní najkratšej cesty sa odporúča nastaviť súradnicový systém
projektu podľa súradnicového systému vrstvy polylínií. 

Zásuvný modul cestného grafu aktivujeme v 
:ref:`paneli správcu zásuvných modulov <spravca-plugin>`. V lište menu prejdeme 
na :menuselection:`Vektor --> Silniční graf --> Nastavení`. Zobrazí sa okno,
kde vyplníme základné nastavenia ako jednotku času, vzdialenosti, topologickú
toleranciu a ďalšie, viď. :num:`#path-nast`. Na predstvenie modulu použijeme
vektorovú vrstva ciest Českej republiky zobrazenú na :num:`path-vector` podľa 
typu.

.. _path-nast:

.. figure:: images/p_path_nast.png
   :scale: 55%

   Nastavenia zásuvného modulu cestnho grafu

.. _path-vector:

.. figure:: images/p_path_vector.png
   :scale: 60%

   Cesty Českej republiky zobrazené podľa typu.

V paneli :item:`Nejkratší cesta` použijeme |2| a v mapovom okne kliknutím 
zvolíme začiatočný a koncový bod cesty. Zobrazí sa ako zelená, resp. červená 
bodka. Následne nastavíme kritérium, t.j. dĺžku alebo čas a potvrdíme stlačením
:item:`Vypočítat`. Po prebehnutí výpočtu sa v mapovom okne zobrazí výsledok 
v podobe polylínie, ktorá sa dá exportovať ako nová vektorová vrstva (použitím
:item:`Export`). Tlačidlo :item:`Vyčistit` slúži na vymazanie obsahu políčok.
Postup je znázornený na :num:`#path`.

.. _path:

.. figure:: images/p_path.png
   :scale: 60%

   Použitie zásuvného modulu cestného grafu a výpočet najoptimálnejšej cesty

.. tip:: Ak nevidíme panel :item:`Nejkratší cesta`, pridáme ju z menu lišty :item:`Zobrazit` ako to znázorňuje :num:`#path-menu`.

    .. _path-menu:
    
    .. figure:: images/p_path_menu.png
       :scale: 55%

       Zobrazenie dialógového okna na výpočet najkratšej cesty

|4| :sup:`Zásuvný modul prostorových dotazů`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|5| :sup:`OpenLayers Plugin` 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _plp:

.. figure:: images/olp.png
   :scale: 70%

   OpenLayers Plugin z lišty menu

