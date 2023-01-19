# Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code
# representation as a new string and find the number of characters of the new encoded representation, including the
# surrounding double quotes.
#
# For example:
#
# "" encodes to "\"\"", an increase from 2 characters to 6.
# "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
# "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
# "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
# Your task is to find the total number of characters to represent the newly encoded strings minus the number of
# characters of code in each original string literal. For example, for the strings above, the total encoded length
# (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part
# of this puzzle) is 42 - 23 = 19.

print((len(r'"qxfcsmh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ffsfyxbyuhqkpwatkjgudo"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"byc\x9dyxuafof\\\xa6uf\\axfozomj\\olh\x6a"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jtqvz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"uzezxa\"jgbmojtwyfbfguz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vqsremfk\x8fxiknektafj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wzntebpxnnt\"vqndz\"i\x47vvjqo\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"higvez\"k\"riewqk"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dlkrbhbrlfrp\\damiauyucwhty"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"d\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qlz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ku"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yy\"\"uoao\"uripabop"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"saduyrntuswlnlkuppdro\\sicxosted"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zzphopswlwdhebwkxeurvizdv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xfoheirjoakrpofles\"nfu"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"q\xb7oh\"p\xce\"n"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qeendp\"ercwgywdjeylxcv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dcmem"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"i\x13r\"l"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ikso\xdcbvqnbrjduh\"uqudzki\xderwk"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wfdsn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pwynglklryhtsqbno"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"hcoj\x63iccz\"v\"ttr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zf\x23\\hlj\\kkce\\d\\asy\"yyfestwcdxyfj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xs"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"m\"tvltapxdvtrxiy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bmud"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"k\"a"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"b\"oas"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"yexnjjupoqsxyqnquy\"uzfdvetqrc"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vdw\xe3olxfgujaj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qomcxdnd\"\\cfoe\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"fpul"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"m\"avamefphkpv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vvdnb\\x\\uhnxfw\"dpubfkxfmeuhnxisd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"hey\\"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ldaeigghlfey"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"eure\"hoy\xa5iezjp\\tm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yygb\"twbj\\r\"\x10gmxuhmp\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"weirebp\x39mqonbtmfmd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ltuz\\hs\"e"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ysvmpc"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"g\x8amjtt\"megl\"omsaihifwa"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yimmm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"iiyqfalh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"cwknlaaf"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"q\x37feg\xc6s\"xx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"uayrgeurgyp\\oi"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xhug\"pt\"axugllbdiggzhvy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"kdaarqmsjfx\xc3d"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"vkwla"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"d\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tmroz\"bvfinxoe\\mum\"wmm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"n\"bbswxne\\p\\yr\"qhwpdd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"skzlkietklkqovjhvj\xfe"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pbg\\pab\"bubqaf\"obzcwxwywbs\\dhtq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xxjidvqh\"lx\\wu\"ij"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"daef\x5fe\x5b\\kbeeb\x13qnydtboof"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ogvazaqy\"j\x73"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"y"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"n\"tibetedldy\\gsamm\"nwu"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wldkvgdtqulwkad"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dpmxnj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"twybw\"cdvf\"mjdajurokbce"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ru\"\\lasij\"i"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"roc\\vra\\lhrm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pbkt\x60booz\"fjlkc"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"j\x4dytvjwrzt"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\uiwjkniumxcs"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"cbhm\"nexccior\"v\"j\"nazxilmfp\x47"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qdxngevzrlgoq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"lrzxftytpobsdfyrtdqpjbpuwmm\x9e"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mdag\x0asnck\xc2ggj\"slb\"fjy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wyqkhjuazdtcgkcxvjkpnjdae"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"aixfk\xc0iom\x21vueob"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dkiiakyjpkffqlluhaetires"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ysspv\"lysgkvnmwbbsy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gy\"ryexcjjxdm\"xswssgtr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"s"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ddxv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qwt\"\x27puilb\"pslmbrsxhrz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qdg\xc9e\\qwtknlvkol\x54oqvmchn\\"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lvo"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"b"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"fk\"aa\"\"yenwch\\\\on"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"srig\x63hpwaavs\\\x80qzk\"xa\"\xe6u\\wr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yxjxuj\"ghyhhxfj\"\xa6qvatre"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yoktqxjxkzrklkoeroil"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"jfmik\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"smgseztzdwldikbqrh\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jftahgctf\"hoqy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tcnhicr\"znpgckt\"ble"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vqktnkodh\"lo\"a\\bkmdjqqnsqr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ztnirfzqq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"s"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"iqj\"y\\hqgzflwrdsusasekyrxbp\\ad"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\xzjhlaiynkioz\"\"bxepzimvgwt"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"s\x36rbw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mniieztwrisvdx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"atyfxioy\x2b\\"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"irde\x85\x5cvbah\\jekw\"ia"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bdmftlhkwrprmpat\"prfaocvp"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"w\\k"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"umbpausy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zfauhpsangy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"p\"zqyw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wtztypyqvnnxzvlvipnq\"zu"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"deicgwq\\oqvajpbov\\or\"kgplwu"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mbzlfgpi\\\\zqcidjpzqdzxityxa"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lfkxvhma"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\xf2yduqzqr\"\\fak\"p\"n"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mpajacfuxotonpadvng"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"anb\\telzvcdu\\a\xf2flfq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lrs\"ebethwpmuuc\"\x86ygr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qmvdbhtumzc\"ci"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"meet"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yopg\x0fdxdq\"h\\ugsu\xffmolxjv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"uhy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"fzgidrtzycsireghazscvmwcfmw\\t"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"cqohkhpgvpru"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bihyigtnvmevx\"xx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zofomwotzuxsjk\"q\"mc\"js\"dnmalhxd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\ktnddux\\fqvt\"ibnjntjcbn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ia"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"htjadnefwetyp\xd5kbrwfycbyy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"\\hkuxqddnao"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"meqqsz\x83luecpgaem"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"cvks\x87frvxo\"svqivqsdpgwhukmju"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"sgmxiai\\o\"riufxwjfigr\xdf"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"fgywdfecqufccpcdn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"faghjoq\x28abxnpxj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zuppgzcfb\"dctvp\"elup\"zxkopx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xqs\x45xxdqcihbwghmzoa"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"anbnlp\\cgcvm\"hc"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xf\"fgrngwzys"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"nrxsjduedcy\x24"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x71sxl\"gj\"sds\"ulcruguz\\t\\ssvjcwhi"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jhj\"msch"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qpovolktfwyiuyicbfeeju\x01"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"nkyxmb\"qyqultgt\"nmvzvvnxnb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ycsrkbstgzqb\"uv\\cisn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"s"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ueptjnn\"\"sh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lp\"z\"d\"mxtxiy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yzjtvockdnvbubqabjourf\"k\"uoxwle"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x82\"wqm\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\xb5cwtuks\x5fpgh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tbvf"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ttbmzdgn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vfpiyfdejyrlbgcdtwzbnm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"uc"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"otdcmhpjagqix"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\\xb1qso\"s"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"scowax"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"behpstjdh\xccqlgnqjyz\"eesn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"r\xe1cbnjwzveoomkzlo\\kxlfouhm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jgrl"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"kzqs\\r"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ctscb\x7fthwkdyko\"\x62pkf\"d\xe6knmhurg"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tc\"kw\x3ftt"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bxb\x5ccl"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jyrmfbphsldwpq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jylpvysl\"\"juducjg"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"en\\m\"kxpq\"wpb\\\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"madouht\"bmdwvnyqvpnawiphgac\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vuxpk\"ltucrw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"aae\x60arr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ttitnne\"kilkrgssnr\xfdurzh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"oalw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pc\"\"gktkdykzbdpkwigucqni\"nxiqx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dbrsaj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bgzsowyxcbrvhtvekhsh\"qgd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"kudfemvk\"\"\"hkbrbil\"chkqoa"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zjzgj\\ekbhyfzufy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\acos\"fqekuxqzxbmkbnn\x1ejzwrm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"elxahvudn\"txtmomotgw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x2eoxmwdhelpr\"cgi\xf7pzvb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"eapheklx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"hfvma\"mietvc\"tszbbm\"czex"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"h\"iiockj\\\xc1et"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"d\"rmjjftm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qlvhdcbqtyrhlc\\"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yy\"rsucjtulm\"coryri\"eqjlbmk"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"r\"bfuht\\jjgujp\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"kukxvuauamtdosngdjlkauylttaokaj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"srgost\"\"rbkcqtlccu\x65ohjptstrjkzy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yxwxl\\yjilwwxffrjjuazmzjs"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dxlw\\fkstu\"hjrtiafhyuoh\"sewabne"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x88sj\"v"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"rfzprz\xec\"oxqclu\"krzefp\\q"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"cfmhdbjuhrcymgxpylllyvpni"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ucrmjvmimmcq\x88\xd9\"lz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lujtt\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gvbqoixn\"pmledpjmo\"flydnwkfxllf"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dvxqlbshhmelsk\x8big\"l"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mx\x54lma\x8bbguxejg"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x66jdati\xeceieo"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"iyyupixei\x54ff"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xohzf\"rbxsoksxamiu"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vlhthspeshzbppa\x4drhqnohjop\"\"mfjd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"f\"tvxxla\"vurian\"\"idjq\x3aptm\xc3olep"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gzqz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"kbq\\wogye\\altvi\\hbvmodny"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"j\xd8"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ofjozdhkblvndl"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"hbitoupimbawimxlxqze"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ypeleimnme"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xfwdrzsc\\oxqamawyizvi\\y"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"enoikppx\xa1ixe\"yo\"gumye"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"fb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vzf"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zxidr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"cu\x31beirsywtskq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lxpjbvqzztafwezd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\jyxeuo\x18bv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"b\"vawc\"p\\\\giern\"b"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"odizunx\"\"t\\yicdn\"x\"sdiz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"\"tebrtsi"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ctyzsxv\xa6pegfkwsi\"tgyltaakytccb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"htxwbofchvmzbppycccliyik\xe5a"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ggsslefamsklezqkrd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"rcep\"fnimwvvdx\"l"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zyrzlqmd\x12egvqs\\llqyie"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x07gsqyrr\\rcyhyspsvn"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"butg\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gywkoxf\"jsg\\wtopxvumirqxlwz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"rj\"ir\"wldwveair\x2es\"dhjrdehbqnzl"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ru\"elktnsbxufk\\ejufjfjlevt\\lrzd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"widsvok"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"oy\"\x81nuesvw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ay"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"syticfac\x1cfjsivwlmy\"pumsqlqqzx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"m"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"rjjkfh\x78cf\x2brgceg\"jmdyas\"\\xlv\xb6p"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tmuvo\"\x3ffdqdovjmdmkgpstotojkv\"as"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"jd\\ojvynhxllfzzxvbn\"wrpphcvx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"twr"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"n\\hdzmxe\"mzjjeadlz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"fb\"rprxuagvahjnri"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"rfmexmjjgh\\xrnmyvnatrvfruflaqjnd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"obbbde\"co\"qr\"qpiwjgqahqm\\jjp\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vpbq\"\"y\"czk\\b\x52ed\"lnzepobp"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"syzeajzfarplydipny\"y\"\xe8ad"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mpyodwb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x47rakphlqqptd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wa\"oj\"aiy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"a"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ropozx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"q\x51nbtlwa"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"etukvgx\\jqxlkq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"tp\"rah\"pg\"s\"bpdtes\\tkasdhqd"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"dn\"qqpkikadowssb\xcah\"dzpsf\\ect\"jdh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pxunovbbrrn\\vullyn\"bno\"\"\"myfxlp\""'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"qaixyazuryvkmoulhcqaotegfj\\mpzm"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bvfrbicutzbjwn\\oml\"cf\"d\"ezcpv\"j"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"rmbrdtneudemigdhelmb"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"aq\\aurmbhy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wujqvzw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gf\"tssmvm\"gm\"hu\x9a\xb7yjawsa"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"hrhqqxow\xe2gsydtdspcfqy\"zw\\ou"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ianwwf\\yko\\tdujhhqdi"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"xylz\"zpvpab"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lwuopbeeegp"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"aoop\x49jhhcexdmdtun"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\\\\mouqqcsgmz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"tltuvwhveau\x43b\"ymxjlcgiymcynwt"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"gsugerumpyuhtjljbhrdyoj"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"lnjm\xb8wg\"ajh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"zmspue\"nfttdon\\b\"eww"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\"w\x67jwaq\x7ernmyvs\\rmdsuwydsd\"th"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ogtgvtlmcvgllyv"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"z\"fqi\"rvddoehrciyl"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"yustxxtot\"muec\"xvfdbzunzvveq"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"mqslw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"txqnyvzmibqgjs\xb6xy\x86nfalfyx"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"kzhehlmkholov"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"plpmywcnirrjutjguosh\\"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"pydbnqofv\"dn\\m"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"aegqof"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"eambmxt\\dxagoogl\\zapfwwlmk"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"afbmqitxxqhddlozuxcpjxgh"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"vgts"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bfdpqtoxzzhmzcilehnflna"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"s\"idpz"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\xcfhgly\"nlmztwybx\"ecezmsxaqw"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"aackfgndqcqiy"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"\x22unqdlsrvgzfaohoffgxzfpir\"s"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"abh\"ydv\"kbpdhrerl"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"bdzpg"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"ekwgkywtmzp"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"wtoodejqmrrgslhvnk\"pi\"ldnogpth"'.replace('\\', '\\\\').replace('"', '\\"')) + 2 + len(r'"njro\x68qgbx\xe4af\"\\suan"'.replace('\\', '\\\\').replace('"', '\\"')) + 2) - ((len(r'"qxfcsmh"') + len(r'"ffsfyxbyuhqkpwatkjgudo"') + len(r'"byc\x9dyxuafof\\\xa6uf\\axfozomj\\olh\x6a"') + len(r'"jtqvz"') + len(r'"uzezxa\"jgbmojtwyfbfguz"') + len(r'"vqsremfk\x8fxiknektafj"') + len(r'"wzntebpxnnt\"vqndz\"i\x47vvjqo\""') + len(r'"higvez\"k\"riewqk"') + len(r'"dlkrbhbrlfrp\\damiauyucwhty"') + len(r'"d\""') + len(r'"qlz"') + len(r'"ku"') + len(r'"yy\"\"uoao\"uripabop"') + len(r'"saduyrntuswlnlkuppdro\\sicxosted"') + len(r'"tj"') + len(r'"zzphopswlwdhebwkxeurvizdv"') + len(r'"xfoheirjoakrpofles\"nfu"') + len(r'"q\xb7oh\"p\xce\"n"') + len(r'"qeendp\"ercwgywdjeylxcv"') + len(r'"dcmem"') + len(r'"\"i\x13r\"l"') + len(r'"ikso\xdcbvqnbrjduh\"uqudzki\xderwk"') + len(r'"wfdsn"') + len(r'"pwynglklryhtsqbno"') + len(r'"hcoj\x63iccz\"v\"ttr"') + len(r'"zf\x23\\hlj\\kkce\\d\\asy\"yyfestwcdxyfj"') + len(r'"xs"') + len(r'"m\"tvltapxdvtrxiy"') + len(r'"bmud"') + len(r'"k\"a"') + len(r'"b\"oas"') + len(r'"\"yexnjjupoqsxyqnquy\"uzfdvetqrc"') + len(r'"vdw\xe3olxfgujaj"') + len(r'"qomcxdnd\"\\cfoe\""') + len(r'"fpul"') + len(r'"m\"avamefphkpv"') + len(r'"vvdnb\\x\\uhnxfw\"dpubfkxfmeuhnxisd"') + len(r'"hey\\"') + len(r'"ldaeigghlfey"') + len(r'"eure\"hoy\xa5iezjp\\tm"') + len(r'"yygb\"twbj\\r\"\x10gmxuhmp\""') + len(r'"weirebp\x39mqonbtmfmd"') + len(r'"ltuz\\hs\"e"') + len(r'"ysvmpc"') + len(r'"g\x8amjtt\"megl\"omsaihifwa"') + len(r'"yimmm"') + len(r'"iiyqfalh"') + len(r'"cwknlaaf"') + len(r'"q\x37feg\xc6s\"xx"') + len(r'"uayrgeurgyp\\oi"') + len(r'"xhug\"pt\"axugllbdiggzhvy"') + len(r'"kdaarqmsjfx\xc3d"') + len(r'"\"vkwla"') + len(r'"d\""') + len(r'"tmroz\"bvfinxoe\\mum\"wmm"') + len(r'"\"n\"bbswxne\\p\\yr\"qhwpdd"') + len(r'"skzlkietklkqovjhvj\xfe"') + len(r'"pbg\\pab\"bubqaf\"obzcwxwywbs\\dhtq"') + len(r'"xxjidvqh\"lx\\wu\"ij"') + len(r'"daef\x5fe\x5b\\kbeeb\x13qnydtboof"') + len(r'"ogvazaqy\"j\x73"') + len(r'"y"') + len(r'"n\"tibetedldy\\gsamm\"nwu"') + len(r'"wldkvgdtqulwkad"') + len(r'"dpmxnj"') + len(r'"twybw\"cdvf\"mjdajurokbce"') + len(r'"ru\"\\lasij\"i"') + len(r'"roc\\vra\\lhrm"') + len(r'"pbkt\x60booz\"fjlkc"') + len(r'"j\x4dytvjwrzt"') + len(r'"\\uiwjkniumxcs"') + len(r'"cbhm\"nexccior\"v\"j\"nazxilmfp\x47"') + len(r'"qdxngevzrlgoq"') + len(r'"\"lrzxftytpobsdfyrtdqpjbpuwmm\x9e"') + len(r'"mdag\x0asnck\xc2ggj\"slb\"fjy"') + len(r'"wyqkhjuazdtcgkcxvjkpnjdae"') + len(r'"aixfk\xc0iom\x21vueob"') + len(r'"dkiiakyjpkffqlluhaetires"') + len(r'"ysspv\"lysgkvnmwbbsy"') + len(r'"gy\"ryexcjjxdm\"xswssgtr"') + len(r'"s"') + len(r'"ddxv"') + len(r'"qwt\"\x27puilb\"pslmbrsxhrz"') + len(r'"qdg\xc9e\\qwtknlvkol\x54oqvmchn\\"') + len(r'"lvo"') + len(r'"b"') + len(r'"fk\"aa\"\"yenwch\\\\on"') + len(r'"srig\x63hpwaavs\\\x80qzk\"xa\"\xe6u\\wr"') + len(r'"yxjxuj\"ghyhhxfj\"\xa6qvatre"') + len(r'"yoktqxjxkzrklkoeroil"') + len(r'"\"jfmik\""') + len(r'"smgseztzdwldikbqrh\""') + len(r'"jftahgctf\"hoqy"') + len(r'"tcnhicr\"znpgckt\"ble"') + len(r'"vqktnkodh\"lo\"a\\bkmdjqqnsqr"') + len(r'"ztnirfzqq"') + len(r'"s"') + len(r'"xx"') + len(r'"iqj\"y\\hqgzflwrdsusasekyrxbp\\ad"') + len(r'"\\xzjhlaiynkioz\"\"bxepzimvgwt"') + len(r'"s\x36rbw"') + len(r'"mniieztwrisvdx"') + len(r'"atyfxioy\x2b\\"') + len(r'"irde\x85\x5cvbah\\jekw\"ia"') + len(r'"bdmftlhkwrprmpat\"prfaocvp"') + len(r'"w\\k"') + len(r'"umbpausy"') + len(r'"zfauhpsangy"') + len(r'"p\"zqyw"') + len(r'"wtztypyqvnnxzvlvipnq\"zu"') + len(r'"deicgwq\\oqvajpbov\\or\"kgplwu"') + len(r'"mbzlfgpi\\\\zqcidjpzqdzxityxa"') + len(r'"lfkxvhma"') + len(r'"\xf2yduqzqr\"\\fak\"p\"n"') + len(r'"mpajacfuxotonpadvng"') + len(r'"anb\\telzvcdu\\a\xf2flfq"') + len(r'"lrs\"ebethwpmuuc\"\x86ygr"') + len(r'"qmvdbhtumzc\"ci"') + len(r'"meet"') + len(r'"yopg\x0fdxdq\"h\\ugsu\xffmolxjv"') + len(r'"uhy"') + len(r'"fzgidrtzycsireghazscvmwcfmw\\t"') + len(r'"cqohkhpgvpru"') + len(r'"bihyigtnvmevx\"xx"') + len(r'"xz"') + len(r'"zofomwotzuxsjk\"q\"mc\"js\"dnmalhxd"') + len(r'"\\ktnddux\\fqvt\"ibnjntjcbn"') + len(r'"ia"') + len(r'"htjadnefwetyp\xd5kbrwfycbyy"') + len(r'"\"\\hkuxqddnao"') + len(r'"meqqsz\x83luecpgaem"') + len(r'"cvks\x87frvxo\"svqivqsdpgwhukmju"') + len(r'"sgmxiai\\o\"riufxwjfigr\xdf"') + len(r'"fgywdfecqufccpcdn"') + len(r'"faghjoq\x28abxnpxj"') + len(r'"zuppgzcfb\"dctvp\"elup\"zxkopx"') + len(r'"xqs\x45xxdqcihbwghmzoa"') + len(r'"anbnlp\\cgcvm\"hc"') + len(r'"xf\"fgrngwzys"') + len(r'"nrxsjduedcy\x24"') + len(r'"\x71sxl\"gj\"sds\"ulcruguz\\t\\ssvjcwhi"') + len(r'"jhj\"msch"') + len(r'"qpovolktfwyiuyicbfeeju\x01"') + len(r'"nkyxmb\"qyqultgt\"nmvzvvnxnb"') + len(r'"ycsrkbstgzqb\"uv\\cisn"') + len(r'"s"') + len(r'"ueptjnn\"\"sh"') + len(r'"lp\"z\"d\"mxtxiy"') + len(r'"yzjtvockdnvbubqabjourf\"k\"uoxwle"') + len(r'"\x82\"wqm\""') + len(r'"\xb5cwtuks\x5fpgh"') + len(r'"wd"') + len(r'"tbvf"') + len(r'"ttbmzdgn"') + len(r'"vfpiyfdejyrlbgcdtwzbnm"') + len(r'"uc"') + len(r'"otdcmhpjagqix"') + len(r'"\\\xb1qso\"s"') + len(r'"scowax"') + len(r'"behpstjdh\xccqlgnqjyz\"eesn"') + len(r'"r\xe1cbnjwzveoomkzlo\\kxlfouhm"') + len(r'"jgrl"') + len(r'"kzqs\\r"') + len(r'"ctscb\x7fthwkdyko\"\x62pkf\"d\xe6knmhurg"') + len(r'"tc\"kw\x3ftt"') + len(r'"bxb\x5ccl"') + len(r'"jyrmfbphsldwpq"') + len(r'"jylpvysl\"\"juducjg"') + len(r'"en\\m\"kxpq\"wpb\\\""') + len(r'"madouht\"bmdwvnyqvpnawiphgac\""') + len(r'"vuxpk\"ltucrw"') + len(r'"aae\x60arr"') + len(r'"ttitnne\"kilkrgssnr\xfdurzh"') + len(r'"oalw"') + len(r'"pc\"\"gktkdykzbdpkwigucqni\"nxiqx"') + len(r'"dbrsaj"') + len(r'"bgzsowyxcbrvhtvekhsh\"qgd"') + len(r'"kudfemvk\"\"\"hkbrbil\"chkqoa"') + len(r'"zjzgj\\ekbhyfzufy"') + len(r'"\\acos\"fqekuxqzxbmkbnn\x1ejzwrm"') + len(r'"elxahvudn\"txtmomotgw"') + len(r'"\x2eoxmwdhelpr\"cgi\xf7pzvb"') + len(r'"eapheklx"') + len(r'"hfvma\"mietvc\"tszbbm\"czex"') + len(r'"h\"iiockj\\\xc1et"') + len(r'"d\"rmjjftm"') + len(r'"qlvhdcbqtyrhlc\\"') + len(r'"yy\"rsucjtulm\"coryri\"eqjlbmk"') + len(r'"tv"') + len(r'"r\"bfuht\\jjgujp\""') + len(r'"kukxvuauamtdosngdjlkauylttaokaj"') + len(r'"srgost\"\"rbkcqtlccu\x65ohjptstrjkzy"') + len(r'"yxwxl\\yjilwwxffrjjuazmzjs"') + len(r'"dxlw\\fkstu\"hjrtiafhyuoh\"sewabne"') + len(r'"\x88sj\"v"') + len(r'"rfzprz\xec\"oxqclu\"krzefp\\q"') + len(r'"cfmhdbjuhrcymgxpylllyvpni"') + len(r'"ucrmjvmimmcq\x88\xd9\"lz"') + len(r'"lujtt\""') + len(r'"gvbqoixn\"pmledpjmo\"flydnwkfxllf"') + len(r'"dvxqlbshhmelsk\x8big\"l"') + len(r'"mx\x54lma\x8bbguxejg"') + len(r'"\x66jdati\xeceieo"') + len(r'"\"iyyupixei\x54ff"') + len(r'"xohzf\"rbxsoksxamiu"') + len(r'"vlhthspeshzbppa\x4drhqnohjop\"\"mfjd"') + len(r'"f\"tvxxla\"vurian\"\"idjq\x3aptm\xc3olep"') + len(r'"gzqz"') + len(r'"kbq\\wogye\\altvi\\hbvmodny"') + len(r'"j\xd8"') + len(r'"ofjozdhkblvndl"') + len(r'"hbitoupimbawimxlxqze"') + len(r'"ypeleimnme"') + len(r'"xfwdrzsc\\oxqamawyizvi\\y"') + len(r'"enoikppx\xa1ixe\"yo\"gumye"') + len(r'"fb"') + len(r'"vzf"') + len(r'"zxidr"') + len(r'"cu\x31beirsywtskq"') + len(r'"lxpjbvqzztafwezd"') + len(r'"\\jyxeuo\x18bv"') + len(r'"b\"vawc\"p\\\\giern\"b"') + len(r'"odizunx\"\"t\\yicdn\"x\"sdiz"') + len(r'"\"\"tebrtsi"') + len(r'"ctyzsxv\xa6pegfkwsi\"tgyltaakytccb"') + len(r'"htxwbofchvmzbppycccliyik\xe5a"') + len(r'"ggsslefamsklezqkrd"') + len(r'"rcep\"fnimwvvdx\"l"') + len(r'"zyrzlqmd\x12egvqs\\llqyie"') + len(r'"\x07gsqyrr\\rcyhyspsvn"') + len(r'"butg\""') + len(r'"gb"') + len(r'"gywkoxf\"jsg\\wtopxvumirqxlwz"') + len(r'"rj\"ir\"wldwveair\x2es\"dhjrdehbqnzl"') + len(r'"ru\"elktnsbxufk\\ejufjfjlevt\\lrzd"') + len(r'"\"widsvok"') + len(r'"oy\"\x81nuesvw"') + len(r'"ay"') + len(r'"syticfac\x1cfjsivwlmy\"pumsqlqqzx"') + len(r'"m"') + len(r'"rjjkfh\x78cf\x2brgceg\"jmdyas\"\\xlv\xb6p"') + len(r'"tmuvo\"\x3ffdqdovjmdmkgpstotojkv\"as"') + len(r'"jd\\ojvynhxllfzzxvbn\"wrpphcvx"') + len(r'"pz"') + len(r'"\"twr"') + len(r'"n\\hdzmxe\"mzjjeadlz"') + len(r'"fb\"rprxuagvahjnri"') + len(r'"rfmexmjjgh\\xrnmyvnatrvfruflaqjnd"') + len(r'"obbbde\"co\"qr\"qpiwjgqahqm\\jjp\""') + len(r'"vpbq\"\"y\"czk\\b\x52ed\"lnzepobp"') + len(r'"syzeajzfarplydipny\"y\"\xe8ad"') + len(r'"mpyodwb"') + len(r'"\x47rakphlqqptd"') + len(r'"wa\"oj\"aiy"') + len(r'"a"') + len(r'"ropozx"') + len(r'"q\x51nbtlwa"') + len(r'"etukvgx\\jqxlkq"') + len(r'"\"tp\"rah\"pg\"s\"bpdtes\\tkasdhqd"') + len(r'"dn\"qqpkikadowssb\xcah\"dzpsf\\ect\"jdh"') + len(r'"pxunovbbrrn\\vullyn\"bno\"\"\"myfxlp\""') + len(r'"qaixyazuryvkmoulhcqaotegfj\\mpzm"') + len(r'"bvfrbicutzbjwn\\oml\"cf\"d\"ezcpv\"j"') + len(r'"rmbrdtneudemigdhelmb"') + len(r'"aq\\aurmbhy"') + len(r'"wujqvzw"') + len(r'"gf\"tssmvm\"gm\"hu\x9a\xb7yjawsa"') + len(r'"hrhqqxow\xe2gsydtdspcfqy\"zw\\ou"') + len(r'"ianwwf\\yko\\tdujhhqdi"') + len(r'"xylz\"zpvpab"') + len(r'"lwuopbeeegp"') + len(r'"aoop\x49jhhcexdmdtun"') + len(r'"\\\\mouqqcsgmz"') + len(r'"tltuvwhveau\x43b\"ymxjlcgiymcynwt"') + len(r'"gsugerumpyuhtjljbhrdyoj"') + len(r'"lnjm\xb8wg\"ajh"') + len(r'"zmspue\"nfttdon\\b\"eww"') + len(r'"\"w\x67jwaq\x7ernmyvs\\rmdsuwydsd\"th"') + len(r'"ogtgvtlmcvgllyv"') + len(r'"z\"fqi\"rvddoehrciyl"') + len(r'"yustxxtot\"muec\"xvfdbzunzvveq"') + len(r'"mqslw"') + len(r'"txqnyvzmibqgjs\xb6xy\x86nfalfyx"') + len(r'"kzhehlmkholov"') + len(r'"plpmywcnirrjutjguosh\\"') + len(r'"pydbnqofv\"dn\\m"') + len(r'"aegqof"') + len(r'"eambmxt\\dxagoogl\\zapfwwlmk"') + len(r'"afbmqitxxqhddlozuxcpjxgh"') + len(r'"vgts"') + len(r'"bfdpqtoxzzhmzcilehnflna"') + len(r'"s\"idpz"') + len(r'"\xcfhgly\"nlmztwybx\"ecezmsxaqw"') + len(r'"aackfgndqcqiy"') + len(r'"\x22unqdlsrvgzfaohoffgxzfpir\"s"') + len(r'"abh\"ydv\"kbpdhrerl"') + len(r'"bdzpg"') + len(r'"ekwgkywtmzp"') + len(r'"wtoodejqmrrgslhvnk\"pi\"ldnogpth"') + len(r'"njro\x68qgbx\xe4af\"\\suan"'))))  # well, that's one-liner
