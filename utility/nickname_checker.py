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
        case "evil liv" | "green jumper" | "<:evilliv:1272415890453041223>" | "lux":
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
            character = "starveil"
            weapon = "galatea"
            cub = "n/a"
            memory = "isabel"
        case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "bunny" | "bnnuy" | "scire" | "best girl" | "bestgirl" | "flat tsundere is not waifu":
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
            weapon = "dwelling will of inscription's key"
            cub = ""
            memory = ""
        case "teddy" | "decryptor":
            character = "decryptor"
            weapon = "hacker's tune"
            cub = "n/a"
            memory = "n/a"
        case "oblivion" | "void luna":
            character = "oblivion"
            weapon = "reconstruction of law"
            cub = ""
            memory = ""
        case "bridget" | "ardeo":
            character = "ardeo"
            weapon = "cestus"
            cub = "n/a"
            memory = "n/a"
        case "solacetune" | "yor" | "yor forger":
            character = "solacetune"
            weapon = "dreamer roamer"
            cub = ""
            memory = ""
        case "lucid dreamer":
            character = "lucid dreamer"
            weapon = "hemera's gaze"
            cub = ""
            memory = ""
        case "pyroath" | "hyperdawn":
            character = "pyroath"
            weapon = "dawn's flaming feathers"
            cub = ""
            memory = ""
        case "fulgor" | "yata" | "tomboy":
            character = "fulgor"
            weapon = "morrow's executioner"
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
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadluxiya2.256.webp"
        case "eclipse":
            name = "Liv: Eclipse"
            colour = 0xf7f1fd
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3q.webp"
            thumbnail_url =  "https://assets.huaxu.app/glb/image/rolecharacter/lifunormal01.256.webp"
        case "storm":
            name = "Nanami: Storm"
            colour = 0x322c1e
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadyongyechao3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadyongyechao2.256.webp"
        case "dawn":
            name = "Lucia: Dawn"
            colour = 0x720e0d
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3sq.webp"
            thumbnail_url =  "https://assets.huaxu.app/glb/image/rolecharacter/roleheadluxiya2s.256.webp"
        case "lux":
            name = "Liv: Lux"
            colour = 0xeb98c8
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3sq.webp"
            thumbnail_url =  "https://assets.huaxu.app/glb/image/rolecharacter/roleheadlifu2s.256.webp"
        case "palefire":
            name = "Lee: Palefire"
            colour = 0x3a499f
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadli3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadli2.256.webp"
        case "nightblade":
            name = "Watanabe: Nightblade"
            colour = 0x79726b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheaddubian3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheaddubian2.256.webp"
        case "zero":
            name = "Bianca: Zero"
            colour = 0x8297f7
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadaolisuo3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadaolisuo2.256.webp"
        case "blast":
            name = "Karenina: Blast"
            colour = 0xd29d2f
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkalie3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadkalienina2.256.webp"
        case "luminance":
            name = "Liv: Luminance"
            colour = 0xcf5bb0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/lifuyongzhuangnormal01.256.webp"
        case "entropy":
            name = "Lee: Entropy"
            colour = 0x2841a5
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadli3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadli2ss.256.webp"
        case "ember":
            name = "Karenina: Ember"
            colour = 0xd43c12
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkalie3ssq.webp"
            thumbnail_url =  "https://assets.huaxu.app/glb/image/rolecharacter/roleheadkalienina2ss.256.webp"
        case "pulse":
            name = "Nanami: Pulse"
            colour = 0xd9b15a
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadyongyechao3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadyongyechao2ss.256.webp"
        case "tenebrion":
            name = "Kamui: Tenebrion"
            colour = 0x43941c
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadshenwei3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadshenwei2ss.256.webp"
        case "crimson abyss":
            name = "Lucia: Crimson Abyss"
            colour = 0xbb0917
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadluxiyaaerfa2ss.256.webp"
        case "bastion":
            name = "Kamui: Bastion"
            colour = 0x6ac420
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadshenwei3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadshenwei2.256.webp"
        case "astral":
            name = "Watanabe: Astral"
            colour = 0xa9885b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheaddubian3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheaddubian2ss.256.webp"
        case "brilliance":
            name = "Ayla: Brilliance"
            colour = 0xbf1390
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadaila3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadaila2.256.webp"
        case "veritas":
            name = "Bianca: Veritas"
            colour = 0x3e46c0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadbianka3ssq.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadbianka2ss.256.webp"
        case "silverfang":
            name = "Sophia: Silverfang"
            colour = 0xd46834
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadsufeiya3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadsufeiya2.256.webp"
        case "arclight":
            name = "Chrome: Arclight"
            colour = 0x4b78b0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkulomu3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadkuluomu2.256.webp"
        case "plume":
            name = "Lucia: Plume"
            colour = 0xa11029
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4luxiya3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr4luxiya2.256.webp"
        case "rozen":
            name = "Vera: Rozen"
            colour = 0x9d1019
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadweila3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadweila2.256.webp"
        case "crocotta":
            name = "Camu: Crocotta"
            colour = 0x554773
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkamu3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadkamu2.256.webp"
        case "rigor":
            name = "Rosetta: Rigor"
            colour = 0x5734a2
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluosaita3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadluosaita2.256.webp"
        case "qilin":
            name = "Changyu: Qilin"
            colour = 0x9c7b58
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadchangyu3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadchangyu2.256.webp"
        case "pavo":
            name = "Qu: Pavo"
            colour = 0x0d834a
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadqu3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadqu2.256.webp"
        case "laurel":
            name = "Luna: Laurel"
            colour = 0xe5e4e3
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluna3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadluna2.256.webp",
        case "2b":
            name = "2B: 2B"
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead2b3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadtwob2.256.webp"
        case "9s":
            name = "9S: 9S"
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead9s3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadnines2.256.webp"
        case "a2":
            name = "A2: A2"
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheada23q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadatwo3.256.webp"
        case "hypnos":
            name = "Wanshi: Hypnos"
            colour = 0x258e8d
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadwanshi3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadwanshi2.webp"
        case "tempest":
            name = "Selena: Tempest"
            colour = 0x5886ec
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadsailinna3q.webp"
            thumbnail_url ="https://assets.huaxu.app/glb/image/rolecharacter/roleheadsailinna2.256.webp"
        case "glory":
            name = "Chrome: Glory"
            colour = 0x89abbf
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3kuluomu3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3kuluomu2.256.webp"
        case "xxi":
            name = "No. 21: XXI"
            colour = 0x8f8ac5
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead21hao3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadtwentyone2.256.webp"
        case "garnet":
            name = "Vera: Garnet"
            colour = 0xdc4848
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3weila3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3weila2.256.webp"
        case "flambeau":
            name = "Roland: Flambeau"
            colour = 0x4b5059
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluolan3qnew.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadluolan2.256.webp"
        case "empyrea":
            name = "Liv: Empyrea"
            colour = 0xd7d8da
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4lifu3q.webp"
            thumbnail_url= "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr4lifu2.256.webp"
        case "capriccio":
            name = "Selena: Capriccio"
            colour = 0x4e74c8
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3sailinna3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3sailinna2.256.webp"
        case "dragontoll":
            name = "Pulao: Dragontoll"
            colour = 0xa72d29
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadpulao3qnew.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadpulao2.256.webp"
        case "starfarer":
            name = "Nanami: Starfarer"
            colour = 0x606973
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr5yongyechao3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr5yongyechao2.256.webp"
        case "starveil":
            name = "Haicma: Starveil"
            colour = 0x3f454e
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadhakama3qnew.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadhakama2.256.webp"
        case "scire":
            name = "Karenina: Scire"
            colour = 0xd3af59
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4kalienina3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr4kalienina2.256.webp"
        case "arca":
            name = "Noan: Arca"
            colour = 0xbbc2fa
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadnuoan3qnew.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadnuoan2.256.webp"
        case "stigmata":
            name = "Bianca: Stigmata"
            colour = 0x7f6fb3
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4bianka3q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr4bianka2.256.webp"
        case "vitrum":
            name = "Bambinata: Vitrum"
            colour = 0xcfe8f7
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2bangbinata2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr2bangbinata3.256.webp"
        case "hyperreal":
            name = "Lee: Hyperreal"
            colour = 0x6389d0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4li2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr4li3.256.webp"
        case "kaleido":
            name = "Ayla: Kaleido"
            colour = 0xce99b0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3aila2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3aila3.256.webp"
        case "crimson weave":
            name = "Lucia: Crimson Weave"
            colour = 0xd54847
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr5luxiya2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr5luxiya3.256.webp"
        case "zitherwoe":
            name = "Hanying: Zitherwoe"
            colour = 0x4d7f7b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2hanying2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr2hanying3.256.webp"
        case "feral":
            name = "No. 21: Feral"
            colour = 0x9a8fac
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3twentyone2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3twentyone3.256.webp"
        case "indomitus":
            name = "Noctis: Indomitus"
            colour = 0xc84a58
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2nuoketi2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr2nuoketi3.256.webp"
        case "echo":
            name = "Alisa: Echo"
            colour = 0xa3a3cd
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3yalisha2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3yalisha3.256.webp"
        case "lost lullaby":
            name = "Lamia: Lost Lullaby"
            colour = 0x6086a0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3lamiya2q.webp"
            thumbnail_url = "https://assets.huaxu.app/glb/image/rolecharacter/roleheadr3lamiya3.256.webp"
        case "brs":
            name = "BRS: BRS"
            colour = 0x2f3743
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/3/3e/t05uf6n6d3vcd06i36fckvjnucfeuo6.png/60px-%E8%A7%92%E8%89%B2_BRS_BRS_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/d/d7/0w81iqz15uqzo2l1st6x7bxbqmhwkzc.png/100px-%E8%A7%92%E8%89%B2_BRS_BRS_%E7%BB%88%E8%A7%A3.png"
        case "epitaph":
            name = "Watanabe: Epitaph"
            colour = 0x63858a
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/b/bf/pfvsmtgub1e2pmw37wwt5zd3n21mht5.png/60px-%E8%A7%92%E8%89%B2_%E6%B8%A1%E8%BE%B9_%E5%B0%98%E9%93%AD_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/6/64/4jvc7di9eh9bvpqlof5m45gxw5d2f83.png/100px-%E8%A7%92%E8%89%B2_%E6%B8%A1%E8%BE%B9_%E5%B0%98%E9%93%AD_%E7%BB%88%E8%A7%A3.png"
        case "shukra":
            name = "Qu: Shukra"
            colour = 0x827776
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/7/75/5e2lnci312lci9fae9hmz8zxadl7a44.png/60px-%E8%A7%92%E8%89%B2_%E6%9B%B2_%E5%90%AF%E6%98%8E_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/9/96/hqohyer1kx5uk98uuibtgobindsoffh.png/150px-%E8%A7%92%E8%89%B2_%E6%9B%B2_%E5%90%AF%E6%98%8E_%E7%BB%88%E8%A7%A3.png"
        case "decryptor":
            name = "Teddy: Decryptor"
            colour = 0x6572b6
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/b/b6/nu4avpkis0e1dzsevr8jwqldfeb2wo7.png/60px-%E8%A7%92%E8%89%B2_%E5%B8%83%E5%81%B6%E7%86%8A_%E8%A7%85%E8%AF%AD_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/3/31/83g0tinfz72uoanwmks7v0zva0x2x4o.png/150px-%E8%A7%92%E8%89%B2_%E5%B8%83%E5%81%B6%E7%86%8A_%E8%A7%85%E8%AF%AD_%E7%BB%88%E8%A7%A3.png"
        case "oblivion":
            name = "Luna: Oblivion"
            colour = 0x832223
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/1/1e/7drdgxz5pbk28ujrv4gaqytjav87suc.png/60px-%E8%A7%92%E8%89%B2_%E9%9C%B2%E5%A8%9C_%E7%BB%88%E7%84%89_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/9/9f/b5bsod8q9xrgldv2jp5otbp3sh26ugp.png"
        case "ardeo":
            name = "Bridget: Ardeo"
            colour = 0xc5a36e
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/1/1a/slr0e8scfqvhodvtljjg81q10xh8xak.png/60px-%E8%A7%92%E8%89%B2_%E5%B8%83%E4%B8%BD%E5%A7%AC%E7%89%B9_%E8%80%80%E7%82%8E_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/c/c0/j27wwp6q06336pxetkvwoy0s1xx604d.png/150px-%E8%A7%92%E8%89%B2_%E5%B8%83%E4%B8%BD%E5%A7%AC%E7%89%B9_%E8%80%80%E7%82%8E_%E7%BB%88%E8%A7%A3.png"
        case "solacetune":
            name = "Hanying: Solacetune"
            colour = 0x557d7b
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/8/85/h0jshiyq0xddk0dty006h337fwtmab7.png/60px-%E8%A7%92%E8%89%B2_%E5%90%AB%E8%8B%B1_%E6%AA%80%E5%BF%83_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/8/81/fl38rgqswh82b65t9eah3v8leweiyxq.png/150px-%E8%A7%92%E8%89%B2_%E5%90%AB%E8%8B%B1_%E6%AA%80%E5%BF%83_%E7%BB%88%E8%A7%A3.png"
        case "lucid dreamer":
            name = "Wanshi: Lucid Dreamer"
            colour = 0x4099a2
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/d/d8/tq4bgip2d7grl9d6e63tyxzoh30w4x5.png/60px-%E8%A7%92%E8%89%B2_%E4%B8%87%E4%BA%8B_%E6%98%8E%E6%99%B0%E6%A2%A6_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/thumb/b/be/csmeplhq7miumtf7595efus40hlt86u.png/150px-%E8%A7%92%E8%89%B2_%E4%B8%87%E4%BA%8B_%E6%98%8E%E6%99%B0%E6%A2%A6_%E7%BB%88%E8%A7%A3.png"
        case "pyroath":
            name = "Lucia: Pyroath"
            colour = 0xe9a276
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/2/2b/8r1c9925z0z1ngvbwbifvydt5o32jzd.png/60px-%E8%A7%92%E8%89%B2_%E9%9C%B2%E8%A5%BF%E4%BA%9A_%E8%AA%93%E7%84%B0_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/a/a0/sodxmic1c3ulorbkz865n9ioq93s4jd.png"
        case "fulgor":
            name = "Yata: Fulgor"
            colour = 0xc14d2c
            chibi_portrait = "https://patchwiki.biligame.com/images/zspms/thumb/7/78/q00xaus0xhks32len61p84dxe9w7ybp.png/60px-%E8%A7%92%E8%89%B2_%E5%85%AB%E5%92%AB_%E5%BE%8A%E9%97%AA_Q%E7%89%88%E5%A4%B4%E5%83%8F.png"
            thumbnail_url = "https://patchwiki.biligame.com/images/zspms/d/dd/opubztfh9ygo8s6w2w19mounq0chliw.png"
        case _:
            name = ""
            colour = ""
            chibi_portrait = ""
            thumbnail_url = ""

    return [colour, chibi_portrait, name, thumbnail_url]
