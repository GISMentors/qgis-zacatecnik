.. |mIconExpressionSelect| image:: ../images/icon/mIconExpressionSelect.png
    :width: 1.5em
.. |mActionCalculateField| image:: ../images/icon/mActionCalculateField.png
   :width: 1.5em
.. |select_location| image:: ../images/icon/select_location.png
   :width: 1.5em
.. |random_selection| image:: ../images/icon/random_selection.png
   :width: 1.5em 
.. |sub_selection| image:: ../images/icon/random_selection.png
   :width: 1.5em 
   

.. _atrdotaz:

Atributové dotazování
=====================

Atributové dotazování slouží k vytvoření výběru prvků z vektorové vrstvy 
dle námi zadaných kritérií. 
Funkce, která toto umožňuje je |mIconExpressionSelect| :sup:`Vabrat prvky pomocí 
vzorce` a můžeme jí spustit buď z nástrojového panelu nebo z atributové tabulky 
dané vrstvy. Dialogové okno vypdá obdobně jako okno kalkulátoru polí 
|mActionCalculateField| a zadávání výrazu zde funguje na stejném principu. 
Tedy v levé části okna (:item:`Výraz`) je prostor pro zadání požadovaného výrazu 
a pravá část okna (:item:`Funkce`) slouží k rychlému přidání funkcí nebo 
parametrů do výrazu.

.. figure:: images/select_exp.png
    
    Okno atributového dotazování


Po zadání našeho výrazu potvrdíme tlačítkem |mIconExpressionSelect|
:item:`Vybrat` čímž se nám vytvoří požadovaný výběr. Z nabídky vedle tlačítka 
můžeme vybrat další možnosti práce s výběrem pomocí atributového dotazu.

.. figure:: images/select_exp_fun.png
    :scale: 100%
    
    Další možnosti práce s výběrem pomocí atributového dotazu

.. tip:: V levé části stavového řádku vidíme aktuální počet vybraných 
    prvků (viz. :num:`expstatus`)
    
Uvedeme si jednoduchý příklad atributového dotazu. Z vrstvy Velkoplošných 
zvláště chráněných území, potřebujeme vybrat národní parky a jejich ochranná 
pásma. Podmínkou samozřejmě je, že musíme mít takovou informaci o prvcích v 
atributové tabulce.

.. figure:: images/select_exp_vzchu_at.png
    
    Informace o prvcích v atributové tabulce
    
Formulace našeho dotazu by v mluveném slově vypadala přibližně takto: "Vyber 
takové prvky, které mají buď atribut :option:`KAT` s hodnotou :option:`NP` nebo 
atribut :option:`KAT` s hodnotou :option:`OP`". Výraz, který potřebujeme vepsat 
do dialogového okna:
    
.. code-block:: bash

    "KAT" = 'OP' or "KAT" = 'NP' 
    
.. figure:: images/select_exp_vzchu.png
    
    Výsledek atributového dotazu ("KAT" = 'OP' or "KAT" = 'NP') ve vrstvě 
    Velkoplošných zvláště chráněných území 
    
.. _expstatus:
    
.. figure:: images/select_exp_vzchu_status.png
    
    Výpis počtu vybraných prvků (v levé části stavového řádku)
    
.. noteadvanced:: Výběr lze vytvořit i na základě geometrie (prostorové 
    dotazování) a to pomocí funkce |select_location|
    :sup:`Vybrat podle umístění...`. Také můžeme pomocí funkcí 
    |random_selection| :sup:`Náhodný výběr...`/|sub_selection| 
    :sup:`Náhodný výběr v podmonožinách...` tvořit náhodné výběry z prvků. Tyto 
    funkce najdeme v hlavním menu :menuselection:`Vektor --> Výzkumné nástroje`

