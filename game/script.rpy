define felix = Character("Felix", color="#d751e4")
define felix_position = Position(xpos=0.5, ypos=0.99)
define mc = Character("[player_name]" , color="#006eff")
define dolnik = Character("Dolník")
define suran = Character("Suran")
default default_name = "mlady muz"
default player_name = ""
transform felix_zoom:
    zoom 0.75
define dolnik_position = Position(xpos=0.5, ypos=1.4)
transform dolnik_zoom:
    zoom 1
$ student_student_class = "nezname"

transform slide_in_left:
    xalign -1.0
    linear 1.0 xalign 0.5  # Moves to center over 1 second

init python:
    def sanitize_player_name(name):
        if not name or not isinstance(name, str) or name.strip() == "":
            return default_name
        else:
            return name.strip().capitalize()

screen custom_options():

    modal True  # blocks other input while open
    frame:
        xalign 0.5
        yalign 0.5
        has vbox spacing 15

        text "Moznosti:" size 30

        textbutton "Otvor Inventar" action ShowMenu("inventory_screen")
        textbutton "Ulozit hru" action ShowMenu("save")
        textbutton "Zatvorit" action Hide("custom_options")

init python:
    config.overlay_screens.append("floating_menu")

default inventory = [
]

init python:
    def show_item_info(item):
        renpy.say(None, f"{item['name']}: {item['desc']}")

screen floating_menu():
    frame:
        xalign 0.98
        yalign 0.02
        background "#0008"
        padding (10, 5)
        textbutton "☰" action Show("custom_options") text_size 22





label start:




    scene black screen

    "Ako sa voláš?"
    $ player_name = renpy.input("Ako sa voláš?")

    $ player_name = sanitize_player_name(player_name)

    "Dobre, [player_name]."




    scene internat

    mc "Milý denník."
    mc "Včera som doletel lietadlom na slovensko."  
    mc "V škole, u mňa doma vo fínsku, som mal veľmy dobrý prospech, tak ma pán učiteľ Mäkinen prihlásil na Erazmus."
    mc "Nakoniec sa rozhodlo že pôjdem na Slovensko."
    mc "Let prebehol v poriadku, a ubytovali ma na tento internát v Dúbravke."
    mc "Bývam tu sám, lebo nešlo so mnou veľa žiakov."
    mc "O hodinu mám byť na Fajnorke, škole ktorú mi priradili."
    mc "Neviem sa dočkať"
    "[player_name] odloží svoj denník, a pripravý sa do školy."




    scene black screen
    with fade


    "Po ceste autobusom"




    scene fajnorka
    with fade


    mc "Tak toto je Fajnorka?"
    mc "Pekná Budova."




    scene fajnorka vchod
    with fade


    mc "Dúfam že tu budú aj milý učitelia."




    scene bg schody
    with fade


    show felix base at felix_zoom, felix_position


    felix "Ako sa voláte [default_name]?"


    mc "[player_name]."


    felix "No dobre, [player_name]!"
    felix "A do akého ročníka patríš, [player_name]?"


    menu:
        "1.":
            jump choices1_a
        "2.":
            jump choices1_b
        "3.":
            jump choices1_c
        "4.":
            jump choices1_d
        "5.":
            jump choices1_e

label choices1_a:
    felix "A do akej triedy?"
    menu:
        "I.A":
            "Vybral si I.A triedu."
            $ student_class = "I.A"
        "I.B":
            "Vybral si I.B triedu."
            $ student_class = "I.B"
        "I.C":
            "Vybral si I.C triedu."
            $ student_class = "I.C"
        "I.D":
            "Vybral si I.D triedu."
            $ student_class = "I.D"

    jump after_choice

label choices1_b:
    felix "A do akej triedy?"
    menu:
        "II.A":
            "Vybral si II.A triedu."
            $ student_class = "II.A"
        "II.B":
            "Vybral si II.B triedu."
            $ student_class = "II.B"
        "II.C":
            "Vybral si II.C triedu."
            $ student_class = "II.C"
        "II.D":
            "Vybral si II.D triedu."
            $ student_class = "II.D"

    jump after_choice

label choices1_c:
    felix "A do akej triedy?"
    menu:
        "III.A":
            "Vybral si III.A triedu."
            $ student_class = "III.A"
        "III.B":
            "Vybral si III.B triedu."
            $ student_class = "III.B"
        "III.C":
            "Vybral si III.C triedu."
            $ student_class = "III.C"
        "III.D":
            "Vybral si III.D triedu."
            $ student_class = "III.D"

    jump after_choice

label choices1_d:
    felix "A do akej triedy?"
    menu:
        "IV.A":
            "Vybral si IV.A triedu."
            $ student_class = "IV.A"
        "IV.B":
            "Vybral si IV.B triedu."
            $ student_class = "IV.B"
        "IV.C":
            "Vybral si IV.C triedu."
            $ student_class = "IV.C"
        "IV.D":
            "Vybral si IV.D triedu."
            $ student_class = "IV.D"

    jump after_choice

label choices1_e:
    felix "V.D, co?"
    $ student_class = "V.D"

    jump after_choice

label after_choice:
    felix "Tak bež do auly už tam na teba čakaju."


    pause 1.0


    scene bg aula
    with fade


    show felix base at felix_zoom, felix_position


    felix "Zdravím všetkych ludi z erazmu na Fajnorke!"
    felix "Dúfam že si užijete pobyt na Slovensku a štúdium na Fajnorke."
    felix "Po tom ako sa zapíšete pri dverach do auly, sa postupne presunte do svojích tried a počkajte na vašeho triedneho učiteľa."
    felix "A prajem vám všetkým pekný deň!"






    scene bg dvere_auly


    mc "Dobrý deň, tu sa prosím vás zapisuje?"

    show dolnik base at dolnik_zoom, dolnik_position
    dolnik "Počkaj, ty si [player_name]?"


    mc "Áno, prečo?"


    dolnik "Ja budem tvoj triedny učiteľ kým budeš tu."
    dolnik "Choď do triedy, tam sa dozvieš viac."
    mc "dobre. Ďakujem."
    dolnik "Nie je za čo"

    scene bg chodba
    with fade

    mc "[student_class]..."
    
    scene bg dvere

    mc "aha."
    mc "to bude asi tu"
    "[player_name] otvorí dvere a vojde dnu."

    scene bg trieda
    with fade

    "[player_name] odignoruje pohľady svojich nových spolužiakov a sadne si do voľnej lavice."

    show dolnik base at slide_in_left

    dolnik "Dobrý deň"
    dolnik "Dnes tu máme nového žiaka z Fínska"
    mc "ja som [player_name], Rád vás všetkých spoznávam."
    dolnik "dobre, keď už máme toto z krku, musím vám rozdať tieto rozvrhy."
    "Rozvrh bol pridaný do inventára!"
    scene bg rozvrh
    mc "nevyzerá zas až tak zle..."

    $ inventory.append({ "name": "Rozvrh", "desc": "Tvoj aktuálny školský rozvrh." })
    
    scene black screen
    show text "O 3 triednicke hodiny neskor..."

    pause 2.5

    scene bg trieda
    show dolnik base at dolnik_zoom, dolnik_position
    dolnik "dobre to je dnes teda všetko."
    dolnik "Pakujte domov!"

    scene internat
    with fade
    mc "Milý denníik."
    mc "dnes som bol zapísaný do novej triedy."
    mc "spolužiakov som ešte nemal čas spoznať, ale učitela máme parádneho."
    mc "už sa neviem dočkať na zajtrajšok."
    "[player_name] odloží denník a ide spať."

    scene black screen
    with fade
    "Zrazu zazvoní budík"

    scene internat
    with fade
    mc "Ach, koľko je hodín?"
    mc "7:23???"
    mc "Musím ísť!"

    scene bg trieda
    mc "Prepáčte že idem neskoro ale-"
    show suran placeholder at slide_in_left
    suran "kde si tak dlho?"
    suran "sadaj."
    scene black screen
    with fade
    "[player_name] sa pomali stráca v matematika a nedáva pozor"
    suran "[player_name]!"
    suran "[player_name]!"
    "[player_name] sa prebudí z bdenia ako obarený."
    show suran placeholder
    with fade
    "čo, oddíchol si si?"
    "no poď pred tabulu"

    scene black screen

    "vyrieš príklad"
    $ vysledok = renpy.input("log3(5+4.log2(x-1)) = 2")

if int(vysledok) == 3:
    scene bg trieda
    with fade
    show suran placeholder
    suran "výborne, jednotka"
else:
    scene bg trieda
    with fade
    show suran placeholder
    suran "no, ale takto to nemá byť."
    suran "päťka, sadaj."
    
