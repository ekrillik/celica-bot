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
        case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "trs" | "<:trs:1275701510293946482>" | "bunny" | "bnnuy" | "scire" | "best girl" | "bestgirl":
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
            colour = 0x750008
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3q.webp"
        case "eclipse":
            colour = 0xf7f1fd
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3q.webp"
        case "storm":
            colour = 0x322c1e
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadyongyechao3q.webp"
        case "dawn":
            colour = 0x720e0d
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluxiya3sq.webp"
        case "lux":
            colour = 0xeb98c8
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3sq.webp"
        case "palefire":
            colour = 0x3a499f
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadli3q.webp"
        case "nightblade":
            colour = 0x79726b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheaddubian3q.webp"
        case "zero":
            colour = 0x8297f7
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadaolisuo3q.webp"
        case "blast":
            colour = 0xd29d2f
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkalie3q.webp"
        case "luminance":
            colour = 0xcf5bb0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadlifu3ssq.webp"
        case "entropy":
            colour = 0x2841a5
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadli3ssq.webp"
        case "ember":
            colour = 0xd43c12
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkalie3ssq.webp"
        case "pulse":
            colour = 0xd9b15a
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadyongyechao3ssq.webp"
        case "tenebrion":
            colour = 0x43941c
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadshenwei3ssq.webp"
        case "crimson abyss":
            colour = 0xbb0917
            chibi_portrait = "https://assets.huaxu.app/glsb/image/role/roleheadluxiya3ssq.webp"
        case "bastion":
            colour = 0x6ac420
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadshenwei3q.webp"
        case "astral":
            colour = 0xa9885b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheaddubian3ssq.webp"
        case "brilliance":
            colour = 0xbf1390
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadaila3q.webp"
        case "veritas":
            colour = 0x3e46c0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadbianka3ssq.webp"
        case "silverfang":
            colour = 0xd46834
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadsufeiya3q.webp"
        case "arclight":
            colour = 0x4b78b0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkulomu3q.webp"
        case "plume":
            colour = 0xa11029
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4luxiya3q.webp"
        case "rozen":
            colour = 0x9d1019
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadweila3q.webp"
        case "crocotta":
            colour = 0x554773
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadkamu3q.webp"
        case "rigor":
            colour = 0x5734a2
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluosaita3q.webp"
        case "qilin":
            colour = 0x9c7b58
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadchangyu3q.webp"
        case "pavo":
            colour = 0x0d834a
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadqu3q.webp"
        case "laurel":
            colour = 0xe5e4e3
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluna3q.webp"
        case "2b":
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead2b3q.webp"
        case "9s":
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead9s3q.webp"
        case "a2":
            colour = 0x222222
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheada23q.webp"
        case "hypnos":
            colour = 0x258e8d
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadwanshi3q.webp"
        case "tempest":
            colour = 0x5886ec
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadsailinna3q.webp"
        case "glory":
            colour = 0x89abbf
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3kuluomu3q.webp"
        case "xxi":
            colour = 0x8f8ac5
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/rolehead21hao3q.webp"
        case "garnet":
            colour = 0xdc4848
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3weila3q.webp"
        case "flambeau":
            colour = 0x4b5059
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadluolan3qnew.webp"
        case "empyrea":
            colour = 0xd7d8da
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4lifu3q.webp"
        case "capriccio":
            colour = 0x4e74c8
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3sailinna3q.webp"
        case "dragontoll":
            colour = 0xa72d29
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadpulao3qnew.webp"
        case "starfarer":
            colour = 0x606973
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr5yongyechao3q.webp"
        case "starveil":
            colour = 0x3f454e
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadhakama3qnew.webp"
        case "scire":
            colour = 0xd3af59
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4kalienina3q.webp"
        case "arca":
            colour = 0xbbc2fa
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadnuoan3qnew.webp"
        case "stigmata":
            colour = 0x7f6fb3
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4bianka3q.webp"
        case "vitrum":
            colour = 0xcfe8f7
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2bangbinata2q.webp"
        case "hyperreal":
            colour = 0x6389d0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr4li2q.webp"
        case "kaleido":
            colour = 0xce99b0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3aila2q.webp"     
        case "crimson weave":
            colour = 0xd54847
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr5luxiya2q.webp"
        case "zitherwoe":
            colour = 0x4d7f7b
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2hanying2q.webp"
        case "feral":
            colour = 0x9a8fac
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3twentyone2q.webp"
        case "indomitus":
            colour = 0xc84a58
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr2nuoketi2q.webp"
        case "echo":
            colour = 0xa3a3cd
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3yalisha2q.webp"
        case "lost lullaby":
            colour = 0x6086a0
            chibi_portrait = "https://assets.huaxu.app/glb/image/role/roleheadr3lamiya2q.webp"
        case "brs":
            colour = 0x2f3743
            chibi_portrait = ""
        case "epitaph":
            colour = 0x63858a
            chibi_portrait = ""
        case "shukra":
            colour = 0x827776
            chibi_portrait = ""
        case "decryptor":
            colour = 0x6572b6
            chibi_portrait = ""
        case "oblivion":
            colour = 0x832223
            chibi_portrait = ""
        case "ardeo":
            colour = 0xc5a36e
            chibi_portrait = ""
        case "solacetune":
            colour = 0x557d7b
            chibi_portrait = ""
        case "lucid dreamer":
            colour = 0x4099a2
            chibi_portrait = ""
        case "pyroath":
            colour = 0xe9a276
            chibi_portrait = ""
        case "fulgor":
            colour = 0xc14d2c
            chibi_portrait = ""

    return [colour, chibi_portrait]