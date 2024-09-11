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
        case "crimson abyss" | "abyss" | "crimson brick":
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
            character = "sophia"
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
            character = "camu"
            weapon = "thanatos"
            cub = "n/a"
            memory = "koya"
        case "rosetta" | "juan" | "rigor":
            character = "rigor"
            weapon = "gungnir"
            cub = "frost oath"
            memory = "leeuwenhoek"
        case "changyu" | "changwho" | "qilin":
            character = "changyu"
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
            character = "roland"
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
            character = "haicma"
            weapon = "galatea"
            cub = "n/a"
            memory = "isabel"
        case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "trs" | "<:trs:1275701510293946482>" | "bunny" | "bnnuy" | "scire" | "best girl" | "bestgirl":
            character = "scire"
            weapon = "illuminare"
            cub = "moonhopper"
            memory = "boone"
        case "noan" | "deadweight":
            character = "noan"
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
        case "supercar" | "car" | "hyper" | "hyperreal":
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
        case "awoo" | "furry" | "feral" | "feral: 21" | "feral:21":
            character = "feral"
            weapon = "managarm"
            cub = "hades fangs"
            memory = "fran"
        case "indomitus" | "noctis":
            character = "noctis"
            weapon = "crimson howl"
            cub = "n/a"
            memory = "n/a"
        case "alisa" | "echo":
            character = "alisa"
            weapon = "astraea"
            cub = "dawn chorus"
            memory = "signa"
        case "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia":
            character = "lamia"
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
            case "chen" | "cjy":
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
            colour = 0x333333
            chibi_portrait = ""
        case "eclipse":
            colour = 0x333333
            chibi_portrait = ""
        case "storm":
            colour = 0x333333
            chibi_portrait = ""
        case "dawn" | "dumbdawn":
            colour = 0x333333
            chibi_portrait = ""
        case "evil liv" | "seggs" | "green jumper" | "<:evilliv:1272415890453041223>" | "lux":
            colour = 0x333333
            chibi_portrait = ""
        case "palefire" | "firegod":
            colour = 0x333333
            chibi_portrait = ""
        case "nightblade":
            colour = 0x333333
            chibi_portrait = ""
        case "zero":
            colour = 0x333333
            chibi_portrait = ""
        case "blast":
            colour = 0x333333
            chibi_portrait = ""
        case "lumi" | "luminance":
            colour = 0x333333
            chibi_portrait = ""
        case "entropy" | "entrobrick":
            colour = 0x333333
            chibi_portrait = ""
        case "ember":
            colour = 0x333333
            chibi_portrait = ""
        case "pulse":
            colour = 0x333333
            chibi_portrait = ""
        case "tenebrion" | "teneb" | "terb":
            colour = 0x333333
            chibi_portrait = ""
        case "crimson abyss" | "abyss" | "crimson brick":
            colour = 0x333333
            chibi_portrait = ""
        case "bastion" | "kimochiyokatta" | "kimochi yokatta":
            colour = 0x333333
            chibi_portrait = ""
        case "astral" | "asstral":
            colour = 0x333333
            chibi_portrait = ""
        case "brilliance":
            colour = 0x333333
            chibi_portrait = ""
        case "veritas" | "veritrash":
            colour = 0x333333
            chibi_portrait = ""
        case "sophia" | "s*phia" | "silverfang":
            colour = 0x333333
            chibi_portrait = ""
        case "arclight":
            colour = 0x333333
            chibi_portrait = ""
        case "plume" | "ploom":
            colour = 0x333333
            chibi_portrait = ""
        case "rozen":
            colour = 0x333333
            chibi_portrait = ""
        case "camu" | "crocotta":
            colour = 0x333333
            chibi_portrait = ""
        case "rosetta" | "juan" | "rigor":
            colour = 0x333333
            chibi_portrait = ""
        case "changyu" | "changwho" | "qilin":
            colour = 0x333333
            chibi_portrait = ""
        case "pavo":
            colour = 0x333333
            chibi_portrait = ""
        case "laurel" | "dark luna":
            colour = 0x333333
            chibi_portrait = ""
        case "2b" | "2B":
            colour = 0x333333
            chibi_portrait = ""
        case "9s" | "9S":
            colour = 0x333333
            chibi_portrait = ""
        case "a2" | "A2":
            colour = 0x333333
            chibi_portrait = ""
        case "hypnos" | "sleepyboi" | "sleepyhead" | "sleepyboy" | "time to sleep" | "sleepytime":
            colour = 0x333333
            chibi_portrait = ""
        case "tempest":
            colour = 0x333333
            chibi_portrait = ""
        case "glory":
            colour = 0x333333
            chibi_portrait = ""
        case "xxi" | "21":
            colour = 0x333333
            chibi_portrait = ""
        case "garnet" | "flare":
            colour = 0x333333
            chibi_portrait = ""
        case "roland" | "kuraimaksu" | "clown" | "theatre" | "curtain call":
            colour = 0x333333
            chibi_portrait = ""
        case "empy" | "solaeter" | "empyrea" | "flashbang":
            colour = 0x333333
            chibi_portrait = ""
        case "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq":
            colour = 0x333333
            chibi_portrait = ""
        case "pulao":
            colour = 0x333333
            chibi_portrait = ""
        case "starfarer" | "nanamech" | "nanamecha":
            colour = 0x333333
            chibi_portrait = ""
        case "haicma" | "hag" | "haicmama" | "nanny":
            colour = 0x333333
            chibi_portrait = ""
        case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "trs" | "<:trs:1275701510293946482>" | "bunny" | "bnnuy" | "scire" | "best girl" | "bestgirl":
            colour = 0x333333
            chibi_portrait = ""
        case "noan" | "deadweight":
            colour = 0x333333
            chibi_portrait = ""
        case "balter" | "stigmata":
            colour = 0x333333
            chibi_portrait = ""
        case "bambinata" | "bambi" | "bombi":
            colour = 0x333333
            chibi_portrait = ""
        case "supercar" | "car" | "hyper" | "hyperreal":
            colour = 0x333333
            chibi_portrait = ""
        case "cow" | "kale" | "kaleido":
            colour = 0x333333
            chibi_portrait = ""     
        case "weave" | "motivation" | "vergil's daughter" | "crimson weave" | "cw":
            colour = 0x333333
            chibi_portrait = ""
        case "zitherwoe":
            colour = 0x333333
            chibi_portrait = ""
        case "awoo" | "furry" | "feral" | "feral: 21" | "feral:21":
            colour = 0x333333
            chibi_portrait = ""
        case "indomitus" | "noctis":
            colour = 0x333333
            chibi_portrait = ""
        case "alisa" | "echo":
            colour = 0x333333
            chibi_portrait = ""
        case "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia":
            colour = 0x333333
            chibi_portrait = ""
        case "brs" | "brick rock shooter":
            colour = 0x333333
            chibi_portrait = ""
        case "uncle" | "king engine" | "kingengine" | "wata" | "epitaph":
            colour = 0x333333
            chibi_portrait = ""
        case "shukra":
            colour = 0x333333
            chibi_portrait = ""
        case "teddy" | "decryptor":
            colour = 0x333333
            chibi_portrait = ""
        case "oblivion" | "void luna":
            colour = 0x333333
            chibi_portrait = ""
        case "bridget":
            colour = 0x333333
            chibi_portrait = ""
        case "solacetune":
            colour = 0x333333
            chibi_portrait = ""
        case "lucid dreamer":
            colour = 0x333333
            chibi_portrait = ""
        case "pyroath" | "hyperdawn":
            colour = 0x333333
            chibi_portrait = ""
        case "fulgor" | "yata" | "tomboy":
            colour = 0x333333
            chibi_portrait = ""


    return