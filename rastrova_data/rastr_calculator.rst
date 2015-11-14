.. |mActionShowRasterCalculator| image::
../images/icon/mActionShowRasterCalculator.png
   :width: 1.5em

Použitie rastrovej kalkulačky
-----------------------------

Pri tvorbe mapy orientácie na svetové strany je lepšie reklasifikovať
(rozdeliť) rozsah hodnôt do kategórií sever (1), východ (2),
juh (3) a západ (4), pričom sever znamená :item:`0°` a východ
:item:`90°`. Jednou z možností je využitie tzv. rastrovej kalkulačky,
konkrétne |mActionShowRasterCalculator| :sup:`Raster kalkulátor`.

Rastrová kalkulačka súvisí s mapovou algebrou. Ide o matematické operácie
s rastrovými mapami, ktoré sú akoby matice čísel s priestorovým
umiestnením. Pomocou mapovej algebry je možné matematickými, ale i
inými operáciami kombinovať viaceré rastrové vrstvy a tým vytvárať
nové vrstvy.

    .. _rstcalculator:

    .. figure:: images/rstcalculator.png
       :scale: 60%

       Mapová algebra

Ak sme mapu orientácií nazvali :map:`aspect`, výraz bude vyzerať
nasledovne: :code:`(("aspect@1" >= 315) AND ("aspect@1" < 45)) * 1 +
(("aspect@1" >= 45) AND ("aspect@1" < 135)) * 2 + (("aspect@1" >= 135) AND
("aspect@1" < 225)) * 3 + (("aspect@1" >= 225) AND ("aspect@1" < 315))
* 4`. Reklasifikovanej vrstve následne nastavíme farebnosť a popisy
(:num:`#nesw` a :num:`#aspectrecl`).

    .. _nesw:

    .. figure:: images/nesw.png
       :class: middle

       Reklasifikácia orientácií svahu na svetové strany pomocou mapovej
       kalkulačky

    .. _aspectrecl:

    .. figure:: images/aspect_recl.png
       :class: middle

       Reklasifikovaná mapa orientácií svahu na svetové strany

.. note:: Pri reklasifikáciách sa zvyčajne používa modul GRASS-u
:grasscmd:`r.reclass`. Na to je však potrebné nainštalovať zásuvný modul
:item:`grass`, ktorý nie je dostupný v každej verzii *QGIS*. Cieľom bolo
ukázať, že reklasifikovať sa dá aj bez bez pluginov.

