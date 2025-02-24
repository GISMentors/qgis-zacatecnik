# Připojení WFS služby

Správce `WFS <open-source-gis/standardy/ogc/wfs.html>` spustíme v
záložce `Vrstva --> Přidat vrstvu --> Přidat
vrstvu WFS` nebo pomocí ikony <sup>Přidání vrstvu WFS</sup>.

<figure>
<img src="images/qgis_ogc_addwfs_manager.png"
alt="images/qgis_ogc_addwfs_manager.png" />
<figcaption>Okno správce WFS služeb.</figcaption>
</figure>

Okno správce umožňuje přidání, odebrání služby a nahrání vrstev do
projektu. Formulář přidání nové služby se aktivuje tlačítkem `Nové`. Ve
formuláři (`wfsform`) stačí v případě nezaheslované služby vyplnit pouze
URL a pojmenování služby. V případě zaheslované služby jsou vyžadovány
přihlašovací údaje.

<div id="wfsform">

<figure>
<img src="images/qgis_ogc_addwfs_add.png" class="small"
alt="images/qgis_ogc_addwfs_add.png" />
<figcaption>Formulář přidání WFS služby.</figcaption>
</figure>

</div>

Po potvrzení a připojení ke službě se tlačítkem `Připojit` zobrazí
seznam vrstev poskytovaných WFS serverem (`wfslayers`).

<div id="wfslayers">

<figure>
<img src="images/qgis_ogc_addwfs_choose.png"
alt="images/qgis_ogc_addwfs_choose.png" />
<figcaption>Seznam dostupných vrstev na připojeném WFS
serveru.</figcaption>
</figure>

</div>

Výběr více vrstev pro přidání lze opět uskutečnit pomocí klávesy `CTRL`,
vrstvy se v takovém případě nahrají do seznamu vrstev samostatně (jako
při přidávání lokálních dat). Tak jako v případě WMS lze změnit
souřadnicový systém sloužící ke stahování dat. Změna se provádí pod
tlačítkem `Změnit ...` ve spodní pravé části okna. Potvrzením `Přidat`
proběhne přidání vrstev do mapy.

## Práce s WFS službami v okně prohlížeče

Procházet, editovat a přidávat WFS připojení lze také z panelu
prohlížeče (`wfsbrowser`). Vyvoláním kontextového menu pravým kliknutím
na položku můžeme provádět vybrané akce.

- WFS - vytvoření připojení
- konkrétní připojení - editace, odstranění
- konkrétní vrstva - přidání do projektu, vlastnosti

Přidat požadovanou vrstvu do projektu jde obdobně jako u lokálních dat,
dvojitým kliknutím nebo přetažením z datového katalogu (prohlížeče).

<div id="wfsbrowser">

<figure>
<img src="images/qgis_ogc_addwfs_browser.png" class="small"
alt="images/qgis_ogc_addwfs_browser.png" />
<figcaption>Práce s WFS službami v okně prohlížeče.</figcaption>
</figure>

</div>
