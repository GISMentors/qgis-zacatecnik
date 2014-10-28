Přidávání prostorových dat
==========================

QGIS podporuje široké spektrum prostorových dat. Prostorová data můžeme
rozdělit podle způsobu uložení na lokální a distribuovaná (síťová).
V obouch kategoriích se následně vyskytují data rastrová a vektorová.
Následující kapitoly se snaží čtenáře seznámit s možnostmi vkládání
prostorových dat do programu QGIS. Kapitoly postihují nejčastější základní
formáty a připojení dat. Do programu QGIS je možné ať od základu nebo pomocí
rozšíření vkládat široké spektrum dat, jež nemůže bý obsaženo.

Lokální data
------------


Lokální data jsou uložena na na vašem PC nebo na síťovém disku.

Vektorová data
^^^^^^^^^^^^^^

Nabídka pro načtení vektorové vrstvy se aktivuje v záložce
\"vrstva/Přidat vektorovou vrstvu\" , nebo ikonou viz [obr 1]

.. figure:: images/qgis_ogc_addvector_icons.png
            :width: 350px

Obr 1

Nejčastější volbou vkládání dat je soubor nebo adresář.
Volba adresář umožňuje označit složku ve které se nachází vektorová data.
Potvrzením tlačítkem otevřít QGIS připraví všechna dostupná data uložená
ve složce k načtení. Oběví se potvrzující okno se všemi dostupnými vrstvami.
Vrstvy lze buď označit všechny nebo podržením klávesy ctrl vybrat jen
požadované vrstvy [obr 2].

.. figure:: images/qgis_ogc_addvector_selectfromfolder.png
            :width: 350px

Obr 2

Vložení jen jedné vrstvy je možné označením soubor na [obr 1].
Kliknutím na tlačítko procházet se otevře navigační okno s možností vybrat
formát vektorových dat [obr 3]. Po potvrzení se označená vrstva načte do
mapového pole.

.. figure:: images/qgis_ogc_addvector_choose.png
            :width: 350px

Obr 3

Rastrová data
^^^^^^^^^^^^^

Nabídka pro načtení rastrové vrstvy se aktivuje v záložce
\"vrstva/Přidat rastrovou vrstvu\" , nebo ikonou viz [obr 4]

.. figure:: images/qgis_ogc_addraster_icons.png
            :width: 350px

Obr 4

Nástroj zobrazí okno, kde lze výběrem označit rastrové soubory pro přidání
do mapy [obr 5]. Podržením klávesy \"ctrl\" je možné vybrat více souborů.
V pravém spodním rohu se nachází stejně jako u výběru vektorových vrstev
roletka s podporovanými formáty, pomocí níž lze filtrovat obsah okna.

.. figure:: images/qgis_ogc_addraster_choose.png
            :width: 350px

Obr 5


Výběr souřadnicového systému
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Při vkládání rastrových nebo vektorových dat se může stát, že po potvrzení
výběru je vyžedována specifikace souřadnicového systému vkládaných dat
[obr 6]. Okno se zobrazí v případě, pokud vkládaný soubor neobsahuje vlastní
specifikaci souřadnicového systému, jako například ESRI Shapefile bez souboru
končícího příponou prj \*.prj. V okně výběru je možné vyhledat pomocí filtru
požadovanou projekci.
Zvolení správné projekce je velice důležité pro překrývání více vrstev s
jinou projekcí, měření nebo pro připojování k webovým službám.


.. figure:: images/qgis_ogc_set_proj.png
            :width: 350px

Obr 6


Síťová data
------------
Pod pojmem síťová data jsou reprezentovány především data přístupná
z internetu jako WMS a WFS. Mnohé společnosti používají k ukládání dat
serverové řešení, které není přístupné z internetu, a tak připojení k
databázi PostGIS můžeme provést i z lokální sítě.


Rastrová data
^^^^^^^^^^^^^

Existuje více variant síťových rastrových služeb. Nejrozšířenější službou
je WMS.
Rychlejší, ale méně používanou alternativou k WMS je WMTS, kde \"T\" v názvu
znamená \"Tile\", tedy dlaždice. WMTS přistupuje k již předgenerovaným dlaždicím,
tudíž tolik nezatěžuje server a data se ke klientovi dostanou rychleji.
Rastrová data je možné ukládat a následně je zobrazovat přímo v databázích.
QGIS poskytuje možnosti jak pracovat s daty z databází PostGIS nebo Oracle.


WMS/WMTS
^^^^^^^^

Bezesporu nejpoužívanější webovou službou je WMS (Web Map Service). Služba WMS
se postupem času vyvíjela a dnes můžeme narazit na různé verze
1.0.0, 1.1.1 nebo 1.3.0. . QGIS podporuje všechny werze WMS, a tak lze bez
obav přistupovat k jakékoliv publikované službě.
V QGISu je správa WMS a WMTS vrstev umístěna do stejného okna. Do správce se
vstupuje buď ikonkou vlevo, nebo v záložce \"Vrstva/Přidat vrstvu WMS\" [obr 7].

.. figure:: images/qgis_ogc_addwms_icons.png
            :width: 350px

Obr 7

Pokud nejsou ve správci vložené žádné připojení, dá se tak udělat přes
tlačítko přidat [obr 8].

.. figure:: images/qgis_ogc_addwms_manager.png
            :width: 350px

Obr 8

Přidání a editace připojení služby WMS nebo WMTS probíhá ve formuláři [obr 9].
Pokud není služba zaheslovaná a nebo není potřeba klást na službu speciální
požadavky (ve většině případů), pro úspěšné vložení stačí zadat název služby,
jak jej chceme pro vlastní potřebu, a připojovací URL.


.. figure:: images/qgis_ogc_addwms_add_edit.png
            :width: 350px

Obr 9

Pokud je nastaveno připojení ke službě správně, vyberáním požadované služby z
menu a potvrzením tlačítkem \"Připojit\" proběhne komunikace se serverem.

Pokud bylo v předchozím formuláři [obr 9] zadáno spojení k WMS serveru,
po úspěšném navázání spojení se serverem se zobrazí v závislosti na dostupných
vrstvách a nastavení serveru nabídka bodobná [obr 10]. Nabídka pouze rozšířila
stávající zobrazení okna. V závislosti na dostupných vrstvách serveru se
zobrazí strom, ze kterého je možné vybírat vrstvy pro následné přidání do mapy.
Tak jako tomu bylo u lokálních vektorových a rastrových dat, je možné použít
klávesu \"ctrl\" k označení více vrstev. Přidání vrstvy může proběhnout jak na
nejnižší úrovni stromu, kde se zpravidla jedná o licenční logo služby, tak je
možné označit nejsyšší úroveň, čímž budou přidány všechny dostupné vrstvy.
Pokud server umožňuje poskytování dat ve více formátech, volba formátu se
prování ve spodní části okna. Na obrázku 9 je v levé spodní části vypsáno
\"WGS 84\" a na stejné úrovni se nachází tlačítko změnit. Již bylo zmíněno,
že služby WMS lze konzumovat ve více formátech (PNG,JPEG,GIF...), taktéž lze
specifikovat souřadnicový systém, v jakém bude služba vyžadována. Změna
souřadnicového systému se provádí pod vyvoláním nabídky tlačítkem \"změnit\".
Okno pro změnu projekce je shodné s oknem definování projekce vkládaných
lokálních rastrových a vektorových dat [obr 6]. QGIS v okně zobrazí poze
podporované souřadnicové systémy ze strany serveru. Po nastavení všech
parametrů služby a výběru vrstev proběhne přidání vrstvy do mapového pole
tlačítkem přidat. Pokud bylo vybráno více vrstev, jeví se v layer manageru
jako jedna.


.. figure:: images/qgis_ogc_addwms_choose.png
            :width: 350px

Obr 10

Jak bylo zmíňeno, správa WMS a WMTS probíhá ve stejném okně. V předchozím
kroku bylo ukázáno jak vkládat WMS služby. Pro připojení WMTS služby je
potřeba v nabídce přidání nového spojení zadat URL na platný WMTS server.
Po vybrání služby a připojení přes tlačítko připojit proběhne komunikace s
WMTS serverem. Po navázání spojení se ve správci vrstev aktivuje záložka
\"sady dlaždic\" [obr 11]. Tabulka zobrazuje dostupné vrstvy ze serveru.
V jednotlivých sloupcích je možné číst informace oo názvu vrstvy, poskytovaném
formátu i projekci. V tabulce není možné vybrat více vrstev najednou, stačí
vybrat jednu vrstvu a potvrdit ok.


.. figure:: images/qgis_ogc_addwmts_choose.png
            :width: 350px

Obr 11

Vektorová data
^^^^^^^^^^^^^^
Pro připojení síťových prostorových dat je připraven formát WFS. Správce WFS
vrstev se aktivuje buď ikonkou vlevo, nebo v záložce
\"Vrstva/Přidat vrstvu WFS\" [obr 12].

.. figure:: images/qgis_ogc_addwfs_icons.png
            :width: 350px

Obr 12

Okno správce [obr 13] umožňuje přidání, odebrání služby nebo slouží k výběru
vrstev.


.. figure:: images/qgis_ogc_addwfs_manager.png
            :width: 350px

Obr 13

Formulář přidání nové služby se aktivuje tlačítkem \"Nové\". Ve formuláři [obr 14]
stačí v případě nezaheslované služby vyplnit pouze URL a pojmenování služby.
V případě zaheslované služby jsou vyžadovány přihlašovací údaje.

.. figure:: images/qgis_ogc_addwfs_add.png
            :width: 350px

Obr 14

Po potvrzení a připojení ke službě ze správce tlačítkem \"Připojit\" se zobrazí
poskytované vrstvy WFS serverem [obr 15]. Tak jako v případě WMS lze změnit
souřadnicový systém sloužící ke stahování dat. Změna se provádí pod tlačítkem
\"změnit\" ve spodní pravé části. Výběr více vrstev pro přidání lze uskutečnit
pomocí klávesy \"ctrl\". Potvrzením \"ok\" proběhne přidání vrstev do mapy.



.. figure:: images/qgis_ogc_addwfs_choose.png
            :width: 350px

Obr 15
