# Tvorba nových vrstev a jejich editace

## Vytvoření Shapefile vrstvy

Novou vrstvu lze vytvořit pomocí tlačítka <sup>Nová Shapefile
vrstva</sup> nebo v hlavním menu `Vrstva --> Vytvořit
vrstvu --> Nová Shapefile vrstva`.

<figure>
<img src="images/new_layer.png" class="small"
alt="images/new_layer.png" />
<figcaption>Nová vektorová vrstva.</figcaption>
</figure>

V první řadě je nutné zadat cestu, kam se nová vrstva vytvoří. Dále při
vytváření zvolíme typ vrstvy (bod, linie nebo polygon), souřadnicový
systém vrstvy, a pokud je třeba, přidáme nové atributy. Také lze
nastavit vytvoření Z hodnot (nadmořské výšky) nebo M hodnot (další
měřené hodnoty).

Vytváření nového atributu:

- `Název` - název atributu (max. 10 znaků) - toto omezení vychází z
  formátu Esri Shapefile, který je zde použit

- `Typ`

  > - `Textová data` (String) - formát buněk je text, nelze použít pro
  >   výpočty (max. 255 znaků)
  > - `Celé číslo` (Integer) - formát buněk je celé číslo, tedy bez
  >   desetinných míst (max. 10 znaků)
  > - `Desetinné číslo` (Real) - formát buněk je desetinné číslo (max.
  >   10 znaků)
  > - `Datum` (Date) - formát buněk je datum (max. 20 znaků)

- `Délka` - počet znaků

- `Přesnost` - počet desetinných míst

- pro přidání atributu vrstvy je nutné kliknout na tlačítko
  `Přidat do seznamu polí`

Ve spodní části okna máme seznam atributů, které máme ve vrstvě
připravené. Atributy lze odstranit označením a kliknutím na tlačítko
`Odstranit pole`. Automaticky je zde přidaný atribut "id", pokud ho
nechceme, lze jej také vymazat.

Pokud máme vše nastaveno, potvrdíme tlačítkem `OK` a nová vrstva se
automaticky nahraje do projektu.

## Editace vrstvy

Editaci vrstvy spustíme pomocí tlačítka <sup>Přepnout editaci</sup> nebo
v hlavním menu `Vrstva -->
Přepnout editaci`. Spuštěním režimu editace se aktivují editační funkce
v panelu a bude nám umožněno vytvářet nové prvky a jejich atributy nebo
editovat stávající. Vrstva, která je momentálně v režimu editace, je v
seznamu vrstev znázorněna s editační ikonkou .

<figure>
<img src="images/edit_layers_icon.png"
alt="images/edit_layers_icon.png" />
<figcaption>Znázornění režimu editace vrstvy v seznamu
vrstev.</figcaption>
</figure>

Režim editace ukončíme opět pomocí tlačítka <sup>Přepnout editaci</sup>.
Provedené změny je vhodné průběžně ukládat pomocí ikony <sup>Uložit
změny vrstvy</sup>. Pokud při editaci zapomeneme uložit změny, QGIS se
nás při ukončení editace zeptá, zda chceme provedené změny uložit, či
nikoliv.

> [!TIP]
> <sup>Aktuální změny</sup> - hromadné ovládání změn a zapínání/vypínaní
> editací ve vrstvách.

Základní nástroje editace jsou dostupné ve výchozím nastavení mezi
ostatními <span class="title-ref">Nástrojovými lištami</span>. Některké
nástroje jsou ale dostupné v samostatné liště `Pokročilá digitalizace`.
Tu můžeme aktivovat v seznamu všech dostupních položek a to pomocí
pravého kliku a následné <span class="title-ref">aktivace</span> vybrané
položky.

<figure>
<img src="images/advanced_digitizing.png"
alt="images/advanced_digitizing.png" />
</figure>

Zapnutí panelu <span class="title-ref">Pokročilá digitalizace</span>.

### Základní editace geometrie

, , <sup>Přidat ... prvek</sup> - kliknutím vytvoříme prvek (bod), nebo
lomové body prvku (linie, polygon). V druhém případě ukončíme tvorbu
prvku kliknutím pravým tlačítkem a přidáme případné atributy. Při
přidávání lomových bodů je možné se vrátit o krok zpět pomocí klávesy
`Backspace` nebo `Del`.

<figure>
<img src="images/edit_polygon.png" alt="images/edit_polygon.png" />
<figcaption>Vytváření nového prvku ve vrstvě polygonů. Pokud by v tomto
momentě byla tvorba prvku pravým kliknutím ukončena, polygon by měl tři
uzly (tvar trojúhelníku).</figcaption>
</figure>

<sup>Nástroj na lomové body</sup> - pomocí nástroje uzlů lze  
- přidávat body kliknutím na křížek ve středu hrany a umístěním bodu
- přidávat body dvojklikem na hranu a umístěním bodu
- posunovat existující body kliknutím na bod a umístěním bodu
- mazat body označením bodu (nebo více bodů pomocí `Shift`) a stisknutím
  klávesy `Backspace` nebo `Del`
- posouvat celé hrany kliknutím na hranu a umístěním hrany

<figure>
<img src="images/edit_polygon_node.png"
alt="images/edit_polygon_node.png" />
<figcaption>Přidání a přesunutí lomového bodu (uzlu,
vertexu).</figcaption>
</figure>

Nástroj uzlů lze použít ve dvou módech, buď pouze pro vrstvu kterou
editujeme, nebo pro všechny vrstvy které jsou v módu editace

<sup>Vymazat vybrané</sup> - smaže vybrané prvky

<sup>Přesunout prvek/prvky</sup> - jednotlivé prvky přesuneme kliknutím
na prvek, posunutím a opětovným kliknutím

<figure>
<img src="images/edit_polygon_move.png"
alt="images/edit_polygon_move.png" />
<figcaption>Přesun prvku.</figcaption>
</figure>

Další variantou funkce je <sup>Kopírovat a přesunout prvek/prvky</sup>,
kdy stejným principem prvky kopírujeme. Pro přesun nebo kopírování více
prvků můžeme pracovat s více prvky, které máme ve výběru.

<sup>Rozdělit objekt</sup> - naklikáme "řez" přes místa, které chceme
rozdělit a pro ukončení klikneme pravým tlačítkem, prvek se nám v
místech průsečíků rozdělí.

<figure>
<img src="images/edit_polygon_split.png"
alt="images/edit_polygon_split.png" />
<figcaption>Rozdělení polygonu na dva.</figcaption>
</figure>

<sup>Sloučit vybrané prvky</sup> - nejdříve pomocí výběru označíme
prvky, které chceme spojit. Při sloučení vyskočí okno, ve kterém je
možné zadat hodnoty atributů "nového" - sloučeného prvku. Tyto hodnoty
můžeme odvodit z konkrétního vstupního prvku, nebo je lze vypočítat
(např. suma, průměr). Výchozí hodnota atributů je `NULL`, tedy prázdná
hodnota.

<figure>
<img src="images/edit_polygon_merge.png"
class="middle Sloučení sousedních polygonů."
alt="images/edit_polygon_merge.png" />
</figure>

<sup>Změnit tvar prvků</sup> - obdobně jako při rozdělení nebo tvorbě
nového prvku lze naklikáním nového tvaru změnit tvar stávajícího prvku.
Pro změnu tvaru musí být při naklikávání "řezu" vždy minimálně dva
průsečíky. V případě změny tvaru polygonu bude část s menší plochou
vymazána (`resh1`).

<div id="resh1">

<figure>
<img src="images/edit_polygon_resh.png"
alt="images/edit_polygon_resh.png" />
<figcaption>Změna tvaru polygonu - zmenšení.</figcaption>
</figure>

</div>

<figure>
<img src="images/edit_polygon_resh2.png"
alt="images/edit_polygon_resh2.png" />
<figcaption>Změna tvaru polygonu - zvětšení.</figcaption>
</figure>

<figure>
<img src="images/edit_line_resh.png" alt="images/edit_line_resh.png" />
<figcaption>Změna tvaru linie.</figcaption>
</figure>

#### Přichytávání (snapping)

Pro topologicky čistou editaci můžeme pomocí lišty `Přichytávání`
nastavit přichytávání kurzoru s určitou citlivostí k uzlům či segmentům
konkrétních vrstev. Přichytávání je nejdříve nutné aktivovat kliknutím
na ikonu <sup>Enable Snapping</sup>, nebo využít klávesovou zkratku `S`.
Přichycení kurzoru se zobrazí výrazně růžovým čtverečkem v případě
lomového bodu (viz `snapvert`) nebo křížkem v případě segmentu
(`snapsegm`).

<figure>
<img src="images/snapping.png" alt="images/snapping.png" />
<figcaption>Základní okno možnosti přichytávání.</figcaption>
</figure>

<div id="snapvert">

<figure>
<img src="images/snapping_vertex.png"
alt="images/snapping_vertex.png" />
<figcaption>Přichycení kurzoru pouze k lomovému bodu.</figcaption>
</figure>

</div>

<div id="snapsegm">

<figure>
<img src="images/snapping_segment.png"
alt="images/snapping_segment.png" />
<figcaption>Přichycení kurzoru k segmentu.</figcaption>
</figure>

</div>

- Nastavení :

  > - <sup>Všechny vrstvy</sup> - přichytávání ke všem viditelným
  >   vektorovým vrstvám projektu
  > - <sup>Aktivní vrstva</sup> - přichytávání pouze v rámci editované
  >   vrstvy, ostatní vrstvy ignoruje
  > - <sup>Pokročilé nastavení</sup> - režim pokročilého nastavení, lze
  >   nastavit různé nastavení pro jednotlivé vrstvy a nabízí možnost
  >   <span class="title-ref">Vyvarovat se protnutí</span>
  > - `Open snapping Options...` - otevře nastavení přichytávání v
  >   samostatném okně

- Přichytit k :

  > - <sup>Lomový bod</sup> - pouze k lomovým bodům (uzlům/vertexům,
  >   `snapvert`)
  > - <sup>Lomový bod a segment</sup> - k obojímu
  > - <sup>Segmentu</sup> - pouze k segmentům (hranám/liniím,
  >   `snapsegm`)

- Tolerance - vzdálenost, od které se kurzor bude k lomovému bodu nebo
  segmentu přichytávat, hodnotu lze zadat v mapových jednotkách
  (vzdálenost na mapě) nebo pixelech (vzdálenost na monitoru)

- <sup>Zapnout topologickou editaci</sup> - při aktivaci lze pomocí
  <sup>Nástroj uzlú</sup> posouvat společný lomový bod přichycení obou
  prvků najednou. Pokud není aktivní, lomový bod lze oddělit

- <sup>Zapnout přichytávání na protnutí</sup> - při aktivaci se bude
  kurzor přichytávat i na případné místo "překřížení" segmentů (linií)

- <sup>Zapnout trasování</sup> - trasování umožňuje vytvářet nové prvky
  tak aby na sebe přímo navazovaly (topologicky čistá data). Funguje na
  principu vyhledání nejkratší vzdálensoti na segmentech mezi zadanými
  body. Trasování může být problematické v případě, že máme vrstvu s
  více navazujícími polygony, kdy nejkratší vzdálenost nemusí vést po
  vnější hraně skupiny polygonů (`snapping_trace_poly`). To lze vyřešit
  přidáním více bodů při trasování, popř. u polygonů využitím funkce
  <span class="title-ref">Vyvarovat se protnutní</span>

<figure>
<img src="images/snapping_trace_line.png" class="middle"
alt="images/snapping_trace_line.png" />
<figcaption>Trasovaní k linii při tvorbě polygonu.</figcaption>
</figure>

<div id="snapping_trace_poly">

<figure>
<img src="images/snapping_trace_poly.png" class="middle"
alt="images/snapping_trace_poly.png" />
<figcaption>Trasovaní s nejkratší vzdáleností při tvorbě
line.</figcaption>
</figure>

</div>

> [!TIP]
> Nastavení přichytávání lze měnit i v momentě, kdy vytváříme prvek a
> potřebujeme změnit parametry jen pro přidání konkrétního uzlu (např.
> `snapvert` a `snapsegm`).

##### Pokročilý režim přichytávání

<figure>
<img src="images/snapping_adv.png" alt="images/snapping_adv.png" />
<figcaption>Režim pokročilého nastavení přichytávání.</figcaption>
</figure>

V pokročilém režimu lze jednotlivé parametry nastavit pro každou vrstvu
zvlášť, navíc je zde u polygonových vrstev funkce
<span class="title-ref">Vyvarovat se protnutí</span>, která zabraňuje
polygonům jejich překryv, což lze mimo jiné využít jako alternativu k
funkci trasování. Nový polygon potom můžeme zakreslit s přesahem do
sousedícího polygonu, tento přesah bude potom automaticky vymazán. Takto
snadno docílíme čistě navazujících polygonů.

<figure>
<img src="images/snapping_avoid.png" alt="images/snapping_avoid.png" />
<figcaption>Příklad použití <code class="interpreted-text"
role="option">Vyvarovat se protnutí</code>. a) bez <code
class="interpreted-text" role="option">Vyvarovat se protnutí</code> -
polygon se vytvoří tak, jak jsme ho zakreslili, a překrývá předchozí
polygon. Při odstranění nového polygonu bychom viděli opět hranici
polygonu jako v prvním kroku. b) <code class="interpreted-text"
role="option">Vyvarovat se protnutí</code> - polygon se vytvoří bez
překryvu, hranice na sebe čistě navazuje.</figcaption>
</figure>

### Editace atributové tabulky

Pokud máme aktivní editaci ( <sup>Přepnout editaci</sup>), můžeme
editovat nejen geometrii, ale i atributovou tabulku vrstvy. V okně
atributové tabulky lze editaci ukládat <sup>Uložit změny vrstvy</sup> i
mazat vybrané prvky <sup>Vymazat vybrané</sup>:

> - kliknutím do libovolného pole můžeme vepisovat a upravovat hodnoty
>   tabulky
> - <sup>Nové pole</sup> - přidá nový atribut do tabulky
> - <sup>Smazat pole</sup> - vyvolá nabídku, ze které vybereme sloupce k
>   vymazání
> - <sup>Spravovat sloupce</sup> - vyvolá nabídku, ve které můžete
>   upravit viditelnost sloupce
> - <sup>Otevřít kalkulátor polí</sup> - pomocí kalkulátoru polí lze
>   vytvářet nebo aktualizovat sloupce (atributy) na základě zadaného
>   výrazu (vzorce)

## Kalkulátor polí

Pomocí funkce <sup>Otevřít kalkulátor polí</sup> můžeme zadáním výrazu
provádět výpočty na základě existujících hodnot v atributové tabulce
nebo funkcí (např. výpočet rozlohy polygonu). Výsledek výrazu můžeme
nechat zapsat do nového sloupce, do virtuálního sloupce, nebo lze
aktualizovat již existující sloupec.

<figure>
<img src="images/field_calc.png" alt="images/field_calc.png" />
<figcaption>Okno kalkulačky polí.</figcaption>
</figure>

Nejdříve je nutné nastavit, zda chceme výsledek zapsat do nového pole,
virtuálního pole, nebo pouze aktualizovat existující pole.

- `Vytvořit nové pole` - vytvoří nové pole, zde je třeba definovat
  parametry nového atributu

- `Vytvořit virtuální pole` - vytvoří virtuální pole, které se při každé
  změně automaticky aktualizuje. Nevýhodou může být, že se pole neukládá
  do zdrojových dat, ale pouze do souboru projektu

- `Aktualizovat existující pole` - přepíše hodnoty ve vybraném poli

  > - \- vybereme z nabídky vrstvu, kterou cheme přepsat

Nyní můžeme přejít k zadání vlastního výrazu - záložka `Výraz`.

Levá část okna (`Výraz`) je prostor zadání výrazu, v horní části máme
několik tlačítek s vybranými operátory a ve spodní části potom náhled
výstupu.

<figure>
<img src="images/field_calc_exp.png" alt="images/field_calc_exp.png" />
</figure>

Pravá část okna (`Funkce`) slouží k rychlému zadání funkcí nebo
parametrů do výrazu, v pravé části se k vybrané funkci/parametru
zobrazuje nápověda. Požadované položky lze vyhledat pomocí filtru nebo
prohledáním příslušných kategorií. Přidání funkce nebo hodnoty pole
pomocí okna funkcí se provádí dvojklikem na položku.

<figure>
<img src="images/field_calc_fun.png" alt="images/field_calc_fun.png" />
</figure>

Při zadávání parametru pole nebo hodnoty pole (`Pole a hodnoty`) je
možné nechat si zobrazit všechny hodnoty (tlačítko: `všechny
jedinečné hodnoty`) nebo prvních 10 hodnot (tlačítko: `10 vzorků`)
atributu.

<figure>
<img src="images/field_calc_fun_field.png"
alt="images/field_calc_fun_field.png" />
</figure>

<figure>
<img src="images/field_calc_area.png"
alt="images/field_calc_area.png" />
</figure>

<div class="noteadvanced">

Druhá záložka - `Editor funkcí` umožňuje definovat vlastní funkce pomocí
jazyka Python

</div>

> [!TIP]
> Editovat stávající atributy lze i přímo z atributové tabulky, a to
> pomocí panelu (`editpanel`), který se aktivuje po přepnutí do režimu
> editace. Zde vybereme atribut, který chceme editovat, a zadáme
> požadovaný výraz (ručně nebo pomocí dialogu ), potom potvrdíme
> aktualizaci buď pro všechny prvky, nebo jen pro prvky vybrané.
>
> <div id="editpanel">
>
> <figure>
> <img src="images/field_edit_panel.png" class="middle"
> alt="images/field_edit_panel.png" />
> <figcaption>Panel editace atributů v atributové tabulce.</figcaption>
> </figure>
>
> </div>
