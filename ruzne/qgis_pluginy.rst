.. |plug1| image:: ../images/icon/mActionShowRasterCalculator.png
   :width: 1.5em
.. |checkbox_unchecked| image:: ../images/icon/checkbox_unchecked.png
   :width: 1.5em
.. |plugin| image:: ../images/icon/plugin.png
   :width: 1.5em
.. |plugin-installed| image:: ../images/icon/plugin-installed.png
   :width: 1.5em
.. |q2t| image:: ../images/icon/q2t.png
   :width: 1.5em
.. |plugin-upgrade| image:: ../images/icon/plugin-upgrade.png
   :width: 1.5em
.. |mActionTransformSettings| image:: ../images/icon/mActionTransformSettings.png
   :width: 1.5em
.. |star| image:: ../images/icon/osm_star.png
   :width: 1.5em



QGIS pluginy
------------

QGIS umožňuje prácu so zásuvnými modulmi, tzv. :wikipedia:`plugin
<https://en.wikipedia.org/wiki/Plug-in>`-mi. Vo
všeobecnosti ide o softvéry, ktoré nepracujú samostatne, ale ako
doplnkové moduly inej aplikácie a tým rozširujú jej funkčnosť. V
súčasnosti existuje pre QGIS viac ako 300 zásuvných modulov. Všetky sú
napísané v programovacom jazyku `Python <https://www.python.org/>`_ . Mnohé
z nich sú stále vo vývoji. Ich kompletný zoznam spolu s príslušnou
charakteristikou, informáciami napríklad o počte stiahnutí, o tom, ktoré
sú označované ako najviac obľúbené či najmenej hodnotené je dostupný
`tu <https://plugins.qgis.org/plugins/>`_ .

Prejdeme na lištu menu a zobrazíme správcu zásuvných modulov v prostredí
QGIS tým, že zvolíme položku |plug1| :sup:`Spravovat a instalovat zásuvné
moduly` pomocou :menuselection:`Zásuvné moduly --> Spravovat a instalovat
zásuvné moduly`. Spustí sa dialógové okno (:num:`#vse`), ktoré slúži na
prehliadanie, zapínanie či vypínanie dostupných modulov. 

.. _vse:

.. figure:: images/p_vse.png
   :scale: 55%

   Správca zásuvných modulov v prostredí QGIS

Pod položkou |plugin-installed| :sup:`Instalované` nájdeme tie, ktoré boli 
nainštalované automaticky pri inštalácii QGISu. Z nich sú niektoré načítané,
iné možno dočasne povoliť alebo zakázať zaškrtnutím ikonky |checkbox_unchecked|. 
V prípade, že klikneme na niektorý z nich, zobrazí sa jeho charakteristika alebo 
účel spolu s ďalšími informáciami ako je názov, popis, počet hodnotení
a stiahnutí modulu, reprezentujúca ikonka, kategória, inštalovaná či
dostupná verzia, autor, zoznam zmien a iné. Na :num:`plugininfo` je znázornený 
príklad zásuvného modulu s názvom |q2t| :sup:`Qgis2threejs`.

.. _plugininfo:

.. figure:: images/p_info.png
   :scale: 55%

   Charakteristika zásuvného modulu na prehliadanie 3D objektov vo webovom prehliadači

Zoznam všetkých plugin-ov možno zobraziť a konkrétny modul načítať zvolením 
|plugin| :sup:`Nenainstalovano` a spustením :item:`Instalovat zásuvný modul`. 
Následne sa dá tento modul preinštalovať alebo úplne odinštalovať 
(:num:`#p-instal`). 

.. _p-instal:

.. figure:: images/p_instal.png
   :scale: 55%

   Zoznam nenainštalovaných modulov :fignote:`(1)`, inštalácia :fignote:`(2)`, možnosť odinštalovania :fignote:`(3)` alebo preinštalovania :fignote:`(4)` ktoréhokoľvek z nich

Pod záložkou |plugin-upgrade| :sup:`Aktualizovatelný` sa nachádzajú zásuvné 
moduly, ktoré sú dostupné aj v novšej verzii. Záložka |mActionTransformSettings| 
:sup:`Nastavení` obsahuje nastavenia týkajúce sa kontroly aktualizácií modulov,
experimentálnych a neschválených modulov a zobrazuje aj zoznam repozitárov, 
ktoré sa dajú pridávať, editovať alebo mazať, viď. :num:`#akt-nast`.

.. _akt-nast:

.. figure:: images/p_akt_nast.png
   :scale: 55%

   Záložky súvisiace s aktualizáciami a nastaveniami zásuvných modulov

.. tip:: Zoznam zásuvných modulov môže užívateľ usporiadať ako mu vyhovuje. 
Po stlačení pravého tlačidla myši v zozname modulov je k dispozícii ich 
usporiadanie podľa abecedy, počtu stiahnutí, hlasov alebo stavu (:num:`#rad`).

    .. _rad:

    .. figure:: images/p_rad.png
       :scale: 55%

       Možnosti zoradenia zásuvných modulov
    
.. note:: Je potrebné pripomenúť, že zásuvné moduly v oficiálnych repozitároch 
boli testované, no jednotlivé repozitáre môžu obsahovať aj menej overené moduly 
rôznej kvality a štádia vývoja. Preto je dobrou pomôckou zobrazenie hodnotenia 
či počtu |star| |star| |star|. 

.. tip:: Ak poznáme aspoň približný názov konkrétneho modulu, pri vyhľadávaní 
môže pomôcť vyplnenie políčka :item:`Hledat` v dialógovom okne.

V ďalšej časti si ukážeme niektoré z užitočných a často používaných zásuvných 
modulov programu QGIS. 





