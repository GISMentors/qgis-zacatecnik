.. |plug1| image:: ../images/icon/mActionShowRasterCalculator.png
   :width: 1.5em
.. |checkbox_unchecked| image:: ../images/icon/checkbox_unchecked.png
   :width: 1.5em
.. |plugin| image:: ../images/icon/plugin.png
   :width: 1.5em
.. |plugin-installed| image:: ../images/icon/plugin-installed.png
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
zásuvné moduly`. Spustí sa dialógové okno (:num:`#menuplugin`), ktoré slúži na
prehliadanie, zapínanie či vypínanie dostupných modulov. 

.. _menuplugin:

.. figure:: images/smt.png
   :class: small

   Správca zásuvných modulov v prostredí QGIS.

Pod položkou |plugin-installed| :sup:`Instalované` nájdeme tie, ktoré boli 
nainštalované automaticky pri inštalácii QGISu. Z nich sú niektoré načítané,
iné je potrebné zapnúť zaškrtnutím ikonky |checkbox_unchecked|. V prípade, že 
klikneme na niektorý z nich, zobrazí sa jeho charakteristika
spolu s ďalšími informáciami ako je názov, popis, počet hodnotení
a stiahnutí modulu, reprezentujúca ikonka, kategória, inštalovaná či
dostupná verzia, autor, zoznam zmien a iné. Na :num:`plugininfo` je znázornený 
príklad zásuvného modulu s názvom `Qgis2threejs`.

.. _plugininfo:

.. figure:: images/smt.png
   :class: small

   Charakteristika zásuvného modulu na prehliadanie 3D objektov vo webovom prehliadači.

Zoznam všetkých plugin-ov možno zobraziť a konkrétny modul načítať zvolením 
|plugin| :sup:`Nenainstalovano` a spustením :item:`Instalovat zásuvný modul`
(:num:`#dialogplugin`). 

.. _dialogplugin:

.. figure:: images/smt.png
   :class: small

   Zoznam nenainštalovaných modulov :fignote:`(1)` a spustenie inštalácie niektorého z nich :fignote:`(2)`.

