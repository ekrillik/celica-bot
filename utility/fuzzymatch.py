import json
import random

from thefuzz import fuzz
from thefuzz import process

def fuzzmatch(string) -> str:
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
        case "sophia" | "s*phia" | "silverfang":
            character = "silverfang"
        case "arclight":
            character = "arclight"
        case "plume" | "ploom":
            character = "plume"
        case "rozen":
            character = "rozen"
        case "camu" | "crocotta":
            character = "crocotta"
        case "rosetta" | "juan" | "rigor" | "rose":
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
        case "hypnos" | "sleepyboi" | "sleepyhead" | "sleepyboy" | "time to sleep" | "sleepytime":
            character = "hypnos"
        case "tempest" | "shitlena" | "iris":
            character = "tempest"
        case "glory":
            character = "glory"
        case "xxi" | "21" | "crazy kid":
            character = "xxi"
        case "garnet" | "flare" | "dog owner" | "yinlin":
            character = "garnet"
        case "flambeau" | "roland" | "kuraimakusu" | "clown" | "theatre" | "curtain call":
            character = "flambeau"
        case "empy" | "solaeter" | "empyrea" | "flashbang" | "sol" | "angel":
            character = "empyrea"
        case "capriccio" | "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq" | "red soup" | "grimace shake" | "irisv2":
            character = "capriccio"
        case "dragontoll" | "pulao" | "windbell's girl":
            character = "dragontoll"
        case "starfarer" | "nanamech" | "nanamecha" | "sagemachina" | "mech":
            character = "starfarer"
        case "starveil" | "haicma" | "hag" | "haicmama" | "nanny" | "mama":
            character = "starveil"
        case "scire" | "daren" | "bonka" | "tsundere" | "radiant daybreak" | "bunny" | "bnnuy" | "scire" | "best girl" | "bestgirl" | "flat tsundere is not waifu" | "trs" | "idol":
            character = "scire"
        case "arca" | "noan" | "deadweight" | "shrek" | "nero":
            character = "arca"
        case "balter" | "stigmata" | "mommy" | "saber" | "excalibaa" | "Balter" | "gothic nun" | "balt":
            character = "stigmata"
        case "vitrum" | "bambinata" | "bambi" | "bombi" | "doll" | "puppet" | "dementia doll":
            character = "vitrum"
        case "supercar" | "car" | "hyper" | "hyperreal" | "xly" | "xiangli yao" | "hypertrash" | "hypermonke" | "hypercuck":
            character = "hyperreal"
        case "cow" | "kale" | "kaleido" | "rich painter"| "zhezhi":
            character = "kaleido"  
        case "crimson weave" | "weave" | "motivation" | "vergil's daughter" | "cw" | "blanc's curse" | "bury the light":
            character = "crimson weave"
        case "zitherwoe" | "zitherhoe":
            character = "zitherwoe"
        case "awoo" | "furry" | "feral" | "feral: 21" | "feral:21" | "best daughter" | "doggo" | "wolfie-chan":
            character = "feral"
        case "indomitus" | "noctis" | "blockhead":
            character = "indomitus"
        case "alisa" | "echo" | "arrest me pls":
            character = "echo"
        case "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia" | "mermaid" | "shawty":
            character = "lost lullaby"
        case "brs" | "brick rock shooter" | "edgy miku" | "black rock shooter":
            character = "brs"
        case "uncle" | "king engine" | "kingengine" | "wata" | "epitaph" | "heartbeat killer" | "old man" | "no longer fears death" | "big boss":
            character = "epitaph"
        case "shukra"| "qukra" | "queen" | "legs":
            character = "shukra"
        case "teddy" | "decryptor" | "smug" | "always beats karen" | "kusogaki":
            character = "decryptor"
        case "oblivion" | "void luna":
            character = "oblivion"
        case "bridget" | "ardeo" | "royal guard" | "dante":
            character = "ardeo"
        case "solacetune" | "yor" | "yor forger":
            character = "solacetune"
        case "lucid dreamer" | "lucid" | "ld":
            character = "lucid dreamer"
        case "pyroath" | "hyperdawn" | "pyro":
            character = "pyroath"
        case "fulgor" | "yata" | "tomboy" | "oraora":
            character = "fulgor"
        case "startrail" | "nanaknight" | "star rail" | "hsr" | "suou yuki" | "yuki" | "nanapi":
            character = "startrail"
        case _:
            character = ""

    return character