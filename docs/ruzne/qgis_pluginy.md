# QGIS pluginy

QGIS umožňuje práci se zásuvnými moduly, tzv. `pluginy
<https://en.wikipedia.org/wiki/Plug-in_(computing)>`. Ve všeobecnosti se
jedná o software, které nepracuje samostatně, ale jako doplňkový modul
jiné aplikace a tím rozšiřuje její funkčnost. V současnosti existuje pro
QGIS víc než 300 zásuvných modulů. Všechny jsou napsané v programovacím
jazyku [Python](https://www.python.org/) nebo
[C++](https://isocpp.org/). Mnohé z nich jsou stále ve vývoji. Jejich
kompletní seznam spolu s příslušnou charakteristikou, informacemi
například o použití, potřebné minimální verzi QGISu, domovské stránce,
autorech, o počtu stáhnutí, o tom, které jsou označené jako
nejoblíbenější je dostupný [zde](https://plugins.qgis.org/plugins/).

Moduly jsou udržované vývojovým týmem QGISu ([QGIS Development
Team](http://qgis-development-team.software.informer.com/)) a jsou
automaticky součástí každé jeho distribuce. Externí pluginy jsou napsané
v programovacím jazyce Python a jsou udržovány příslušnými autory.
Chyby, angl. *bugy* v modulech by měly být zveřejnovány a dostupné na
stránkách [projektu](http://hub.qgis.org/projects/qgis-user-plugins).

## Správce zásuvných modulů

V prvním kroku v menu zvolíme `Zásuvné moduly --> Spravovat a instalovat
zásuvné moduly`, ikona . Spustí se dialogové okno (`vse`), které slouží
k prohlížení, vypínání a zapínání dostupných modulů příslušné verze
QGISu.

<div id="vse">

<figure>
<img src="images/p_vse.png" alt="images/p_vse.png" />
<figcaption>Správce zásuvných modulů v prostředí QGIS.</figcaption>
</figure>

</div>

Pod položkou <sup>Instalované</sup> najdeme ty, které byly nainstalované
automaticky při instalaci QGISu. Z nich jsou některé načtené, jiné lze
dočasně povolit nebo zakázat zaškrtnutím ikonky
<img src="../images/icon/checkbox_unchecked.png" style="width:1.5em"
alt="checkbox_unchecked" />. V případě, že klikneme na některý z modulů,
zobrazí se jeho charakteristika nebo účel, spolu s dalšími informacemi
jako je název, popis, počet hodnocení a stáhnutí modulu, reprezentující
ikona, kategorie, instalovaná nebo dostupná verze, autor, seznam změn a
další. Na `plugininfo` je znázorněný příklad zásuvného modulu s názvem
<img src="../images/icon/q2t.png" style="width:1.5em" alt="q2t" />
<sup>Qgis2threejs</sup>.

<div id="plugininfo">

<figure>
<img src="images/p_info.png" alt="images/p_info.png" />
</figure>

</div>

Seznam všech dostupných pluginů je možno zobrazit a konkrétní modul
načíst zvolením <sup>Nenainstalováno</sup> a spuštěním
<span class="title-ref">Instalovat zásuvný modul</span>. Následně se dá
tento modul přeinstalovat nebo úplně odinstalovat (`p-instal`).

<div id="p-instal">

<figure>
<img src="images/p_instal.png"
class="middle Seznam nenainstalovaných modulů :fignote:`(1)`, instalace :fignote:`(2)`, možnost odinstalování :fignote:`(3)` nebo přeinstalování :fignote:`(4)` kteréhokoli z modulů."
alt="images/p_instal.png" />
</figure>

</div>

Pod záložkou <sup>Aktualizovatelný</sup> se nachází zásuvné moduly,
které jsou dostupné i v novější verzi. Záložka <sup>Nastavení</sup>
obsahuje nastavení týkající se kontroly aktualizací modulů,
experimentálních a neschválených modulů a zobrazuje i seznam repozitářů,
které lze přidávat, editovat nebo mazat, viz `akt-nast`. Po zaškrtnutí
políček
<img src="../images/icon/checkbox_unchecked.png" style="width:1.5em"
alt="checkbox_unchecked" /> při položkách
<span class="title-ref">Zobrazit také experimentální</span> a
<span class="title-ref">neschválené moduly</span> je k dispozici téměř
500 zásuvných modulů.

<div id="akt-nast">

<figure>
<img src="images/p_akt_nast.png" class="middle"
alt="images/p_akt_nast.png" />
<figcaption>Záložky související s aktualizacemi a nastavením zásuvných
modulů.</figcaption>
</figure>

</div>

> [!TIP]
> Seznam zásuvných modulů může uživatel uspořádat dle svých potřeb. Po
> stisknutí pravého tlačítka myši v seznamu modulů je k dispozici jejich
> uspořádání dle abecedy, počtu stáhnutí, hlasů nebo stavu (`rad`).
>
> <div id="rad">
>
> <figure>
> <img src="images/p_rad.png" alt="images/p_rad.png" />
> <figcaption>Možnosti seřazení zásuvných modulů.</figcaption>
> </figure>
>
> </div>

> [!NOTE]
> Je zapotřebí připomenout, že zásuvné moduly v oficiálních repozitářech
> byly testovány, nicméně jednotlivé repozitáře mohou obsahovat i méně
> ověřené moduly různé kvality a stadia vývoje. Proto je dobrou pomůckou
> zobrazení hodnocení či počtu
> <img src="../images/icon/osm_star.png" style="width:1.5em" alt="star" />
> <img src="../images/icon/osm_star.png" style="width:1.5em" alt="star" />
> <img src="../images/icon/osm_star.png" style="width:1.5em" alt="star" />.

> [!TIP]
> Pokud známe alespoň přibližný název konkrétního modulu, při
> vyhledávání může pomoci vyplnění políčka
> <span class="title-ref">Hledat</span> v dialogovém okně.

## Příklady zásuvných modulů

V další části si částečně ukážeme některé z užitečných a často
používaných zásuvních modulů programu QGIS:

<div class="only">

latex

<div class="tabularcolumns">

p{10cm}\|

</div>

</div>

<div class="only">

html

<div class="cssclass">

border

</div>

</div>

| Zásuvný modul \| Charakteristika \|                                                                                                                |     |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| <img src="../images/icon/another_dxf_importer.png" style="width:1.5em"                                                                             
 alt="1" /> <sup>Another DXF Importer</sup> \| importuje formát `*.dxf`\|                                                                            |     |
| <img src="../images/icon/coordinate_capture.png" style="width:1.5em"                                                                               
 alt="2" /> <sup>Získání souřadnic</sup> \| získává souřadnice myši \|                                                                               |     |
| <img src="../images/icon/roadgraph.png" style="width:1.5em" alt="3" /> <sup>Zásuvný modul síťových analýz</sup> \| řeší problém nejkratší cesty \| |     |
| <img src="../images/icon/quickmapservices.png" style="width:1.5em"                                                                                 
 alt="4" /> <sup>Quick Map Services</sup> \| načítání mapových služeb \|                                                                             |     |
| <img src="../images/icon/geodata_cz_sk.png" style="width:1.5em"                                                                                    
 alt="5" /> <sup>GeoData CZ/SK</sup> \| mapové služby a jiné zdroje z ČR a SR                                                                        |     |
| <img src="../images/icon/ruian.png" style="width:1.5em" alt="6" /> <sup>RUIAN</sup> \| načítání dat z RÚIAN \|                                     |     |

### <img src="../images/icon/another_dxf_importer.png" style="width:1.5em"
alt="1" /> <sup>Another DXF Importer</sup>

V případě, že máme k dispozici soubor AutoCAD DXF ([Drawing Exchange
Format](https://en.wikipedia.org/wiki/AutoCAD_DXF)), do prostředí
programu QGIS ho umíme načíst buď přímo přes GDAL/OGR, pokud však import
nedopadne podle očekávání pak je možné využít zásovný modul Another DXF
Importer. V předchozích verzích byl dostupný také modul Konvertor
Dxf2Shp, ten se však již dále nevyvíjí.

<div id="dxf2shp">

<figure>
<img src="images/p_anotherdxfimporter.png"
alt="images/p_anotherdxfimporter.png" />
<figcaption>Dialogové okno modulu pro import AutoCAD DXF
souboru.</figcaption>
</figure>

</div>

Po načtení modulu ze `správce zásuvných modulů <spravce-plugin>` se po
kliknutí na ikonu
<img src="../images/icon/another_dxf_importer.png" style="width:1.5em"
alt="1" /> objeví dialogové okno, kde je zapotřebí nastavit vstupní
`*.dxf` soubor, název, cestu a typ nového `*.shp` souboru nebo
GeoPackage.

> [!NOTE]
> Pokud se po spuštění modulu tlačítkem `OK` zobrazí dialogové okno
> související se souřadnicovými systémy, systém nastavíme.

### <img src="../images/icon/coordinate_capture.png" style="width:1.5em"
alt="2" /> <sup>Získání souřadnic</sup>

Tento zásuvný modul se používá velmi jednoduše a umožňuje zobrazení
souřadnic myši pro dva vybrané souřadnicové systémy. Dialogové okno je
zobrazeno na `zis-sur`. Kliknutím na ikonu
<img src="../images/icon/checkbox.png" style="width:1.5em"
alt="geographic" /> nastavíme požadovaný souřadnicový systém, zvolením
<img src="../images/icon/coordinate_capture.png" style="width:1.5em"
alt="2" /> <sup>Zapnout získávání</sup> se symbol myši změní na
<img src="../ruzne/images/p_reticle.png" style="width:1.5em"
alt="reticle" />. Po kliknutí do mapového okna se objeví malá červená
tečka. Její souřadnice v souřadnicovém systému projektu se zobrazí v
okně vedle symbolu
<img src="../ruzne/images/p_askcor.png" style="width:1.5em"
alt="askcor" />. Na `zis-sur` jsou na ukázku zobrazené souřadnice
vybraného bodu v souřadnicových systémech s EPSG 4326 (WGS 84) a 5514
(S-JTSK (Greenwich) / Krovak East North). Ikona
<img src="../ruzne/images/p_askcorcopy.png" style="width:1.5em"
alt="askcorcopy" /> umožňuje souřadnice kopírovat do schránky v podobě
čtyř hodnot (pro `zis-sur` by to bylo
`13.71955,49.85887,-796222.963,-1061087.065`).

<div id="zis-sur">

<figure>
<img src="images/p_zis_sur2.png" alt="images/p_zis_sur2.png" />
<figcaption>Dialogové okno modulu na zobrazení souřadnic z mapového
okna.</figcaption>
</figure>

</div>

> [!NOTE]
> Pro novou verzi QGIS byl tento modul portován a aktuálně není přeložen
> do češtiny. Funkcionalita však zústává v zásadě stejná.

### <img src="../images/icon/roadgraph.png" style="width:1.5em" alt="3" /> <sup>Zásuvný modul síťových analýz</sup>

Ve vrstvě polylinií modul vypočte a následně vykreslí nejkratší cestu
mezi dvěma zvolenými body. Je napsaný v programovacím jazyku C++.
Umožňuje určit optimální trasu na základě délky nebo času. Výsledek je
automaticky exportován jako nová vektorová vrstva.

> [!NOTE]
> Při výpočtu nejkratší cesty se doporučuje nastavit souřadnicový systém
> projektu dle souřadnicového systému vrstvy polylinií.

Zásuvný modul aktivujeme v `panelu správce zásuvných modulů 
<spravce-plugin>`. V liště menu přejdeme na `Vektor --> 
Silniční graf --> Nastavení`. Zobrazí se okno, kde vyplníme základní
nastavení jako jednotku času, vzdálenosti, topologickou toleranci a
další, viz `path-nast`. Na nastavení modulu použijeme vektorovou vrstvu
cest České republiky zobrazenou na `path-vector` dle typu.

<div id="path-nast">

<figure>
<img src="images/p_path_nast.png" class="small"
alt="images/p_path_nast.png" />
<figcaption>Nastavení zásuvného modulu cestného grafu.</figcaption>
</figure>

</div>

<div id="path-vector">

<figure>
<img src="images/p_path_vector.png" class="middle"
alt="images/p_path_vector.png" />
<figcaption>Silnice České republiky zobrazené dle jejich
typu.</figcaption>
</figure>

</div>

V panelu <span class="title-ref">Nejkratší cesta</span> použijeme
<img src="../images/icon/coordinate_capture.png" style="width:1.5em"
alt="2" /> a v mapovém okně kliknutím zvolíme počáteční a koncový bod
cesty. Zobrazí se jako zelená, resp. červená tečka. Následně nastavíme
kritérium, t.j. délku nebo čas a potvrdíme stisknutím
<span class="title-ref">Vypočítat</span>. Po proběhnutí výpočtu se v
mapovém okně zobrazí výsledek v podobě polylinie, která se dá exportovat
jako nová vektorová vrstva (použitím
<span class="title-ref">Export</span>). Tlačítko
<span class="title-ref">Vyčistit</span> slouží na smazání obsahu
políček. Postup je znázorněný na `path`.

<div id="path">

<figure>
<img src="images/p_path.png"
class="middle Použití zásuvného modulu síťových analýz a výpočet nejoptimálnější cesty."
alt="images/p_path.png" />
</figure>

</div>

> [!TIP]
> Pokud nevidíme panel <span class="title-ref">Nejkratší cesta</span>,
> přidáme ho z menu lišty <span class="title-ref">Zobrazit</span>
> (`Zobrazit --> Panely --> Nejkratší cesta`), jak je to znázorněno na
> `path-menu`.
>
> <div id="path-menu">
>
> <figure>
> <img src="images/p_path_menu.png" class="small"
> alt="images/p_path_menu.png" />
> <figcaption>Zobrazení dialogového okna na výpočet nejkratší
> cesty.</figcaption>
> </figure>
>
> </div>

> [!NOTE]
> Tento modul je možno nahradit interním algoritmem, který je dostupný
> mezi nástroji zpracování.

<div id="p-path-proc">

<figure>
<img src="images/p_path_proc.png" class="middle"
alt="images/p_path_proc.png" />
<figcaption>Dialogové okno algoritmu pro hledání nejkratší
cesty.</figcaption>
</figure>

</div>

### <img src="../images/icon/quickmapservices.png" style="width:1.5em"
alt="4" /> <sup>Quick Map Services</sup>

Pomocí tohoto zásuvného modulu je možné připojovat různé mapové služby
postavené na protokolech XYZ nebo WMS. V základním nastavení jsou např.
Open Street Map. Je však možno přidat další a také vyhledávat dle
pozice. K dispozici jsou např. i mapy.cz.

Se zásuvným modulem začneme pracovat tak, že z menu jako
`Web --> QuickMapServices --> ???` vybereme zdroj, který nás zajímá.

<div id="p-qms-dot">

<figure>
<img src="images/p_qms_menu.png"
class="middle Použití zásuvného modulu Quick Map Services"
alt="images/p_qms_menu.png" />
</figure>

</div>

<div id="p-qms-vysl">

<figure>
<img src="images/p_qms_vysl.png" alt="images/p_qms_vysl.png" />
<figcaption>Přidáná mapová služba Open Street Map.</figcaption>
</figure>

</div>

### <img src="../images/icon/geodata_cz_sk.png" style="width:1.5em"
alt="5" /> <sup>GeoData CZ/SK</sup>

*GeoData CZ/SK Plugin*
(`Zásuvné moduly --> GeoData --> Procházet datové zdroje`) umožňuje
přidávat do mapového okna množství dat z oblasti České a SLovenské
republiky obrazových služeb z XYZ a WMS zdrojů a také jiných typů zdrojů
Na `p-geodata` je dialogové okno pluginu.

<div id="p-geodata">

<figure>
<img src="images/p_geodata_cz_sk.png" class="large"
alt="images/p_geodata_cz_sk.png" />
<figcaption>Ukázka dialogového okna pluginu</figcaption>
</figure>

</div>

### <img src="../images/icon/ruian.png" style="width:1.5em" alt="6" /> <sup>RUIAN</sup>

*RUIAN Plugin* umožňuje přidávat do mapového okna dat z registru RÚIAN
(Registr územní identifikace, adres a nemovitostí). Na `p-ruian` je
dialogové okno pluginu.

<div id="p-ruian">

<figure>
<img src="images/p_ruian.png" class="large" alt="images/p_ruian.png" />
<figcaption>Ukázka dialogového okna pluginu</figcaption>
</figure>

</div>

> [!NOTE]
> Další ze zmíněných modulů budou obsahem školení QGIS pro pokročilé, a
> to především GRASS plugin.
