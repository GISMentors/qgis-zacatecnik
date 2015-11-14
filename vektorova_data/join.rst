.. |selectstring| image:: ../images/icon/selectstring.png
   :width: 2.5em
.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |radiobuttonon| image:: ../images/icon/radiobuttonon.png
   :width: 1.5em
.. |symbologyAdd| image:: ../images/icon/symbologyAdd.png
   :width: 1.5em
.. |symbologyRemove| image:: ../images/icon/symbologyRemove.png
   :width: 1.5em
.. |symbologyEdit| image:: ../images/icon/symbologyEdit.png
   :width: 1.5em
.. |join| image:: ../images/icon/join.png
   :width: 1.5em
.. |mActionAddDelimitedTextLayer| image:: ../images/icon/mActionAddDelimitedTextLayer.png
   :width: 1.5em

Připojení tabulkových dat 
=========================

Pokud máme vektorovou vrstvu, můžeme k jejím prvkům připojit data z tabulek. Atributová tabulka vektorové vrstvy i připojovaná tabulka musí mít sloupec, ve kterém budou hodnoty, přes které se bude připojení vytvářet. Podle tohoto sloupce QGIS pozná, který řádek tabulky a prvek ve vrstvě patří k sobě.

.. tip:: Možné využití v praxi:

            - připojení získaných dat v tabulkách k prvkům 
            - připojení naměřených dat z terénu k prvkům
    

    
.. todo:: - .csvt
          - příklad

.. .. _ptab:

.. .. table:: Poznámky z terénu

   +-----+--------+---------+---------+--------+
   | bod | biotop | teplota | vlhkost | druh   |
   +=====+========+=========+=========+========+
   | 435 | louka  | 29      | 49      | ManRel |
   +-----+--------+---------+---------+--------+
   | ... | ...    | ...     | ...     | ...    |
   +-----+--------+---------+---------+--------+
   

Postup připojení dat
--------------------

Nejprve je vhodné převést naši tabulku na data s oddělenými hodnotami, např. formát :wikipedia:`CSV`, což provedeme přímo v tabulkovém procesoru - při ukládání nebo exportu vybereme formát .csv 
    
 -  nahrajeme .csv soubor jako vrstvu, buď přetažením z prohlížeče nebo pomocí |mActionAddDelimitedTextLayer| :sup:`Přidat vrstvu s odděleným textem`, kde bychom zvolili |radiobuttonon| :sup:`Žádna geometrie (pouze atributová tabulka)`

 -  otevřeme vlastnosti vektorové vrstvy, ke které chceme tabulku připojit a zvolíme záložku |join| :sup:`Připojení`

 -  přidáme nové připojení pomocí tlačítka |symbologyAdd|
    
.. _join:

.. figure:: images/join.png
    
   Okno přidání připojení
    
|

 - :item:`Připojit vrstvu` |selectstring| - vyberem vrstvu (.csv tabulku) 
 - :item:`Připojit pole` |selectstring| - vyberem atribut (týká se tabulky .csv), který chceme připojit 
 - :item:`Cílové pole` |selectstring| - vybereme souhlasný atribut, přes který se bude tabulka připojovat
 - |checkbox| :item:`Kešovat připojenou vrstvu ve virtuální paměti` - pro rychlejší práci s daty
 - |checkbox| :item:`Choose which fields are joined` - zaškrtneme pokud chceme připojit pouze některé atributy
 - |checkbox| :item:`Custom field name prefix` - zde můžeme zvolit vlastní předponu názvů připojených atributů (jejich sloupců)

 -  po přidání se připojení objeví v seznamu, zavřeme vlastnsti a můžeme překontrolovat připojení zobrazením atributové tabulky vrstvy.
        
     - pomocí tlačítka |symbologyEdit| lze připojení editovat
     - pomocí tlačítka |symbologyRemove| lze připojení ručit
        
 -  s takto připojenou tabulkou můžeme dále pracovat stejně jako by byla přímo ve vektorové vrstvě (např.měnit symbol, provádět dotazování a analýzy)
              
.. note:: Při připojení se zdrojová data (vektorové vrstvy ani připojené tabulky) nemění. Data z tabulky jsou připojením pouze odkazována k odpovídajícím prvkům atributové tabulce vrstvy.
    
 -  po odebrání tabulky ze seznamu vrstev, nebo přímo vymazání souboru .csv se připojení zruší
 -  pro trvalé uložení připojených dat do vektorové vrstvy lze použít funkci exportu vrstvy (:item:`Uložit jako...`)
