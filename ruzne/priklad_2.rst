.. |mActionSelect| image:: ../images/icon/mActionSelect.png
   :width: 1.5em


Ukázka zpracování dat
---------------------

V následující ukázce je popsán postup zpracování dat o obcích ČR, které jsou 
získány z `RÚIANu <http://www.cuzk.cz/ruian/RUIAN.aspx>`_. Tyto data zkombinujeme z daty, která jsou poskytována
`Statistickým úřadem <https://www.czso.cz/>`_. 

Tento postup je zkloubením základních postupů, které jsou součástí školení pro 
začátečníky. Požadovaným výsledkem je jednak grafická vizualizace různých 
statistických údajů, které jsou odvozeny ze základních ukazatelů, ale také 
zkloubení dat pomocí prostorových analýz s jinými datovými sadami.


Podkladová data
===============

Jak již bylo zmíněno, budeme používat datovou sadu **obcí ČR** z datasetu *RÚIAN*. 

Další datová sada pochází ze statistického úřadu. Tyto data poskytují různorodé
údaje definující sadu faktorů popisující každou obec. 
Data je možné získat `zde <https://www.czso.cz/csu/czso/csu_a_uzemne_analyticke_podklady>`_
(**Aktuální údaje za všechny obce ČR (data mimo SLDB)**) i s popisem evidovaných hodnot.


Příprava dat
============

Jako první si načteme vrstvu obcí. Můžeme použít například data ze `školení QGIS 
<http://training.gismentors.eu/geodata/qgis/data.zip>`_.

Data stáhnuté ze statistického úřadu si upravíme pro import do QGISu. Jako první
si odstraníme řádky 1-3,5,6 a takto upravenou tabulku si uložíme do formátu 
:map:`CSV`.

.. warning:: Některé sloupce, které mají číslenou hodnotu je vhodné upravit. 
   Například sloupce spadající pod kategorii 30 (výměry druhů pozemků) obsahujou
   pomlčku. Při importu 
   takovýchto dat bude pak atribut používán jako *textový řetězec* a ne jako 
   *číslo*.

   Takovéto hodnoty je lepší hromadně nahradit vhodnou hodnotou.
   Podobný případ se týká například sloupce 8.5 (počet dlouhodobě 
   nezaměstnaných). Zde jsou sice uvedeny všude *čísla*, ale pokud je celé číslo
   čtyřciferné tak jsou stovky a tisíce *odděleny mezerou*. I tento případ je
   nutné opravit, jinak *není možné provádět matematické operace*.

   Obě opravy je možné udělat jak před importem, tak až po importu. Výběr záleží
   na uživateli.

Takto upravený soubor načteme podle `postupu <http://training.gismentors.eu/qgis-zacatecnik/vektorova_data/import_delim.html>`_
s ohledem na to, že importujeme *data bez geometrie*. 
Vrstvu pro naše účely pojmenujeme :item:`stat`

.. _imported_data:

.. figure:: images/stat_imported_data.png
   :class: large
        
   Import tabulkových dat a zobrazení obou datových sad v QGISu.


Připojení dat
=============

Dalším krokem je připojení dat z vrstvy :item:`stat` k vrstvě :item:`obce` tak,
abychom u každé obce viděli všechny atributy z obou vrstev.

Klíčovým je atribut podle kterého se data z obou vrstev spárujou. V tomto
případě použijeme kód obce. Tento atribut se nachází v obou vrstvách - v jedné 
je pojmenován **kod_ob** a v druhé **kodobce**. Je to číselný identifikátor 
unikátní pro každou obec v ČR. Samotné připojení je popsáno `zde 
<http://training.gismentors.eu/qgis-zacatecnik/vektorova_data/join.html>`_. 
V našem případě bude definice připojení vypadat jako na následujícím obrázku 
:num:`#join`.

.. _join:

.. figure:: images/stat_join.png
   :class: small
        
   Připojení atributů vrstvy stat k vrstvě obce.

Po tomto kroku máme všechy data z vrstvy stat připojené ke stávajícím atributům
vrstvy obce a můžeme je využít na další zpracování.
