# Data AOPK

Agentura Ochrany Přírody a Krajiny ČR ([AOPK
ČR](http://www.ochranaprirody.cz/)) poskytuje různá data týkající se
ochrany přírody (oblasti chráněných území, [VMB - vrstva mapování
biotopů](https://portal.nature.cz/publik_syst/ctihtmlpage.php?what=1035)
, nálezy organismů) v různé podobě (souborové formáty, webové služby -
WMS,WFS, ...). Obecné informace k získávání a poskytování dat můžeme
nalézt na Portálu informačního systému ochrany přírody ([Portál
ISOP](https://portal.nature.cz/publik_syst/ctihtmlpage.php?what=3&nabidka=hlavni)).
Obecně jsou data poskytována ve třech úrovních a to jako otevřená data,
otevřená data po registraci, a data poskytovaná na základě žádosti
(smlouvy).

Jako rozcestník k získání dat můžeme použít stránky
<https://data.nature.cz/>. Ke každé datové sadě je zde základní popis,
licenční podmínky, odkaz ke stažení dat popř. na webovou službu.

<figure>
<img src="images/data_nature.png" class="middle"
alt="images/data_nature.png" />
<figcaption>Přehled dostupných dat AOPK na <span
class="title-ref">https://data.nature.cz/</span></figcaption>
</figure>

V případě, že datová sada vyžaduje registraci, odkaz stažení dat Vás
přesměřuje na přihlášení do ISOP (pokud již nejste přihlášení). Pokud
nemáte zaregistrovaný účet můžete použít odkaz [Založit nový účet v
informačním systému AOPK ČR](https://idm.nature.cz/idm/#/registration)
přímo z přihlašovacího formuláře.

<figure>
<img src="images/login.png" class="small" alt="images/login.png" />
<figcaption>Přihlašovací formulář ISOP</figcaption>
</figure>

V současné době je nutná registrace u datových sad **Aktualizace
základního mapování biotopů** a **Nálezová databáze ochrany přírody**.

<figure>
<img src="images/registrace.png" class="small"
alt="images/registrace.png" />
<figcaption>Registrační formulář</figcaption>
</figure>

## Nálezová databáze ochrany přírody

[Nálezová databáze ochrany přírody](https://portal.nature.cz/nd/) je
databáze nálezů organismů, které jsou lokalizované v čase a prostoru. Od
roku 2017 je databáze, s výjimkou citlivých nálezů chráněných druhů,
plně dostupná veřejnosti, nutné je pouze se zaregistrovat. Přístup do
nálezové databáze ochrany přírody je umožněn prostřednictvím aplikce
[Filtr nálezových dat](https://portal.nature.cz/nd/find.php?). Pokud
potřebujeme přístup ke všem druhům bez výjimky, lze požádat o *plný
přístup*. Ten je potom poskytován na základě smlouvy.

<figure>
<img src="images/nd_uvod.png" class="middle" alt="images/nd_uvod.png" />
<figcaption>Úvodní stránka nálezové databáze</figcaption>
</figure>

Databáze obsahuje údaje z různorodých zdrojů. Jsou zde uvedeny záznamy z
vědeckých publikací, informace z odborných pracovišť, výsledky projektů
zaměřených na mapování a monitoring, importovaná data (Fytocenologická
databáze , AVIF, ...), data z inventarizačních průzkumů, historické
záznamy, náhodná pozorování, citizen science - data od veřejnosti
(aplikace BioLog). Zastoupení jednotlivých zdrojů lze prohlížet ve
[statistikách](https://portal.nature.cz/nd/x_nd_statistiky.php) na
stránkách ISOP. Každý rok zde přibývá přibližně 1 až 1.5 milionu nových
záznamů.

### NDOP Downloader

Pro stažení nálezových dat přímo v QGIS můžeme použít zásuvný modul
[NDOP Downloader](https://opengeolabs.github.io/qgis-ndop-downloader/)
<img src="images/icon.png" style="width:1.5em" alt="ndop_downloader" />.
Tento zásuvný modul lze nainstalovat pomocí menu
<span class="title-ref">Zásuvné moduly --\> Spravovat a instalovat
zásuvné moduly</span>. První je nutné povolit experimentální zásuvné
moduly. V záložce nastavení zaškrtneme políčko
<span class="title-ref">Zobrazit také experimentální zásuvné
moduly</span>.

Po zadání přihlašovacích údajů lze stáhnout nálezy podle zadaného taxonu
nebo oblasti (KÚ,ZCHÚ). Pokud zaškrtnete položku
<span class="title-ref">Uložit přihlašovací údaje</span>, údaje se uloží
do konfiguračního souboru <span class="title-ref">.ndop.cfg</span> v
domovském adresáři.

<figure>
<img src="images/ndop_downloader.png" class="middle"
alt="images/ndop_downloader.png" />
<figcaption>Okno NDOP Downloaderu v QGIS</figcaption>
</figure>

Výstupem jsou dostupná data lokalizací (.shp komprimované v .zip) a
tabulková data (.csv) pro všechny záznamy. Lokalizace se po ukončení
stahování nahrají do projektu. Tabulková data se nahrají do projektu
jako Oddělený text a zobrazí se jako body (na základě souřadnic v
tabulce). Tato data obsahují body a centroidy většiny polygonů a linií.

**Parametry**:

- **Taxon** - Lze vybrat pomocí rolovací nabídky, nebo vepsáním názvu s
  funkcí našeptávače. Lze zadávat česká i latinská jména.
- **Region** - Obdobně jako u taxonu. V případě že položka zůstane
  nevyplněná, získáme data z clého území ČR. Naopak, pokud vybyreme
  území regionu a necháme prázdné políčko taxonu, získáme data všech
  taxonů ve vybraném regionu.
- **Výstupní složka** - Vybereme výsupní složku kam se nám data uloží.
  Pokud ponecháme prázdné, stáhnou se data do složky dočasných souborů.
  V případě, že nechceme stahovat tabulková data zaškrtneme možnost
  <span class="title-ref">Nestahovat tabulková data</span>. Stažené
  soubory se nahrají do projektu a ponesou název odvozený od použitého
  filtru a typu dat. Pokud je do filtru zadán taxon, bude název odvozen
  od názvu druhu (např.
  <span class="title-ref">Mantis_religiosa_shp_b</span> - bodová vrstva
  (.shp)). Poukd filtrujeme pouze podle regionu bude název odvozen od
  názvu regionu.

Po potvrzení tlačítkem Ok se okno zavře a spustí se filtrace a
stahování. QGIS během stahování **nelze v současné době používat**.
Stejně jako při použití oficiálního webové filtru, stahování může trvat
několik minut, v závislosti na počtu záznamů, stažení tabulkových dat
atd.

V informačním panelu v horní části obrazovky uvidíte informace o průběhu
stahování. Při stahování se také vypíše počet záznamů a hrubý odhad doby
trvání konkrétního kroku. Po úspěšném stažení se objeví zelený panel s
odkazem na složku kam byla data stažena.

<figure>
<img src="images/ndop_result.png" class="middle"
alt="images/ndop_result.png" />
<figcaption>Data stažené pomocí zásuvného modulu NDOP
Downloader</figcaption>
</figure>

### Webový filtr nálezových dat

Základní způsob jak stahovat data z nálezové databáze je použití
webového filtru přímo na stránkách [Nálezová databáze ochrany přírody
AOPK](https://portal.nature.cz/nd/). Na úvodní stránce nálezové databáze
lze zadat název druhu, a po zadání vyhledání nás stránka přesměřuje na
*Filtr nálezových dat*, kde můžeme data filtrovat na základě více
parametrů např: autora nálezu, datumu/období, území (katastry, CHÚ,
síťové mapování, ...), ručně zakresleného území v mapě (max.
25km<sup>2</sup>) , kategorie ochrany, ...

<figure>
<img src="images/filtr.png" class="middle" alt="images/filtr.png" />
<figcaption>Filtr nálezových dat veřejného přístupu</figcaption>
</figure>

Po zadání parametrů pro filtrování stiskneme tlačítko `Filtrovat`.
Výsledky filtru se nám vypíší jako jednotlivé záznamy, ve formě tabulky.
Zde uvidíme základní a nejdůležitější informace o nálezu (co? - kde? -
kdy? - kdo?). Výsledky je také možné zobrazit v mapě nebo síťové mapě,
popř. pokud jsme nefiltrovaly na základě druhů lze využít *Sumarizace
výsledků podle druhů*.

<figure>
<img src="images/priklad_filtr.png" class="middle"
alt="images/priklad_filtr.png" />
<figcaption>Příklad filtrování druhu <em>Mantis
religiosa</em></figcaption>
</figure>

Ve výpisu výsledků lze otevřít *Kartu nálezu* - podrobné informace o
konkrétním nálezu, *Kartu akce* - podrobné informace o mapovací akci,
zobrazit konkrétní nález v mapě (*Mapa*) nebo otevřít *Kartu druhu*, kde
jsou shrnuty informace o konkrétním druhu.

#### Karta nálezu - data o nálezu

U každého nálezu je k dispozici mnoho údajů:

> - ID nálezu
> - CO - informace o druhu - název druhu, taxonomické zařazení, ochrana;
>   doplňující informace - počet, druh pozorování, poznámky
> - KDE - území, souřadnice (v případě území - centroid), typ zákresu,
>   id lokalizace
> - KDY - datum, id akce
> - KDO - autor
> - zdroj dat - projekt, datová sada
> - věrohodnost, validace - lze zpochybnit
> - mapa zákresu, popř. fotografie

<figure>
<img src="images/karta_nalezu.png" class="middle"
alt="images/karta_nalezu.png" />
<figcaption>Karta konkrétního nálezu</figcaption>
</figure>

Ve spodní části výpisu filtru máme možnost exportu tabulkových dat (CSV,
XML, HTML, TXT) i lokalizace nálezů (SHP):

> \- tabulková data - lze exportovat i souřadnice centroidů, ty následně
> zorbazit v QGIS jako body - *Stránka* - export informací o nálezech na
> dané stránce - *Vše* - export informací o všech naálezech (omezeno na
> prvních 1000 nálezů) - *Lokalizace* - export lokalizací nálezů v .shp,
> obsahuje pouze atribut *id_lokalizace* - po stažení lze spárovat s
> exportovanými tabulkami

<figure>
<img src="images/export.png" class="middle" alt="images/export.png" />
<figcaption>Možnost exportu ve filtru nálezů</figcaption>
</figure>

<figure>
<img src="images/export_tab.png" class="middle"
alt="images/export_tab.png" />
<figcaption>Export tavulkových dat výsledku filtru</figcaption>
</figure>
