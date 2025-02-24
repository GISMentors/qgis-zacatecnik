# Vlastnosti vrstvy

## Atributová tabulka

Vektorová data se skládájí ze dvou základních složek -- geometrie (body,
linie, polygony) a informací o jednotlivých prvcích tzv. atributů.

Atributovou tabulku otevřeme pomocí ikony <sup>Otevřít atributovou
tabulku</sup> (klávesová zkratka `F6`), nebo pravým kliknutím vyvoláme
kontextové menu a zvolíme `Otevřít atributovou tabulku`. Tabulka slouží
k prohlížení a editaci atributové složky dat. V názvu okna je vypsaný
název vrstvy, celkový počet prvků (<span class="title-ref">Features
total</span>), počet odfiltrovaných prvků
(<span class="title-ref">filtered</span>) a počet prvků ve výběru
(<span class="title-ref">selected</span>).

<figure>
<img src="images/at_table.png" alt="images/at_table.png" />
<figcaption>Atributová tabulka vrstvy.</figcaption>
</figure>

Okno atributové tabulky lze otevírat ve dvou režimech, a to buď v
samostatném okně, nebo jako panel. Přepínat tyto režimy lze v liště
atributové tabulky pomocí funkce<sup>Atributová tabulka jako
panel</sup>. Výchozí chování lze nastavit v hlavním nastavení QGISu
(`Nastavení -> Nastavení...` záložka `Zdroje dat`).

V okně atributové tabulky můžeme zobrazit jak atributovou tabulku
(výchozí), tak i formulář atributů. Tato zobrazení se přepínají pomocí
tlačítek v pravém dolním rohu: <sup>Přepnout na zobrazení tabulky</sup>
a <sup>Přepnout na zobrazení formuláře</sup>.

**Základní funkce atributové tabulky**

- kliknutím na název pole, lze hodnoty seřadit.

- kliknutím na číslo řádku můžeme označit jednotlivé prvky do výběru

- pomocí tlačítka <sup>Přesunout výběr nahoru</sup> lze zobrazit vybrané
  prvky na prvním místě tabulky, což nám vybraná data zpřehlední.

- lze použít funkce výběru, které jsou dostupné i v hlavním okně:

  > - <sup>Vybrat prvky pomocí vzorce</sup>
  > - <sup>Vybrat prvky pomocí vzorce</sup>
  > - <sup>Převrátit výběr prvků</sup>
  > - <sup>Zrušit výběr ve všech vrstvách</sup>
  > - <sup>Posunout mapu na výběr</sup>
  > - <sup>Přiblížit na výběr</sup>

- tlačítko <sup>Vybrat/filtrovat prvky pomocí formuláře (Ctrl+F)</sup>
  umožňuje vytvářet výběr nebo fltrovat prvky za pomocí formuláře (viz
  `vybrat-prvky` ). Pro návrat do atributové tabulky stiskněte tlačítko
  <sup>Přepnout na zobrazení tabulky</sup>.

- pomocí tlačítka <sup>Uspořádat sloupce tabulky</sup> lze měnit pořadí
  sloupců, nebo jednotlivé sloupce skrýt.

<figure>
<img src="images/at_table_sort.png" alt="images/at_table_sort.png" />
<figcaption>Možnost uspořádání sloupců.</figcaption>
</figure>

> [!TIP]
> Pomocí nabídky v levém dolním rohu lze zvolit filtr zobrazených prvků.
> Ve výchozím nastavení filtr zobrazuje všechny prvky ve vrstvě, tedy
> hodnota: `Zobrazit všechny 
> prvky`
>
> Pomocí funkce <sup>Pravidla</sup> podmíněného formátování lze pole v
> atributové tabulce stylizovat na podle námi definovaných pravidel

## Vlastnosti

Vlastnosti vyvoláme dvojklikem na vrstvu nebo pravým tlačítkem myši
kontextové menu a zvolíme `Vlastnosti`.

### Informace

Jako první vidíme ve vlastnostech vrstvy záložku informace. Zde najdeme
základní popis zdrojových dat - cesta k souboru, kódování, souřadnicový
systém, ale i počet prvků a seznam atributů

<figure>
<img src="images/info.png" alt="images/info.png" />
<figcaption>Informace vektorové vrstvy.</figcaption>
</figure>

### Zdroj

Zde nalezneme základní nastavení ke zdroji vrstvy -název vrstvy,
kódování textu, souřadnicový systém (SRS) a nastavení filtru.

<figure>
<img src="images/properties.png" alt="images/properties.png" />
<figcaption>Zdroj vektorové vrstvy.</figcaption>
</figure>

### Styl

#### Symbologie

Pomocí rolovací nabídky vybereme typ symbologie:

- <sup>Jednoduchý symbol</sup> - zde máme na výběr z uložených symbolů.
  V levém sloupci máme zobrazený typ symbolu a jeho jednotlivé části.
  Při kliknutí na konkrétní složku symbolu můžeme měnit její vlastnosti
  (barvy, typ výplně, šířka ohraničení atd.).

<figure>
<img src="images/symbol_simple.png" alt="images/symbol_simple.png" />
<figcaption>Jednoduchá symbologie. V levé části vlastnosti označené
složky symbolu.</figcaption>
</figure>

> [!TIP]
> Pomocí tlačítek můžeme další složky symbolu přidávat , odebírat ,
> zamykat nebo měnit jejich pořadí , . Tímto způsobem si můžeme vytvořit
> vlastní symbologii.

- <sup>Kategorizovaný</sup> - vhodný pro kategoriální proměnné

  > - `sloupec` - pro výběr atributu
  > - `barevný rozsah` - výběr barev
  > - pro vytvoření kategorii kliknout na `klasifikovat`

<figure>
<img src="images/symbol_kat.png" alt="images/symbol_kat.png" />
<figcaption>Kategorizovaná symbologie.</figcaption>
</figure>

- <sup>Odstupňovaný</sup> - vhodný pro spojité proměnné

  > - nastavení obdobné jako u možnosti <sup>Kategorizovaný</sup>
  > - možnost režimu intervalů a počet tříd
  > - možnost zobrazení histogramu

<figure>
<img src="images/symbol_odst.png" alt="images/symbol_odst.png" />
<figcaption>Odstupňovaná symbologie.</figcaption>
</figure>

#### Popisky

Kromě rozlišení prvků pomocí symbologie lze také přidat k jednotlivým
prvkům popisek na základě jednoho z atributů.

<figure>
<img src="images/labels.png" alt="images/labels.png" />
<figcaption>Vlastnosti popisků vrstvy.</figcaption>
</figure>

Na této záložce je nejdříve nutné vybrat z rolovací nabídky položku
<sup>Single labels</sup>. Tím se nám otevřou možnosti stylizace popisků,
kde můžeme nastavit formát textu, obalovou zónu kolem textu, pozadí,
stínování, možnosti umístění a vykreslování. Nejdříve je ale nutné
nastavit zdroj popisku. Pomocí rolovací nabídky `Popisky z` vybreme
zdrojový atribut popisku.

<figure>
<img src="images/labels_sample.png" alt="images/labels_sample.png" />
<figcaption>Příklad popisků s použitím obalové zóny textu.</figcaption>
</figure>

<div class="noteadvanced">

Jako zdroj popisků lze použít i vzorec, a to buď přímým vepsáním do
nabídky, nebo vytvořením vzorce pomocí kalkulátoru .

</div>

## Panel stylování

Pro pohodlnější práci se stylováním, slouží panel stylování
`Stylování vrstvy`, který lze aktivovat pravým kliknutím na prázdné
místo v hlavním panelu a výběrem z nabídky nebo mocí klávesové zkratky
`F7`. Výhodou panelu stylování je, že lze rychle, bez znovuotevírání
okna, přepínat mezi vrstvyami,veškeré provedené změny v symbologii se
vykreslí ihned, a také je zde možnost kroku zpět na předchozí
symbologii, nebo přímo procházení historie všech změn.

<figure>
<img src="images/styl_panel.png" class="small"
alt="images/styl_panel.png" />
<figcaption>Panel stylování</figcaption>
</figure>

## Práce se styly

### Více stylů u vrstvy

V rámci projektu lze vytvořit různé "verze" nastylování u konkrétní
vrstvy. Takto přednastavený styl můžeme potom podle potřeby měnit. Tato
funkce může být užitečná např. při vytváření mapových výstupů jednoho
zdroje dat s různou symbologií. Styly lze ovládat (přídání, smazání,
přejmenování, zvolení, export) pomocí tlačítka ve spodní části okna
vlastností, nebo z kontextového menu vrstvy (pravý klik na vrstvu v
panelu vrstev), zde je přepínání jednotlivých stylů rychlejší. V panelu
stylování se styly ovládají v samostatné záložce <sup>Správce
stylů</sup>.

<figure>
<img src="images/styl_kat.png" class="middle"
alt="images/styl_kat.png" />
<figcaption>Výběr stylu pomocí kontextového menu z panelu
vrstev</figcaption>
</figure>

<figure>
<img src="images/styl_kont.png" class="middle"
alt="images/styl_kont.png" />
<figcaption>Výběr stylu pomocí kontextového menu z panelu
vrstev</figcaption>
</figure>

### Uložení a načtení nastavení vrstvy pomocí souboru

Celé nastavení (styl, formuláře, atd.) vrstvy lze také uložit do
samostatného souboru (*.qml,*.sld), což můžeme využít pro sdílení mezi
kolegy, nebo pro pozdější použití nastavení vrstvy v jiném projektu.

Možnost uložení a načtení najdeme v okně
<span class="title-ref">Vlastnoti vrstvy</span> kliknutím na tlačítko
`Styl`. První dvě možnosti v nabídce umožní `Načíst styl...` a
`Uložit styl...`.

<figure>
<img src="images/styl_soubor_menu.png" class="small"
alt="images/styl_soubor_menu.png" />
<figcaption>Možnosti práce se styly</figcaption>
</figure>

U QML souboru můžeme zvolit (stejně jako při kopírování stylů), které
součásti nastavení se budou ukládat popř. načítat.

<figure>
<img src="images/styl_soubor_nacteni.png" class="small"
alt="images/styl_soubor_nacteni.png" />
<figcaption>Načítání nastavení vrstvy ze souboru</figcaption>
</figure>
