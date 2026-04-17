# -*- coding: utf-8 -*-
"""
content_de.py
=============
Alle 2-Wochen-Plan-Inhalte für jeden NST-Typ x Hauptproblem auf Deutsch.
"""

PLANS_DE = {
    # ─── LÖWE ────────────────────────────────────────────────────────────────
    ("lion", "weight"): {
        "headline": "Dein 2-Wochen-Fettabbau-Sprint – Löwen-Stil",
        "intro": (
            "Als Löwe (Natural Signature Type) bist du dopamingetrieben, "
            "wettbewerbsorientiert und brauchst schnelle Ergebnisse. Ein langsamer, "
            "moderater Ansatz wird deine Motivation zerstören. Du blühst bei "
            "aggressiven, kurzen Sprints auf – genau das werden wir tun."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Der aggressive Sprint",
                "days": [
                    ("Tage 1–5", "Kaloriendefizit von 500–700 kcal unter deinem Erhaltungsbedarf. "
                     "Protein hoch halten (mindestens 2 g pro kg Körpergewicht) um Muskeln zu schützen. "
                     "Mahlzeiten: hauptsächlich Protein + gesunde Fette (Eier, Fleisch, Fisch, Avocado, Nüsse). "
                     "Kohlenhydrate minimieren – nur nach dem Training erlaubt."),
                    ("Tage 6–7", "Refeed-Tage: Erhaltungskalorien essen. Komplexe Kohlenhydrate hinzufügen "
                     "(Reis, Haferflocken, Süßkartoffeln). Das setzt Leptin zurück, unterstützt Dopamin "
                     "und verhindert, dass sich dein Stoffwechsel zu schnell anpasst."),
                ]
            },
            {
                "label": "Woche 2 – Härter pushen, scharf bleiben",
                "days": [
                    ("Tage 8–12", "Aggressives Defizit wiederholen. Ergebnisse tracken – "
                     "Löwen werden durch sichtbare Erfolge motiviert. Täglich wiegen und den "
                     "Trend notieren. L-Tyrosin hinzufügen (500–1000 mg vor dem Training) um "
                     "Dopamin zu unterstützen und den Antrieb hochzuhalten."),
                    ("Tage 13–14", "Zweiter Refeed. Fortschritt feiern. Du hast einen vollen "
                     "2-Wochen-Sprint abgeschlossen. Die meisten sehen in diesem Zeitraum 1,5–3 kg Fettabbau."),
                ]
            }
        ],
        "tips": [
            "KEIN langes, langweiliges Cardio – es tötet dein Dopamin. Wähle HIIT oder schweres Krafttraining.",
            "Iss für Energie, nicht für Genuss. Verführerische Lebensmittel aus dem Haus räumen.",
            "Keine Kohlenhydrate vor dem Training – sie beruhigen das ZNS und du musst aufgeladen sein.",
            "Alles tracken. Erfolge halten dich am Laufen. Rückschläge motivieren dich zum Kämpfen.",
            "Supplement-Tipp: L-Tyrosin unterstützt die Dopaminproduktion – dein wichtigster Neurotransmitter.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("lion", "energy"): {
        "headline": "Dein 2-Wochen-Energie-Reset – Löwen-Stil",
        "intro": (
            "Löwen laufen auf Dopamin. Wenn deine Energie einbricht, bedeutet das meistens, "
            "dass Dopamin erschöpft ist – durch Übertraining, schlechte Ernährung oder zu viel "
            "Stress ohne Erholung. So lädst du in 2 Wochen wieder auf."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Das Fundament neu aufbauen",
                "days": [
                    ("Tage 1–3", "Trainingsintensität um 30 % reduzieren. Löwen hassen das, aber "
                     "dein Nervensystem braucht es. Fokus auf Schlaf: 7–8 Stunden anstreben. "
                     "Protein + Fett-Mahlzeiten essen um L-Tyrosin-Transport und Dopamin-Wiederaufbau zu unterstützen."),
                    ("Tage 4–7", "L-Tyrosin hinzufügen (500 mg morgens, 500 mg vor dem Training). "
                     "Koffein nach 14 Uhr eliminieren. Jeden Morgen 10 Minuten in der Sonne spazieren – "
                     "das steigert Dopamin natürlich ohne es zu erschöpfen."),
                ]
            },
            {
                "label": "Woche 2 – Wieder zünden",
                "days": [
                    ("Tage 8–11", "Trainingsintensität auf 80 % zurückbringen. "
                     "Löwen erholen sich schnell wenn Dopamin wieder aufgebaut ist. "
                     "Mahlzeiten-Timing: Protein + Fett morgens, Kohlenhydrate nach dem Training."),
                    ("Tage 12–14", "Volles Training wieder aufnehmen. Du solltest jetzt "
                     "deutlich mehr Energie spüren. Wenn nicht: Schlaf priorisieren und Stressquellen reduzieren."),
                ]
            }
        ],
        "tips": [
            "Dopamin-Erschöpfung ist die häufigste Ursache für Energie-Absturz beim Löwen.",
            "L-Tyrosin ist dein wichtigstes Supplement – es ist der direkte Vorläufer von Dopamin.",
            "Koffein nach 14 Uhr stört den Schlaf und erschöpft Dopamin-Rezeptoren.",
            "Kurze, intensive Workouts laden Dopamin auf – lange, moderate Einheiten erschöpfen es.",
            "Supplement-Tipp: L-Tyrosin + Vitamin D3 + Zink ist der Energie-Stack des Löwen.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("lion", "training"): {
        "headline": "Dein 2-Wochen-Trainings-Konsistenz-Plan – Löwen-Stil",
        "intro": (
            "Löwen trainieren gerne – aber oft zu intensiv, zu oft, oder sie hören auf "
            "wenn sie keine sofortigen Ergebnisse sehen. Hier ist der Plan, der zu deiner "
            "Natur passt und dich langfristig konsistent hält."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Struktur mit Feuer",
                "days": [
                    ("Tage 1–4", "4 Trainingstage: 2x Kraft (schwer, 4–6 Wiederholungen), 2x HIIT (20 Min.). "
                     "Löwen brauchen Intensität und Abwechslung – aber mit Struktur. "
                     "Jede Session hat ein klares Ziel: einen neuen Rekord aufstellen oder die letzte Leistung schlagen."),
                    ("Tage 5–7", "Aktive Erholung: Spaziergang, leichtes Dehnen, Sauna. "
                     "Löwen unterschätzen Erholung – sie ist der Schlüssel zu Fortschritt."),
                ]
            },
            {
                "label": "Woche 2 – Eskalieren und gewinnen",
                "days": [
                    ("Tage 8–12", "Gewichte erhöhen oder Wiederholungen steigern. "
                     "Löwen sind durch sichtbaren Fortschritt motiviert – tracke jede Session. "
                     "Füge L-Tyrosin (500 mg) 30 Min. vor dem Training hinzu für maximalen Fokus."),
                    ("Tage 13–14", "Erholung. Plane die nächsten 4 Wochen – "
                     "Löwen brauchen einen klaren Gegner (Ziel) um motiviert zu bleiben."),
                ]
            }
        ],
        "tips": [
            "Setze dir jede Woche ein konkretes Leistungsziel – Löwen brauchen etwas zum Besiegen.",
            "Trainingspartner oder Wettkampf-Element steigert die Löwen-Performance um 30–40 %.",
            "Vermeide zu viele Ausdauereinheiten – sie senken Dopamin und demotivieren dich.",
            "Tracke jeden Trainingsrekord – dein Fortschritt ist dein Treibstoff.",
            "Supplement-Tipp: L-Tyrosin + Kreatin + Koffein ist der Pre-Workout-Stack des Löwen.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("lion", "sleep"): {
        "headline": "Dein 2-Wochen-Schlaf-Optimierungsplan – Löwen-Stil",
        "intro": (
            "Löwen schlafen schlecht weil ihr Dopaminsystem auch nachts auf Hochtouren läuft. "
            "Dein Gehirn will Probleme lösen, Ziele planen und Gegner besiegen – auch um Mitternacht. "
            "Hier ist der Plan, der dein Nervensystem herunterfährt ohne deine Energie zu zerstören."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Das Nervensystem herunterfahren",
                "days": [
                    ("Tage 1–4", "Kein Bildschirm 60 Minuten vor dem Schlafen. "
                     "Löwen brauchen einen klaren 'Abschalter'. Erstelle eine kurze Abend-Routine: "
                     "10 Min. Lesen, 5 Min. Atemtechnik (4-7-8 Atmung), dann Bett. "
                     "Kein Koffein nach 13 Uhr."),
                    ("Tage 5–7", "Magnesium Glycinat (300 mg) + L-Theanin (200 mg) 30 Min. vor dem Schlafen. "
                     "Diese Kombination beruhigt das Nervensystem ohne dich am nächsten Tag träge zu machen."),
                ]
            },
            {
                "label": "Woche 2 – Tiefschlaf optimieren",
                "days": [
                    ("Tage 8–11", "Schlaftemperatur senken (18–20 Grad). Löwen schlafen besser kühl. "
                     "Kohlenhydrate am Abend hinzufügen (Reis, Haferflocken) – sie senken Dopamin "
                     "und fördern Serotonin für besseren Schlaf."),
                    ("Tage 12–14", "Bewertung: Die meisten Löwen berichten nach 10–14 Tagen "
                     "von deutlich tieferem Schlaf. Wenn nicht: Training spätestens um 18 Uhr beenden."),
                ]
            }
        ],
        "tips": [
            "Dein Dopaminsystem braucht einen klaren Abschalter – eine feste Abendroutine ist Pflicht.",
            "Magnesium Glycinat ist das effektivste Schlaf-Supplement für Löwen.",
            "Kohlenhydrate am Abend sind für Löwen vorteilhaft – sie senken Dopamin und fördern Schlaf.",
            "Trainiere nicht nach 19 Uhr – Adrenalin und Dopamin halten dich wach.",
            "Supplement-Tipp: Magnesium Glycinat + L-Theanin + Ashwagandha ist der Schlaf-Stack des Löwen.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    # ─── FALKE ───────────────────────────────────────────────────────────────
    ("falcon", "weight"): {
        "headline": "Dein 2-Wochen-Fettabbau-Sprint – Falken-Stil",
        "intro": (
            "Als Falke (Natural Signature Type) läufst du auf Dopamin und Adrenalin. "
            "Du brauchst Abwechslung, Tempo und sofortige Ergebnisse – sonst verlierst du das Interesse. "
            "Dieser Plan ist schnell, abwechslungsreich und auf deine Natur zugeschnitten."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Schnell starten, Feuer halten",
                "days": [
                    ("Tage 1–5", "Intermittierendes Fasten (16:8) kombiniert mit Kaloriendefizit (400–600 kcal). "
                     "Falken profitieren von klaren Essensfenstern – kein endloses Zählen, nur ein Zeitfenster. "
                     "Protein hoch (2 g/kg), Mahlzeiten variieren täglich um Langeweile zu vermeiden."),
                    ("Tage 6–7", "Cheat-Fenster: 1 Mahlzeit nach Wahl. Falken brauchen diese Ventile "
                     "um langfristig dabei zu bleiben. Das ist keine Schwäche – das ist Strategie."),
                ]
            },
            {
                "label": "Woche 2 – Intensivieren und variieren",
                "days": [
                    ("Tage 8–12", "Trainingsart wechseln: andere Übungen, anderes Tempo. "
                     "Falken verlieren bei Wiederholung die Motivation. Defizit beibehalten. "
                     "L-Tyrosin (500 mg) + Koffein vor dem Training für maximale Energie."),
                    ("Tage 13–14", "Ergebnisse messen. Falken brauchen sichtbaren Beweis. "
                     "Fotos, Maße, Gewicht – alles dokumentieren. Das ist dein Treibstoff für die nächste Runde."),
                ]
            }
        ],
        "tips": [
            "Variiere deine Mahlzeiten täglich – Falken werden durch Wiederholung demotiviert.",
            "Intermittierendes Fasten passt perfekt zum Falken – einfach, klar, effektiv.",
            "Kein langer Ausdauersport – kurze, intensive Einheiten sind dein Element.",
            "Tracke Ergebnisse visuell – Fotos und Maße motivieren Falken mehr als Zahlen.",
            "Supplement-Tipp: L-Tyrosin + Koffein + Omega-3 ist der Fettabbau-Stack des Falken.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("falcon", "energy"): {
        "headline": "Dein 2-Wochen-Energie-Reset – Falken-Stil",
        "intro": (
            "Falken erschöpfen sich durch zu viele Projekte, zu wenig Fokus und "
            "ständige Reizüberflutung. Dein Dopaminsystem ist überlastet – nicht leer. "
            "Der Unterschied ist entscheidend für die Lösung."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Entlasten und fokussieren",
                "days": [
                    ("Tage 1–4", "Täglich nur 3 Hauptaufgaben. Falken verzetteln sich – "
                     "weniger ist mehr. Handybenachrichtigungen auf 2x täglich reduzieren. "
                     "Omega-3 (2–3 g täglich) für Dopamin-Rezeptor-Gesundheit."),
                    ("Tage 5–7", "Bewegung: 20 Min. intensive Aktivität täglich – "
                     "das entlädt überschüssiges Adrenalin und setzt Endorphine frei. "
                     "Kein Koffein nach 13 Uhr – Falken sind besonders empfindlich."),
                ]
            },
            {
                "label": "Woche 2 – Energie kanalisieren",
                "days": [
                    ("Tage 8–11", "Ein großes Projekt pro Woche – Falken brauchen ein klares Ziel "
                     "um ihre Energie zu bündeln. L-Tyrosin (500 mg morgens) für stabilen Dopaminspiegel."),
                    ("Tage 12–14", "Bewertung: Fühlst du dich fokussierter? Wenn ja, behalte die "
                     "3-Aufgaben-Regel bei. Wenn nicht: Schlaf prüfen – Falken unterschätzen Schlaf massiv."),
                ]
            }
        ],
        "tips": [
            "Reizüberflutung ist der Energie-Killer des Falken – weniger Input, mehr Output.",
            "Omega-3 ist das wichtigste Supplement für Falken – es schützt Dopamin-Rezeptoren.",
            "Kurze, intensive Workouts laden Falken auf – lange Einheiten erschöpfen sie.",
            "Fokus auf ein Projekt statt viele – Falken verlieren Energie durch Verzettelung.",
            "Supplement-Tipp: Omega-3 + L-Tyrosin + Magnesium ist der Energie-Stack des Falken.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("falcon", "training"): {
        "headline": "Dein 2-Wochen-Trainings-Konsistenz-Plan – Falken-Stil",
        "intro": (
            "Falken starten stark – und hören dann auf wenn die Neuheit nachlässt. "
            "Das ist keine Schwäche, das ist deine Neurologie. Dieser Plan nutzt deine "
            "Natur: Abwechslung, Tempo und klare Meilensteine halten dich dabei."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Abwechslung als System",
                "days": [
                    ("Tage 1–4", "Kein fixer Trainingsplan – wähle täglich aus 3 Optionen: "
                     "Kraft, HIIT oder Sport. Falken brauchen Wahlfreiheit. "
                     "Einzige Regel: mindestens 20 Minuten Intensität täglich."),
                    ("Tage 5–7", "Aktive Erholung oder Outdoor-Aktivität. "
                     "Falken erholen sich besser in Bewegung als in Ruhe."),
                ]
            },
            {
                "label": "Woche 2 – Meilensteine setzen",
                "days": [
                    ("Tage 8–12", "Wähle eine Fähigkeit die du verbessern willst "
                     "(z.B. 10 Klimmzüge, 5 km unter 25 Min.). Falken brauchen ein Ziel zum Jagen. "
                     "Täglich 5 Min. gezieltes Üben dieser Fähigkeit."),
                    ("Tage 13–14", "Teste dein Ziel. Falken sind durch Leistungsbeweise motiviert. "
                     "Plane das nächste Ziel sofort – kein Vakuum entstehen lassen."),
                ]
            }
        ],
        "tips": [
            "Variiere dein Training wöchentlich – Falken brauchen Neuheit um motiviert zu bleiben.",
            "Setze dir kurzfristige Ziele (2 Wochen) statt langfristige (6 Monate).",
            "Trainiere mit anderen – soziale Stimulation hält Falken länger dabei.",
            "Musik oder Podcast beim Training steigert die Falken-Performance deutlich.",
            "Supplement-Tipp: L-Tyrosin + Koffein + Kreatin ist der Trainings-Stack des Falken.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("falcon", "sleep"): {
        "headline": "Dein 2-Wochen-Schlaf-Optimierungsplan – Falken-Stil",
        "intro": (
            "Falken schlafen schlecht weil ihr Gehirn ständig neue Ideen generiert "
            "und Adrenalin auch nachts aktiv bleibt. Du brauchst einen klaren Übergang "
            "vom aktiven in den Ruhemodus – und das ist lernbar."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Den Übergang schaffen",
                "days": [
                    ("Tage 1–4", "30 Minuten vor dem Schlafen: alle Ideen aufschreiben (Brain Dump). "
                     "Falken können nicht schlafen wenn Gedanken unfertig sind. "
                     "Papier und Stift neben dem Bett – alles raus, dann Ruhe."),
                    ("Tage 5–7", "L-Theanin (200 mg) + Magnesium Glycinat (300 mg) vor dem Schlafen. "
                     "Kein Bildschirm 45 Minuten vor dem Bett. Falken reagieren stark auf Blaulicht."),
                ]
            },
            {
                "label": "Woche 2 – Schlafqualität steigern",
                "days": [
                    ("Tage 8–11", "Feste Schlafzeit einhalten – auch am Wochenende. "
                     "Falken hassen Routine, aber der Schlaf-Wach-Rhythmus ist nicht verhandelbar. "
                     "Dunkelheit und Kühle im Schlafzimmer (18–20 Grad)."),
                    ("Tage 12–14", "Bewertung: Schläfst du schneller ein? "
                     "Wenn ja, behalte Brain Dump + Supplements bei. "
                     "Wenn nicht: Koffein komplett auf vor 12 Uhr begrenzen."),
                ]
            }
        ],
        "tips": [
            "Brain Dump vor dem Schlafen ist die effektivste Methode für Falken – Gedanken auf Papier bringen.",
            "L-Theanin beruhigt das aktive Falken-Gehirn ohne Schläfrigkeit zu erzeugen.",
            "Feste Schlafzeiten sind für Falken besonders wichtig – ihr Rhythmus ist leicht störbar.",
            "Kein Koffein nach 12 Uhr – Falken metabolisieren Koffein langsamer als andere Typen.",
            "Supplement-Tipp: L-Theanin + Magnesium Glycinat + Melatonin (0,5 mg) ist der Schlaf-Stack des Falken.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    # ─── CHAMÄLEON ───────────────────────────────────────────────────────────
    ("chameleon", "weight"): {
        "headline": "Dein 2-Wochen-Fettabbau-Plan – Chamäleon-Stil",
        "intro": (
            "Als Chamäleon (Natural Signature Type) bist du sozial motiviert und "
            "brauchst Harmonie in deinem Alltag. Harte Diäten erzeugen inneren Konflikt "
            "und soziale Spannung – das sabotiert dich. Dieser Plan arbeitet mit deiner Natur, nicht dagegen."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Sanft starten, Gewohnheiten aufbauen",
                "days": [
                    ("Tage 1–5", "Kaloriendefizit von 300–400 kcal – moderat, nicht aggressiv. "
                     "Chamäleons brauchen einen Ansatz, der sozial kompatibel ist. "
                     "Mahlzeiten: mediterrane Ernährung (Gemüse, Fisch, Olivenöl, Hülsenfrüchte). "
                     "Kein Verzicht auf soziale Mahlzeiten – stattdessen klügere Auswahl treffen."),
                    ("Tage 6–7", "Gemeinsam kochen oder essen gehen – aber bewusst wählen. "
                     "Chamäleons essen besser wenn sie soziale Unterstützung haben."),
                ]
            },
            {
                "label": "Woche 2 – Konsistenz durch Verbindung",
                "days": [
                    ("Tage 8–12", "Einen Accountability-Partner finden – jemand dem du täglich "
                     "deine Mahlzeiten zeigst. Chamäleons performen besser mit sozialer Verantwortung. "
                     "5-HTP (50–100 mg abends) um Serotonin zu unterstützen und emotionales Essen zu reduzieren."),
                    ("Tage 13–14", "Fortschritt feiern – mit anderen. Chamäleons brauchen "
                     "soziale Bestätigung um motiviert zu bleiben."),
                ]
            }
        ],
        "tips": [
            "Soziale Unterstützung ist dein stärkstes Werkzeug – finde einen Partner für deine Reise.",
            "Vermeide isolierte Diäten – Chamäleons brauchen Gemeinschaft um durchzuhalten.",
            "5-HTP unterstützt Serotonin und reduziert emotionales Essen – dein häufigster Fallstrick.",
            "Mediterrane Ernährung passt perfekt zum Chamäleon – lecker, sozial kompatibel, effektiv.",
            "Supplement-Tipp: 5-HTP + Omega-3 + Magnesium ist der Fettabbau-Stack des Chamäleons.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("chameleon", "energy"): {
        "headline": "Dein 2-Wochen-Energie-Reset – Chamäleon-Stil",
        "intro": (
            "Chamäleons erschöpfen sich durch emotionale Belastung und das ständige "
            "Anpassen an andere. Dein Serotoninsystem ist überlastet. "
            "Dieser Plan gibt dir Energie zurück durch Grenzen, Nährstoffe und Selbstfürsorge."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Serotonin aufbauen",
                "days": [
                    ("Tage 1–4", "Täglich 20 Minuten alleine sein – kein Handy, keine Ablenkung. "
                     "Chamäleons brauchen Stille um sich zu regenerieren. "
                     "5-HTP (100 mg abends) + Magnesium (300 mg) für Serotonin-Unterstützung."),
                    ("Tage 5–7", "Tryptophan-reiche Mahlzeiten: Truthahn, Eier, Bananen, Haferflocken. "
                     "Diese Lebensmittel sind direkte Vorläufer von Serotonin."),
                ]
            },
            {
                "label": "Woche 2 – Grenzen setzen, Energie schützen",
                "days": [
                    ("Tage 8–11", "Täglich eine Grenze setzen – ein Nein aussprechen das du sonst "
                     "vermieden hättest. Chamäleons verlieren Energie durch zu viel Ja-Sagen. "
                     "Jedes Nein gibt dir Energie zurück."),
                    ("Tage 12–14", "Bewertung: Fühlst du dich weniger erschöpft? "
                     "Grenzen + Serotonin-Unterstützung sind die zwei wichtigsten Hebel für Chamäleons."),
                ]
            }
        ],
        "tips": [
            "Grenzen setzen ist Energie-Management – jedes Nein ist ein Ja zu dir selbst.",
            "5-HTP ist das wichtigste Supplement für Chamäleons – es unterstützt Serotonin direkt.",
            "Tryptophan-reiche Ernährung ist deine natürliche Energie-Quelle.",
            "Allein-Zeit täglich ist keine Schwäche – es ist dein Aufladen.",
            "Supplement-Tipp: 5-HTP + Magnesium + Vitamin B6 ist der Energie-Stack des Chamäleons.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("chameleon", "training"): {
        "headline": "Dein 2-Wochen-Trainings-Konsistenz-Plan – Chamäleon-Stil",
        "intro": (
            "Chamäleons trainieren am besten in Gemeinschaft. Alleine ist die Motivation "
            "schwach – mit anderen ist sie stark. Dieser Plan nutzt deine soziale Natur "
            "als deinen größten Vorteil."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Gemeinschaft als Fundament",
                "days": [
                    ("Tage 1–4", "Gruppentraining oder Trainingspartner finden. "
                     "Chamäleons erscheinen für andere – nutze das. "
                     "Kursformat, Mannschaftssport oder feste Verabredung mit einem Freund."),
                    ("Tage 5–7", "Aktive Erholung: Yoga, Spaziergang mit jemandem, leichtes Dehnen. "
                     "Chamäleons erholen sich besser in angenehmer Gesellschaft."),
                ]
            },
            {
                "label": "Woche 2 – Routine verankern",
                "days": [
                    ("Tage 8–12", "Feste Trainingszeiten mit anderen vereinbaren. "
                     "Chamäleons halten Termine mit anderen besser ein als Termine mit sich selbst. "
                     "Magnesium (300 mg) nach dem Training für Muskelregeneration."),
                    ("Tage 13–14", "Fortschritt mit deinem Trainingspartner besprechen. "
                     "Plane die nächsten 2 Wochen gemeinsam – Chamäleons bleiben durch Verbindlichkeit dabei."),
                ]
            }
        ],
        "tips": [
            "Gruppentraining oder Trainingspartner ist für Chamäleons unverzichtbar.",
            "Melde dich für Kurse an – die Verbindlichkeit hält dich dabei.",
            "Vermeide Solo-Training wenn möglich – Chamäleons verlieren ohne soziale Stimulation die Motivation.",
            "Teile deine Fortschritte mit anderen – soziale Bestätigung ist dein Treibstoff.",
            "Supplement-Tipp: Magnesium + Vitamin D3 + Omega-3 ist der Trainings-Stack des Chamäleons.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("chameleon", "sleep"): {
        "headline": "Dein 2-Wochen-Schlaf-Optimierungsplan – Chamäleon-Stil",
        "intro": (
            "Chamäleons schlafen schlecht wenn emotionale Spannungen ungelöst sind. "
            "Dein Serotoninsystem braucht Abschluss und Harmonie bevor es sich entspannen kann. "
            "Dieser Plan gibt dir genau das."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Emotionalen Abschluss schaffen",
                "days": [
                    ("Tage 1–4", "Abend-Ritual: 10 Minuten Dankbarkeits-Journal – "
                     "3 positive Dinge des Tages aufschreiben. Chamäleons brauchen emotionalen Abschluss "
                     "um loszulassen. Konflikte des Tages kurz reflektieren und mental abschließen."),
                    ("Tage 5–7", "5-HTP (50 mg) + Magnesium Glycinat (300 mg) vor dem Schlafen. "
                     "Warmes Bad oder Dusche 1 Stunde vor dem Bett – senkt die Körpertemperatur und fördert Schlaf."),
                ]
            },
            {
                "label": "Woche 2 – Tiefschlaf durch Harmonie",
                "days": [
                    ("Tage 8–11", "Keine belastenden Gespräche nach 20 Uhr. "
                     "Chamäleons nehmen Konflikte mit ins Bett – das verhindert Tiefschlaf. "
                     "Beruhigende Musik oder Naturgeräusche beim Einschlafen."),
                    ("Tage 12–14", "Bewertung: Schläfst du tiefer? "
                     "Emotionaler Abschluss + Serotonin-Unterstützung sind die Schlüssel für Chamäleons."),
                ]
            }
        ],
        "tips": [
            "Emotionaler Abschluss vor dem Schlafen ist für Chamäleons wichtiger als jedes Supplement.",
            "5-HTP fördert Serotonin und verbessert die Schlafqualität von Chamäleons deutlich.",
            "Keine Konflikte nach 20 Uhr – dein Nervensystem kann dann nicht mehr abschalten.",
            "Dankbarkeits-Journal ist wissenschaftlich belegt für besseren Schlaf.",
            "Supplement-Tipp: 5-HTP + Magnesium Glycinat + L-Theanin ist der Schlaf-Stack des Chamäleons.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    # ─── WOLF ────────────────────────────────────────────────────────────────
    ("wolf", "weight"): {
        "headline": "Dein 2-Wochen-Fettabbau-Plan – Wolfs-Stil",
        "intro": (
            "Als Wolf (Natural Signature Type) bist du sensibel, tief empfindend und "
            "reagierst stark auf Stress. Aggressive Diäten erhöhen Cortisol und sabotieren "
            "deinen Fettabbau. Dieser Plan ist sanft, nachhaltig und auf dein Nervensystem abgestimmt."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Cortisol senken, Fundament legen",
                "days": [
                    ("Tage 1–5", "Kaloriendefizit von 200–300 kcal – sehr moderat. "
                     "Wölfe reagieren auf Stress mit Cortisol-Ausschüttung, die Fettabbau blockiert. "
                     "Mahlzeiten: entzündungshemmend (Fisch, Beeren, grünes Gemüse, Nüsse). "
                     "Ashwagandha (300–600 mg) täglich um Cortisol zu senken."),
                    ("Tage 6–7", "Erholung und Genuss. Wölfe brauchen Tage ohne Druck. "
                     "Iss was dir gut tut – ohne Schuldgefühle. Das ist Teil des Plans."),
                ]
            },
            {
                "label": "Woche 2 – Sanft intensivieren",
                "days": [
                    ("Tage 8–12", "Defizit leicht erhöhen (300–400 kcal). "
                     "Wölfe können jetzt mehr tragen wenn das Nervensystem stabilisiert ist. "
                     "Bewegung: Yoga, Schwimmen, leichtes Krafttraining – keine hochintensiven Einheiten."),
                    ("Tage 13–14", "Fortschritt würdigen. Wölfe sind oft zu selbstkritisch – "
                     "erkenne an was du erreicht hast, auch wenn es weniger ist als erhofft."),
                ]
            }
        ],
        "tips": [
            "Cortisol ist dein größter Feind beim Fettabbau – Stress-Management ist Ernährungs-Management.",
            "Ashwagandha ist das wichtigste Supplement für Wölfe – es senkt Cortisol nachweislich.",
            "Sanfte Bewegung (Yoga, Schwimmen) ist effektiver für Wölfe als HIIT.",
            "Entzündungshemmende Ernährung unterstützt dein sensibles Nervensystem.",
            "Supplement-Tipp: Ashwagandha + Omega-3 + Magnesium ist der Fettabbau-Stack des Wolfes.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("wolf", "energy"): {
        "headline": "Dein 2-Wochen-Energie-Reset – Wolfs-Stil",
        "intro": (
            "Wölfe erschöpfen sich durch emotionale Überbelastung, Grübeln und "
            "ein hyperaktives Nervensystem. Dein Cortisol ist chronisch erhöht. "
            "Dieser Plan senkt Cortisol, baut GABA auf und gibt dir deine Energie zurück."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Das Nervensystem beruhigen",
                "days": [
                    ("Tage 1–4", "Ashwagandha (600 mg täglich) + Magnesium Glycinat (400 mg abends). "
                     "Diese Kombination ist klinisch belegt für Cortisol-Senkung. "
                     "Täglich 15 Minuten Meditation oder Atemübungen – Wölfe profitieren enorm davon."),
                    ("Tage 5–7", "Bewegung: nur sanfte Aktivitäten (Spaziergang, Yoga, Schwimmen). "
                     "Kein HIIT – es erhöht Cortisol und macht es schlimmer."),
                ]
            },
            {
                "label": "Woche 2 – Energie aufbauen",
                "days": [
                    ("Tage 8–11", "Vitamin B-Komplex + Vitamin D3 hinzufügen. "
                     "Wölfe sind häufig in beiden Bereichen defizitär. "
                     "Mahlzeiten-Timing: regelmäßig essen, kein Auslassen – Blutzucker-Schwankungen "
                     "treffen Wölfe besonders hart."),
                    ("Tage 12–14", "Bewertung: Fühlst du dich ruhiger und energiereicher? "
                     "Cortisol-Senkung braucht Zeit – sei geduldig mit dir."),
                ]
            }
        ],
        "tips": [
            "Chronisch erhöhtes Cortisol ist die Hauptursache für Energie-Mangel beim Wolf.",
            "Ashwagandha + Magnesium ist die effektivste Kombination für Wölfe.",
            "Meditation ist für Wölfe kein Nice-to-have – es ist medizinisch notwendig.",
            "Regelmäßige Mahlzeiten stabilisieren den Blutzucker und verhindern Energie-Abstürze.",
            "Supplement-Tipp: Ashwagandha + Magnesium Glycinat + Vitamin D3 + B-Komplex ist der Energie-Stack des Wolfes.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("wolf", "training"): {
        "headline": "Dein 2-Wochen-Trainings-Konsistenz-Plan – Wolfs-Stil",
        "intro": (
            "Wölfe meiden Training oft weil es sich wie weiterer Stress anfühlt. "
            "Das ist ein Zeichen dass dein Nervensystem überlastet ist – nicht dass du faul bist. "
            "Dieser Plan baut Training als Stressventil auf, nicht als Stressquelle."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Bewegung als Medizin",
                "days": [
                    ("Tage 1–4", "Täglich 20–30 Minuten sanfte Bewegung: Spaziergang in der Natur, "
                     "Yoga oder leichtes Schwimmen. Kein Leistungsdruck. "
                     "Wölfe brauchen Bewegung die das Nervensystem beruhigt, nicht auflädt."),
                    ("Tage 5–7", "Erholung. Wölfe brauchen mehr Regenerationszeit als andere Typen. "
                     "Magnesium Glycinat (400 mg) nach dem Training für Muskelentspannung."),
                ]
            },
            {
                "label": "Woche 2 – Sanft steigern",
                "days": [
                    ("Tage 8–12", "Leichtes Krafttraining hinzufügen (2x pro Woche, 30 Min.). "
                     "Wölfe profitieren von Krafttraining für Selbstvertrauen und Stressresistenz. "
                     "Wichtig: kein Versagen-Training – höre auf bevor es zu anstrengend wird."),
                    ("Tage 13–14", "Bewertung: Fühlt sich Bewegung besser an? "
                     "Wölfe berichten nach 2 Wochen sanftem Training von deutlich besserem Wohlbefinden."),
                ]
            }
        ],
        "tips": [
            "Natur-Bewegung ist für Wölfe besonders wertvoll – Wald, Wasser, frische Luft.",
            "Kein Leistungsdruck beim Training – Wölfe brauchen Bewegung als Erholung, nicht als Wettkampf.",
            "Yoga ist für Wölfe eines der effektivsten Trainingsformen.",
            "Trainiere alleine oder mit einem vertrauten Menschen – Wölfe mögen keine lauten Gruppen.",
            "Supplement-Tipp: Magnesium Glycinat + Ashwagandha + Vitamin D3 ist der Trainings-Stack des Wolfes.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("wolf", "sleep"): {
        "headline": "Dein 2-Wochen-Schlaf-Optimierungsplan – Wolfs-Stil",
        "intro": (
            "Wölfe schlafen schlecht weil Grübeln, Sorgen und ein überaktives Nervensystem "
            "das Einschlafen verhindern. Dein GABA-System ist unteraktiv. "
            "Dieser Plan beruhigt dein Gehirn auf neurologischer Ebene."
        ),
        "weeks": [
            {
                "label": "Woche 1 – GABA aufbauen, Grübeln stoppen",
                "days": [
                    ("Tage 1–4", "Magnesium Glycinat (400 mg) + Ashwagandha (300 mg) 1 Stunde vor dem Schlafen. "
                     "Diese Kombination erhöht GABA und senkt Cortisol – die zwei Haupthebel für Wölfe. "
                     "Atemübung vor dem Schlafen: 4 Sekunden ein, 7 halten, 8 aus (4-7-8 Methode)."),
                    ("Tage 5–7", "Kein Grübeln im Bett erlaubt. Wenn Gedanken kommen: aufstehen, "
                     "kurz aufschreiben, dann zurück ins Bett. Wölfe müssen Grübeln aktiv unterbrechen."),
                ]
            },
            {
                "label": "Woche 2 – Tiefschlaf durch Sicherheit",
                "days": [
                    ("Tage 8–11", "Schlafumgebung optimieren: vollständige Dunkelheit, kühle Temperatur "
                     "(18–19 Grad), weiche Bettwäsche. Wölfe schlafen tiefer wenn sie sich sicher und geborgen fühlen. "
                     "Entspannende Musik oder Naturgeräusche als Einschlafhilfe."),
                    ("Tage 12–14", "Bewertung: Schläfst du schneller ein und tiefer durch? "
                     "GABA-Unterstützung + Grübel-Unterbrechung sind die zwei Schlüssel für Wölfe."),
                ]
            }
        ],
        "tips": [
            "GABA-Unterstützung durch Magnesium ist für Wölfe das effektivste Schlaf-Werkzeug.",
            "Grübeln aktiv unterbrechen – aufschreiben und loslassen.",
            "Sicherheit und Geborgenheit im Schlafzimmer sind für Wölfe besonders wichtig.",
            "4-7-8 Atemtechnik ist klinisch belegt für schnelleres Einschlafen.",
            "Supplement-Tipp: Magnesium Glycinat + Ashwagandha + L-Theanin ist der Schlaf-Stack des Wolfes.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    # ─── EULE ────────────────────────────────────────────────────────────────
    ("owl", "weight"): {
        "headline": "Dein 2-Wochen-Fettabbau-Plan – Eulen-Stil",
        "intro": (
            "Als Eule (Natural Signature Type) brauchst du Struktur, Daten und einen klaren Plan. "
            "Spontane Diäten funktionieren nicht für dich – du brauchst ein System. "
            "Hier ist dein präziser, datengesteuerter 2-Wochen-Plan."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Das System aufsetzen",
                "days": [
                    ("Tage 1–3", "Kalorien und Makros berechnen: Erhaltungsbedarf – 400 kcal = Ziel. "
                     "Eulen brauchen genaue Zahlen. App oder Tabelle nutzen um alles zu tracken. "
                     "Mahlzeiten für die Woche vorplanen – Eulen performen besser mit Vorbereitung."),
                    ("Tage 4–7", "Plan strikt einhalten. Eulen sind gut in Disziplin wenn das System klar ist. "
                     "Täglich wiegen und in Tabelle eintragen – Eulen lieben Datenpunkte."),
                ]
            },
            {
                "label": "Woche 2 – Optimieren und anpassen",
                "days": [
                    ("Tage 8–10", "Daten der ersten Woche analysieren. Wo war der Plan schwierig? "
                     "Eulen optimieren gerne – nutze das. Kleine Anpassungen vornehmen."),
                    ("Tage 11–14", "Verfeinerten Plan umsetzen. Eulen werden durch Präzision motiviert – "
                     "je genauer das System, desto besser die Compliance."),
                ]
            }
        ],
        "tips": [
            "Tracking ist für Eulen kein Aufwand – es ist Motivation. Tracke alles.",
            "Meal Prep am Wochenende spart Zeit und verhindert schlechte Entscheidungen.",
            "Eulen brauchen einen klaren Plan – Improvisation führt zu Scheitern.",
            "Daten-Analyse nach Woche 1 ist Pflicht – Eulen optimieren sich durch Erkenntnisse.",
            "Supplement-Tipp: Omega-3 + Vitamin D3 + Magnesium ist der Fettabbau-Stack der Eule.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("owl", "energy"): {
        "headline": "Dein 2-Wochen-Energie-Reset – Eulen-Stil",
        "intro": (
            "Eulen erschöpfen sich durch Überanalyse, Perfektionismus und "
            "das Gefühl nie fertig zu sein. Dein GABA-System ist erschöpft durch chronischen "
            "mentalen Stress. Dieser Plan gibt deinem Gehirn die Pause die es braucht."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Mentale Last reduzieren",
                "days": [
                    ("Tage 1–4", "Täglich eine 'Done List' statt To-Do-Liste. "
                     "Eulen fokussieren sich auf was noch fehlt – das erschöpft. "
                     "Aufschreiben was du erreicht hast gibt Energie zurück. "
                     "Magnesium L-Threonat (2 g täglich) für kognitive Erholung."),
                    ("Tage 5–7", "Keine Entscheidungen nach 20 Uhr. Eulen grübeln abends – "
                     "das erschöpft das Gehirn für den nächsten Tag. Klare Cut-off-Zeit einführen."),
                ]
            },
            {
                "label": "Woche 2 – Energie durch Struktur",
                "days": [
                    ("Tage 8–11", "Tagesstruktur optimieren: wichtigste Aufgabe morgens, "
                     "wenn kognitive Energie am höchsten ist. Eulen sind Morgenmenschen – "
                     "nutze das Fenster von 8–12 Uhr für Tiefenarbeit."),
                    ("Tage 12–14", "Bewertung: Fühlst du dich weniger erschöpft? "
                     "Mentale Entlastung + Magnesium sind die zwei Schlüssel für Eulen."),
                ]
            }
        ],
        "tips": [
            "Perfektionismus ist der Energie-Killer der Eule – gut genug ist oft besser als perfekt.",
            "Magnesium L-Threonat überquert die Blut-Hirn-Schranke und unterstützt kognitive Erholung.",
            "Done List statt To-Do-Liste – fokussiere auf Fortschritt, nicht auf Rückstand.",
            "Tiefenarbeit in den Morgenstunden maximiert die Eulen-Produktivität.",
            "Supplement-Tipp: Magnesium L-Threonat + Omega-3 + Vitamin B12 ist der Energie-Stack der Eule.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("owl", "training"): {
        "headline": "Dein 2-Wochen-Trainings-Konsistenz-Plan – Eulen-Stil",
        "intro": (
            "Eulen trainieren am besten mit einem präzisen, geplanten System. "
            "Spontanes Training funktioniert nicht – aber ein durchdachter Plan mit "
            "klaren Metriken und Fortschritts-Tracking ist dein stärkstes Werkzeug."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Das Trainings-System aufsetzen",
                "days": [
                    ("Tage 1–3", "Trainingsplan für 2 Wochen schriftlich erstellen: "
                     "Tage, Übungen, Sets, Wiederholungen, Gewichte. "
                     "Eulen brauchen Klarheit bevor sie starten. Kein Plan = kein Training."),
                    ("Tage 4–7", "Plan exakt umsetzen. Eulen sind gut in Disziplin wenn das System klar ist. "
                     "Jede Session dokumentieren – Gewichte, Wiederholungen, Befinden."),
                ]
            },
            {
                "label": "Woche 2 – Daten nutzen, optimieren",
                "days": [
                    ("Tage 8–10", "Daten der ersten Woche analysieren. "
                     "Welche Übungen liefen gut? Wo gibt es Steigerungspotenzial? "
                     "Eulen lieben diese Analyse – sie ist dein Motivations-Treibstoff."),
                    ("Tage 11–14", "Optimierten Plan umsetzen. Eulen werden durch Präzision und "
                     "messbare Verbesserungen motiviert – tracke jeden Fortschritt."),
                ]
            }
        ],
        "tips": [
            "Schriftlicher Trainingsplan ist für Eulen unverzichtbar – kein Plan, kein Training.",
            "Jede Session dokumentieren – Eulen werden durch Daten und Fortschritt motiviert.",
            "Vermeide spontane Trainingsänderungen – Eulen verlieren durch Unstrukturiertheit die Motivation.",
            "Wöchentliche Analyse des Fortschritts hält Eulen langfristig dabei.",
            "Supplement-Tipp: Kreatin + Magnesium + Omega-3 ist der Trainings-Stack der Eule.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },

    ("owl", "sleep"): {
        "headline": "Dein 2-Wochen-Schlaf-Optimierungsplan – Eulen-Stil",
        "intro": (
            "Eulen schlafen schlecht weil ihr analytisches Gehirn auch nachts aktiv ist – "
            "Probleme lösen, Szenarien durchdenken, Pläne schmieden. "
            "Du brauchst ein System das dein Gehirn in den Ruhemodus versetzt."
        ),
        "weeks": [
            {
                "label": "Woche 1 – Das Schlaf-System aufsetzen",
                "days": [
                    ("Tage 1–4", "Feste Schlafzeit und Aufwachzeit – auch am Wochenende. "
                     "Eulen brauchen Routine als Anker. Abend-Protokoll schriftlich festhalten: "
                     "21:30 Bildschirm aus, 22:00 Lesen, 22:30 Bett."),
                    ("Tage 5–7", "Magnesium L-Threonat (2 g) + L-Theanin (200 mg) 1 Stunde vor dem Schlafen. "
                     "Gedanken-Dump: alle offenen Punkte aufschreiben bevor du ins Bett gehst."),
                ]
            },
            {
                "label": "Woche 2 – Schlafqualität messen und optimieren",
                "days": [
                    ("Tage 8–11", "Schlafqualität täglich bewerten (1–10). "
                     "Eulen lieben Daten – tracke Einschlafzeit, Aufwachzeit, Schlafgefühl. "
                     "Optimierungen basierend auf Daten vornehmen."),
                    ("Tage 12–14", "Bewertung: Welche Maßnahmen haben am meisten geholfen? "
                     "Eulen optimieren sich durch Erkenntnisse – nutze deine Daten für den nächsten Monat."),
                ]
            }
        ],
        "tips": [
            "Schriftliches Abend-Protokoll ist für Eulen der effektivste Schlaf-Hack.",
            "Gedanken-Dump vor dem Schlafen entleert das analytische Gehirn.",
            "Magnesium L-Threonat unterstützt kognitive Erholung und verbessert die Schlafqualität.",
            "Schlaf-Tracking motiviert Eulen – Daten machen den Fortschritt sichtbar.",
            "Supplement-Tipp: Magnesium L-Threonat + L-Theanin + Melatonin (0,5 mg) ist der Schlaf-Stack der Eule.",
        ],
        "cta": (
            "Du hast den ersten Schritt gemacht. Jetzt lass es real werden. The Core Path ist ein 30-Tage-Programm, das auf deinen Natural Signature Type zugeschnitten ist. Teste es 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollständige Rückerstattung — keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erhältst du ein exklusives Angebot."
        )
    },
}

# ─── TYPE META (Deutsch) ─────────────────────────────────────────────────────
TYPE_META_DE = {
    "lion": {
        "nst": "Natural Signature Type — Der Löwe",
        "color": "#f59e0b",
        "image": "lion.png",
        "name": "Der Löwe",
        "emoji": "🦁",
        "tagline": "Natural Signature Type – Der Löwe",
        "description": (
            "Du bist dopamingetrieben, wettbewerbsorientiert und brauchst Herausforderungen "
            "um auf Hochtouren zu laufen. Du liebst es zu gewinnen, schnell Ergebnisse zu sehen "
            "und Grenzen zu überschreiten. Deine Stärke ist dein unerschütterlicher Antrieb."
        ),
        "strengths": ["Hohes Durchhaltevermögen unter Druck", "Schnelle Entscheidungsfindung",
                      "Natürliche Führungsqualitäten", "Starke Ergebnisorientierung"],
        "challenges": ["Ungeduld bei langsamen Prozessen", "Risiko von Übertraining",
                       "Schwierigkeiten beim Abschalten", "Impulsive Entscheidungen unter Stress"],
    },
    "falcon": {
        "nst": "Natural Signature Type — Der Falke",
        "color": "#3b82f6",
        "image": "falcon.png",
        "name": "Der Falke",
        "emoji": "🦅",
        "tagline": "Natural Signature Type – Der Falke",
        "description": (
            "Du bist kreativ, schnell und brauchst ständig neue Reize. Dein Gehirn läuft "
            "auf Dopamin und Adrenalin – Routine ist dein größter Feind. Du bringst Ideen "
            "zum Leben und inspirierst andere durch deine Energie."
        ),
        "strengths": ["Kreativität und Innovationskraft", "Schnelles Lernen",
                      "Hohe Energie und Begeisterungsfähigkeit", "Anpassungsfähigkeit"],
        "challenges": ["Schwierigkeiten mit Routine und Konsistenz", "Leicht ablenkbar",
                       "Projekte werden begonnen aber nicht beendet", "Reizüberflutung"],
    },
    "chameleon": {
        "nst": "Natural Signature Type — Das Chamäleon",
        "color": "#10b981",
        "image": "chameleon.png",
        "name": "Das Chamäleon",
        "emoji": "🦎",
        "tagline": "Natural Signature Type – Das Chamäleon",
        "description": (
            "Du bist sozial intelligent, empathisch und passt dich intuitiv an andere an. "
            "Dein Serotoninsystem macht dich zu einem natürlichen Harmonisator. "
            "Du bringst Menschen zusammen und schaffst ein positives Umfeld."
        ),
        "strengths": ["Hohe emotionale Intelligenz", "Natürliche Empathie",
                      "Teamfähigkeit und Kooperation", "Soziale Flexibilität"],
        "challenges": ["Schwierigkeiten Nein zu sagen", "Emotionales Essen unter Stress",
                       "Eigene Bedürfnisse werden hintenangestellt", "Entscheidungsschwäche"],
    },
    "wolf": {
        "nst": "Natural Signature Type — Der Wolf",
        "color": "#8b5cf6",
        "image": "wolf.png",
        "name": "Der Wolf",
        "emoji": "🐺",
        "tagline": "Natural Signature Type – Der Wolf",
        "description": (
            "Du bist tief empfindend, intuitiv und hoch sensibel. Dein Nervensystem "
            "nimmt mehr wahr als das der meisten anderen – das ist eine Stärke und eine Herausforderung. "
            "Du hast tiefe Verbindungen und ein ausgeprägtes Gespür für Authentizität."
        ),
        "strengths": ["Tiefe Empathie und Intuition", "Starke innere Werte",
                      "Kreativität durch Tiefgründigkeit", "Loyalität und Verlässlichkeit"],
        "challenges": ["Überempfindlichkeit gegenüber Kritik", "Chronisch erhöhtes Cortisol",
                       "Grübeln und Überanalyse", "Schwierigkeiten mit Konflikten"],
    },
    "owl": {
        "nst": "Natural Signature Type — Die Eule",
        "color": "#6366f1",
        "image": "owl.png",
        "name": "Die Eule",
        "emoji": "🦉",
        "tagline": "Natural Signature Type – Die Eule",
        "description": (
            "Du bist analytisch, strukturiert und präzise. Dein GABA-dominantes System "
            "macht dich zu einem natürlichen Planer und Qualitätssicherer. "
            "Du denkst bevor du handelst und lieferst konsistent hohe Qualität."
        ),
        "strengths": ["Analytisches Denken und Präzision", "Hohe Zuverlässigkeit",
                      "Systematisches Vorgehen", "Qualitätsbewusstsein"],
        "challenges": ["Perfektionismus und Überanalyse", "Schwierigkeiten mit Veränderungen",
                       "Entscheidungslähmung", "Mentale Erschöpfung durch Grübeln"],
    },
}

# ─── ADJEKTIVE (Deutsch) ──────────────────────────────────────────────────────
ADJECTIVES_DE = {
    "lion": ["Dominant", "Risikofreudig", "Zielstark", "Direkt", "Extrovertiert"],
    "falcon": ["Kreativ", "Spontan", "Ideenreich", "Impulsiv", "Begeisterungsfähig"],
    "chameleon": ["Anpassungsfähig", "Offen", "Vielseitig", "Sozial flexibel", "Harmonieorientiert"],
    "wolf": ["Sensibel", "Einfühlsam", "Verletzlich", "Tiefgründig", "Introvertiert"],
    "owl": ["Strukturiert", "Routiniert", "Präzise", "Planorientiert", "Zuverlässig"],
}

# ─── FRAGEN (Deutsch) ─────────────────────────────────────────────────────────
QUESTIONS_DE = [
    {"id": 1, "type": "lion",      "text": "Ich muss schnell Ergebnisse erzielen."},
    {"id": 2, "type": "lion",      "text": "Ich brauche kontinuierlich Herausforderungen, sonst verliere ich die Motivation."},
    {"id": 3, "type": "falcon",    "text": "Ich verliere schnell das Interesse, wenn alles gleich bleibt."},
    {"id": 4, "type": "falcon",    "text": "Unter Druck werde ich fokussierter und performe besser."},
    {"id": 5, "type": "chameleon", "text": "Ich sage manchmal Ja, obwohl ich innerlich Nein meine, um Konflikte zu vermeiden."},
    {"id": 6, "type": "chameleon", "text": "Entscheidungen fallen mir schwer, weil ich stark darauf achte, wie sie andere beeinflussen."},
    {"id": 7, "type": "wolf",      "text": "Ich nehme Kritik sehr oft persönlich."},
    {"id": 8, "type": "wolf",      "text": "Ein negatives Erlebnis beschäftigt mich den ganzen Tag."},
    {"id": 9, "type": "owl",       "text": "Ich brauche immer einen klaren Plan."},
    {"id": 10, "type": "owl",      "text": "Unerwartete Änderungen machen mich nervös."},
]

PROBLEMS_DE = [
    {"id": "weight",   "text": "Ich nehme zu / kann nicht abnehmen"},
    {"id": "energy",   "text": "Ich bin ständig erschöpft / habe keine Energie"},
    {"id": "training", "text": "Ich trainiere nicht regelmäßig"},
    {"id": "sleep",    "text": "Ich schlafe schlecht"},
]

UI_DE = {
    "title": "Kostenloser Natural Signature Type Test",
    "subtitle": "Entdecke deinen Typ in 2 Minuten",
    "start_btn": "Test starten",
    "yes_btn": "✓ Ja, das bin ich",
    "no_btn": "✗ Eher nicht",
    "question_label": "Frage",
    "of_label": "von",
    "adjectives_title": "Welche Eigenschaften beschreiben dich?",
    "adjectives_subtitle": "Wähle bis zu 3 Adjektive, die am besten zu dir passen.",
    "problem_title": "Was ist dein größtes Problem gerade?",
    "email_title": "Fast geschafft! Wo sollen wir deinen Plan hinschicken?",
    "name_placeholder": "Dein Vorname",
    "email_placeholder": "Deine E-Mail-Adresse",
    "consent_text": "Ich habe die Datenschutzerklärung gelesen und stimme zu. (inkl. Haftungsausschluss)",
    "submit_btn": "Mein Ergebnis anzeigen →",
    "result_title": "Dein Natural Signature Type",
    "primary_type": "Primärtyp",
    "secondary_type": "Sekundärtyp",
    "your_plan": "Dein persönlicher 2-Wochen-Plan",
    "download_btn": "2-Wochen-Plan als PDF herunterladen",
    "cta_title": "Bereit für den nächsten Schritt?",
    "cta_subtitle": "Du hast deinen Typ entdeckt. Jetzt ist es Zeit, wirklich etwas zu verändern.",
    "core_path_btn": "Core Path starten — 49€",
    "whatsapp_btn": "Mit René auf WhatsApp chatten",
    "whatsapp_hours": "Mo–Fr · 9–18 Uhr",
    "whatsapp_note": "Außerhalb der Geschäftszeiten? René antwortet am nächsten Werktag.",
    "disclaimer": "Kein Arzt. Alle Empfehlungen basieren auf Fachliteratur, Zertifikaten (Ernährungscoach, Natural Signature Typing) und jahrelanger Erfahrung.",
    "strengths_label": "Deine Stärken",
    "challenges_label": "Deine Herausforderungen",
    "week1_label": "Woche 1",
    "week2_label": "Woche 2",
    "daily_actions": "Tägliche Maßnahmen",
    "pro_tip": "Profi-Tipp",
    "guarantee_title": "Geld-zurück-Garantie",
    "guarantee_text": "Teste The Core Path 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollst\u00e4ndige R\u00fcckerstattung \u2014 keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erh\u00e4ltst du ein exklusives Angebot.",
    "privacy_link": "Datenschutzerklärung",
    "hero_title": "Entdecke deinen Natural Signature Type",
    "hero_subtitle": "10 Fragen. 2 Minuten. Dein persönlicher 2-Wochen-Plan.",
    "questions_title": "Beantworte die folgenden Fragen",
    "yes": "Ja",
    "no": "Nein",
    "email_name": "Dein Name",
    "email_address": "Deine E-Mail-Adresse",
    "email_placeholder_name": "Max Mustermann",
    "email_placeholder_email": "max@beispiel.de",
    "privacy_text": "Ich habe die Datenschutzerklärung gelesen und stimme zu.",
    "secondary_label": "Sekundärtyp",
    "your_problem": "Dein Ziel",
    "week_label": "Woche",
    "tips_title": "Wichtige Tipps für deinen Typ",
    "cta_badge": "Bereit für den nächsten Level?",
    "cta_desc": "30-Tage-Programm — abgestimmt auf deinen Natural Signature Type.",
    "cta_guarantee": "30 Tage Geld-zur\u00fcck-Garantie: Teste The Core Path 30 Tage lang komplett risikofrei. Nicht zufrieden? Vollst\u00e4ndige R\u00fcckerstattung \u2014 keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erh\u00e4ltst du ein exklusives Angebot.",
    "cta_btn": "Core Path starten \u2014 49\u20ac",
    "cta_btn_sub": "30 Tage Geld-zur\u00fcck-Garantie inklusive",
    "pdf_header": "Deine kostenlose Natural Signature Type Auswertung",
    "pdf_greeting": "Hallo",
    "pdf_type_label": "Dein Natural Signature Type",
    "pdf_goal_label": "Dein Hauptziel",
    "pdf_tips_title": "Wichtige Tipps für deinen Typ",
    "pdf_cta_title": "The Core Path - Dein nächster Schritt",
    "pdf_cta_sub": "30-Tage-Programm - abgestimmt auf deinen Natural Signature Type",
    "pdf_guarantee": "30 Tage Geld-zur\u00fcck-Garantie: Teste The Core Path 30 Tage lang komplett risikofrei. Nicht zufrieden? Du erh\u00e4ltst dein Geld vollst\u00e4ndig zur\u00fcck - keine Fragen gestellt. Die 30 Tage durchgezogen und willst mehr? Als Core Path Absolvent erh\u00e4ltst du ein exklusives Angebot.",
    "pdf_disclaimer": "Hinweis: Rene Rusch ist kein Arzt. Die Inhalte dieses Berichts basieren auf professionellen Zertifikaten (inkl. Natural Signature Typing und Ernaehrungscoaching), wissenschaftlicher Fachliteratur und jahrelanger praktischer Erfahrung. Dieser Bericht ersetzt keine aerztliche Beratung. Konsultiere einen qualifizierten Gesundheitsexperten, bevor du wesentliche Aenderungen an deiner Ernaehrung, deinem Training oder deiner Supplementierung vornimmst.",
    "pdf_footer": "NeuroHealthMastery | neurohealthmastery.com | Erstellt am",
}

PROBLEM_LABELS_DE = {
    "weight":   "Gewicht / Abnehmen",
    "energy":   "Energie / Erschöpfung",
    "training": "Training / Bewegung",
    "sleep":    "Schlaf",
}
