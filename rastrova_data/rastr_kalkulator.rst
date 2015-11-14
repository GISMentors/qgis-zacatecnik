.. |mActionShowRasterCalculator| image:: 
   ../images/icon/mActionShowRasterCalculator.png
   :width: 1.5em

.. index::
   pair: algebra; mapová algebra


Použití rastrového kalkulátoru
------------------------------

Při tvorbě mapy orientace vůči světovým stranám je lepší reklasifikovat
(rozdělit) rozsah hodnot do kategorií sever (1), východ (2), jih (3) a západ
(4), přičemž sever znamená :item:`0°` a východ :item:`90°`. Jednou z možností je
využití tzv. rastrového kalkulátoru, konkrétně |mActionShowRasterCalculator|
:sup:`Raster kalkulátor`.

Rastrový kalkulátor souvisí s mapovou algebrou. Jedná se o matematické operace s
rastrovými mapami, které jsou jako matice čísel s prostorovým umístěním. Pomocí
mapové algebry je možné matematickými, ale i jinými operacemi kombinovat více
rastrových vrstev a vytvářet tak nové vrstvy.

.. _rstcalculator:

.. figure:: images/rstcalculator.png
   :scale: 60%

   Princip mapové algebry

Pokud jsme mapu orientací nazvali :map:`aspect`, výraz bude vypadat následovně:
:code:`(("aspect@1"  >= 315)  AND  ("aspect@1" < 45)) * 1 + (("aspect@1"  
>= 45)  AND  ("aspect@1" < 135)) * 2 + (("aspect@1"  >= 135)  AND  ("aspect@1" 
< 225)) * 3 + (("aspect@1"  >= 225)  AND  ("aspect@1" < 315)) * 4`.
Reklasifikované vrstvě následně nastavíme  barevnost a popisy (:num:`#nesw` a
:num:`#aspectrecl`).

.. _nesw:

.. figure:: images/nesw.png
   :class: middle

   Reklasfikace orientace svahů vůči světovým stranám pomocí mapového kalkulátoru

.. _aspectrecl:

.. figure:: images/aspect_recl.png
   :class: middle

   Reklasifikovaná mapa orientací svahů vůči světovým stranám 

.. note::

   Při reklasifikacích se obvykle používá modul GRASS-u :grasscmd:`r.reclass`.
   Na to je však potřebné  nainstalovat zásuvný modul :item:`grass`, který není
   dostupný v každé verzi *QGIS*. Cílem bylo ukázat, že reklasifikace je možná
   i bez pluginů. 
