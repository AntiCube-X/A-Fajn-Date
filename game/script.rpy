define felix = Character("felix", color="#d751e4")
define felix_position = Position(xpos=0.5, ypos=0.99)
define mc = Character("[player_name]" , color="#006eff")
define ucitel = Character("Ucitel")
default default_name = "mlady muz"
default player_name = ""
transform felix_zoom:
    zoom 0.75

$ class = "nezname"



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
    mc "Bývam tu sám, lobo nešlo so mnou veľa žiakov."
    mc "O hodinu mám byť na *Fajnorke*, škole ktorú mi priradili."
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

    felix "Ako sa volate [default_name]?"

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
            $ class = "I.A"
        "I.B":
            "Vybral si I.B triedu."
            $ class = "I.B"
        "I.C":
            "Vybral si I.C triedu."
            $ class = "I.C"
        "I.D":
            "Vybral si I.D triedu."
            $ class = "I.D"

    jump after_choice

label choices1_b:
    felix "A do akej triedy?"
    menu:
        "II.A":
            "Vybral si II.A triedu."
            $ class = "II.A"
        "II.B":
            "Vybral si II.B triedu."
            $ class = "II.B"
        "II.C":
            "Vybral si II.C triedu."
            $ class = "II.C"
        "II.D":
            "Vybral si II.D triedu."
            $ class = "II.D"

    jump after_choice

label choices1_c:
    felix "A do akej triedy?"
    menu:
        "III.A":
            "Vybral si III.A triedu."
            $ class = "III.A"
        "III.B":
            "Vybral si III.B triedu."
            $ class = "III.B"
        "III.C":
            "Vybral si III.C triedu."
            $ class = "III.C"
        "III.D":
            "Vybral si III.D triedu."
            $ class = "III.D"

    jump after_choice

label choices1_d:
    felix "A do akej triedy?"
    menu:
        "IV.A":
            "Vybral si IV.A triedu."
            $ class = "IV.A"
        "IV.B":
            "Vybral si IV.B triedu."
            $ class = "IV.B"
        "IV.C":
            "Vybral si IV.C triedu."
            $ class = "IV.C"
        "IV.D":
            "Vybral si IV.D triedu."
            $ class = "IV.D"

    jump after_choice

label choices1_e:
    felix "V.D, co?"
    $ class = "V.D"

    jump after_choice

label after_choice:
    felix "Tak bez do auly uz tam na teba cakaju."


    pause 1.0


    scene bg aula
    with fade

    show felix base at felix_zoom, felix_position

    felix "Zravim vsetkych ludi s erazmu na fajnorke!"
    felix "Dufam ze si uzijete pobyt na Slovensku a studium na Fajnorke."
    felix "Po tom ako sa zapisete pri dverach do auly, sa postupne presunte do svojich tried a pockajte na vasho triedneho ucitela."
    felix "A prajem vam vsetkym pekny den!"



    scene bg dvere_auly

    mc "Dobry den, tu sa prosimvas zapisuje?"

    ucitel "Dobry den, ano tu sa mozete podpisat" #ukaze mu fajnoracku kroniku
# TU MA BYT NAHODNY  UCITEL NIKTO MA AKTUALNE NENAPADA
    ucitel "Pockat ty si [player_name]?"

    mc "Ano, preco?"

    ucitel "Ja budem tvoja triedna ucitelka tento rok."