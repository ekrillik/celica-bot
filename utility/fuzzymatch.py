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
            character = "daybreak"
            # characters = ["decryptor", "oblivion"]
            # index = random.randint(0, len(characters) - 1)
            # character = characters[index]
        case "best girl" | "bestgirl":
            characters = ["eclipse", "lux", "luminance", "empyrea"]
            index = random.randint(0, 3)
            character = characters[index]
            print(character)
        case "alternate wife":
            characters = ["tempest", "capriccio", "pianissimo"]
            index = random.randint(0, 2)
            character = characters[index]
            print(character)
        case "lost content":
            characters = ["2b", "9s", "a2", "brs", "dante", "vergil"]
            index = random.randint(0, len(characters) - 1)
            character = characters[index]
        case "lotus" | "lucia lotus":
            character = "lotus"
        case "eclipse" | "liv eclipse" | "小姐" | "livblush":
            character = "eclipse"
        case "storm" | "nanami storm":
            character = "storm"
        case "dawn" | "dumbdawn" | "lucia dawn":
            character = "dawn"
        case "evil liv" | "green jumper" | "<:evilliv:1272415890453041223>" | "lux" | "liv lux":
            character = "lux"
        case "palefire" | "firegod" | "lee palefire":
            character = "palefire"
        case "nightblade" | "watanabe nightblade":
            character = "nightblade"
        case "zero" | "bianca zero":
            character = "zero"
        case "blast" | "karenina blast":
            character = "blast"
        case "lumi" | "luminance" | "liv luminance":
            character = "luminance"
        case "entropy" | "entrobrick" | "entropiss" | "entrokek" | "lee entropy":
            character = "entropy"
        case "ember" | "cheese's wife" | "karenina ember":
            character = "ember"
        case "pulse" | "nanami pulse":
            character = "pulse"
        case "tenebrion" | "teneb" | "terb" | "kamui tenebrion":
            character = "tenebrion"
        case "crimson abyss" | "abyss" | "crimson brick" | "ca" | "CA" | "blue rose" | "lucia crimson abyss" | "piero's wife":
            character = "crimson abyss"
        case "bastion" | "kimochiyokatta" | "kimochi yokatta" | "kamui bastion":
            character = "bastion"
        case "astral" | "asstral" | "watanabe astral":
            character = "astral"
        case "brilliance" | "ayla brilliance":
            character = "brilliance"
        case "veritas" | "veritrash" | "bianca veritas":
            character = "veritas"
        case "sophia" | "s*phia" | "silverfang" | "ireng" | "sophia silverfang":
            character = "silverfang"
        case "arclight" | "chrome arclight":
            character = "arclight"
        case "plume" | "ploom" | "lucia plume":
            character = "plume"
        case "rozen" | "vera rozen":
            character = "rozen"
        case "camu" | "crocotta" | "camu crocotta":
            character = "crocotta"
        case "rosetta" | "juan" | "rigor" | "rose" | "kuda" | "kuda lumping" | "rosetta rigor" | "choto's horsewife":
            character = "rigor"
            boss = "rosetta"
        case "changyu" | "changwho" | "qilin" | "who?" | "changyu qilin":
            character = "qilin"
        case "pavo" | "qu pavo":
            character = "pavo"
        case "laurel" | "dark luna" | "cutie pie" | "luna laurel":
            character = "laurel"
        case "2b":
            character = "2b"
        case "9s":
            character = "9s"
        case "a2":
            character = "a2"
        case "wanshi hypnos" | "hypnos" | "sleepyboi" | "sleepyhead" | "sleepyboy" | "time to sleep" | "sleepytime":
            character = "hypnos"
        case "selena tempest" |"tempest" | "shitlena" | "iris" | "living corpse":
            character = "tempest"
        case "chrome glory" | "glory"| "daddy" | "cer's glory hole":
            character = "glory"
        case "no21 xxi" | "no. 21 xxi" | "no 21 xxi" |  "xxi" | "21" | "crazy kid":
            character = "xxi"
        case "vera garnet" | "garnet" | "flare" | "dog owner" | "yinlin" | "zex's master":
            character = "garnet"
        case "roland flamebeau" | "flambeau" | "roland" | "kuraimakusu" | "clown" | "theatre" | "curtain call" | "badut":
            character = "flambeau"
        case "liv empyrea" | "empy" | "solaeter" | "empyrea" | "flashbang" | "sol" | "angel" | "liv's gingerbread":
            character = "empyrea"
        case "selena capriccio" | "capriccio" | "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq" | "red soup" | "grimace shake" | "irisv2" | "magikarp" | "kuyang" | "capybara" | "selena hallucinations" | "hallucinations":
            character = "capriccio"
        case "pulao dragontoll" | "dragontoll" | "pulao" | "windbell's girl" | "windbell's wife":
            character = "dragontoll"
        case "nanami starfarer" | "starfarer" | "nanamech" | "nanamecha" | "sagemachina" | "mech":
            character = "starfarer"
        case "haicma starveil" | "starveil" | "haicma" | "hag" | "haicmama" | "nanny" | "mama":
            character = "starveil"
        case "karenina scire" | "scire" | "daren" | "bonka" | "tsundere" | "radiant daybreak" | "bunny" | "bnnuy" | "scire" | "flat tsundere is not waifu" | "trs" | "idol" | "yoyo" | "trs's wife":
            character = "scire"
        case "noan arca" | "arca" | "noan" | "deadweight" | "shrek" | "nero":
            character = "arca"
        case "bianca stigmata" | "balter" | "stigmata" | "mommy" | "saber" | "excalibaa" | "Balter" | "gothic nun" | "balt" | "mint's pillow":
            character = "stigmata"
        case "bambinata vitrum" | "vitrum" | "bambinata" | "bambi" | "bombi" | "doll" | "puppet" | "dementia doll" | "swich's wife":
            character = "vitrum"
        case "lee hyperreal"| "supercar" | "car" | "hyper" | "hyperreal" | "xly" | "xiangli yao" | "hypertrash" | "hypermonke" | "hypercuck" | "zeru's sun" | "hyperbrick":
            character = "hyperreal"
        case "ayla kaleido" | "cow" | "kale" | "kaleido" | "rich painter"| "zhezhi" | "booba" | "the black mangaka":
            character = "kaleido"  
        case "lucia crimson weave" | "crimson weave" | "weave" | "cw" | "blanc's curse" | "matt's girl" | "ojek" | "kang ojek" | "aloha" | "sayonara" | "creamson weeb" | "tsubrickie" | "tsubricki":
            character = "crimson weave"
        case "hanying zitherwoe" | "zitherwoe" | "zitherhoe":
            character = "zitherwoe"
        case "no21 feral" | "no. 21 feral" | "no 21 feral" | "21 feral" | "awoo" | "furry" | "feral" | "feral: 21" | "feral:21" | "best daughter" | "doggo" | "wolfie-chan" | "fluffy" | "aether's daughter":
            character = "feral"
        case "noctis indomitus" | "indomitus" | "noctis" | "blockhead":
            character = "indomitus"
        case "alisa echo" | "alisa" | "echo" | "arrest me pls" | "altr's secretary":
            character = "echo"
        case "lamia lost lullaby" | "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia" | "mermaid" | "shawty" | "kev's waifu" | "skibidi" | "skibidi toilet"|"sewage" |"sushi on seaweed" | "disapproved by uncle roger" | "haiyaa the fish so raw":
            character = "lost lullaby"
            boss = "lamia"
        case "brs" | "brick rock shooter" | "edgy miku" | "black rock shooter":
            character = "brs"
        case "watanabe epitaph" | "uncle" | "king engine" | "kingengine" | "wata" | "epitaph" | "heartbeat killer" | "old man" | "no longer fears death" | "big boss" | "green guy" | "boomer" | "epipen":
            character = "epitaph"
        case "qu shukra" |"shukra"| "qukra" | "queen" | "legs":
            character = "shukra"
        case "teddy decryptor" | "teddy" | "decryptor" | "smug" | "always beats karen" | "kusogaki" | "brat":
            character = "decryptor"
        case "luna oblivion"| "oblivion" | "void luna" | "xeno's queen":
            character = "oblivion"
        case "bridget ardeo" | "bridget" | "ardeo" | "royal guard":
            character = "ardeo"
        case "hanying solacetune" | "solacetune" | "yor" | "yor forger" | "ponzu's milkers":
            character = "solacetune"
        case "wanshi lucid dreamer" | "lucid dreamer" | "lucid" | "ld" | "ocelot" | "aurora's wife":
            character = "lucid dreamer"
        case "lucia pyroath" | "pyroath" | "hyperdawn" | "pyro" | "newlywed":
            character = "pyroath"
        case "yata fulgor" | "fulgor" | "yata" | "tomboy" | "oraora" | "knockmeout":
            character = "fulgor"
        case "nanami startrail" | "startrail" | "nanaknight" | "star rail" | "hsr" | "suou yuki" | "yuki" | "nanapi" | "fox's knight":
            character = "startrail"
        case "ishmael parhelion" | "ishmael" | "parhelion" | "ish" | "changli" | "mother" | "most powerful alien":
            character = "parhelion"
        case "lilith daemonissa" | "lilith" | "daemonissa" | "maso" | "masochist" | "umbrella":
            character = "daemonissa"
        case "selena pianissimo" | "pianissimo" | "elis" | "ntr musician" | "piano":
            character = "pianissimo"
        case "jetavie daybreak" | "daybreak" | "jetavie" | "omgkawaiiangel-chan" | "vtuber" | "gyaru" | "shi-yori's wife":
            character = "daybreak"
        case "vera geiravor" | "geiravor" | "valkyrie" | "valk" | "gardevoir":
            character = "geiravor"
        case "dante" | "donut" | "dunce":
            character = "dante"
        case "vergil" | "veggie" | "virgin" | "sparda's virgin":
            character = "vergil"
        case "tololo":
            character = "tololo"
        case "walter" | "Cryo's wife" | "lily" :
            character = "crepuscule"
        # Boss nicknames
        case "mado":
            boss = "madorea"
        case "moth":
            boss = "pterygota queen"
        case "musashi":
            boss = "musashi ix"
        case "baby shark":
            boss = "shark-speare"
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
        case "emp":
            boss = "emperor"
        case "primal projection" | "projection" | "ishmael":
            boss = "projection"

        case _:
            character = ""

    if match_type == "character":
        return character
    elif match_type == "boss":
        return boss