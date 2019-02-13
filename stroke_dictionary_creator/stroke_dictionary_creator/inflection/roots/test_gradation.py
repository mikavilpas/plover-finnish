import unittest
from ensure import ensure
from . import gradation as g

class TestGradation(unittest.TestCase):
    def test_gradate_joukahainen_refwords_and_gradition_classes(self):
        gradate = g.gradate_joukahainen

        ensure(gradate("botaanikko", "arvelu", "av1")).equals("botaaniko")

        # risti
        ensure(gradate("hantti", "risti", "av1")).equals("hanti")
        ensure(gradate("hauki", "risti", "av5")).equals("haui")

        # paperi
        ensure(gradate("lennokki", "paperi", "av1")).equals("lennoki")

        # lovi
        ensure(gradate("appi", "lovi", "av1")).equals("api")
        ensure(gradate("arki", "lovi", "av3")).equals("arji")
        ensure(gradate("hauki", "lovi", "av5")).equals("haui")

        # nalle
        ensure(gradate("nukke", "nalle", "av1")).equals("nuke")

        # kala
        ensure(gradate("haapa", "kala", "av1")).equals("haava")
        ensure(gradate("aika", "kala", "av3")).equals("aija")
        ensure(gradate("aika", "kala", "av3")).equals("aija")
        ensure(gradate("haka", "kala", "av5")).equals("haa")

        # koira
        ensure(gradate("kukka", "koira", "av1")).equals("kuka")
        ensure(gradate("kukka", "koira", "av1")).equals("kuka")
        ensure(gradate("märkä", "koira", "av5")).equals("märä")

        # asema
        ensure(gradate("emäntä", "asema", "av1")).equals("emännä")

        # karahka
        ensure(gradate("haarukka", "karahka", "av1")).equals("haaruka")

        # suurempi
        ensure(gradate("kauempi", "suurempi", "av1")).equals("kauemmi")

        # askel
        ensure(gradate("Etelämanner", "askel", "av2")).equals("Etelämanter")
        ensure(gradate("säen", "askel", "av6")).equals("säken")

        # sisar
        ensure(gradate("runotar", "sisar", "av2")).equals("runottar")
        ensure(gradate("ien", "sisar", "av6")).equals("iken")

        # uistin
        ensure(gradate("ahdin", "uistin", "av2")).equals("ahtin")
        ensure(gradate("poljin", "uistin", "av4")).equals("polkin")
        ensure(gradate("puin", "uistin", "av6")).equals("pukin")

        # onneton
        ensure(gradate("eittämätön", "onneton", "av2")).equals("eittämättön")

        # vieras
        ensure(gradate("allas", "vieras", "av2")).equals("altas")
        ensure(gradate("äes", "vieras", "av6")).equals("äkes")

        # iäkäs
        ensure(gradate("alokas", "iäkäs", "av2")).equals("alokkas")

        # hame
        ensure(gradate("eläke", "hame", "av2")).equals("eläkke")
        ensure(gradate("elje", "hame", "av4")).equals("elke")

        # aavistaa
        ensure(gradate("aallottaa", "aavistaa", "av1")).equals("aallotaa")

        # heittää
        ensure(gradate("vyöttää", "heittää", "av1")).equals("vyötää")

        # inttää
        ensure(gradate("itää", "inttää", "av1")).equals("idää")
        ensure(gradate("kolisuttaa", "inttää", "av1")).equals("kolisutaa")

        # sulaa
        ensure(gradate("haettaa", "sulaa", "av1")).equals("haetaa")
        ensure(gradate("purkaa", "sulaa", "av5")).equals("puraa")

        # hohtaa
        ensure(gradate("jäätää", "hohtaa", "av1")).equals("jäädää")

        # hujahtaa
        ensure(gradate("hujahtaa", "hujahtaa", "av1")).equals("hujahdaa")

        # kirjoittaa
        ensure(gradate("aidoittaa", "kirjoittaa", "av1")).equals("aidoitaa")

        # vuotaa
        ensure(gradate("suoltaa", "vuotaa", "av1")).equals("suollaa")

        # huutaa
        ensure(gradate("vääntää", "huutaa", "av1")).equals("väännää")

        # sukeltaa
        ensure(gradate("ahertaa", "sukeltaa", "av1")).equals("aherraa")

        # paleltaa
        ensure(gradate("uskaltaa", "paleltaa", "av1")).equals("uskallaa")

        # murtaa
        ensure(gradate("sortaa", "murtaa", "av1")).equals("sorraa")

        # juontaa
        ensure(gradate("juontaa", "juontaa", "av1")).equals("juonnaa")

        # pahentaa
        ensure(gradate("löysentää", "pahentaa", "av1")).equals("löysennää")

        # kaivaa
        ensure(gradate("varttaa", "kaivaa", "av1")).equals("vartaa")
        ensure(gradate("jakaa", "kaivaa", "av5")).equals("jaaa")

        # soutaa
        ensure(gradate("yltää", "soutaa", "av1")).equals("yllää")

        # laskea
        ensure(gradate("kyteä", "laskea", "av1")).equals("kydeä")
        ensure(gradate("nylkeä", "laskea", "av3")).equals("nyljeä")
        ensure(gradate("tukea", "laskea", "av5")).equals("tuea")

        # tuntea
        ensure(gradate("tuntea", "tuntea", "av1")).equals("tunnea")

        # lähteä
        ensure(gradate("lähteä", "lähteä", "av1")).equals("lähdeä")

        # sallia
        ensure(gradate("ahnehtia", "sallia", "av1")).equals("ahnehdia")
        ensure(gradate("hylkiä", "sallia", "av3")).equals("hyljiä")
        ensure(gradate("pyrkiä", "sallia", "av5")).equals("pyriä")

        # voida
        #
        # Not sure why this is marked as av2 when
        # https://en.wiktionary.org/wiki/hipel%C3%B6id%C3%A4 says it has no
        # gradation.
        ensure(gradate("hipelöidä", "voida", "av2")).equals("hipelöitä")

        # kanavoida
        ensure(gradate("debytoida", "kanavoida", "av2")).equals("debytoita")

        # nuolaista
        ensure(gradate("rangaista", "nuolaista", "av2")).equals("rankaista")

        # katsella
        ensure(gradate("herroitella", "katsella", "av2")).equals("herroittella")
        ensure(gradate("jaella", "katsella", "av6")).equals("jakella")

        # haravoida
        ensure(gradate("murkinoida", "haravoida", "av2")).equals("murkinoita")

        # aleta
        ensure(gradate("edetä", "aleta", "av2")).equals("etetä")
        ensure(gradate("huveta", "aleta", "av2")).equals("hupeta")
        ensure(gradate("iljetä", "aleta", "av4")).equals("ilketä")
        ensure(gradate("laueta", "aleta", "av6")).equals("lauketa")

        # haluta
        ensure(gradate("hellitä", "haluta", "av2")).equals("heltitä")

        # juoruta
        ensure(gradate("kavuta", "juoruta", "av2")).equals("kaputa")

        # salata
        ensure(gradate("donkata", "salata", "av2")).equals("donkkata")
        ensure(gradate("hyljätä", "salata", "av4")).equals("hylkätä")

        # katketa
        ensure(gradate("kammeta", "katketa", "av2")).equals("kampeta")
        ensure(gradate("teljetä", "katketa", "av4")).equals("telketä")
        ensure(gradate("aueta", "katketa", "av6")).equals("auketa")
        ensure(gradate("laueta", "katketa", "av6")).equals("lauketa")
        ensure(gradate("noeta", "katketa", "av6")).equals("noketa")
        ensure(gradate("oieta", "katketa", "av6")).equals("oiketa")
        ensure(gradate("pietä", "katketa", "av6")).equals("piketä")

        # kohota
        ensure(gradate("lingota", "kohota", "av2")).equals("linkota")


    # def test_gradate_joukahainen_av2(self):
    #     gradate = g.gradate_joukahainen_av2

    #     # ('b',  'bb'), # kind of like kotus B. (lobata -> lobbaan)
    #     ensure(gradate("lobata")).equals("lobbata")
    #     # ('g',  'gg'), # kind of like kotus B. (digata -> diggaan)
    #     ensure(gradate("digata")).equals("diggaan")
    #     # ('t',  'tt'), # kotus C
    #     ensure(gradate("aate")).equals("aatte")
    #     # ('p',  'pp'), # kotus B
    #     ensure(gradate("lape")).equals("lappe")
    #     # ('k',  'kk'), # kotus A
    #     ensure(gradate("aluke")).equals("alukke")
    #     # ('mm', 'mp'), # kotus H
    #     # ('v',  'p'),  # kotus E
    #     # ('nn', 'nt'), # kotus J
    #     # ('ll', 'lt'), # kotus I
    #     # ('rr', 'rt'), # kotus K
    #     # ('d',  't'),  # kotus F
    #     # ('ng', 'nk'), # kotus G
    #     pass

    def test_gradate_joukahainen_av6(self):
        # TODO: go over tricky cases here.

        ensure(gradate("selitä", "haluta", "av6")).equals("selkikä") # selitä-selkiän
        ensure(gradate("keritä", "haluta", "av6")).equals("kerkitä") # keritä-kerkiän
        ensure(gradate("siitä", "haluta", "av6")).equals("heltitä")  # siitä-sikiän

        ensure(gradate("hylätä", "salata", "av6")).equals("hylkätä")
        ensure(gradate("haleta", "katketa", "av6")).equals("halketa")
        ensure(gradate("juleta", "katketa", "av6")).equals("julketa")
        ensure(gradate("keretä", "katketa", "av6")).equals("kerketä")
        ensure(gradate("virota", "kohota", "av6")).equals("virkota")

        ensure(gradate("pyyhin", "uistin", "av6")).equals("pyyhkin")

        raise Exception("not done")
