# -*- coding: utf-8 -*-
""" Contains test data for byline import """

BYLINE_CASES = [  # List of cases: ( "Input string", "Expected output" )
    (
        "Mike Fürstenberg, Kulturkonsulent i Studentliv, Studentsamskipnaden i Oslo og Akershus",
        "text: Mike Fürstenberg, Kulturkonsulent i Studentliv, Studentsamskipnaden i Oslo og Akershus"
    ), (
        "Thea Marie Astrup • Skjalg Bøhmer Vold (foto)",
        "text: Thea Marie Astrup\nphoto: Skjalg Bøhmer Vold"
    ), (
        "Geir Molnes • Sébastian Dahl (Foto)",
        "text: Geir Molnes\nphoto: Sébastian Dahl"
    ), (
        "Espen Mikkelsen, Styreleder Erasmus Student Network UiO",
        "text: Espen Mikkelsen, Styreleder Erasmus Student Network UiO"
    # ), (
        # "Amanda Schei og Ingrid Keenan, Liberal liste",
        # "text: Amanda Schei, Liberal liste\ntext: Ingrid Keenan, Liberal liste"
    ), (
        "Fredrik Morberg, leder SBIO",
        "text: Fredrik Morberg, leder SBIO"
    ), (
        "Himanshu Gulati, Formann i Fremskrittspartiets Ungdom (FpU)",
        "text: Himanshu Gulati, Formann i Fremskrittspartiets Ungdom (FpU)"
    ), (
        "Tine Tång Engvik, Nestleder Blindern SV",
        "text: Tine Tång Engvik, Nestleder Blindern SV"
    ), (
        "Edle Ravndal, professor, dr. philos., Senter for rus og avhengighetsforskning (SERAF)",
        "text: Edle Ravndal, professor, dr. philos., Senter for rus og avhengighetsforskning (SERAF)",
    ), (
        "Eirin Nordal, internasjonalt ansvarlig i NSO og Jorid Martinsen, Velferds- og likestillingsansvarlig i NSO",
        "text: Eirin Nordal, internasjonalt ansvarlig i NSO\ntext: Jorid Martinsen, Velferds- og likestillingsansvarlig i NSO"
    ), (
        "Jon Skogdal, tidl. ingeniørstudent ved HiOA, nå student ved UiO",
        "text: Jon Skogdal, tidl. ingeniørstudent ved HiOA, nå student ved UiO"
    ), (
        "Aksel Braanen Sterri, tidligere studentpolitiker og forfatter av _Tilbake til politikken: Hvordan Arbeiderpartiet igjen skal bli folkets parti_",
        "text: Aksel Braanen Sterri, tidligere studentpolitiker og forfatter av _Tilbake til politikken: Hvordan Arbeiderpartiet igjen skal bli folkets parti_"
    ), (
        "*Eirik Billingsø Elvevold (tekst) _e.b.elvevold@universitas.no_ • Birte Nystad Mangussen (foto)*",
        "text: Eirik Billingsø Elvevold\nphoto: Birte Nystad Mangussen"
    ), (
        "*Petter Fløttum _petter.flottum@universitas.no_*",
        "text: Petter Fløttum"
    ), (
        "*Petter Fløttum og Ingrid Elise Gipling _petter.flottum@gmail.com_*",
        "text: Petter Fløttum\ntext: Ingrid Elise Gipling"
    ), (
        "*Jana Aleksic (master student at UiO)*",
        "text: Jana Aleksic (master student at UiO)",
    ), (
        "*Sigurd Oland Nedrelid (tekst) • Hans Dalane-Hval (arkivfoto)*",
        "text: Sigurd Oland Nedrelid\narchivephoto: Hans Dalane-Hval"
    ), (
        "*Stian Valla Taraldsvik, student, Queen Mary University of London*",
        "text: Stian Valla Taraldsvik, student, Queen Mary University of London"
    ), (
        "*Hans Dalane-Hval (foto og video) og Ingrid Elise Gipling (tekst)*",
        "photo and video: Hans Dalane-Hval\ntext: Ingrid Elise Gipling"
    ), (
        "*Skrevet av: Hilde Vinje, masterstudent i klassiske språk, Vilde Mortensdatter Horvei, masterstudent i kunsthistorie, Britt Medalen Nilsen, masterstudent i idéhistorie og Bendik Hellem Aaby, masterstudent i filosofi*",
        "text: Hilde Vinje, masterstudent i klassiske språk\ntext: Vilde Mortensdatter Horvei, masterstudent i kunsthistorie\ntext: Britt Medalen Nilsen, masterstudent i idéhistorie\ntext: Bendik Hellem Aaby, masterstudent i filosofi"
    ), (
        "*Magnus Newth (text) mgnewth@universitas.no • Dorthe Karlsen (photography)*",
        "text: Magnus Newth\nphoto: Dorthe Karlsen"
    ), (
        "Truls Oftedal Ellingsen, leder Econa, Handelshøyskolen BI",
        "text: Truls Oftedal Ellingsen, leder Econa, Handelshøyskolen BI"
    ), (
        "Matthis Kleeb Solheim, fotograf i Universitas",
        "text: Matthis Kleeb Solheim, fotograf i Universitas"
    ), (
        "Geir Molnes (tekst), Patrick da Silva Sæther (foto)",
        "text: Geir Molnes\nphoto: Patrick da Silva Sæther"
    ), (
        "*I SØR-AFRIKA: Oda Kristin Korneliussen (tekst og foto)*",
        "text and photo: Oda Kristin Korneliussen, I SØR-AFRIKA"
    ), (
        "*_PÅ VESTBREDDEN:_ Camilla Kleiberg Jensen (tekst og foto)*",
        "text and photo: Camilla Kleiberg Jensen, PÅ VESTBREDDEN"
    ), (
        "*Kristina Holt (tekst og foto)*",
        "text and photo: Kristina Holt"
    ), (
        "I Egypt: Sunniva Rebekka Skjeggestad (tekst og foto)",
        "text and photo: Sunniva Rebekka Skjeggestad, I Egypt",
    ), (
        "tekst og foto Eskil Wie og Frode Nagel Dahl",
        "text and photo: Eskil Wie\ntext and photo: Frode Nagel Dahl"
    ), (
        "Anders Ballangrud – Birte Nystad Magnussen (foto)",
        "text: Anders Ballangrud\nphoto: Birte Nystad Magnussen"
    ), (
        "En matglad Universitas-redaksjon (tekst + småfoto), Birte Nystad Magnussen (hovedbilde)",
        "text and photo: En matglad Universitas-redaksjon\nphoto: Birte Nystad Magnussen"
    ), (
        "Ingvild Sagmoen (tekst), Jenny Dahl Bakken (tekst) Geir Molnes (tekst) • Skjalg Bøhmer Vold (foto)",
        "text: Ingvild Sagmoen\ntext: Jenny Dahl Bakken\ntext: Geir Molnes\nphoto: Skjalg Bøhmer Vold"
    ), (
        "Espen Mikkelsen, Styreleder Erasmus Student Network UiO",
        "text: Espen Mikkelsen, Styreleder Erasmus Student Network UiO"
    ), (
        "*Skrevet av: Hilde Vinje, masterstudent i klassiske språk, Vilde Mortensdatter Horvei, masterstudent i kunsthistorie, Britt Medalen Nilsen, masterstudent i idéhistorie og Bendik Hellem Aaby, masterstudent i filosofi*",
        "text: Hilde Vinje, masterstudent i klassiske språk\ntext: Vilde Mortensdatter Horvei, masterstudent i kunsthistorie\ntext: Britt Medalen Nilsen, masterstudent i idéhistorie\ntext: Bendik Hellem Aaby, masterstudent i filosofi"
    ),
]
