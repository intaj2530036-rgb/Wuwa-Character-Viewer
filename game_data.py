"""
game_data.py
-------------
Character data for the Multi-Game Viewer.

Structure:
character_data = {
    "<Game Name>": {
        "<Character Name>": {
            "element": str,
            "weapon": str,
            "role": str,
            "image": str,   # URL, "local:filename.jpg", or "" for none
            "description": str
        },
        ...
    },
    ...
}

Image Sources:
- Wuthering Waves: wuthering.wiki official rolecard images
- Genshin Impact: genshin.jmp.blue API character card artwork
- Arknights: arkwaifu.cc official game artwork
"""

character_data = {
    "Wuthering Waves": {
        "Rover": {
            "element": "Spectro",
            "weapon": "Sword",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1502.png",
            "description": ""
        },
        "Aemeath": {
            "element": "Fusion",
            "weapon": "Sword",
            "role": "DPS",
            "image": "local:Aemeath_Full_Sprite.jpg",
            "description": "Nope. As long as it's food, me likey. Though... I don't really need to eat anymore, haha."
        },
        "Carlotta": {
            "element": "Glacio",
            "weapon": "Pistol",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1107.png",
            "description": "Desuwaaaaaa-"
        },
        "Changli": {
            "element": "Fusion",
            "weapon": "Sword",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1205.png",
            "description": ""
        },
        "Brant": {
            "element": "Havoc",
            "weapon": "Sword",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1206.png",
            "description": ""
        },
        "Lupa": {
            "element": "Fusion",
            "weapon": "Broadblade",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1207.png",
            "description": "You're gonna keep me from fighting? HAH !! CAREFUL NOW"
        },
        "Augusta": {
            "element": "Electro",
            "weapon": "Broadblade",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1306.png",
            "description": ""
        },
        "Iuno": {
            "element": "Aero",
            "weapon": "Gauntlet",
            "role": "Sub-DPS, Healer",
            "image": "https://wuthering.wiki/img/rolecard_1410.png",
            "description": ""
        },
        "Shorekeeper": {
            "element": "Spectro",
            "weapon": "Rectifier",
            "role": "Support, Healer",
            "image": "https://wuthering.wiki/img/rolecard_1505.png",
            "description": ""
        },
        "Zani": {
            "element": "Spectro",
            "weapon": "Gauntlet",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1507.png",
            "description": "I want a vacation"
        },
        "Jiyan": {
            "element": "Aero",
            "weapon": "Broadblade",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1404.png",
            "description": ""
        },
        "Yinlin": {
            "element": "Electro",
            "weapon": "Rectifier",
            "role": "Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1302.png",
            "description": ""
        },
        "Jinhsi": {
            "element": "Spectro",
            "weapon": "Broadblade",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1304.png",
            "description": ""
        },
        "Encore": {
            "element": "Fusion",
            "weapon": "Rectifier",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1203.png",
            "description": ""
        },
        "Verina": {
            "element": "Spectro",
            "weapon": "Rectifier",
            "role": "Support, Healer",
            "image": "https://wuthering.wiki/img/rolecard_1503.png",
            "description": ""
        },
        "Calcharo": {
            "element": "Electro",
            "weapon": "Broadblade",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1301.png",
            "description": ""
        },
        "Lingyang": {
            "element": "Glacio",
            "weapon": "Gauntlet",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1104.png",
            "description": ""
        },
        "Jianxin": {
            "element": "Aero",
            "weapon": "Gauntlet",
            "role": "Support, Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1405.png",
            "description": ""
        },
        "Mortefi": {
            "element": "Fusion",
            "weapon": "Pistol",
            "role": "Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1204.png",
            "description": ""
        },
        "Sanhua": {
            "element": "Glacio",
            "weapon": "Sword",
            "role": "Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1102.png",
            "description": ""
        },
        "Baizhi": {
            "element": "Glacio",
            "weapon": "Rectifier",
            "role": "Support, Healer",
            "image": "https://wuthering.wiki/img/rolecard_1103.png",
            "description": ""
        },
        "Yangyang": {
            "element": "Aero",
            "weapon": "Sword",
            "role": "Sub-DPS, Support",
            "image": "https://wuthering.wiki/img/rolecard_1402.png",
            "description": ""
        },
        "Chixia": {
            "element": "Fusion",
            "weapon": "Pistol",
            "role": "Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1202.png",
            "description": ""
        },
        "Danjin": {
            "element": "Havoc",
            "weapon": "Sword",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1602.png",
            "description": ""
        },
        "Taoqi": {
            "element": "Havoc",
            "weapon": "Broadblade",
            "role": "Sub-DPS, Support",
            "image": "https://wuthering.wiki/img/rolecard_1601.png",
            "description": ""
        },
        "Yuanwu": {
            "element": "Electro",
            "weapon": "Gauntlet",
            "role": "Sub-DPS, Support",
            "image": "https://wuthering.wiki/img/rolecard_1303.png",
            "description": ""
        },
        "Aalto": {
            "element": "Aero",
            "weapon": "Pistol",
            "role": "Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1403.png",
            "description": ""
        },
        "Youhu": {
            "element": "Glacio",
            "weapon": "Gauntlet",
            "role": "Sub-DPS, Support",
            "image": "https://wuthering.wiki/img/rolecard_1106.png",
            "description": ""
        },
        "Xiangli Yao": {
            "element": "Electro",
            "weapon": "Gauntlet",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1305.png",
            "description": ""
        },
        "Camellya": {
            "element": "Havoc",
            "weapon": "Sword",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1603.png",
            "description": ""
        },
        "Phoebe": {
            "element": "Spectro",
            "weapon": "Rectifier",
            "role": "DPS",
            "image": "https://wuthering.wiki/img/rolecard_1506.png",
            "description": "The fish are over there...wow fish..."
        },
        "Roccia": {
            "element": "Havoc",
            "weapon": "Gauntlet",
            "role": "Sub-DPS",
            "image": "https://wuthering.wiki/img/rolecard_1604.png",
            "description": ""
        },
        "Male Rover": {
            "element": "Spectro",
            "weapon": "Sword",
            "role": "Sub-DPS, Support",
            "image": "https://wuthering.wiki/img/rolecard_1605.png",
            "description": "You Will Obey!!!"
        },
        "Jueyuan": {
            "element": "Spectro",
            "weapon": "Rectifier",
            "role": "Support, Healer",
            "image": "https://wuthering.wiki/img/rolecard_1503.png",
            "description": ""
        }
    },

    "Genshin Impact": {
        "Hu Tao": {
            "element": "Pyro",
            "weapon": "Polearm",
            "role": "DPS",
            "image": "",
            "description": "Life and death, in the end, are merely different sides of the same coin."
        },
        "Zhongli": {
            "element": "Geo",
            "weapon": "Polearm",
            "role": "Support",
            "image": "",
            "description": "I am merely a guest in this era."
        },
        "Raiden Shogun": {
            "element": "Electro",
            "weapon": "Polearm",
            "role": "DPS",
            "image": "",
            "description": "The Shogun's resolve is as unwavering as ever."
        },
        "Nahida": {
            "element": "Dendro",
            "weapon": "Catalyst",
            "role": "Sub-DPS, Support",
            "image": "",
            "description": "Knowledge is like a garden, if it is not cultivated, it cannot be harvested."
        },
        "Diluc": {
            "element": "Pyro",
            "weapon": "Claymore",
            "role": "DPS",
            "image": "",
            "description": "Runs the Dawn Winery by day, hunts the night's troublemakers without a second thought."
        },
        "Klee": {
            "element": "Pyro",
            "weapon": "Catalyst",
            "role": "DPS",
            "image": "",
            "description": "Sweet, curious, and just a little too fond of explosives for anyone's comfort."
        },
        "Bennett": {
            "element": "Pyro",
            "weapon": "Sword",
            "role": "Support, Healer",
            "image": "",
            "description": "Eternally unlucky, endlessly optimistic, and somehow always the one keeping the team alive."
        },
        "Xiangling": {
            "element": "Pyro",
            "weapon": "Polearm",
            "role": "Sub-DPS",
            "image": "",
            "description": "A chef first and a fighter second, though her cooking might be the more dangerous of the two."
        },
        "Yoimiya": {
            "element": "Pyro",
            "weapon": "Bow",
            "role": "DPS",
            "image": "",
            "description": "Lights up Inazuma's skies with fireworks by night and arrows by day."
        },
        "Ganyu": {
            "element": "Cryo",
            "weapon": "Bow",
            "role": "DPS",
            "image": "",
            "description": "Half-qilin, overworked, and the most reliable secretary the Liyue Qixing could ask for."
        },
        "Ayaka": {
            "element": "Cryo",
            "weapon": "Sword",
            "role": "DPS",
            "image": "",
            "description": "Graceful as falling snow, sharp as the blade she carries."
        },
        "Eula": {
            "element": "Cryo",
            "weapon": "Claymore",
            "role": "DPS",
            "image": "",
            "description": "A noblewoman with a grudge and a greatsword, in roughly that order of priority."
        },
        "Shenhe": {
            "element": "Cryo",
            "weapon": "Polearm",
            "role": "Support",
            "image": "",
            "description": "Raised among exorcists, still learning what it means to live among people."
        },
        "Qiqi": {
            "element": "Cryo",
            "weapon": "Sword",
            "role": "Healer",
            "image": "",
            "description": "A zombie who forgets things easily, but never forgets to help those in need."
        },
        "Venti": {
            "element": "Anemo",
            "weapon": "Bow",
            "role": "Support",
            "image": "",
            "description": "A wandering bard with a love for wine, music, and quietly nudging fate along."
        },
        "Xiao": {
            "element": "Anemo",
            "weapon": "Polearm",
            "role": "DPS",
            "image": "",
            "description": "Carries the weight of countless karmic debts so others don't have to."
        },
        "Kazuha": {
            "element": "Anemo",
            "weapon": "Sword",
            "role": "Support",
            "image": "",
            "description": "A wandering swordsman who reads the wind better than most read words."
        },
        "Sucrose": {
            "element": "Anemo",
            "weapon": "Catalyst",
            "role": "Support",
            "image": "",
            "description": "An alchemist obsessed with slimes, forever trying to make the world a little better through science."
        },
        "Albedo": {
            "element": "Geo",
            "weapon": "Sword",
            "role": "Sub-DPS",
            "image": "",
            "description": "Chief alchemist of Mondstadt, with a calm exterior hiding endless curiosity."
        },
        "Itto": {
            "element": "Geo",
            "weapon": "Claymore",
            "role": "DPS",
            "image": "",
            "description": "Self-proclaimed gang leader, surprisingly soft-hearted, perpetually broke."
        },
        "Ningguang": {
            "element": "Geo",
            "weapon": "Catalyst",
            "role": "Sub-DPS, Support",
            "image": "",
            "description": "Built an empire from nothing and never lets anyone forget it, gracefully."
        },
        "Tartaglia": {
            "element": "Hydro",
            "weapon": "Bow",
            "role": "DPS",
            "image": "",
            "description": "A Fatui Harbinger who treats every fight like the best day of his life."
        },
        "Kokomi": {
            "element": "Hydro",
            "weapon": "Catalyst",
            "role": "Healer, Support",
            "image": "",
            "description": "A reluctant military leader who'd rather be home in bed than commanding a war."
        },
        "Xingqiu": {
            "element": "Hydro",
            "weapon": "Sword",
            "role": "Sub-DPS, Support",
            "image": "",
            "description": "A wealthy merchant's son who'd rather read wuxia novels than count coins."
        },
        "Furina": {
            "element": "Hydro",
            "weapon": "Sword",
            "role": "DPS, Support",
            "image": "",
            "description": "Former Hydro Archon turned theater star, dramatic in absolutely everything she does."
        },
        "Mona": {
            "element": "Hydro",
            "weapon": "Catalyst",
            "role": "Sub-DPS",
            "image": "",
            "description": "A proud astrologist who's terrible with money but excellent at reading the stars."
        },
        "Yae Miko": {
            "element": "Electro",
            "weapon": "Catalyst",
            "role": "DPS",
            "image": "",
            "description": "Shrine maiden, publisher, and fox spirit who enjoys teasing mortals just a little too much."
        },
        "Fischl": {
            "element": "Electro",
            "weapon": "Bow",
            "role": "Sub-DPS",
            "image": "",
            "description": "Self-styled Prinzessin der Verurteilung, complete with a raven who does most of the talking."
        },
        "Keqing": {
            "element": "Electro",
            "weapon": "Sword",
            "role": "DPS",
            "image": "",
            "description": "A pragmatist who doesn't believe in gods, even while living in a city full of them."
        },
        "Tighnari": {
            "element": "Dendro",
            "weapon": "Bow",
            "role": "DPS",
            "image": "",
            "description": "A forest ranger with sharp ears, sharper aim, and zero patience for nonsense."
        }
    },

    "Arknights": {
        "Amiya": {
            "element": "Caster",
            "weapon": "Caster",
            "role": "Sub-DPS, Support",
            "image": "",
            "description": "I'll do my best, for everyone's sake."
        },
        "SilverAsh": {
            "element": "Artsfist",
            "weapon": "Guard",
            "role": "DPS",
            "image": "",
            "description": "Watch closely, this is how it's done."
        },
        "Texas": {
            "element": "Stalker",
            "weapon": "Sniper",
            "role": "Sub-DPS",
            "image": "",
            "description": "..."
        },
        "Eyjafjalla": {
            "element": "Phalanx Caster",
            "weapon": "Caster",
            "role": "DPS",
            "image": "",
            "description": "The flames of war... they never truly go out."
        },
        "Exusiai": {
            "element": "Bombarrow",
            "weapon": "Sniper",
            "role": "DPS",
            "image": "",
            "description": "A grenade-launching nun with a smile that's somehow more unsettling than the explosions."
        },
        "Saria": {
            "element": "Protector",
            "weapon": "Defender",
            "role": "Support, Healer",
            "image": "",
            "description": "Gentle, steady, and able to shield an entire team without breaking a sweat."
        },
        "Hoshiguma": {
            "element": "Guardian",
            "weapon": "Defender",
            "role": "Tank, Defense",
            "image": "",
            "description": "An oni who'd rather stand between her squad and danger than anywhere else."
        },
        "Ifrit": {
            "element": "Splash Caster",
            "weapon": "Caster",
            "role": "DPS",
            "image": "",
            "description": "Quiet, intense, and capable of turning a battlefield into an inferno."
        },
        "Skadi": {
            "element": "Lord",
            "weapon": "Guard",
            "role": "DPS",
            "image": "",
            "description": "A deep-sea hunter who treats every fight as a hunt, and rarely loses."
        },
        "Ch'en": {
            "element": "Swordmaster",
            "weapon": "Guard",
            "role": "DPS",
            "image": "",
            "description": "An incorruptible enforcer with a blade fast enough to end most fights in seconds."
        },
        "Mudrock": {
            "element": "Artificer",
            "weapon": "Defender",
            "role": "Defense, Sub-DPS",
            "image": "",
            "description": "Slow to anger, nearly impossible to move once she's made up her mind."
        },
        "Suzuran": {
            "element": "Underground Aid",
            "weapon": "Supporter",
            "role": "Support",
            "image": "",
            "description": "A florist who's seen the worst of the underground and still chooses kindness."
        },
        "Lappland": {
            "element": "Reaper",
            "weapon": "Guard",
            "role": "Sub-DPS, Debuffer",
            "image": "",
            "description": "Chaotic, unpredictable, and having far too much fun in the middle of a fight."
        },
        "Ash": {
            "element": "Artilleryman",
            "weapon": "Sniper",
            "role": "DPS",
            "image": "",
            "description": "A reporter who's a little too good at finding, and causing, explosions."
        },
        "Kal'tsit": {
            "element": "Therapist",
            "weapon": "Medic",
            "role": "Healer, Support",
            "image": "",
            "description": "Ancient, calculating, and somehow always three steps ahead of everyone else."
        },
        "Shining": {
            "element": "Therapist",
            "weapon": "Medic",
            "role": "Healer",
            "image": "",
            "description": "A doctor whose bedside manner is as warm as her healing arts are precise."
        },
        "Mostima": {
            "element": "Mech-accord Caster",
            "weapon": "Caster",
            "role": "Support, DPS",
            "image": "",
            "description": "A fortune-teller who insists she's cursed, while quietly being one of the most reliable people around."
        },
        "Blaze": {
            "element": "Instructor",
            "weapon": "Guard",
            "role": "DPS",
            "image": "",
            "description": "A masked soldier of few words, defined entirely by what she does in battle."
        },
        "Mlynar": {
            "element": "Reaper",
            "weapon": "Guard",
            "role": "DPS",
            "image": "",
            "description": "A noble swordsman whose elegance on the battlefield matches his manners off it."
        },
        "Nearl the Radiant Knight": {
            "element": "Lord",
            "weapon": "Defender",
            "role": "Support",
            "image": "",
            "description": "A knight reborn from grief into resolve, leading from the front no matter the cost."
        },
        "Pallas": {
            "element": "Heavyshooter",
            "weapon": "Sniper",
            "role": "DPS",
            "image": "",
            "description": "Carries a rifle nearly as big as she is, and uses it like it weighs nothing."
        },
        "W": {
            "element": "Hookmaster",
            "weapon": "Specialist",
            "role": "Sub-DPS",
            "image": "",
            "description": "Unpredictable, dangerous, and impossible to read, exactly how she likes it."
        },
        "Schwarz": {
            "element": "Deadeye",
            "weapon": "Sniper",
            "role": "DPS",
            "image": "",
            "description": "A marksman of few words who lets a single shot speak for him."
        },
        "Thorns": {
            "element": "Artilleryman",
            "weapon": "Guard",
            "role": "DPS",
            "image": "",
            "description": "Heavy ordnance on legs, built for one purpose: overwhelming firepower."
        }
    }
}
