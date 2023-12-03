class Line:


    def __init__(self, long_name, colour, train_num_prefix):
        self.long_name = long_name
        self.colour = colour
        self.train_num_prefix = train_num_prefix

    def __str__(self):
        return self.long_name, self.colour, self.train_num_prefix



    def set_stations(self, stations):
        self.stations = stations
        for q in self.stations:
            q.lines.append(
            if self in q.lines:
                list_stations.append(q.code)
            else:
                continue
        #self.endpoints = [list_stations[0], list_stations[len(self.stations)-1]]
        #self.nb_stations = len(self.list_stations)
        return list_stations







northern_MTV = Line("Bellville via Monte Vista", "green", "28")
northern_MUT = Line("Bellville via Mutual", "green", "35")
central_BLV = Line("Bellville via Lavistown", "blue", "90")
central_CHN = Line("Chris Hani via Esplanade", "blue", "99")
central_KPT = Line("Kapteinsklip via Pinelands", "blue", "95")
cpflats = Line("Retreat via Pinelands", "brown", "05")
southern = Line("Simonstown via Retreat", "red", "01")

list_stations = []


class Station:


    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.lines = []






cpt = Station("Cape Town", "CPT", [northern_MTV, northern_MUT, central_BLV, central_KPT, central_CHN, southern, cpflats], True)
esp = Station("Esplanade", "ESP", [northern_MTV, central_BLV, central_CHN], True)
yst = Station("Ysterplaat", "YST", [northern_MTV, central_BLV, central_CHN], True)
ktm = Station("Kentemade", "KTM", [northern_MTV], False)
cen = Station("Century City", "CEN", [northern_MTV], False)
aka = Station("Akasiapark", "AKA", [northern_MTV], False)
mtv = Station("Monte Vista", "MTV", [northern_MTV], False)
deg = Station("De Grendel", "DEG", [northern_MTV], False)
avo = Station("Avondale", "AVO", [northern_MTV], False)
oos = Station("Oosterzee", "OOS", [northern_MTV], False)
blv = Station("Bellville", "BLV", [northern_MTV, northern_MUT, central_BLV], True)
wol = Station("Woltemade", "WOL", [northern_MUT], False)
mut = Station("Mutual", "MUT", [central_BLV, central_CHN, northern_MUT], True)
ttn = Station("Thornton", "TTN", [northern_MUT], False)
gdw = Station("Goodwood", "GDW", [northern_MUT], False)
vas = Station("Vasco", "VAS", [northern_MUT], False)
els = Station("Elsies Rivier", "ELS", [northern_MUT], False)
prw = Station("Parow", "PRW", [northern_MUT], False)
tyg = Station("Tygerberg", "TYG", [northern_MUT], False)
wsk = Station("Woodstock", "WSK", [central_KPT, northern_MUT, southern, cpflats], True)
slt = Station("Salt River", "SLT", [central_KPT, northern_MUT, southern, cpflats], True)
koe = Station("Koeberg Road", "KOE", [central_KPT, northern_MUT, cpflats], True)
mai = Station("Maitland", "MAI", [central_KPT, northern_MUT, cpflats], True)
nda = Station("Ndabeni", "NDA", [central_KPT, cpflats], True)
pnl = Station("Pinelands", "PNL", [central_KPT, cpflats], True)
lng = Station("Langa", "LNG", [central_BLV, central_KPT, central_CHN], True)
btw = Station("Bonteheuwel", "BTW", [central_BLV, central_KPT, central_CHN], True)
lvs = Station("Lavistown", "LVS", [central_BLV], False)
blh = Station("Belhar", "BLH", [central_BLV], False)
uni = Station("Unibell", "UNI", [central_BLV], False)
pen = Station("Pentech", "PEN", [central_BLV], False)
srp = Station("Sarepta", "SRP", [central_BLV], False)
ntr = Station("Netreg", "NTR", [central_KPT, central_CHN], True)
hdv = Station("Heideveld", "HDV", [central_KPT, central_CHN], True)
nya = Station("Nyanga", "NYA", [central_KPT, central_CHN], True)
ppi = Station("Philippi", "PPI", [central_KPT, central_CHN], True)
lnt = Station("Lentegeur", "LNT", [central_KPT], False)
mtc = Station("Mitchell's Plain", "MTC", [central_KPT], False)
kpt = Station("Kapteinsklip", "KPT", [central_KPT], False)
sto = Station("Stock Road", "STO", [central_CHN], False)
mdl = Station("Mandelay", "MDL", [central_CHN], False)
nol = Station("Nolungile", "NOL", [central_CHN], False)
non = Station("Nonkqubela", "NON", [central_CHN], False)
kyl = Station("Khayelitsha", "KYL", [central_CHN], False)
kuy = Station("Kuyasa", "KUY", [central_CHN], False)
chn = Station("Chris Hani", "CHN", [central_CHN], False)
hzd = Station("Hazendal", "HZD", [cpflats], False)
ath = Station("Athlone", "ATH", [cpflats], False)
cra = Station("Crawford", "CRA", [cpflats], False)
ldn = Station("Lansdowne", "LDN", [cpflats], False)
wtn = Station("Wetton", "WTN", [cpflats], False)
ott = Station("Ottery", "OTT", [cpflats], False)
stf = Station("Southfield", "STF", [cpflats], False)
hea = Station("Heathfield", "HEA", [cpflats, southern], True)
ret = Station("Retreat", "RET", [cpflats, southern], True)
obs = Station("Observatory", "OBS", [southern], False)
mow = Station("Mowbray", "MOW", [southern], False)
ros = Station("Rosebank", "ROS", [southern], False)
rdb = Station("Rondebosch", "RDB", [southern], False)
new = Station("Newlands", "NEW", [southern], False)
cla = Station("Claremont", "CLA", [southern], False)
har = Station("Harfield Road", "HAR", [southern], False)
ken = Station("Kenilworth", "KEN", [southern], False)
wyn = Station("Wynberg", "WYN", [southern], False)
wit = Station("Wittebome", "WIT", [southern], False)
plu = Station("Plumstead", "PLU", [southern], False)
ste = Station("Steurhof", "STE", [southern], False)
die = Station("Diep Water", "DIE", [southern], False)
stb = Station("Steenberg", "STB", [southern], False)
lks = Station("Lakeside", "LKS", [southern], False)
flb = Station("False Bay", "FLB", [southern], False)
mui = Station("Muizenberg", "MUI", [southern], False)
stj = Station("St. James", "STJ", [southern], False)
klk = Station("Kalk Bay", "KLK", [southern], False)
fis = Station("Fish Hoek", "FIS", [southern], False)
sun = Station("Sunny Cove", "SUN", [southern], False)
gle = Station("Glencairn", "GLE", [southern], False)
sim = Station("Simonstown", "SIM", [southern], False)

stations = [cpt,esp,yst,ktm,cen,aka,mtv,deg,avo,oos,blv,wol,mut,ttn,gdw,vas,els,prw,tyg,wsk,slt,koe,mai,nda,pnl,lng,btw,lvs,blh,uni,pen,srp,ntr,hdv,nya,ppi,lnt,mtc,kpt,sto,mdl,nol,non,kyl,kuy,chn,hzd,ath,cra,ldn,wtn,ott,stf,hea,ret,obs,mow,ros,rdb,new,cla,har,ken,wyn,wit,plu,ste,die,stb,lks,flb,mui,stj,klk,fis,sun,gle,sim]




    
    
