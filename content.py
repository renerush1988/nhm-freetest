"""
content.py
==========
All 2-week plan content for each NST type × main problem combination.
Language: English
"""

PLANS = {
    # ─── LION (1A) ────────────────────────────────────────────────────────────
    ("lion", "weight"): {
        "headline": "Your 2-Week Fat Loss Sprint — Lion Style",
        "intro": (
            "As a Lion (Natural Signature Type), you are dopamine-driven, "
            "competitive, and need to see results fast. A slow, moderate approach "
            "will kill your motivation. You thrive on aggressive, short sprints — "
            "so that's exactly what we're going to do."
        ),
        "weeks": [
            {
                "label": "Week 1 — The Aggressive Sprint",
                "days": [
                    ("Days 1–5", "Calorie deficit of 500–700 kcal below your maintenance. "
                     "Keep protein high (at least 2g per kg of bodyweight) to protect muscle. "
                     "Meals: mostly protein + healthy fats (eggs, meat, fish, avocado, nuts). "
                     "Minimize carbs — save them for post-workout only."),
                    ("Days 6–7", "Refeed days: eat at maintenance calories. Add complex carbs "
                     "(rice, oats, sweet potato). This resets leptin, supports dopamine, "
                     "and keeps your metabolism from adapting too quickly."),
                ]
            },
            {
                "label": "Week 2 — Push Harder, Stay Sharp",
                "days": [
                    ("Days 8–12", "Repeat the aggressive deficit. Track your results — "
                     "Lions are motivated by visible wins. Weigh yourself daily and note "
                     "the trend. Add L-Tyrosine (500–1000mg before training) to support "
                     "dopamine and keep your drive high."),
                    ("Days 13–14", "Second refeed. Celebrate the progress. You've completed "
                     "a full 2-week sprint. Most people see 1.5–3 kg of fat loss in this window."),
                ]
            }
        ],
        "tips": [
            "Do NOT do long, boring cardio — it kills your dopamine. Choose HIIT or heavy lifting instead.",
            "Eat for fuel, not pleasure. Keep tempting foods out of the house.",
            "No pre-workout carbs — they calm the CNS and you need to be fired up.",
            "Track everything. Wins keep you going. Losses motivate you to fight back.",
            "Supplement tip: L-Tyrosine supports dopamine production — your key neurotransmitter.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("lion", "energy"): {
        "headline": "Your 2-Week Energy Reset — Lion Style",
        "intro": (
            "Lions run on dopamine. When your energy crashes, it usually means "
            "dopamine is depleted — from overtraining, poor nutrition, or too much "
            "stress without recovery. Here's how to recharge in 2 weeks."
        ),
        "weeks": [
            {
                "label": "Week 1 — Rebuild the Foundation",
                "days": [
                    ("Days 1–3", "Reduce training intensity by 30%. Lions hate this, but "
                     "your nervous system needs it. Focus on sleep: aim for 7–8 hours. "
                     "Eat protein + fat meals to support L-Tyrosine transport and dopamine rebuilding."),
                    ("Days 4–7", "Add L-Tyrosine (500mg in the morning, 500mg pre-workout). "
                     "Eliminate caffeine after 2pm. Add a 10-minute walk in sunlight each morning "
                     "— this boosts dopamine naturally without depleting it."),
                ]
            },
            {
                "label": "Week 2 — Reignite",
                "days": [
                    ("Days 8–11", "Return to full training intensity. You'll notice the difference "
                     "now that your dopamine reserves are partially restored. Add a new challenge "
                     "to your training — a new PR attempt, a new exercise, a competition goal."),
                    ("Days 12–14", "Assess your energy levels. If they're back, maintain the "
                     "L-Tyrosine protocol and the sleep discipline. If still low, consider "
                     "a full blood panel — Lions sometimes push too hard for too long."),
                ]
            }
        ],
        "tips": [
            "Dopamine depletion is your #1 enemy. Protect it with protein-rich meals and adequate sleep.",
            "Short, intense workouts beat long, draining ones for your type.",
            "Novelty restores motivation — change something in your routine every week.",
            "Avoid alcohol — it crashes dopamine the next day and wrecks your drive.",
            "Supplement tip: L-Tyrosine + Magnesium Glycinate (before bed) is a powerful combo for Lions.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("lion", "training"): {
        "headline": "Your 2-Week Training Consistency Plan — Lion Style",
        "intro": (
            "Lions don't lack motivation — they lack structure that keeps them engaged. "
            "You get bored, you skip. You feel unchallenged, you quit. "
            "This plan is built around what actually works for your type."
        ),
        "weeks": [
            {
                "label": "Week 1 — Build the Habit with Intensity",
                "days": [
                    ("Days 1–3", "Train 3 days this week. Each session: 20–30 minutes, "
                     "high intensity, compound movements only (squat, deadlift, bench, overhead press). "
                     "Keep sets to 3–5, reps to 3–5. Heavy and fast. No fluff."),
                    ("Days 4–7", "Rest or active recovery (walking, mobility). "
                     "Set a specific goal for next week — a new weight to hit, a PR to beat. "
                     "Lions need a target to chase."),
                ]
            },
            {
                "label": "Week 2 — Chase the Target",
                "days": [
                    ("Days 8–11", "Train 4 days. Attempt your PR goal on Day 8. "
                     "Add one new exercise or variation you've never tried — this satisfies "
                     "your novelty drive and keeps dopamine high."),
                    ("Days 12–14", "Two more sessions. End the week with a workout that "
                     "makes you feel powerful. Write down what you achieved this week — "
                     "Lions are motivated by their own track record."),
                ]
            }
        ],
        "tips": [
            "Never train longer than 45–60 minutes — quality over quantity for your type.",
            "You need a goal, not a routine. Set a new PR every 2 weeks.",
            "Train with someone competitive — Lions perform better when there's a rival.",
            "Skip the warm-up fluff. Do 3–5 minutes of CNS activation (box jumps, explosive push-ups).",
            "Supplement tip: Caffeine + L-Tyrosine pre-workout is ideal for Lions — boosts dopamine and drive.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("lion", "sleep"): {
        "headline": "Your 2-Week Sleep Optimization Plan — Lion Style",
        "intro": (
            "Lions often sacrifice sleep for results. But poor sleep depletes dopamine, "
            "crashes testosterone, and kills the very drive that makes you a Lion. "
            "Two weeks of better sleep will change everything."
        ),
        "weeks": [
            {
                "label": "Week 1 — Break the Bad Habits",
                "days": [
                    ("Days 1–4", "Set a hard stop time: no screens 60 minutes before bed. "
                     "Lions are stimulation-seekers — your brain won't shut off unless you force it. "
                     "Replace screens with reading (non-fiction, strategy, competition — things that "
                     "satisfy your brain without blue light)."),
                    ("Days 5–7", "Add Magnesium Glycinate (300–400mg, 30 minutes before bed). "
                     "This calms the nervous system without sedating you. "
                     "Keep the bedroom cold (17–19°C). Lions sleep better in cool environments."),
                ]
            },
            {
                "label": "Week 2 — Lock In the Routine",
                "days": [
                    ("Days 8–11", "Same bedtime every night — even on weekends. "
                     "Lions hate routine, but sleep is non-negotiable for dopamine recovery. "
                     "Track your sleep quality with any app or wearable — data motivates Lions."),
                    ("Days 12–14", "Assess: are you waking up more refreshed? "
                     "If yes, lock in this protocol permanently. "
                     "If not, consider cutting caffeine completely after 12pm."),
                ]
            }
        ],
        "tips": [
            "Poor sleep = low dopamine the next day. For Lions, this is catastrophic for performance.",
            "No alcohol before bed — it fragments sleep and crashes recovery hormones.",
            "Morning sunlight (10 min) sets your circadian rhythm and boosts dopamine.",
            "Train hard, but not within 3 hours of bedtime — adrenaline will keep you awake.",
            "Supplement tip: Magnesium Glycinate + Ashwagandha is the Lion's sleep stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    # ─── FALCON (1B) ──────────────────────────────────────────────────────────
    ("falcon", "weight"): {
        "headline": "Your 2-Week Fat Loss Sprint — Falcon Style",
        "intro": (
            "As a Falcon (Natural Signature Type), you're dopamine-driven, creative, "
            "and need variety to stay engaged. A boring diet kills you. "
            "This plan uses intermittent fasting and variety to keep you sharp and losing fat."
        ),
        "weeks": [
            {
                "label": "Week 1 — The IF Sprint",
                "days": [
                    ("Days 1–5", "Implement a 14–16 hour daily fast (e.g., eat between 12pm–8pm). "
                     "During your eating window: high protein, moderate fat, low carbs. "
                     "Falcons respond well to fasting because it stimulates brain activity "
                     "and keeps dopamine elevated during the fasted state."),
                    ("Days 6–7", "Refeed days: eat at maintenance. Add complex carbs. "
                     "Try a new food or recipe — Falcons need novelty even in their diet."),
                ]
            },
            {
                "label": "Week 2 — Switch It Up",
                "days": [
                    ("Days 8–12", "Change your eating window slightly (e.g., 10am–6pm). "
                     "Add one new meal or food source. Keep the deficit. "
                     "Falcons build momentum through variety — don't let the plan get stale."),
                    ("Days 13–14", "Second refeed. Assess results. "
                     "Falcons typically see 1–2.5 kg of fat loss in 2 weeks with this approach."),
                ]
            }
        ],
        "tips": [
            "Intermittent fasting is your superpower — it stimulates your brain and supports fat loss.",
            "Change your meals regularly. Eating the same thing every day will make you quit.",
            "Post-workout carbs only — no pre-workout carbs (they calm the CNS you need fired up).",
            "L-Tyrosine + Choline-rich foods (eggs, liver) support your dopamine AND acetylcholine.",
            "Supplement tip: L-Tyrosine + Alpha-GPC is the Falcon's cognitive and fat loss stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("falcon", "energy"): {
        "headline": "Your 2-Week Energy Reset — Falcon Style",
        "intro": (
            "Falcons crash when they're understimulated or when acetylcholine is depleted. "
            "If you're tired, it's usually because your brain is bored or your neurotransmitters "
            "are running low. Here's how to fix it."
        ),
        "weeks": [
            {
                "label": "Week 1 — Stimulate and Restore",
                "days": [
                    ("Days 1–4", "Add choline-rich foods daily: eggs (3–4/day), liver once a week, "
                     "or supplement with Alpha-GPC (300mg in the morning). "
                     "This directly supports acetylcholine — your primary neurotransmitter."),
                    ("Days 5–7", "Introduce a new physical activity or skill (new sport, new movement, "
                     "new workout style). Falcons recharge through novelty — this is not optional, "
                     "it's neurological medicine for your type."),
                ]
            },
            {
                "label": "Week 2 — Sustain the Charge",
                "days": [
                    ("Days 8–11", "Keep the choline protocol. Add a 10-minute learning session daily "
                     "(podcast, book, skill) — Falcons are energized by mental stimulation."),
                    ("Days 12–14", "Assess energy. If improved, maintain the protocol. "
                     "If still low, check sleep quality and reduce training volume temporarily."),
                ]
            }
        ],
        "tips": [
            "Boredom is your biggest energy drain. Change something every week.",
            "Eggs daily are non-negotiable for Falcons — choline is your fuel.",
            "Short, intense workouts energize you. Long, repetitive ones drain you.",
            "Fasting in the morning keeps your brain sharp and energy stable.",
            "Supplement tip: Alpha-GPC + L-Tyrosine is the Falcon's energy stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("falcon", "training"): {
        "headline": "Your 2-Week Training Consistency Plan — Falcon Style",
        "intro": (
            "Falcons are the most naturally athletic type — but they get bored fastest. "
            "The key to consistency is variety, challenge, and skill. "
            "This plan keeps you engaged and progressing."
        ),
        "weeks": [
            {
                "label": "Week 1 — Explosive and Varied",
                "days": [
                    ("Days 1–4", "Train 4 days. Each session: different focus. "
                     "Day 1: explosive power (jumps, sprints, cleans). "
                     "Day 2: skill work (new movement or technique). "
                     "Day 3: strength. Day 4: conditioning circuit."),
                    ("Days 5–7", "Active recovery. Try something completely new: "
                     "a martial arts class, a climbing session, a sport you've never played. "
                     "This is training for Falcons."),
                ]
            },
            {
                "label": "Week 2 — Raise the Bar",
                "days": [
                    ("Days 8–12", "Repeat the varied structure but increase intensity. "
                     "Add a performance metric to each session (time, weight, reps). "
                     "Falcons are motivated by measurable improvement."),
                    ("Days 13–14", "Two sessions. End with something fun and challenging. "
                     "Reflect on what you learned and improved this week."),
                ]
            }
        ],
        "tips": [
            "Never repeat the exact same workout twice in a row — you'll lose interest fast.",
            "Skill acquisition is training for you. Learning a new movement counts.",
            "Train with people who challenge you athletically.",
            "Keep sessions under 60 minutes — quality and variety over duration.",
            "Supplement tip: Alpha-GPC pre-workout enhances motor learning and focus for Falcons.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("falcon", "sleep"): {
        "headline": "Your 2-Week Sleep Optimization Plan — Falcon Style",
        "intro": (
            "Falcons have racing minds. When you lie down, your brain keeps generating ideas. "
            "The solution isn't to suppress it — it's to give your brain a proper shutdown protocol."
        ),
        "weeks": [
            {
                "label": "Week 1 — Wind Down the Machine",
                "days": [
                    ("Days 1–4", "Create a 30-minute pre-sleep ritual: write down all ideas and "
                     "tomorrow's plan (brain dump). This tells your brain it's safe to stop processing. "
                     "Then: dim lights, calm music or silence, no screens."),
                    ("Days 5–7", "Add L-Theanine (200mg) 30 minutes before bed. "
                     "It calms the mind without sedation — perfect for the active Falcon brain. "
                     "Keep bedroom cool and dark."),
                ]
            },
            {
                "label": "Week 2 — Optimize Recovery",
                "days": [
                    ("Days 8–11", "Add Magnesium Glycinate (300mg) to your evening stack. "
                     "Track sleep with an app — Falcons love data and will optimize once they see it."),
                    ("Days 12–14", "Assess sleep quality. Most Falcons see significant improvement "
                     "with the brain dump + L-Theanine + Magnesium combo."),
                ]
            }
        ],
        "tips": [
            "Your brain needs a 'save and close' signal before sleep. The brain dump is that signal.",
            "Avoid intense mental stimulation (news, social media, debates) in the last hour before bed.",
            "Morning training is better for Falcons — it uses up the mental energy early.",
            "Consistency in sleep timing matters more than duration for your type.",
            "Supplement tip: L-Theanine + Magnesium Glycinate is the Falcon's sleep stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    # ─── CHAMELEON (2A) ───────────────────────────────────────────────────────
    ("chameleon", "weight"): {
        "headline": "Your 2-Week Fat Loss Plan — Chameleon Style",
        "intro": (
            "As a Chameleon (Natural Signature Type), you need variety to stay motivated. "
            "The good news: almost every diet approach works for you. "
            "The bad news: you'll get bored of any single approach quickly. "
            "This plan rotates strategies to keep you engaged and losing fat."
        ),
        "weeks": [
            {
                "label": "Week 1 — Carb Cycling",
                "days": [
                    ("Days 1–3 (Low Carb)", "Calorie deficit of 400–500 kcal. "
                     "Protein high, carbs very low (under 50g), fats moderate. "
                     "Focus on lean meats, vegetables, eggs, and healthy fats."),
                    ("Days 4–5 (Moderate Carb)", "Deficit of 200–300 kcal. "
                     "Add complex carbs around training (rice, oats, sweet potato). "
                     "This variety keeps your adrenaline sensitivity intact."),
                    ("Days 6–7 (Refeed)", "Eat at maintenance. Enjoy a wider variety of foods. "
                     "Chameleons need this mental reset to stay on track."),
                ]
            },
            {
                "label": "Week 2 — Switch to Training-Based Nutrition",
                "days": [
                    ("Training Days (3–4 days)", "Higher calories: maintenance minus 200 kcal. "
                     "More carbs around training. Higher energy for performance."),
                    ("Rest Days (3–4 days)", "Lower calories: maintenance minus 500 kcal. "
                     "Lower carbs, higher protein and fat. Let the body burn stored fat."),
                ]
            }
        ],
        "tips": [
            "Variety is your adherence tool. Change your meal plan every 2–3 weeks.",
            "Carb cycling works exceptionally well for Chameleons.",
            "Don't go too extreme with deficits — moderate and consistent beats aggressive and unsustainable.",
            "L-Tyrosine supports your adrenaline production — key for your type's energy and motivation.",
            "Supplement tip: L-Tyrosine + Rhodiola Rosea supports adrenaline sensitivity for Chameleons.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("chameleon", "energy"): {
        "headline": "Your 2-Week Energy Reset — Chameleon Style",
        "intro": (
            "Chameleons lose energy when they're stuck in repetitive routines or under chronic stress. "
            "Your adrenaline sensitivity means stress hits you harder than other types. "
            "This plan resets your energy system."
        ),
        "weeks": [
            {
                "label": "Week 1 — Reduce Stress Load",
                "days": [
                    ("Days 1–4", "Identify your top 3 energy drains (people, tasks, situations). "
                     "Reduce exposure where possible. Add post-workout carbs to shut down cortisol "
                     "after training — this is critical for Chameleons."),
                    ("Days 5–7", "Add Rhodiola Rosea (200–400mg in the morning) — an adaptogen "
                     "that supports adrenaline sensitivity without overstimulating. "
                     "Prioritize 7–8 hours of sleep."),
                ]
            },
            {
                "label": "Week 2 — Rebuild Adrenaline Sensitivity",
                "days": [
                    ("Days 8–11", "Introduce variety into your daily routine — new training style, "
                     "new social environment, new project. Chameleons recharge through novelty and connection."),
                    ("Days 12–14", "Assess energy. If improved, maintain the adaptogen + sleep protocol. "
                     "Add L-Tyrosine (500mg morning) to support dopamine → adrenaline production."),
                ]
            }
        ],
        "tips": [
            "Chronic stress depletes your adrenaline sensitivity — your most important energy mechanism.",
            "Post-workout carbs are not optional for you — they reset cortisol and restore energy.",
            "Social connection recharges Chameleons. Isolation drains you.",
            "Avoid prolonged aggressive dieting — it spikes cortisol and crashes your energy.",
            "Supplement tip: Rhodiola Rosea + L-Tyrosine is the Chameleon's energy stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("chameleon", "training"): {
        "headline": "Your 2-Week Training Consistency Plan — Chameleon Style",
        "intro": (
            "Chameleons are great at starting training programs — and terrible at finishing them. "
            "Not because of laziness, but because repetition kills your motivation. "
            "This plan is built to keep you coming back."
        ),
        "weeks": [
            {
                "label": "Week 1 — Variety is the Plan",
                "days": [
                    ("Days 1–4", "Train 4 days with completely different styles: "
                     "Day 1: strength. Day 2: HIIT or circuit. Day 3: skill or sport. Day 4: bodyweight. "
                     "Chameleons thrive when no two sessions feel the same."),
                    ("Days 5–7", "Active recovery. Join a group class, play a sport, or try something new. "
                     "Social training environments are highly motivating for your type."),
                ]
            },
            {
                "label": "Week 2 — Add a Deadline",
                "days": [
                    ("Days 8–12", "Set a mini-challenge for the end of the week: "
                     "a specific weight to lift, a time to beat, a skill to demonstrate. "
                     "Chameleons perform best when there's a deadline."),
                    ("Days 13–14", "Complete the challenge. Celebrate. "
                     "Then immediately set the next one — momentum is everything for your type."),
                ]
            }
        ],
        "tips": [
            "Never follow the same program for more than 4 weeks — switch it up.",
            "Group training and team sports are ideal for Chameleons.",
            "Deadlines and mini-challenges replace the motivation that routine kills.",
            "Short rest periods and high density work well for your adrenaline sensitivity.",
            "Supplement tip: Pre-workout with L-Tyrosine + caffeine works well for Chameleons on training days.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("chameleon", "sleep"): {
        "headline": "Your 2-Week Sleep Optimization Plan — Chameleon Style",
        "intro": (
            "Chameleons often struggle with sleep when stress is high or when they've been "
            "people-pleasing all day. Your nervous system needs a proper reset. "
            "Here's how to make it happen."
        ),
        "weeks": [
            {
                "label": "Week 1 — Stress Shutdown Protocol",
                "days": [
                    ("Days 1–4", "Create a hard boundary: no work, no social media, no problem-solving "
                     "after 9pm. Chameleons absorb stress from others — you need to consciously disconnect. "
                     "Add a 10-minute journaling session to process the day."),
                    ("Days 5–7", "Add Magnesium Glycinate (300mg) + L-Theanine (200mg) before bed. "
                     "This combination calms the adrenaline-driven nervous system without sedation."),
                ]
            },
            {
                "label": "Week 2 — Consistency",
                "days": [
                    ("Days 8–11", "Same bedtime every night. Chameleons adapt to routines quickly "
                     "once they see the benefit. Track your mood and energy the next morning."),
                    ("Days 12–14", "Assess: are you waking up more refreshed and less reactive? "
                     "If yes, lock in the protocol. If not, reduce evening social stimulation further."),
                ]
            }
        ],
        "tips": [
            "You absorb other people's stress. Limit high-drama interactions in the evening.",
            "Post-workout carbs (even a small amount before bed) help shut down cortisol for Chameleons.",
            "Consistent sleep timing is more important than sleep duration for your type.",
            "Avoid stimulating conversations or debates in the last hour before bed.",
            "Supplement tip: Magnesium Glycinate + Ashwagandha is ideal for Chameleons under stress.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    # ─── WOLF (2B) ────────────────────────────────────────────────────────────
    ("wolf", "weight"): {
        "headline": "Your 2-Week Fat Loss Plan — Wolf Style",
        "intro": (
            "As a Wolf (Natural Signature Type), you're emotionally driven and highly sensitive. "
            "Aggressive diets spike your cortisol, trigger emotional eating, and backfire. "
            "This plan takes a steady, sustainable approach that works with your nature, not against it."
        ),
        "weeks": [
            {
                "label": "Week 1 — Steady and Supportive",
                "days": [
                    ("Days 1–5", "Moderate calorie deficit: 300–400 kcal below maintenance. "
                     "Focus on whole foods, high protein, and carbs timed around training and before bed. "
                     "The pre-bed carbs are important — they support serotonin and help you sleep."),
                    ("Days 6–7", "Maintenance calories. Cook a meal you genuinely enjoy. "
                     "Wolves need to feel good about their food — restriction without pleasure leads to bingeing."),
                ]
            },
            {
                "label": "Week 2 — Build Momentum",
                "days": [
                    ("Days 8–12", "Continue the moderate deficit. Add taurine-rich foods "
                     "(fish, shellfish, meat) to support GABA — your calming neurotransmitter. "
                     "Avoid processed foods and refined sugar — they increase glutamate and anxiety."),
                    ("Days 13–14", "Maintenance. Reflect on the 2 weeks. "
                     "Wolves are motivated by emotional wins — acknowledge your progress, "
                     "no matter how small."),
                ]
            }
        ],
        "tips": [
            "Never use an aggressive deficit — high cortisol is your biggest fat loss enemy.",
            "Emotional eating is real for Wolves. Identify your triggers and have a non-food response ready.",
            "Carbs before bed support serotonin and improve sleep — do not cut them out.",
            "One slip-up is not failure. Wolves are prone to all-or-nothing thinking — fight it.",
            "Supplement tip: Taurine + Magnesium Glycinate supports GABA and reduces cortisol for Wolves.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("wolf", "energy"): {
        "headline": "Your 2-Week Energy Reset — Wolf Style",
        "intro": (
            "Wolves lose energy when they feel emotionally drained, unappreciated, or overwhelmed. "
            "Your energy is deeply connected to your emotional state. "
            "This plan addresses both the physical and emotional roots of your fatigue."
        ),
        "weeks": [
            {
                "label": "Week 1 — Calm the System",
                "days": [
                    ("Days 1–4", "Reduce training intensity by 20–30%. Add gentle movement: "
                     "walking, yoga, or swimming. Wolves recover through low-intensity, "
                     "emotionally positive activities. "
                     "Prioritize sleep: 8 hours minimum. Add carbs before bed to support serotonin."),
                    ("Days 5–7", "Add Magnesium Glycinate (300mg) + Ashwagandha (300–600mg) daily. "
                     "These reduce cortisol and support GABA — your key calming neurotransmitter."),
                ]
            },
            {
                "label": "Week 2 — Rebuild from the Inside",
                "days": [
                    ("Days 8–11", "Return to regular training but keep volume moderate. "
                     "Focus on movements that feel good — bodybuilding-style training with "
                     "mind-muscle connection is ideal for Wolves."),
                    ("Days 12–14", "Assess emotional and physical energy. "
                     "If improved, maintain the supplement and sleep protocol. "
                     "Consider adding a mindfulness or meditation practice — 5 minutes daily is enough."),
                ]
            }
        ],
        "tips": [
            "Your energy is emotional first, physical second. Address the emotional drain.",
            "Avoid high-cortisol situations: overtraining, under-eating, toxic relationships.",
            "Mind-muscle connection training (bodybuilding style) is energizing for Wolves.",
            "Serotonin support through carb timing and tryptophan-rich foods (turkey, eggs, dairy) is key.",
            "Supplement tip: Ashwagandha + Magnesium Glycinate + 5-HTP (low dose) is the Wolf's energy stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("wolf", "training"): {
        "headline": "Your 2-Week Training Consistency Plan — Wolf Style",
        "intro": (
            "Wolves don't lack discipline — they lose motivation when training feels punishing "
            "or when they don't feel the results. You need to FEEL your training working. "
            "This plan is built around that."
        ),
        "weeks": [
            {
                "label": "Week 1 — Train to Feel",
                "days": [
                    ("Days 1–4", "Train 3–4 days. Focus on bodybuilding-style training: "
                     "moderate weight, higher reps (10–15), slow tempo, mind-muscle connection. "
                     "The pump and the burn are your motivation — lean into them."),
                    ("Days 5–7", "Rest or gentle movement. Wolves need emotional recovery too — "
                     "do something that makes you feel good about yourself outside the gym."),
                ]
            },
            {
                "label": "Week 2 — Build the Habit",
                "days": [
                    ("Days 8–12", "4 training days. Add one exercise you genuinely enjoy each session. "
                     "Wolves are motivated by positive emotional associations with training."),
                    ("Days 13–14", "Two sessions. End the week with a workout that makes you feel strong. "
                     "Write down 3 things you're proud of from this week."),
                ]
            }
        ],
        "tips": [
            "A bad workout can ruin your week — keep intensity manageable and focus on feel.",
            "Train with a supportive partner or in a positive environment.",
            "Mind-muscle connection and the pump are your performance metrics — not just weight on the bar.",
            "Avoid neurological overload (heavy, explosive work) — it depletes you faster than other types.",
            "Supplement tip: L-Glutamine + Magnesium supports recovery and GABA for Wolves.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("wolf", "sleep"): {
        "headline": "Your 2-Week Sleep Optimization Plan — Wolf Style",
        "intro": (
            "Wolves are the most prone to sleep disruption from emotional stress. "
            "A difficult conversation, a negative experience, or unresolved anxiety "
            "will keep you awake for hours. This plan addresses the root causes."
        ),
        "weeks": [
            {
                "label": "Week 1 — Emotional Shutdown Protocol",
                "days": [
                    ("Days 1–4", "Create a 'worry window': 15 minutes before 8pm where you write down "
                     "everything that's bothering you. After that, no more rumination — it's been processed. "
                     "Add carbs before bed (small amount: rice, oats, banana) to boost serotonin."),
                    ("Days 5–7", "Add 5-HTP (50–100mg) 30 minutes before bed — this directly supports "
                     "serotonin production and helps Wolves fall asleep faster. "
                     "Add Magnesium Glycinate (300mg) for deeper sleep."),
                ]
            },
            {
                "label": "Week 2 — Deepen the Rest",
                "days": [
                    ("Days 8–11", "Maintain the protocol. Add a 5-minute gratitude practice before bed — "
                     "this shifts the emotional state from anxiety to calm. Wolves respond powerfully to this."),
                    ("Days 12–14", "Assess: are you falling asleep faster and waking less? "
                     "Most Wolves see significant improvement with this stack within 10 days."),
                ]
            }
        ],
        "tips": [
            "Unresolved emotional stress is your #1 sleep enemy. Process it before bed.",
            "Serotonin support (carbs before bed, 5-HTP) is the most effective tool for Wolf sleep.",
            "Avoid confrontational or emotionally charged content in the evening.",
            "A consistent bedtime routine gives Wolves the emotional security they need to relax.",
            "Supplement tip: 5-HTP + Magnesium Glycinate + L-Theanine is the Wolf's sleep stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    # ─── OWL (3) ──────────────────────────────────────────────────────────────
    ("owl", "weight"): {
        "headline": "Your 2-Week Fat Loss Plan — Owl Style",
        "intro": (
            "As an Owl (Natural Signature Type), you are the best at following a plan. "
            "You don't need motivation tricks — you need a clear, structured protocol "
            "with all the information upfront. Here it is."
        ),
        "weeks": [
            {
                "label": "Week 1 — Steady Deficit",
                "days": [
                    ("Days 1–7", "Consistent calorie deficit of 300–400 kcal daily. "
                     "High carb, low fat approach — Owls are the highest cortisol producers "
                     "and carbs are your cortisol management tool. "
                     "Protein: 1.8–2g per kg bodyweight. "
                     "Meal timing: consistent — same times every day."),
                ]
            },
            {
                "label": "Week 2 — Maintain and Measure",
                "days": [
                    ("Days 8–14", "Same protocol. Track everything: weight, energy, sleep quality. "
                     "Owls are data-driven — the numbers will keep you motivated. "
                     "Add taurine-rich foods (fish, shellfish) to support GABA and reduce cortisol."),
                ]
            }
        ],
        "tips": [
            "Consistency over 12 weeks beats any aggressive 2-week approach for your type.",
            "High carb, low fat is your optimal macronutrient split — don't let keto trends mislead you.",
            "Cortisol is your biggest fat loss enemy. Manage it with carbs, sleep, and stress reduction.",
            "Never change the plan mid-week — Owls perform best with predictability.",
            "Supplement tip: Ashwagandha + 5-HTP supports serotonin and cortisol control for Owls.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("owl", "energy"): {
        "headline": "Your 2-Week Energy Reset — Owl Style",
        "intro": (
            "Owls lose energy when their routine is disrupted, when cortisol is chronically high, "
            "or when serotonin is low. You need structure, predictability, and calm. "
            "This plan restores all three."
        ),
        "weeks": [
            {
                "label": "Week 1 — Stabilize the System",
                "days": [
                    ("Days 1–4", "Lock in a consistent daily schedule: wake time, meal times, "
                     "training time, sleep time — all fixed. Owls recharge through predictability. "
                     "Add high-carb meals (with protein) to support serotonin and reduce cortisol."),
                    ("Days 5–7", "Add Ashwagandha (300–600mg daily) — the most effective adaptogen "
                     "for Owls. It reduces cortisol and supports the inhibitory neurotransmitter balance "
                     "your type needs."),
                ]
            },
            {
                "label": "Week 2 — Protect the Routine",
                "days": [
                    ("Days 8–11", "Maintain the schedule. Add a 5-minute mindfulness or breathing "
                     "practice in the morning — this activates the parasympathetic nervous system "
                     "and reduces the cortisol spike that Owls experience upon waking."),
                    ("Days 12–14", "Assess energy. Owls typically see clear improvement within "
                     "10–14 days of consistent routine and cortisol management."),
                ]
            }
        ],
        "tips": [
            "Disrupted routine is your biggest energy drain. Protect your schedule fiercely.",
            "High-carb meals support serotonin — your most important neurotransmitter.",
            "Avoid overtraining — Owls produce the most cortisol and recover the slowest.",
            "Mindfulness and breathing exercises are not optional for Owls — they are medicine.",
            "Supplement tip: Ashwagandha + Magnesium Glycinate + 5-HTP is the Owl's energy stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("owl", "training"): {
        "headline": "Your 2-Week Training Consistency Plan — Owl Style",
        "intro": (
            "Owls are already consistent — but they often overtrain or choose the wrong type of training. "
            "You don't need intensity. You need structure, repetition, and technical mastery."
        ),
        "weeks": [
            {
                "label": "Week 1 — Structure First",
                "days": [
                    ("Days 1–4", "Train 3–4 days with a fixed, written program. "
                     "Owls perform best with repetition — use the same exercises for 4–6 weeks. "
                     "Focus on technique perfection. Moderate intensity (70–80% of max). "
                     "Long rest periods (2–3 minutes) — Owls have high adrenaline and need full recovery."),
                    ("Days 5–7", "Rest. Owls are the highest cortisol producers — "
                     "rest days are not optional. Use them for mobility, walking, or reading."),
                ]
            },
            {
                "label": "Week 2 — Refine and Progress",
                "days": [
                    ("Days 8–12", "Same program. Add a small progression: +2.5kg or +1 rep per set. "
                     "Owls build confidence through measurable, incremental progress."),
                    ("Days 13–14", "Rest. Plan the next 2 weeks in writing — "
                     "Owls are energized by having a clear plan ahead."),
                ]
            }
        ],
        "tips": [
            "Do NOT change your program every week — repetition is your strength.",
            "Avoid explosive or high-neurological work — it depletes your already-stressed nervous system.",
            "Endurance sports (running, cycling) are ideal for Owls — steady, structured, measurable.",
            "Write your program down. Owls need to see the plan to trust it.",
            "Supplement tip: Magnesium Glycinate + Ashwagandha supports recovery and cortisol control for Owls.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },

    ("owl", "sleep"): {
        "headline": "Your 2-Week Sleep Optimization Plan — Owl Style",
        "intro": (
            "Owls are chronic overthinkers. When the lights go off, the analysis begins. "
            "Your low serotonin and high cortisol make sleep difficult — but very fixable "
            "with the right protocol."
        ),
        "weeks": [
            {
                "label": "Week 1 — Shut Down the Analytical Mind",
                "days": [
                    ("Days 1–4", "Create a written evening routine (Owls love written protocols). "
                     "9pm: stop all work. 9:15pm: write tomorrow's plan in detail — "
                     "this gives your brain permission to stop planning. "
                     "9:30pm: dim lights, no screens. 10pm: bed."),
                    ("Days 5–7", "Add 5-HTP (50–100mg) + Magnesium Glycinate (300mg) 30 min before bed. "
                     "This directly addresses your low serotonin and calms the nervous system."),
                ]
            },
            {
                "label": "Week 2 — Reinforce the System",
                "days": [
                    ("Days 8–11", "Add a small carb snack before bed (rice cake, banana, oats) — "
                     "this boosts serotonin and helps Owls fall asleep faster. "
                     "Keep the written routine exactly as planned."),
                    ("Days 12–14", "Assess: most Owls see dramatic improvement within 10 days "
                     "with this protocol. If not, reduce caffeine to morning only."),
                ]
            }
        ],
        "tips": [
            "Your brain needs explicit permission to stop working. The written plan provides that.",
            "5-HTP is the most effective supplement for Owl sleep — it directly supports serotonin.",
            "Carbs before bed are beneficial for Owls — they support serotonin and reduce cortisol.",
            "Keep your bedroom environment identical every night — Owls sleep best with predictability.",
            "Supplement tip: 5-HTP + Magnesium Glycinate + Ashwagandha is the Owl's sleep stack.",
        ],
        "cta": (
            "You've just taken the first step. Now it's time to actually change something. "
            "The Core Path is a 30-day program built around your Natural Signature Type — "
            "every day takes less than 60 seconds: one check-in, 4-5 questions, your way. "
            "Complete 6 out of 7 check-ins per week for 30 days and you get your money back. "
            "Every cent. Plus an exclusive upgrade offer. That's not a trial — that's a "
            "guarantee that only works if you show up."
        )
    },
}

# Type metadata
TYPE_META = {
    "lion": {
        "name": "The Lion",
        "nst": "Natural Signature Type — The Lion",
        "emoji": "🦁",
        "color": "#f59e0b",
        "image": "lion.png",
        "tagline": "Dominant. Driven. Built to win.",
        "description": (
            "You are dopamine-dominant, highly competitive, and goal-oriented. "
            "You thrive on challenges, need to see results fast, and perform best "
            "under pressure. You are a natural leader who doesn't back down."
        ),
        "strengths": ["Extremely competitive", "High resilience to stress", "Fast results-oriented", "Natural leader"],
        "challenges": ["Impatience", "Dopamine depletion risk", "Difficulty with authority", "Impulsiveness"],
    },
    "falcon": {
        "name": "The Falcon",
        "nst": "Natural Signature Type — The Falcon",
        "emoji": "🦅",
        "color": "#3b82f6",
        "image": "falcon.png",
        "tagline": "Creative. Explosive. Always evolving.",
        "description": (
            "You are the most naturally athletic type — quick to learn, creative, "
            "and driven by novelty. You thrive on variety and new challenges. "
            "When things get repetitive, you lose interest fast."
        ),
        "strengths": ["Fastest learner", "Highly creative", "Naturally athletic", "Performs under pressure"],
        "challenges": ["Boredom with routine", "Acetylcholine depletion", "Starts many things, finishes fewer", "Impulsiveness"],
    },
    "chameleon": {
        "name": "The Chameleon",
        "nst": "Natural Signature Type — The Chameleon",
        "emoji": "🦎",
        "color": "#10b981",
        "image": "chameleon.png",
        "tagline": "Adaptable. Social. Driven by connection.",
        "description": (
            "You are the most socially adaptable type — you read people effortlessly "
            "and adjust your behavior to any situation. You need variety, connection, "
            "and the feeling of being liked and respected."
        ),
        "strengths": ["Highly adaptable", "Great at reading people", "Works well in teams", "Responds to almost any approach"],
        "challenges": ["Indecisiveness", "People-pleasing", "Adrenaline sensitivity", "Procrastination"],
    },
    "wolf": {
        "name": "The Wolf",
        "nst": "Natural Signature Type — The Wolf",
        "emoji": "🐺",
        "color": "#8b5cf6",
        "image": "wolf.png",
        "tagline": "Empathetic. Deep. Emotionally powerful.",
        "description": (
            "You feel everything deeply — both the highs and the lows. "
            "You are the most empathetic type, highly intuitive, and motivated "
            "by emotional connection and the feeling of progress."
        ),
        "strengths": ["Highest empathy", "Great listener", "Deeply motivated when emotionally connected", "Consistent when feeling good"],
        "challenges": ["Emotional eating risk", "Cortisol sensitivity", "Takes criticism personally", "All-or-nothing thinking"],
    },
    "owl": {
        "name": "The Owl",
        "nst": "Natural Signature Type — The Owl",
        "emoji": "🦉",
        "color": "#6366f1",
        "image": "owl.png",
        "tagline": "Structured. Precise. Built for the long game.",
        "description": (
            "You are the most disciplined and analytical type. You love structure, "
            "follow plans better than anyone, and make decisions based on data and logic. "
            "Sudden changes stress you out — but with the right plan, you are unstoppable."
        ),
        "strengths": ["Best at following a plan", "Detail-oriented", "Patient", "Excellent long-term consistency"],
        "challenges": ["Highest cortisol producer", "Overthinking", "Stress from change", "Low serotonin"],
    },
}

PROBLEM_LABELS = {
    "weight": "I want to lose weight / can't lose fat",
    "energy": "I'm constantly exhausted / have no energy",
    "training": "I don't train consistently",
    "sleep": "I sleep poorly",
}

ADJECTIVES = {
    "lion": ["Dominant", "Risk-taking", "Goal-driven", "Direct", "Extroverted"],
    "falcon": ["Creative", "Spontaneous", "Full of ideas", "Impulsive", "Extroverted"],
    "chameleon": ["Adaptable", "Open", "Versatile", "Socially flexible", "Harmony-seeking"],
    "wolf": ["Sensitive", "Empathetic", "Vulnerable", "Deep", "Introverted"],
    "owl": ["Structured", "Routine-oriented", "Precise", "Plan-driven", "Introverted"],
}
