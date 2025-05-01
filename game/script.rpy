define Felix = Character("Felix", color="#d751e4")
define felix_position = Position(xpos=0.5, ypos=0.99)
define mc = Character("[player_name]" , color="#006eff")
define dolnik = Character("dolnik")
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

define energy = 3
default dayofweek = "pondelok"
default dayofweeknumber = 1

screen DayDisplay:
    text "[dayofweek]" ypos 0.85 xpos 0.05
    text "ENERGY: [energy]" ypos 0.9 xpos 0.05

label morning:
    $ energy -= 1
    show city morning
    menu:
        "vyhon si":
            "HELL YEAH"
        "daj si ranajky":
            "mnam mnam mnam"
        "chod spat":
            "chrrrr mimimimimi"
    hide city
return
    
label schoolday:
    $ energy -= 1
    hide city
    show school day
    menu:
        "chod do skoly":
            "Tak ok"
        "daj si obed v skole":
            "mnam mnam mnam"
        "chod za skolu":
            "muhahahaahhaah"
    hide school
return

label day:
    $ energy -= 1
    show city day
    menu:
        "vyhon si znova":
            "HELL YEAH"
        "daj si obed":
            "mnam mnam mnam"
        "chod spat":
            "chrrrr mimimimimi"
    hide city
return
    
label night:
    $ energy -= 1
    show city night
    menu:
        "chod srat":
            "AAAAAHHHHH"
        "daj si veceru":
            "mnam mnam mnam"
        "chod spat":
            "chrrrr mimimimimi"
    hide city
return
    

label daychange:
    $ dayofweeknumber += 1

    if dayofweeknumber == 9:
        $ dayofweeknumber = 1

    elif dayofweeknumber == 1:
        $ dayofweek = "pondelok"

    elif dayofweeknumber == 2:
        $ dayofweek = "utorok"

    elif dayofweeknumber == 3:
        $ dayofweek = "streda"

    elif dayofweeknumber == 4:
        $ dayofweek = "stvrtok"

    elif dayofweeknumber == 5:
        $ dayofweek = "piatok"

    elif dayofweeknumber == 6:
        $ dayofweek = "sobota"

    elif dayofweeknumber == 7:
        $ dayofweek = "nedela"

    else:
        $ dayofweek = "ERROR"
return







label start:




    scene black screen


    "Ako sa voláš?"
    $ player_name = renpy.input("Ako sa voláš?")
    $ player_name = player_name.strip()
    $ player_name = player_name.capitalize()




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


    show Felix base at felix_zoom, felix_position


    Felix "Ako sa voláte [default_name]?"


    mc "[player_name]."


    Felix "No dobre, [player_name]!"
    Felix "A do akého ročníka patríš, [player_name]?"


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
    Felix "A do akej triedy?"
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
    Felix "A do akej triedy?"
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
    Felix "A do akej triedy?"
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
    Felix "A do akej triedy?"
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
    Felix "V.D, co?"
    $ student_class = "V.D"

    jump after_choice

label after_choice:
    Felix "Tak bez do auly uz tam na teba cakaju."


    pause 1.0


    scene bg aula
    with fade


    show Felix base at felix_zoom, felix_position


    Felix "Zravim vsetkych ludi s erazmu na fajnorke!"
    Felix "Dufam ze si uzijete pobyt na Slovensku a studium na Fajnorke."
    Felix "Po tom ako sa zapisete pri dverach do auly, sa postupne presunte do svojich tried a pockajte na vasho triedneho ucitela."
    Felix "A prajem vam vsetkym pekny den!"






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
    
    scene black screen
    show text "O 3 triednicke hodiny neskor..."

    pause 1.0

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
    
    while True:
        show screen DayDisplay
        if energy == 3:
            call morning
        elif energy == 2 and dayofweeknumber <= 5:
            call schoolday
        elif energy == 2:
            call day
        elif energy == 1:
            call night
        else:
            $ energy = 3
            call daychange



    
