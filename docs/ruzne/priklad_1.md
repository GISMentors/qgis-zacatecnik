# Ukázka jednoduchých prostorových funkcí

Kolik procent území ČR je ve vzdálenosti do 100 km od hranice Hlavního
města Prahy?

## Data

`kraje.shp`

## Řešení

1.  Nástrojem *Buffer* vytvoříme obalovou zónu 100 km kolem Prahy.
2.  Nástrojem *Dissolve* sloučíme kraje a vytvoříme hranici ČR.
3.  Vypočteme plochu ČR.
4.  Nástrojem *Intersect* vytvoříme průnik obalové zóny s hranicí ČR.
5.  Vypočteme plochu průniku a procenta vybrané plochy k původní ploše.

> [!NOTE]
> Postup řešení v programu ArcGIS Desktop je dostupný
> [zde](http://maps.fsv.cvut.cz/frvsgis/web.html). S Open Source
> programem QGIS však lze dosáhnout stejného výsledku.

## Postup v QGIS

Po spuštění programu QGIS se zobrazí standardní rozhraní, viz
`Popis rozhraní <popisrozhrani>`. Souřadnicový systém projektu je
přednastavený na WGS 84 (`4236`), což lze zkontrolovat ve stavovém řádku
vpravo dole. Budeme pracovat s daty České republiky, kde se obvykle
používá souřadnicový systém S-JTSK (`5514`).

V prvním kroku proto nastavíme souřadnicový systém projektu. Z menu
lišty vybereme `Nastavení --> Možnosti`. Otevře se dialogové okno, kde v
záložce `SRS` nastavíme `Vždy začít nové projekty s tímto SRS` na
`EPSG:5514 - S-JTSK (Greenwich)/Krovak East North`, a to kliknutím na
ikonku <sup>Vyberte SRS</sup>. Tento souřadnicový systém nastavíme i pro
nové vrstvy v položce `SRS pro nové vrstvy` a `Použít výchozí SRS`. Na
závěr povolíme
<img src="../images/icon/checkbox.png" style="width:1.5em"
alt="box_yes" /> `"on-the-fly" SRS transformaci` pro případ, že bychom v
projektu pracovali s vrstvami v souřadnicovém systému, který je odlišný
od systému projektu. Postup je popsaný v kapitole
`Souřadnicový systém<sour-system>`.

V dalším kroku kliknutím na <sup>Přidat vektorovou vrstvu</sup> do
mapového okna přidáme vrstvu `kraje.shp`. Tlačítkem <sup>Vybrat prvky
oblastí nebo jednoklikem</sup> klikneme do mapy na místo, kde se nachází
kraj Hlavního města Prahy (`u-select-praha`).

> [!NOTE]
> V případě, že by šlo o složitější výběr, použijeme <sup>Vybrat prvky
> pomocí vzorce</sup> a prvky vybereme atributovým dotazem.

<div id="u-select-praha">

<figure>
<img src="images/u-select-praha.png" class="middle"
alt="images/u-select-praha.png" />
</figure>

</div>

Následně vytvoříme obalovou zónu 100 km od hranice Prahy. Použijeme
prostorovou analýzu <sup>Buffer</sup>. Z menu lišty vybereme `Vektor 
--> Nástroje geoprocessingu --> Obalové zóny`. V dialogovém okně
nastavíme vstupní vrstvu, t.j. `kraje`, zaklikneme
<img src="../images/icon/checkbox.png" style="width:1.5em"
alt="box_yes" /> <sup>Použít pouze vybrané prvky</sup>, protože chceme
obalovou zónu jen kolem konkrétního vybraného kraje. Míru aproximace
zvýšíme na `70`, protože předvolená hodnota `5` segmentů je málo na to,
aby obalová zóna odpovídala kruhu. Dále nastavíme velikost obalové zóny
v metrech, název výstupního souboru a povolíme
<img src="../images/icon/checkbox.png" style="width:1.5em"
alt="box_yes" /> <sup>Přidat výsledek do mapového okna</sup> a potvrdíme
`OK` (`u-p100km`).

> [!NOTE]
> Maximální možný počet segmentů na aproximaci je `99`. Výhodou je sice
> přesnější výsledek, nicméně výpočty budou trvat delší dobu.

<div id="u-p100km">

<figure>
<img src="images/u-p100km.png" class="small"
alt="images/u-p100km.png" />
<figcaption>Tvorba obalové zóny velikosti 100 km kolem hranice
Prahy.</figcaption>
</figure>

</div>

Do mapového okna se přidá nová vektorová vrstva `P100km`. Nastavíme jí
styl `pravým tlačítkem myši --> Vlastnosti --> Styl`, například jako na
`u-p100km-styl` transparentní výplň, červené ohraničení široké 1 mm.

<div id="u-p100km-styl">

<figure>
<img src="images/u-p100km-styl.png" class="middle"
alt="images/u-p100km-styl.png" />
<figcaption>Nastavení stylu obalové zóny.</figcaption>
</figure>

</div>

Dále provedeme sjednocení všech krajů, resp. vrstvu České republiky.
Budeme ji potřebovat na určení plochy ČR. Využijeme nástroj
geoprocessingu <sup>Rozpustit</sup>. Před touto funkcí ještě zrušíme
výběr kraje Prahy pomocí <sup>Zrušit výber prvků ve všech
vrstvách</sup>. Výstupní vektorovou vrstvu pojmenujeme `hraniceCR`, viz
`u-dissolve`.

<div id="u-dissolve">

<figure>
<img src="images/u-dissolve.png" class="small"
alt="images/u-dissolve.png" />
<figcaption>Spojení všech krajů do jednoho polygonu pomocí nástroje
<em>Dissolve</em>.</figcaption>
</figure>

</div>

Otevřeme atributovou tabulku vrstvy `hraniceCR` (pravým
`Otevřít atributovou tabulku`) a pak použijeme kalkulačku polí - ikona v
horní liště atributové tabulky <sup>Otevřít kalkulátor polí</sup>.
Vytvoříme nový atribut (pole) s názvem `area_sum` (desetinné číslo), do
kterého vložíme hodnotu plochy polygonu. Datový typ nastavíme tedy jako
`real`, šířka např. `15` a jako výraz napíšeme `$area` (`u-area`). Změny
uložíme ikonou a editovací režim vypneme opětovným stisknutím .

> [!NOTE]
> Výraz nemusíme psát ručně. V středním poli dialogového okna kalkulačky
> je množství položek. V našem případě vybereme
> `Geometrie --> $area (dvojklik)`.

<div id="u-area">

<figure>
<img src="images/u-hraniceCR-area.png"
alt="images/u-hraniceCR-area.png" />
<figcaption>Vytvoření atributu s výměrou České republiky.</figcaption>
</figure>

</div>

Poté použijeme nástroj <sup>Průsečník</sup>, kde vstupem budou vrstvy
`hraniceCR` a `P100km`. Výsledek je zobrazen na `intersect-map`.

<div id="intersect-map">

<figure>
<img src="images/u_intersect-map.png"
class="middle Výsledek nástroje *Intersect*, území České republiky ve vzdálenosti 100 km od hranic Prahy."
alt="images/u_intersect-map.png" />
</figure>

</div>

Posledním krokem je určení procentuálního zastoupení plochy republiky do
100 km od Prahy. Nejdřív vypočteme plochu průniku `hraniceCR_intersect`,
přičemž postupujeme obdobně jako při ploše vrstvy `hraniceCR` (vytvoříme
sloupec s názvem `area`).

> [!TIP]
> Kvůli přehlednosti vymažeme všechny nepotřebné sloupce v atributové
> tabulce vrstvy `hraniceCR_intersect` tak, že nejdříve zapneme
> editovací mód kliknutím na <sup>Prepnout režim editaci</sup>, potom
> zvolíme <sup>Smazat sloupec</sup> a označíme názvy těch atributů,
> které chceme vymazat. Ponecháme jenom pole `area_sum` a `area`.

Pak přidáme nový atribut `procento`, do kterého pomocí mapové kalkulačky
vložíme výsledek `"area"/"area_sum * 100"`. Ten je na `vysledok-u1`
(48,6 % území České republiky je ve vzdálenosti do 100 km od hranic
Prahy).

<div id="vysledok-u1">

<figure>
<img src="images/u-vysledok-u1.png" alt="images/u-vysledok-u1.png" />
<figcaption>Výpočet procentuálního zastoupení území ve vzdálenosti do
100 km od Prahy.</figcaption>
</figure>

</div>
