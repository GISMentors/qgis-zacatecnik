Data AOPK
=========
Agentura Ochrany Přírody a Krajiny ČR
(`AOPK ČR <http://www.ochranaprirody.cz/>`_) poskytuje různá data týkající se
ochrany přírody (oblasti chráněných území, `VMB - vrstva mapování biotopů <https://portal.nature.cz/publik_syst/ctihtmlpage.php?what=1035>`_ , nálezy
organismů) v různé podobě (souborové formáty, webové služby - WMS,WFS, ...)
Obecné informace k získávání a poskytování dat můžeme nalézt na Portálu
informačního systému ochrany přírody (`Portál ISOP <https://portal.nature.cz/publik_syst/ctihtmlpage.php?what=3&nabidka=hlavni>`_)
. Obecně jsou data poskytována ve třech úrovních a to jako otevřená data,
otevřená data po registraci, a data poskytovaná na základě žádosti (smlouvy).

Jako rozcestník k získání dat můžeme použít stránky `https://data.nature.cz/
<https://data.nature.cz/>`_. Ke každé datové sadě je zde základní popis,
licenční podmínky, odkaz ke stažení dat popř. na webovou službu.

.. figure:: images/data_nature.png 
   :class: middle 
   :scale-latex: 40 

   Přehled dostupných dat AOPK na `https://data.nature.cz/` 

V případě, že datová sada vyžaduje registraci, odkaz stažení dat Vás přesměřuje
na přihlášení do ISOP (pokud již nejste přihlášení). Pokud nemáte zaregistrovaný
 účet můžete použít odkaz `Založit nový účet v informačním systému AOPK ČR <https://idm.nature.cz/idm/#/registration>`_ přímo z přihlašovacího formuláře.

.. figure:: images/login.png 
   :class: small 
   :scale-latex: 40 

   Přihlašovací formulář ISOP

V současné době je nutná registrace u datových sad **Aktualizace základního
mapování biotopů** a **Nálezová databáze ochrany přírody**.

.. figure:: images/registrace.png 
   :class: small 
   :scale-latex: 40 

   Registrační formulář

Nálezová databáze ochrany přírody
---------------------------------

`Nálezová databáze ochrany přírody <https://portal.nature.cz/nd/>`_ je databáze
nálezů organismů, které jsou lokalizované v čase a prostoru. Od roku 2017 je
databáze, s výjimkou neveřejných nálezů chráněných druhů, plně dostupná
veřejnosti, nutné je pouze se zaregistrovat. Přístup do nálezové databáze
ochrany přírody je umožněn prostřednictvím aplikce `Filtr nálezových dat <https://portal.nature.cz/nd/find.php?>`_. Pokud potřebujeme přístup ke všem
druhům bez výjimky, lze požádat o *plný přístup*. Ten je potom poskytován na
základě smlouvy.

.. figure:: images/nd_uvod.png 
   :class: middle 
   :scale-latex: 40 

   Úvodní stránka nálezové databáze

Databáze obsahuje údaje z různorodých zdrojů. Jsou zde uvedeny záznamy z
vědeckých publikací, informace z odborných pracovišť, výsledky projektů
zaměřených na mapování a monitoring, importovaná data (Fytocenologická databáze
, AVIF, ...), data z inventarizačních průzkumů, historické záznamy, náhodná
pozorování, citizen science - data od veřejnosti (aplikace BioLog). Zastoupení
jednotlivých zdrojů lze prohlížet ve `statistikách
<https://portal.nature.cz/nd/x_nd_statistiky.php>`_ na stránkách ISOP. Každý
rok zde přibývá přibližně 1 až 1.5 milionu nových záznamů.

Filtr nálezových dat
********************
Na úvodní stránce nálezové databáze lze zadat název druhu, a po zadání vyhledání
 nás stránka přesměřuje na *Filtr nálezových dat*, kde můžeme data filtrovat
 na základě více parametrů např: autora nálezu, datumu/období, území (katastry,
 CHÚ, síťové mapování, ...), ručně zakresleného území v mapě (max. 25km:sup:`2`)
 , kategorie ochrany, ...

.. figure:: images/filtr.png 
   :class: middle 
   :scale-latex: 40 

   Filtr nálezových dat veřejného přístupu


Po zadání parametrů pro filtrování stiskneme tlačítko :item:`Filtrovat`.
Výsledky filtru se nám vypíší jako jednotlivé záznamy, ve formě tabulky. Zde
uvidíme základní a nejdůležitější informace o nálezu (co? - kde? - kdy? - kdo?).
 Výsledky je také možné zobrazit v mapě nebo síťové mapě, popř. pokud jsme
 nefiltrovaly na základě druhů lze využít *Sumarizace výsledků podle druhů*.


.. figure:: images/priklad_filtr.png 
   :class: middle 
   :scale-latex: 40 

   Příklad filtrování druhu *Mantis religiosa*


Ve výpisu výsledků lze otevřít *Kartu nálezu* - podrobné informace o konkrétním
nálezu, *Kartu akce* - podrobné informace o mapovací akci, zobrazit konkrétní
nález v mapě (*Mapa*) nebo otevřít *Kartu druhu*, kde jsou shrnuty informace o
konkrétním druhu.



Karta nálezu - data o nálezu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
U každého nálezu je k dispozici mnoho údajů:

    - ID nálezu
    - CO - informace o druhu -  název druhu, taxonomické zařazení, ochrana;
      doplňující informace -  počet, druh pozorování, poznámky
    - KDE - území, souřadnice (v případě území - centroid), typ zákresu, id
      lokalizace
    - KDY - datum, id akce
    - KDO - autor
    - zdroj dat - projekt, datová sada
    - věrohodnost, validace - lze zpochybnit
    - mapa zákresu, popř. fotografie

.. figure:: images/karta_nalezu.png 
   :class: middle 
   :scale-latex: 40 

   Karta konkrétního nálezu

Ve spodní části výpisu filtru máme možnost exportu tabulkových dat (CSV, XML,
HTML, TXT) i lokalizace nálezů (SHP):

    -  tabulková data - lze exportovat i souřadnice centroidů, ty následně
    zorbazit v QGIS jako body
        - *Stránka* - export informací o nálezech na dané stránce
        - *Vše* - export informací o všech naálezech (omezeno na prvních 1000
        nálezů)
    - *Lokalizace* -  export lokalizací nálezů v .shp, obsahuje pouze atribut
    *id_lokalizace* - po stažení lze spárovat s exportovanými tabulkami

.. figure:: images/export.png 
   :class: middle
   :scale-latex: 40 

   Možnost exportu ve filtru nálezů

.. figure:: images/export_tab.png 
   :class: middle 
   :scale-latex: 40 

   Export tavulkových dat výsledku filtru
