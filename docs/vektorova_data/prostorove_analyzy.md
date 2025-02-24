<div class="todo">

přidat u překryvných analýz obrázky prakticých příkladů (i na bodech)

</div>

# Prostorové analýzy

V prostředí QGIS máme k dispozici širokou škálu funkcí pro prostorové
analýzy vektorových dat. Základní funkce nalezneme v hlavním menu
`Vektor --> Nástroje geoprocessingu`.

<div class="noteadvanced">

Další možností jak spouštět analýzy je pomocí okna
`Nástroje zpracování`, které sdružuje funkce z knihovny GDAL a dalších
dostupných externích nástrojů, jako jsou například GRASS GIS, SAGA nebo
R. Jednotlivé funkce lze rychle vyhledávat pomocí filtru v horní části
okna (nutno zadat anglický název funkce).

<figure>
<img src="images/geoprocess.png" class="small"
alt="images/geoprocess.png" />
<figcaption>Okno <code class="interpreted-text"
role="item">Nástroje zpracování</code>.</figcaption>
</figure>

</div>

## Obalová zóna dle pevné vzdálenosti (buffer)

Jednou z nejzákladnějších prostorových analýz je obalová zóna (tzv.
buffer). Obalové zóny jsou reprezentovány polygony s hranicí o dané
vzdálenosti od prvků. U bodových prvků má obalová zóna tvar kruhu (nebo
aproximace kruhu), u linií a polygonů se hranice obalové zóny generuje
vzdálenostmi od uzlů. Cílem analýzy je tedy vytvořit novou polygonovou
vrstvu obalových zón. Tuto funkci najdeme v menu
`Vektor --> Nástroje geoprocessingu --> Obalová
zóna dle pevné vzdálenosti`. Velikost bufferu lze nastavit i jako
proměnlivou hodnotu.

<figure>
<img src="images/prost_buffer.png" class="medium"
alt="images/prost_buffer.png" />
<figcaption>Dialogové okno obalové zóny.</figcaption>
</figure>

- `Vstupní vrsvta` - vstupní vrstva pro vytvoření obalových zón

- `Vzdálenost` - vzdálenost obalové zóny v metrech (v závislosti
  nastavení QGIS a použitého SRS)

- `Segmenty` - počet liniových segmentů při zaoblených částěch obalové
  zóny (`aprox`)

  > - nízká hodnota (min. 5) - méně uzlů - rychlejší výpočty, ale méně
  >   přesné
  > - vysoká hodnota (max. 99) - více uzlů - pomalejší výpočty, zaoblené
  >   části více odpovídají kruhu kruhu

<div id="aprox">

<figure>
<img src="images/prost_buffer_seg.png"
alt="images/prost_buffer_seg.png" />
<figcaption>Obalová zóna s rozdílným počtem segmentů pro aproximaci
(vlevo 5, vpravo 50).</figcaption>
</figure>

</div>

\- `Styl zakončení` - styl zakončení obalové zóny na konci linií
(<span class="title-ref">kulatý</span>,
<span class="title-ref">plochý</span>,
<span class="title-ref">čtverec</span>) `zakonceni` - `Připojit styl` -
styl obalové zóny při rozích (<span class="title-ref">kulatý</span>,
<span class="title-ref">kosý</span>,
<span class="title-ref">zaoblený</span>) `spoj` - `Miter limit` -
maximální vzdálenost od odsazené křivky při vytváření kosého spoje

<div id="zakonceni">

<figure>
<img src="images/prost_buffer_zak.png"
alt="images/prost_buffer_zak.png" />
<figcaption>Typy stylů zakončení (<span class="title-ref">kulatý</span>
, <span class="title-ref">plochý</span>, <span
class="title-ref">čtverec</span>).</figcaption>
</figure>

</div>

<div id="spoj">

<figure>
<img src="images/prost_buffer_spoj.png"
alt="images/prost_buffer_spoj.png" />
<figcaption>Typy stylů připojení (<span class="title-ref">kulatý</span>,
<span class="title-ref">kosý</span>, <span
class="title-ref">zaoblený</span>).</figcaption>
</figure>

</div>

- `Výsledek rozpuštění` - zaškrtneme, pokud nechceme, aby se nám
  výsledné obalové zóny překrývaly, výsledkem analýzy je jeden prvek
- `Obalová zóna` - zadáme cestu a název výstupního souboru
- `Otevřít výstupní soubor po doběhnutí algoritmu`
  - výsledná vrstva se přidá do projektu

V následujícím příkladu jsme vytvořili obalovou zónu 10 km kolem dálnic
(s možností rozpuštění výsledků).

<figure>
<img src="images/prost_buffer_dalnice.png"
alt="images/prost_buffer_dalnice.png" />
</figure>

## Překryvné analýzy

Další skupinou prostorových analýz jsou tzv. překryvné analýzy.
Principem je vytvořit novou vektorovou vrstvu na základě interakce prvků
jedné nebo více vektorových vrstev. Pro dosažení správného výsledku je
nutné, aby vrstvy byly ve shodném souřadnicovém systému. Překryvné
operace opět nalezneme v menu `Vektor --> Nástroje geoprocessingu`.

<figure>
<img src="images/prost_okno.png" class="medium"
alt="images/prost_okno.png" />
</figure>

- `Vstupní vrsvta` - vstupní vrstva
- `Oříznout vrsvtu` - druhá vrstva, která vstupuje do analýzy
- `Oříznuto` - zadáme cestu a název výstupního souboru
- `Otevřít výstupní soubor po doběhnutí algoritmu` - výsledná vrstva se
  nahraje do projektu

<figure>
<img src="images/prost_puvod.png" class="middle"
alt="images/prost_puvod.png" />
<figcaption>Původní vrstvy vstupující do ukázkových
příkladů.</figcaption>
</figure>

### Ořezávač (<span class="title-ref">Clip</span>)

Vytvoří novou vrstvu, ve které je <span class="title-ref">Vstupní
vektorová vrstva</span> ořezána vrstvou vybranou v nabídce
<span class="title-ref">Oříznout vrstvu</span>. Prvky výstupní vrstvy
nesou atributy pouze z vrstvy zadané jako
<span class="title-ref">Vstupní vektorová vrstva</span>.

<figure>
<img src="images/prost_orez.png" alt="images/prost_orez.png" />
<figcaption>Výsledek funkce Ořezání... - čtverec jsme ořezali podle
kruhu.</figcaption>
</figure>

### Průsečík (<span class="title-ref">Interesction</span>)

Vytvoří novou vrstvu s prvky pouze v místech překryvu vstupních vrstev.
Každý prvek nese atributy obou vstupních vrstev.

<figure>
<img src="images/prost_prus.png" alt="images/prost_prus.png" />
<figcaption>Výsledek funkce Průsečík.</figcaption>
</figure>

### Sjednotit (<span class="title-ref">Union</span>)

Vytvoří novou vrstvu se všemi původními prvky, v místech překryvu vrstev
jsou vytvořeny nové prvky.

<figure>
<img src="images/prost_sjed.png" alt="images/prost_sjed.png" />
<figcaption>Výsledek funkce Sjednotit.</figcaption>
</figure>

### Symetrický rozdíl (<span class="title-ref">Symmetric difference</span>)

Vytvoří novou vrstvu, kde v místech překryvu vrstev nejsou vytvořeny
prvky. Prvky vznikají tedy pouze tam, kde se vstupní vrstvy
nepřekrývají.

<figure>
<img src="images/prost_sym.png" alt="images/prost_sym.png" />
<figcaption>Výsledek funkce Symetrický rozdíl.</figcaption>
</figure>

### Rozdíl (<span class="title-ref">Difference</span>)

Vytvoří novou vrstvu, která je rozdílem vstupních vrstev. Ve
<span class="title-ref">Vstupní vektorové vrstvě</span> se odstraní
plochy, které se překrývají s vrstvou v nabídce
<span class="title-ref">Rozdíl ve vrstvě</span>.

<figure>
<img src="images/prost_rozd.png" alt="images/prost_rozd.png" />
</figure>

### Rozpustit (<span class="title-ref">Dissolve</span>)

Vytvoří novou vrstvu, ve které jsou definované prvky jedné vrstvy
sloučeny do jednoho. Pokud chceme aplikovat pro všechny prvky, zvolíme
`Dissolve all (do not use fields)`. Pokud chceme metodu aplikovat podle
atributů, tak v nabídce `Unique ID fields` můžeme vybrat atributy, pro
které chceme rozpuštění aplikovat.

<figure>
<img src="images/prost_rozp_okno.png" class="medium"
alt="images/prost_rozp_okno.png" />
</figure>

<figure>
<img src="images/prost_rozp.png" alt="images/prost_rozp.png" />
<figcaption>Výsledek funkce Rozpustit (vstupní vrstva: výsledek
Sjednocení).</figcaption>
</figure>

V následujícím příkladu provedeme sjednocení vrstvy velkoplošných
chráněných území a obalové zóny dálnic (10 km).

<figure>
<img src="images/prost_sjed_priklad.png"
alt="images/prost_sjed_priklad.png" />
<figcaption>Sjednocení vrstvy velkoplošných chráněných území a obalové
zóny dálnic (10 km).</figcaption>
</figure>

Díky tomu, že vytvořená vrstva sjednocení nese atributy obou vstupních
vrstev (obalová zóna nesla pouze atribut "typ" s hodnotou "dalnice"),
můžeme zjistit různé informace. Například odfiltrováním 10. prvku, tedy
prvku, který představuje obalovou zónu nezasahující do žádného
velkoplošného chráněného území, můžeme snadno vypočítat poměr chráněného
území, do kterého zasahuje obalová zóna 10 km od dálnic.

> > [!NOTE]
> > Pokud máme vybrané nějaké prvky, je automaticky aktivováno.
