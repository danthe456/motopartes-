"""Lista canónica de motos y alias (borrador). Edita este archivo para corregir.
Cada moto: (id, marca, modelo, cc, familia_motor, [alias]). Alias en texto simple; 're:' = regex.
"""
M = []
def m(id, marca, modelo, cc, fam, *alias): M.append((id, marca, modelo, cc, fam, list(alias)))

# ---- AKT / AYCO (familias por cilindraje) ----
m('akt-ak110','AKT','AK110',110,'AKT-110','AK110','AK 110','AKT110','AK100','AY90','AY110','AX4','AX 4')
m('akt-flex125','AKT','Flex 125',125,'AKT-125','FLEX','AKT125FLEX')
m('akt-tt125','AKT','TT 125',125,'AKT-125','AK125TT','AKT125TT','TT125','AK 125 TT','AK125 SPORT','AK125SPORT')
m('akt-evo125','AKT','EVO 125',125,'AKT-125','EVO125','AK125EVO','AK 125 EVO','EVO')
m('akt-nkd125','AKT','NKD 125',125,'AKT-125','NKD','NAKED','AK125NKD')
m('akt-sl125','AKT','SL 125',125,'AKT-125','SL125','AKT SL','re:\\bSL\\b')
m('akt-ttr125','AKT','TTR 125',125,'AKT-125','TTR125','AKT125TTR','AK125TTR')
m('akt-jet4','AKT','Jet 4 125',125,'AKT-125','JET4','JET 4')
m('akt-jet5','AKT','Jet 5 150',150,'AKT-150','JET5','JET 5')
m('akt-tt150','AKT','TT 150',150,'AKT-150','AK150TT','TT150','AK 150 TT','150TT','AK150 EVO','EVO150','150EVO','AKT150','AK150NE','AKT 150 NE')
m('akt-ttr150','AKT','TTR 150',150,'AKT-150','TTR150','150TTR','AK150TTR')
m('akt-ttr180','AKT','TTR 180',180,'AKT-180','TTR180','AK180','TTX180','AKT180','AK180TTR','CR5','CR4')
m('akt-ttx200','AKT','TTX / SM / XM 200',200,'AKT-200','AK200','AKT200','TTX','AK200SM','AK200XM','200SM','XM180','XM200','SM200','ERONTE200','CERONTE 200','CERONTE')
m('akt-nv','AKT','NV 125',125,'AKT-125','AKT NV','NV125','DYNAMIC')
m('akt-rtx150','AKT','RTX 150',150,'AKT-150','RTX150','RTX 150','RTX')
m('akt-ninja300','AKT','Ninja 300',300,'KAWASAKI-300','NINJA300','NINJA 300')
m('akt-ax100','Suzuki','AX 100 / AX 115',100,'SUZUKI-AX100','AX100','AX 100','AX115','AX 115','AKT AX 100','AY 100')
m('akt-cr4','AKT','CR4 162',162,'AKT-160','CR4162','CR4-162')
m('akt-dominar','Bajaj','Dominar 400',400,'BAJAJ-400','DOMINAR','DOMINAR400')

# ---- Bajaj ----
m('baj-boxer100','Bajaj','Boxer 100 / BM100',100,'BAJAJ-100','BOXER100','BOXER 100','BOXERBM100','BOXER BM100','BM100','CT100','BOXER CT','K-TEC','KTEC','BOXER(TODAS)','re:\\bBOXER\\b(?! BM ?150)')
m('baj-boxer150','Bajaj','Boxer BM 150',150,'BAJAJ-150','BOXER BM150','BOXERBM150','BM150')
m('baj-platino','Bajaj','Platino 100-125',110,'BAJAJ-100','PLATINO','PLATINO100','PLATINO110','PLATINO125')
m('baj-caliber','Bajaj','Caliber 115',115,'BAJAJ-100','CALIBER','CALIBRE','CALIBER115')
m('baj-disc100','Bajaj','Discover 100',100,'BAJAJ-100','DISCOVER100','DISCOVER 100','DISCOVER110','DISCOVER 110')
m('baj-disc125','Bajaj','Discover 125',125,'BAJAJ-125','DISCOVER125','DISCOVER 125','DISC125','DISCOVER','XCD125','XCD 125','DICOVER')
m('baj-disc135','Bajaj','Discover 135',135,'BAJAJ-135','DISCOVER135','DISCOVER 135')
m('baj-disc150','Bajaj','Discover 150',150,'BAJAJ-150','DISCOVER150','DISCOVER 150')
m('baj-p135','Bajaj','Pulsar 135',135,'BAJAJ-135','PULSAR135','PULSAR 135','P135')
m('baj-p150','Bajaj','Pulsar 150',150,'BAJAJ-150','PULSAR150','PULSAR 150','NS150','AS150','AS 150')
m('baj-p160','Bajaj','Pulsar 160 NS',160,'BAJAJ-160','PULSAR160','NS160','160NS','NS 160')
m('baj-p180','Bajaj','Pulsar 180',180,'BAJAJ-180','PULSAR180','PULSAR 180','P180','PU180','PULSAR I','PULSAR II','PULSAR 180 II','NEON','180UG','PULSAR180UG','PULSAR 180 UG')
m('baj-p200ns','Bajaj','Pulsar 200 NS / AS',200,'BAJAJ-200','PULSAR200','PULSAR 200','NS200','NS 200','200NS','200AS','AS200','AS 200','NS/AS 200','200 NS','NS-200')
m('baj-p220','Bajaj','Pulsar 220',220,'BAJAJ-220','PULSAR220','PULSAR 220','re:PULSAR\\s?200[\\-/]220')
m('baj-avenger','Bajaj','Avenger 220',220,'BAJAJ-220','AVENGER')
m('ktm-duke200','KTM','Duke 200 / 390',200,'KTM-DUKE','DUKE200','DUKE 200','DUKE390','DUKE')

# ---- Yamaha ----
m('yam-fz16','Yamaha','FZ 16 / SZ-R / FZ 2.0',150,'YAMAHA-150','FZ16','FZ 16','SZ16','SZ-R','SZR','FZ2.0','FZ 2.0','FAZER150','FAZER 150','FZN150','FZN 150','YZF','R15','FAZER')
m('yam-ybr125','Yamaha','YBR 125',125,'YAMAHA-125','YBR125','YBR 125','YBR')
m('yam-xtz125','Yamaha','XTZ 125',125,'YAMAHA-125','XTZ125','XTZ 125')
m('yam-libero','Yamaha','Libero 110 / 125',125,'YAMAHA-125','LIBERO','LIBERÓ')
m('yam-crypton','Yamaha','Crypton 110 / 115',115,'YAMAHA-110','CRYPTON','T110','T 110')
m('yam-ybr250','Yamaha','YBR 250 / FZ 250 / XTZ 250',250,'YAMAHA-250','YBR250','FZ250','XTZ250','FAZEER250','FAZER250','XT225','XT 225')
m('yam-dt','Yamaha','DT 125 / 175',125,'YAMAHA-DT','DT125','DTK','DT100','DT175','DT200','DT 125')
m('yam-rx','Yamaha','RX 115 / 135',115,'YAMAHA-RX','RX115','RX 115','RX100','RX 100','RX135')

# ---- Suzuki ----
m('suz-gn125','Suzuki','GN 125 / Intruder / Nova',125,'SUZUKI-125','GN125','GN 125','GNNOVA','GN NOVA','NOVA','INTRUDER','GN','QUINQUI','MOTO VENEZOLANA')
m('suz-gs125','Suzuki','GS 125',125,'SUZUKI-125','GS125','GS 125','GS 125 GSX')
m('suz-gs150','Suzuki','GS 150 / GSX 150 / Gixxer',150,'SUZUKI-150','GS150','GSX150','GSX 150','GIXXER','GZ150','GS150R','GS 150R')
m('suz-fd125','Suzuki','FD 125 Best',125,'SUZUKI-125','FD125','FD 125','BEST')
m('suz-viva','Suzuki','Viva / Vivax 115',115,'SUZUKI-115','VIVA','VIVAX')
m('suz-fr80','Suzuki','FR 80',80,'SUZUKI-80','FR80','FR 80')
m('suz-ts125','Suzuki','TS 100 / 125 ER-Z',125,'SUZUKI-TS','TS125','TS 125','TS100','TS 100')
m('suz-dr','Suzuki','DR 150 / 200',200,'SUZUKI-DR','DR150','DR 150','DR200','DR 200','DR 125')
m('suz-vstrom','Suzuki','V-Strom 250',250,'SUZUKI-250','VSTROM','V-STROM','V STROM')
m('suz-hayate','Suzuki','Hayate 110',110,'SUZUKI-110','HAYATE')

# ---- Honda ----
m('hon-cb110','Honda','CB 110',110,'HONDA-110','CB110','CB 110')
m('hon-cb125','Honda','CB 125 / CG 125 / Storm',125,'HONDA-125','CB125','CB 125','CG125','CG 125','STORM','SDH125','CBZ125','JH125','JC125')
m('hon-cbf150','Honda','CBF 150 / Invicta',150,'HONDA-150','CBF150','CBF 150','INVICTA','CB150','CBZ160','CBZ 160','CB160')
m('hon-xr125','Honda','XR 125 L / Brio',125,'HONDA-125','XR125','XR 125','BRIO','XL125','XL 125','BROSS')
m('hon-xr150','Honda','XR 150 L / MRX',150,'HONDA-150','XR150','XR 150','MRX')
m('hon-xl185','Honda','XL 185 / XLR',185,'HONDA-185','XL185','XLR','XL 185')
m('hon-biz','Honda','C100 Biz / Wave / NXG 100',100,'HONDA-100','C100','C70','C90','BIZ','WAVE','NXG100','NXG 100','NXG')
m('hon-hero','Hero','Thriller / Hunk',150,'HERO-150','THRILLER','TRHILLER','HUNK','HERO')

# ---- TVS ----
m('tvs-rtr160','TVS','Apache RTR 160 / 180',160,'TVS-160','RTR160','RTR 160','RTR180','RTR 180','APACHE160','APACHE 160','APACHE 160/180','APACHE')
m('tvs-rtr200','TVS','Apache RTR 200',200,'TVS-200','RTR200','RTR 200')
m('tvs-sport100','TVS','Sport 100',100,'TVS-100','TVS100','TVS SPORT','SPORT 100')
m('tvs-raider','TVS','Raider 125',125,'TVS-125','RAIDER')
m('victory-one','Victory','One 100',100,'VICTORY-100','VICTORY')

# ---- Otras ----
m('kym-agility','Kymco','Agility / Fly 150',150,'KYMCO-150','AGILITY','FLY150','FLY 150','FLY')
m('ben-180s','Benelli','180S',180,'BENELLI','BENELLI 180S','180S')
m('ben-tnt150','Benelli','TNT 150',150,'BENELLI','TNT150','TNT 150')
m('jia-sigma','Jialing / Sigma','Sigma / LF / SG',150,'CHINA-150','SIGMA','LF150','LF110','LF125','SG125','JIALING','TX200','RENEGADE','FURAX','VENUS','MIX110','QM110','QM125')
m('cb-carguero','Motocarguero','Torito / Zh 150',150,'CARGUERO','TORITO','MOTOCARRO','MOTOCARGUERO','THREE WEELER','CARGUERO')

def _add(id, *alias):
    for x in M:
        if x[0] == id: x[5].extend(alias); return
    raise KeyError(id)

m('yam-xtz150','Yamaha','XTZ 150',150,'YAMAHA-150','XTZ150','XTZ 150')
m('yam-bws','Yamaha','BWS 100',100,'YAMAHA-100','BWS100','BWS 100','BWS')
m('suz-v80','Suzuki','V 80',80,'SUZUKI-80','V80','V 80')
m('hon-cbr','Honda','CBR 125 / 190',125,'HONDA-CBR','CBR125','CBR190','CBR 190','CB50')
m('hero-eco100','Hero','Eco 100 / Deluxe',100,'HERO-100','ECO100','ECO 100','DELUXE','ECO')
m('hero-xpulse','Hero','X-Pulse 200',200,'HERO-200','XPULSE','X-PULSE')
m('baj-ns125','Bajaj','NS 125',125,'BAJAJ-125','NS125','NS 125')
m('oth-wind125','Por definir','Wind 125',125,'PENDIENTE','WIND125','WIND 125')
m('oth-striker','Por definir','Striker 125',125,'PENDIENTE','STRIKER')
m('oth-venom','Por definir','Venom 250',250,'PENDIENTE','VENOM250','VENOM 250')
_add('suz-fr80','FR100','FR 100','ER100','ER/100')
_add('yam-dt','DT124','DT 124')
_add('tvs-rtr200','TVS 200 RTR','200 RTR')
_add('hon-cbf150','CBF125','CBF 125','CB125F')

# Grupos: alias genérico que aplica a TODAS las motos de esa familia_motor
GROUPS = {
    'AKT-125': ['AKT125','AKT 125','AK125','AK 125','AY125'],
    'AKT-150': ['AK150','AKT 150'],
}
