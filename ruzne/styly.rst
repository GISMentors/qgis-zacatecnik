

Příklad stylování kategorizovanou obrysovou čárou 
-------------------------------------------------

V některých případech, zejména pokud tvoříme symbologii pro prezentaci dat, je
nutné věnovat stylování dat větší péči.
Níže je uveden případ stylování dvou vrstev - :map:`parcel a budov`, které se 
vzájemně překrývají. Data jsou získána z RÚIAN-u.

Zadání
^^^^^^

Chceme ostylovat vrstvu :map:`parcel` podle atributu :dbcolumn:`druh pozemku`. 
Druhá vrstva, kterou chceme ostylovat je vrstva :map:`stavebních objektů`,
která by měla být nastylovaná podle atributu :dbcolumn:`typ stavebního objektu`. 
Jelikož se obě vrstvy vzájemně překrývají, tak vrstva stavebních obejktů bude 
vykreslována, ``jenom obrysem``, tedy *bez výplně*.


Nastvení stylu vrstvy parcel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vrstva :map:`parcel` bude zobrazovat druh pozemku (orná půda/zahrada/zastavěná 
plocha a nádvoří/...). Druh pozemku je uveden jako jeden z atributů pomocí 
příslušného kódu - :dbcolumn:`druhpozemkukod`.


Ve vlastnostech vrstvy :map:`parcely` v záložce Styl zvolíme typ stylování 
``kategorizovaný``. U položky :item:`Sloupec` vybereme atribut, podle kterého 
chceme stylovat - v našem případě :dbcolumn:`druhpozemkukod`. 
Vzhledem k tomu, že přes vrstvu parcel budeme vykreslovat ještě vrstvu budov, 
tak budeme parcely stylovat pouze výplní bez ohraničení. 
V nastavení :item:`Symbolu` proto upravíme položku :item:`Styl ohraničení` 
na hodnotu ``Bez čáry``. 

Při takovémto nastavení bude mezi jednotlivými parcelami jemná mezera, ale 
nebude působit rušivě. Pokdu by jsme chtěli styl bez mezery, 
tak bychom zvolili barvu ohraničení na stejnou jako je barva výplně.
Jednotlivé podstatné části nastavení jsou zvýrazněny v :num:`#no-outline`. 

.. _no-outline:

.. figure:: images/style_no_outline.png
   :class: large

   Jednotlivé kroky nastavení kategorizovaného stylování a úprava výchozího
   symbolu.
        

Dalším krokem je vytvoření barevného stylu pro každou hodnotu 
:dbcolumn:`druhu pozemku`.
Pomocí talčítka :item:`Klasifikovat` se vygenerují všechny existující hodnoty
pro zvolený atribut a jedna navíc. 
V tomto případě pro generování používáme ``náhodnou paletu`` barev. 
Jelikož chceme každý druh pozemku obarvit dle hodnoty kódu, tak si každou barvu
ručně opravíme dle svého uvážení. 
Kliknutím do  položky :item:`symbol` u každé hodnoty si můžeme nastavit barvu. 
Dalším požadavkem je, aby se nám v legendě nezobrazoval kód druhu pozemku ale 
přesná hodnota podle číselníku `ČÚZK <http://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Ciselniky-ISKN/Ciselniky-k-nemovitosti.aspx#SC_D_POZEMKU>`_. 
Každou hontotu lze přepsat přímo. 
Ukázka autamticky vygenerovaného stylování a již upravených stylů i s popiskama
pro legendu je na :num:`#change1`.

.. _change1:

.. figure:: images/style_colour_and_legend.png
   :class: large

   Automaticky vygenerované stylování podle zvoleného atributu a jeho ručná
   úprava - symbologie i legendy.



Výsledek stylování se projeví po uložení stylu v mapovém okně (symbologie) i 
panelu vrstev (legenda).

.. figure:: images/style_parcely.png
   :class: large

   Výsledek předchozích kroků stylování v mapovém okně a panelu vrstev.

Nastavení stylu stavebních objektů
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stavební obejtky se budou vykreslovat pouze obvodem nad vrstvou :map:`parcel`. 
Styl vykreslení jejich obvodu se bude lišit podle hodnoty atributu 
:dbcolumn:`typstavebnihoobjektukod`.

Ve vlastnostech vrsvty :map:`stavební objekty` v záložce opět zvolíme typ 
stylování ``kategorizovaný``. 
U položky :item:`Sloupec` vybereme atribut :dbcolumn:`typstavebnihoobjektukod`. 
V položce nastavení :item:`symbolu`  změníme Typ vrstvy symbolů na položku
``Obrys:Jednoduchá čára``. 
Dle potřeby nastavíme i :item:`šířku pera a styl`. 
V případě potřeby je ještě možné použít různé typy efektů pro vykreslování.

.. figure:: images/style_outline.png
   :class: large

   Nastavení symbolu pro vykreslování pouze obrysové čáry prvků

Tak jako v předchozím kroku provedeme klasifikaci podle zvoleného atributu. 
V tomto případě zvolený atribut obsahuje pouze 3 různé hodnoty.
Každý vygenerovaný styl si opět můžeme upravit podle vlastních potřeb, jako i 
popisky pro legendu.



.. figure:: images/style_colour_and_legend2.png
   :class: large
    
   Ruční úprava stylů i popisků legendy je nutná i v tomto případě



Výsledná kombinace obou stylů vrstev je ještě upravena změnou průhlednosti 
vrstvy :map:`parcel` (barvy jsou na :num:`#vysledek` jemnější).

.. _vysledek:

.. figure:: images/style_parcely_stavby.png
   :class: large

   Zobrazení obou vrstev v mapoveém okně. V panelu vrstev je vidět upravené
   legendy u každé vrstvy.

.. tip::
   Vytvořený styl se ukládá jako součást QGIS projektu. 
   Styl každé vrstvy je však možné uložit jako samostatný soubor a pak jej 
   použít u další vrstvy.

   Volba pro uložení  ses nachází přímo v záložce styl ve spodní části. 
   Tlačítkem :item:`Styl` se otevře menu (:num:`#save`), které slouží jak
   pro ukožení stávajícího stylu vrstvy, tak pro načtení uloženého stylu a jeho
   aplikaci na vrstvu.

   .. _save:

   .. figure:: images/style_save.png
      
      Možnost exportu a import stylů pro vrstvu.
      

   Styly se možné uložit do 2 formátů - *SLD* a *QML* (interní soubor pro 
   ukládání stylů QGISu). QML je soubor typu XML, takže je možné jej jednoduše
   editovat i mimo QGIS.
 



