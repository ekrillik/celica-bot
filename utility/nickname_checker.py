def check_nickname(nickname, caller): 
    match nickname:
        case "lotus":
            character = "lotus"
            weapon = "lotus berserker"
            cub = "n/a"
            memory = "n/a"
        case "eclipse":
            character = "eclipse"
            weapon = "type zero"
            cub = "n/a"
            memory = "n/a"
        case "storm":
            character = "storm"
            weapon = "inverse chimera"
            cub = "n/a"
            memory = "n/a"
        case "dawn" | "dumbdawn":
            character = "dawn"
            weapon = "inverse shadow"
            cub = "n/a"
            memory = "n/a"
        case "evil liv" | "seggs" | "green jumper" | "<:evilliv:1272415890453041223>" | "lux":
            character = "lux"
            weapon = "benediction"
            cub = "n/a"
            memory = "n/a"
        case "palefire" | "firegod":
            character = "palefire"
            weapon = "wolf fang"
            cub = "n/a"
            memory = "n/a"
        case "nightblade":
            character = "nightblade"
            weapon = "soul ripper"
            cub = "n/a"
            memory = "n/a"
        case "zero":
            character = "zero"
            weapon = "ramiel"
            cub = "n/a"
            memory = "n/a"
        case "blast":
            character = "blast"
            weapon = "berserk fusion"
            cub = "n/a"
            memory = "n/a"
        case "lumi" | "luminance":
            character = "luminance"
            weapon = "dragon wind"
            cub = "n/a"
            memory = "n/a"
        case "entropy" | "entrobrick":
            character = "entropy"
            weapon = "zero scale"
            cub = "n/a"
            memory = "n/a"
        case "ember":
            character = "ember"
            weapon = "fusion dragon"
            cub = "nitor"
            memory = "n/a"
        case "pulse":
            character = "pulse"
            weapon = "hydro heat"
            cub = "n/a"
            memory = "n/a"
        case "tenebrion" | "teneb" | "terb":
            character = "tenebrion"
            weapon = "darkness"
            cub = "n/a"
            memory = "n/a"
        case "crimson abyss" | "abyss" | "crimson brick" | "ca" | "CA":
            character = "crimson abyss"
            weapon = "sakura"
            cub = "n/a"
            memory = "n/a"
        case "bastion" | "kimochiyokatta" | "kimochi yokatta":
            character = "bastion"
            weapon = "big kamui"
            cub = "n/a"
            memory = "n/a"
        case "astral" | "asstral":
            character = "astral"
            weapon = "peacemaker"
            cub = "n/a"
            memory = "n/a"
        case "brilliance":
            character = "brilliance"
            weapon = "purple peony"
            cub = "n/a"
            memory = "n/a"
        case "veritas" | "veritrash":
            character = "veritas"
            weapon = "tonitrus"
            cub = "n/a"
            memory = "n/a"
        case "sophia" | "s*phia" | "silverfang":
            character = "silverfang"
            weapon = "scion"
            cub = "n/a"
            memory = "n/a"
        case "arclight":
            character = "arclight"
            weapon = "st. elmo"
            cub = "n/a"
            memory = "n/a"
        case "plume" | "ploom":
            character = "plume"
            weapon = "crimson birch"
            cub = "seeshell"
            memory = "n/a"
        case "rozen":
            character = "rozen"
            weapon = "sariel"
            cub = "n/a"
            memory = "n/a"
        case "camu" | "crocotta":
            character = "crocotta"
            weapon = "thanatos"
            cub = "n/a"
            memory = "koya"
        case "rosetta" | "juan" | "rigor":
            character = "rigor"
            weapon = "gungnir"
            cub = "frost oath"
            memory = "leeuwenhoek"
        case "changyu" | "changwho" | "qilin":
            character = "qilin"
            weapon = "baji"
            cub = "n/a"
            memory = "n/a"
        case "pavo":
            character = "pavo"
            weapon = "qinghe"
            cub = "n/a"
            memory = "wu'an"
        case "laurel" | "dark luna":
            character = "laurel"
            weapon = "ozma"
            cub = "noctua"
            memory = "flamel"
        case "2b" | "2B":
            character = "2b"
            weapon = "virtuous contract - mod"
            cub = "n/a"
            memory = "n/a"
        case "9s" | "9S":
            character = "9s"
            weapon = "cruel oath - mod"
            cub = "n/a"
            memory = "n/a"
        case "a2" | "A2":
            character = "a2"
            weapon = "type-4o lance - mod"
            cub = "n/a"
            memory = "n/a"
        case "hypnos" | "sleepyboi" | "sleepyhead" | "sleepyboy" | "time to sleep" | "sleepytime":
            character = "hypnos"
            weapon = "scale"
            cub = "n/a"
            memory = "n/a"
        case "tempest":
            character = "tempest"
            weapon = "waldmeister"
            cub = "n/a"
            memory = "lucrezia"
        case "glory":
            character = "glory"
            weapon = "apollo"
            cub = "boreas"
            memory = "n/a"
        case "xxi" | "21":
            character = "xxi"
            weapon = "snore"
            cub = "n/a"
            memory = "n/a"
        case "garnet" | "flare":
            character = "garnet"
            weapon = "phoenix"
            cub = "n/a"
            memory = "tifa"
        case "roland" | "kuraimaksu" | "clown" | "theatre" | "curtain call":
            character = "flambeau"
            weapon = "durendal"
            cub = "n/a"
            memory = "jack"
        case "empy" | "solaeter" | "empyrea" | "flashbang":
            character = "empyrea"
            weapon = "hestia"
            cub = "n/a"
            memory = "elizabeth"
        case "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq":
            character = "capriccio"
            weapon = "sarastro"
            cub = "n/a"
            memory = "seraphine"
        case "pulao":
            character = "pulao"
            weapon = "infinity"
            cub = "n/a"
            memory = "marco"
        case "starfarer" | "nanamech" | "nanamecha":
            character = "starfarer"
            weapon = "implosion"
            cub = "jet jaeger"
            memory = "unimate"
        case "haicma" | "hag" | "haicmama" | "nanny":
            character = "starfarer"
            weapon = "galatea"
            cub = "n/a"
            memory = "isabel"
        case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "trs" | "<:trs:1275701510293946482>" | "bunny" | "bnnuy" | "scire" | "best girl" | "bestgirl" | "flat tsundere is not waifu":
            character = "scire"
            weapon = "illuminare"
            cub = "moonhopper"
            memory = "boone"
        case "noan" | "deadweight":
            character = "arca"
            weapon = "prometheus"
            cub = "n/a"
            memory = "shelley"
        case "balter" | "stigmata":
            character = "stigmata"
            weapon = "hecate"
            cub = "shimmer"
            memory = "charlotte"
        case "bambinata" | "bambi" | "bombi":
            character = "bambinata"
            weapon = "sound of silence"
            cub = "n/a"
            memory = "n/a"
        case "supercar" | "car" | "hyper" | "hyperreal" | "xly" | "xiangli yao":
            character = "hyperreal"
            weapon = "stokes"
            cub = "punchy"
            memory = "turing"
        case "cow" | "kale" | "kaleido":
            character = "kaleido"
            weapon = "star voyager"
            cub = "rainbow"
            memory = "aline"       
        case "weave" | "motivation" | "vergil's daughter" | "crimson weave" | "cw":
            character = "crimson weave"
            weapon = "nightblaze"
            cub = "motorbolt"
            memory = "diesel"
        case "zitherwoe":
            character = "zitherwoe"
            weapon = "perpetuity"
            cub = "n/a"
            memory = "n/a"
        case "awoo" | "furry" | "feral" | "feral: 21" | "feral:21" | "best daughter":
            character = "feral"
            weapon = "managarm"
            cub = "hades fangs"
            memory = "fran"
        case "indomitus" | "noctis":
            character = "indomitus"
            weapon = "crimson howl"
            cub = "n/a"
            memory = "n/a"
        case "alisa" | "echo":
            character = "echo"
            weapon = "astraea"
            cub = "dawn chorus"
            memory = "signa"
        case "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia":
            character = "lost lullaby"
            weapon = "metis"
            cub = "cetus"
            memory = "derketo"
        case "brs" | "brick rock shooter":
            character = "brs"
            weapon = "black rock cannon"
            cub = "n/a"
            memory = "n/a"
        case "uncle" | "king engine" | "kingengine" | "wata" | "epitaph":
            character = "epitaph"
            weapon = "night falcon"
            cub = "n/a"
            memory = "alphonse"
        case "shukra":
            character = "shukra"
            weapon = ""
            cub = ""
            memory = ""
        case "teddy" | "decryptor":
            character = "teddy"
            weapon = ""
            cub = ""
            memory = ""
        case "oblivion" | "void luna":
            character = "oblivion"
            weapon = ""
            cub = ""
            memory = ""
        case "bridget":
            character = "bridget"
            weapon = ""
            cub = ""
            memory = ""
        case "solacetune":
            character = "solacetune"
            weapon = ""
            cub = ""
            memory = ""
        case "lucid dreamer":
            character = "lucid dreamer"
            weapon = ""
            cub = ""
            memory = ""
        case "pyroath" | "hyperdawn":
            character = "pyroath"
            weapon = ""
            cub = ""
            memory = ""
        case "fulgor" | "yata" | "tomboy":
            character = "fulgor"
            weapon = ""
            cub = "n/a"
            memory = "n/a"
        
        case _:
            if(caller == "character"):
                character = nickname
            elif(caller == "weapon"):
                weapon = nickname
            elif(caller == "memory"):
                memory = nickname
            else:
                cub = nickname

    if(caller == "character"):
        item_name = character
    elif(caller == "weapon"):
        item_name = weapon
    elif(caller == "cub"):
        item_name = cub
    elif(caller == "memory"):
        item_name = memory

    return item_name

def abbreviation_checker(nickname):
        match nickname:
            case "dv" | "davinci":
                memory = "da vinci"
            case "cot":
                memory = "cottie"
            case "eins":
                memory = "einsteina"
            case "guin":
                memory = "guinevere"
            case "char":
                memory = "charlotte"
            case "uni":
                memory = "unimate"
            case "leeu":
                memory = "leeuwenhoek"
            case "bath":
                memory = "bathlon"
            case "cond":
                memory = "condelina"
            case "chen" | "cjy" | "zuwen":
                memory = "chen jiyuan"
            case "lantern":
                memory = "lantern festival reunion"
            case "sam":
                memory = "samantha"
            case "shakes":
                memory = "shakespeare"
            case "liz" | "eliz":
                memory = "elizabeth"
            case "sera" | "seraph":
                memory = "seraphine"
            case "cath":
                memory = "catherine"
            case "fred":
                memory = "frederick"
            case "phil":
                memory = "philip"
            case "derk":
                memory = "derketo"
            case _:
                memory = "n/a"
            
        return memory

def character_theme(nickname):
    match nickname:
        case "lotus":
            name = "Lucia: Lotus"
            colour = 0x750008
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3q.webp"
        case "eclipse":
            name = "Liv: Eclipse"
            colour = 0xf7f1fd
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3q.webp"
        case "storm":
            name = "Nanami: Storm"
            colour = 0x322c1e
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadyongyechao3q.webp"
        case "dawn":
            name = "Lucia: Dawn"
            colour = 0x720e0d
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3sq.webp"
        case "lux":
            name = "Liv: Lux"
            colour = 0xeb98c8
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3sq.webp"
        case "palefire":
            name = "Lee: Palefire"
            colour = 0x3a499f
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadli3q.webp"
        case "nightblade":
            name = "Watanabe: Nightblade"
            colour = 0x79726b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheaddubian3q.webp"
        case "zero":
            name = "Bianca: Zero"
            colour = 0x8297f7
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadaolisuo3q.webp"
        case "blast":
            name = "Karenina: Blast"
            colour = 0xd29d2f
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkalie3q.webp"
        case "luminance":
            name = "Liv: Luminance"
            colour = 0xcf5bb0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3ssq.webp"
        case "entropy":
            name = "Lee: Entropy"
            colour = 0x2841a5
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadli3ssq.webp"
        case "ember":
            name = "Karenina: Ember"
            colour = 0xd43c12
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkalie3ssq.webp"
        case "pulse":
            name = "Nanami: Pulse"
            colour = 0xd9b15a
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadyongyechao3ssq.webp"
        case "tenebrion":
            name = "Kamui: Tenebrion"
            colour = 0x43941c
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadshenwei3ssq.webp"
        case "crimson abyss":
            name = "Lucia: Crimson Abyss"
            colour = 0xbb0917
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3ssq.webp"
        case "bastion":
            name = "Kamui: Bastion"
            colour = 0x6ac420
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadshenwei3q.webp"
        case "astral":
            name = "Watanabe: Astral"
            colour = 0xa9885b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheaddubian3ssq.webp"
        case "brilliance":
            name = "Ayla: Brilliance"
            colour = 0xbf1390
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadaila3q.webp"
        case "veritas":
            name = "Bianca: Veritas"
            colour = 0x3e46c0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadbianka3ssq.webp"
        case "silverfang":
            name = "Sophia: Silverfang"
            colour = 0xd46834
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadsufeiya3q.webp"
        case "arclight":
            name = "Chrome: Arclight"
            colour = 0x4b78b0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkulomu3q.webp"
        case "plume":
            name = "Lucia: Plume"
            colour = 0xa11029
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4luxiya3q.webp"
        case "rozen":
            name = "Vera: Rozen"
            colour = 0x9d1019
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadweila3q.webp"
        case "crocotta":
            name = "Camu: Crocotta"
            colour = 0x554773
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkamu3q.webp"
        case "rigor":
            name = "Rosetta: Rigor"
            colour = 0x5734a2
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluosaita3q.webp"
        case "qilin":
            name = "Changyu: Qilin"
            colour = 0x9c7b58
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadchangyu3q.webp"
        case "pavo":
            name = "Qu: Pavo"
            colour = 0x0d834a
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadqu3q.webp"
        case "laurel":
            name = "Luna: Laurel"
            colour = 0xe5e4e3
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluna3q.webp"
        case "2b":
            name = "2B: 2B"
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead2b3q.webp"
        case "9s":
            name = "9S: 9S"
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead9s3q.webp"
        case "a2":
            name = "A2: A2"
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheada23q.webp"
        case "hypnos":
            name = "Wanshi: Hypnos"
            colour = 0x258e8d
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadwanshi3q.webp"
        case "tempest":
            name = "Selena: Tempest"
            colour = 0x5886ec
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadsailinna3q.webp"
        case "glory":
            name = "Chrome: Glory"
            colour = 0x89abbf
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3kuluomu3q.webp"
        case "xxi":
            name = "No. 21: XXI"
            colour = 0x8f8ac5
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead21hao3q.webp"
        case "garnet":
            name = "Vera: Garnet"
            colour = 0xdc4848
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3weila3q.webp"
        case "flambeau":
            name = "Roland: Flambeau"
            colour = 0x4b5059
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluolan3qnew.webp"
        case "empyrea":
            name = "Liv: Empyrea"
            colour = 0xd7d8da
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4lifu3q.webp"
        case "capriccio":
            name = "Selena: Capriccio"
            colour = 0x4e74c8
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3sailinna3q.webp"
        case "dragontoll":
            name = "Pulao: Dragontoll"
            colour = 0xa72d29
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadpulao3qnew.webp"
        case "starfarer":
            name = "Nanami: Starfarer"
            colour = 0x606973
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr5yongyechao3q.webp"
        case "starveil":
            name = "Haicma: Starveil"
            colour = 0x3f454e
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadhakama3qnew.webp"
        case "scire":
            name = "Karenina: Scire"
            colour = 0xd3af59
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4kalienina3q.webp"
        case "arca":
            name = "Noan: Arca"
            colour = 0xbbc2fa
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadnuoan3qnew.webp"
        case "stigmata":
            name = "Bianca: Stigmata"
            colour = 0x7f6fb3
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4bianka3q.webp"
        case "vitrum":
            name = "Bambinata: Vitrum"
            colour = 0xcfe8f7
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2bangbinata2q.webp"
        case "hyperreal":
            name = "Lee: Hyperreal"
            colour = 0x6389d0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4li2q.webp"
        case "kaleido":
            name = "Ayla: Kaleido"
            colour = 0xce99b0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3aila2q.webp"     
        case "crimson weave":
            name = "Lucia: Crimson Weave"
            colour = 0xd54847
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr5luxiya2q.webp"
        case "zitherwoe":
            name = "Hanying: Zitherwoe"
            colour = 0x4d7f7b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2hanying2q.webp"
        case "feral":
            name = "No. 21: Feral"
            colour = 0x9a8fac
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3twentyone2q.webp"
        case "indomitus":
            name = "Noctis: Indomitus"
            colour = 0xc84a58
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2nuoketi2q.webp"
        case "echo":
            name = "Alisa: Echo"
            colour = 0xa3a3cd
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3yalisha2q.webp"
        case "lost lullaby":
            name = "Lamia: Lost Lullaby"
            colour = 0x6086a0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3lamiya2q.webp"
        case "brs":
            name = "BRS: BRS"
            colour = 0x2f3743
            chibi_portrait = ""
        case "epitaph":
            name = "Watanabe: Epitaph"
            colour = 0x63858a
            chibi_portrait = ""
        case "shukra":
            name = "Qu: Shukra"
            colour = 0x827776
            chibi_portrait = ""
        case "decryptor":
            name = "Teddy: Decryptor"
            colour = 0x6572b6
            chibi_portrait = ""
        case "oblivion":
            name = "Luna: Oblivion"
            colour = 0x832223
            chibi_portrait = ""
        case "ardeo":
            name = "Bridget: Ardeo"
            colour = 0xc5a36e
            chibi_portrait = ""
        case "solacetune":
            name = "Hanying: Solacetune"
            colour = 0x557d7b
            chibi_portrait = ""
        case "lucid dreamer":
            name = "Wanshi: Lucid Dreamer"
            colour = 0x4099a2
            chibi_portrait = ""
        case "pyroath":
            name = "Lucia: Pyroath"
            colour = 0xe9a276
            chibi_portrait = ""
        case "fulgor":
            name = "Yata: Fulgor"
            colour = 0xc14d2c
            chibi_portrait = ""
        case _:
            name = ""
            colour = ""
            chibi_portrait = ""

    return [colour, chibi_portrait, name]