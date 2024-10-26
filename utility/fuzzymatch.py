import json
import random

from thefuzz import fuzz
from thefuzz import process

def fuzzmatch(string, match_type = "character") -> str:
    with open('data/fuzzydict.json') as file:
        loadedData = json.load(file)
        choices = loadedData['dictionary']

    nickname = ""

    for choice in choices:
        if fuzz.token_sort_ratio(choice, string) > 90:
            print(choice)
            nickname = choice
        
    match nickname:
        case "beloved girl":
            characters = ["tempest", "capriccio"]
            index = random.randint(0, 1)
            character = characters[index]
        case "best girl" | "bestgirl":
            characters = ["eclipse", "lux", "luminance", "empyrea"]
            index = random.randint(0, 3)
            character = characters[index]
            print(character)
        case "lotus":
            character = "lotus"
        case "eclipse":
            character = "eclipse"
        case "storm":
            character = "storm"
        case "dawn" | "dumbdawn":
            character = "dawn"
        case "evil liv" | "green jumper" | "<:evilliv:1272415890453041223>" | "lux":
            character = "lux"
        case "palefire" | "firegod":
            character = "palefire"
        case "nightblade":
            character = "nightblade"
        case "zero":
            character = "zero"
        case "blast":
            character = "blast"
        case "lumi" | "luminance":
            character = "luminance"
        case "entropy" | "entrobrick" | "entropiss" | "entrokek":
            character = "entropy"
        case "ember":
            character = "ember"
        case "pulse":
            character = "pulse"
        case "tenebrion" | "teneb" | "terb":
            character = "tenebrion"
        case "crimson abyss" | "abyss" | "crimson brick" | "ca" | "CA" | "blue rose":
            character = "crimson abyss"
        case "bastion" | "kimochiyokatta" | "kimochi yokatta":
            character = "bastion"
        case "astral" | "asstral":
            character = "astral"
        case "brilliance":
            character = "brilliance"
        case "veritas" | "veritrash":
            character = "veritas"
        case "sophia" | "s*phia" | "silverfang" | "ireng":
            character = "silverfang"
        case "arclight":
            character = "arclight"
        case "plume" | "ploom":
            character = "plume"
        case "rozen":
            character = "rozen"
        case "camu" | "crocotta":
            character = "crocotta"
        case "rosetta" | "juan" | "rigor" | "rose" | "kuda" | "kuda lumping":
            character = "rigor"
        case "changyu" | "changwho" | "qilin" | "who?":
            character = "qilin"
        case "pavo":
            character = "pavo"
        case "laurel" | "dark luna" | "cutie pie":
            character = "laurel"
        case "2b":
            character = "2b"
        case "9s":
            character = "9s"
        case "a2":
            character = "a2"
        case "hypnos" | "sleepyboi" | "sleepyhead" | "sleepyboy" | "time to sleep" | "sleepytime" | "aurora's wife":
            character = "hypnos"
        case "tempest" | "shitlena" | "iris":
            character = "tempest"
        case "glory"| "daddy":
            character = "glory"
        case "xxi" | "21" | "crazy kid":
            character = "xxi"
        case "garnet" | "flare" | "dog owner" | "yinlin" | "zex's master":
            character = "garnet"
        case "flambeau" | "roland" | "kuraimakusu" | "clown" | "theatre" | "curtain call" | "badut":
            character = "flambeau"
        case "empy" | "solaeter" | "empyrea" | "flashbang" | "sol" | "angel" | "liv's gingerbread":
            character = "empyrea"
        case "capriccio" | "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq" | "red soup" | "grimace shake" | "irisv2" | "magikarp" | "kuyang":
            character = "capriccio"
        case "dragontoll" | "pulao" | "windbell's girl" | "windbell's wife":
            character = "dragontoll"
        case "starfarer" | "nanamech" | "nanamecha" | "sagemachina" | "mech":
            character = "starfarer"
        case "starveil" | "haicma" | "hag" | "haicmama" | "nanny" | "mama":
            character = "starveil"
        case "scire" | "daren" | "bonka" | "tsundere" | "radiant daybreak" | "bunny" | "bnnuy" | "scire" | "flat tsundere is not waifu" | "trs" | "idol" | "yoyo" | "trs's wife":
            character = "scire"
        case "arca" | "noan" | "deadweight" | "shrek" | "nero":
            character = "arca"
        case "balter" | "stigmata" | "mommy" | "saber" | "excalibaa" | "Balter" | "gothic nun" | "balt" | "mint's pillow":
            character = "stigmata"
        case "vitrum" | "bambinata" | "bambi" | "bombi" | "doll" | "puppet" | "dementia doll":
            character = "vitrum"
        case "supercar" | "car" | "hyper" | "hyperreal" | "xly" | "xiangli yao" | "hypertrash" | "hypermonke" | "hypercuck" | "zeru's sun" | "hyperbrick":
            character = "hyperreal"
        case "cow" | "kale" | "kaleido" | "rich painter"| "zhezhi" | "booba":
            character = "kaleido"  
        case "crimson weave" | "weave" | "motivation" | "vergil's daughter" | "cw" | "blanc's curse" | "bury the light" | "matt's girl" | "ojek" | "kang ojek":
            character = "crimson weave"
        case "zitherwoe" | "zitherhoe":
            character = "zitherwoe"
        case "awoo" | "furry" | "feral" | "feral: 21" | "feral:21" | "best daughter" | "doggo" | "wolfie-chan" | "fluffy" | "aether's daughter":
            character = "feral"
        case "indomitus" | "noctis" | "blockhead":
            character = "indomitus"
        case "alisa" | "echo" | "arrest me pls" | "altr's secretary":
            character = "echo"
        case "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia" | "mermaid" | "shawty" | "kev's waifu" | "skibidi" | "skibidi toilet":
            character = "lost lullaby"
            boss = "lamia"
        case "brs" | "brick rock shooter" | "edgy miku" | "black rock shooter":
            character = "brs"
        case "uncle" | "king engine" | "kingengine" | "wata" | "epitaph" | "heartbeat killer" | "old man" | "no longer fears death" | "big boss" | "green guy" | "boomer":
            character = "epitaph"
        case "shukra"| "qukra" | "queen" | "legs":
            character = "shukra"
        case "teddy" | "decryptor" | "smug" | "always beats karen" | "kusogaki" | "brat":
            character = "decryptor"
        case "oblivion" | "void luna" | "xeno's queen":
            character = "oblivion"
        case "bridget" | "ardeo" | "royal guard" | "dante":
            character = "ardeo"
        case "solacetune" | "yor" | "yor forger":
            character = "solacetune"
        case "lucid dreamer" | "lucid" | "ld" | "ocelot":
            character = "lucid dreamer"
        case "pyroath" | "hyperdawn" | "pyro":
            character = "pyroath"
        case "fulgor" | "yata" | "tomboy" | "oraora":
            character = "fulgor"
        case "startrail" | "nanaknight" | "star rail" | "hsr" | "suou yuki" | "yuki" | "nanapi":
            character = "startrail"
        # Boss nicknames
        case "machi":
            boss = "machiavelli"
        case "red liv":
            boss = "unknown data cluster"
        case "md" | "me" | "moon devourer":
            boss = "moon eater"
        case "dshark":
            boss = "dark shark"
        case "phantom tifa" | "tifa":
            boss = "iron maiden: phantom"
        case "tb" | "rm" | "radiant marcher":
            boss = "trailblazer"
        case "poria":
            boss = "fushen"

        case _:
            character = ""

    if match_type == "character":
        return character
    elif match_type == "boss":
        return boss