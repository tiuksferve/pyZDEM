# This is part of the PyZDEM solution - Written by Tiago Ferreira Veiga (aka Tiuks Ferve)
# veigatf@gmail.com // instagram: @tiuksferve // Mobile: +55 61 999-682-129 // ABAP SENIOR DEVELOPER
# PLEASE DO NOT REMOVE CREDITS - YOU CAN CHANGE THE CODE - ADD YOUR NAME AT THE "CONTRIBUTORS" AREA 
# Contributors: NONE (05.12.2017 - mm.dd.aaaa)
# This code turned into a huge Python3 laboratory... Enjoy!
from zdembd import Banco
    
class Gaps(object):
    def __init__(self, gapid = "", onda = "", cenar = "", proce = "", descr = "", tipog = "", modul = "", versa = "", ust1 = "", ust2 = "", ustr = "", nrrdm = "", stsfu = "", stsgp = "", paral = "", glive = "", nross = "", artft = "", justf = "", qtdcp = "", datdv = "", gongo = ""):
        self.info = {}
        self.gapid = gapid   
        self.onda = onda     
        self.cenar = cenar
        self.proce = proce
        self.descr = descr
        self.tipog = tipog
        self.modul = modul   
        self.versa = versa   
        self.ust1 = ust1    
        self.ust2 = ust2    
        self.ustr = ustr
        self.nrrdm = nrrdm
        self.stsfu = stsfu
        self.stsgp = stsgp   
        self.paral = paral   
        self.glive = glive  
        self.nross = nross   
        self.artft = artft
        self.justf = justf
        self.qtdcp = qtdcp
        self.datdv = datdv
        self.gongo = gongo       

    def insertGap(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()
            # insert data at the master data table
            c.execute("insert into tbgaps (gapid, onda, cenar, proce, descr, tipog, modul, versa, ust1, ust2, ustr, nrrdm, stsfu, stsgp, paral, glive, nross, artft, qtdcp, datdv, gongo) values ('" + self.gapid + "', '" + self.onda + "', '" + self.cenar + "', '" + self.proce + "', '" + self.descr + "', '" + self.tipog + "', '" + self.modul + "', '" + self.versa + "', '" + self.ust1 + "', '" + self.ust2 + "', '" + self.ustr + "', '" + self.nrrdm + "', '" + self.stsfu + "', '" + self.stsgp + "', '" + self.paral + "', '" + self.glive + "', '" + self.nross + "', '" + self.artft + "', '" + self.qtdcp + "', '" + self.datdv + "', '" + self.gongo + "')")
            # insert data on delta table (inserted)
            c.execute("insert into tbins (gapid, onda, cenar, proce, descr, tipog, modul, versa, ust1, ust2, ustr, nrrdm, stsfu, stsgp, paral, glive, nross, artft, qtdcp, datdv, gongo) values ('" + self.gapid + "', '" + self.onda + "', '" + self.cenar + "', '" + self.proce + "', '" + self.descr + "', '" + self.tipog + "', '" + self.modul + "', '" + self.versa + "', '" + self.ust1 + "', '" + self.ust2 + "', '" + self.ustr + "', '" + self.nrrdm + "', '" + self.stsfu + "', '" + self.stsgp + "', '" + self.paral + "', '" + self.glive + "', '" + self.nross + "', '" + self.artft + "', '" + self.qtdcp + "', '" + self.datdv + "', '" + self.gongo + "')")         
            banco.conexao.commit()
            c.close()
                    
            return "GAP inserted sucessfully!"
        except:
            return "An error occured at the GAP insertion"

    def updateGap(self, gapidu, versau):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            # update line/data
            queryUpdate = "update tbgaps set gapid = '" + self.gapid + "', onda = '" + self.onda + "', cenar = '" + self.cenar + "', proce = '" + self.proce + "', descr = '" + self.descr + "', tipog = '" + self.tipog + "', modul = '" + self.modul + "', versa = '" + self.versa + "', ust1 = '" + self.ust1 + "', ust2 = '" + self.ust2 + "', ustr = '" + self.ustr + "', nrrdm = '" + self.nrrdm + "', stsfu = '" + self.stsfu + "', stsgp = '" + self.stsgp + "', paral = '" + self.paral + "', glive = '" + self.glive + "', nross = '" + self.nross + "', artft = '" + self.artft + "', qtdcp = '" + self.qtdcp + "', datdv = '" + self.datdv + "', gongo = '" + self.gongo + "'  where gapid=? AND versa=? "
            c.execute(queryUpdate, (gapidu, versau))
            
            banco.conexao.commit()
            c.close()
            
            return "GAP updated!"
        except:
            return "An error occured on GAP update."

    def deleteGap(self, gapidd, versad):

        banco = Banco()
        try:

            c = banco.conexao.cursor()
            # First insert deleted data at the delta deleted table
            c.execute("insert into tbdel (gapid, onda, cenar, proce, descr, tipog, modul, versa, ust1, ust2, ustr, nrrdm, stsfu, stsgp, paral, glive, nross, artft, justf, qtdcp, datdv, gongo) values ('" + self.gapid + "', '" + self.onda + "', '" + self.cenar + "', '" + self.proce + "', '" + self.descr + "', '" + self.tipog + "', '" + self.modul + "', '" + self.versa + "', '" + self.ust1 + "', '" + self.ust2 + "', '" + self.ustr + "', '" + self.nrrdm + "', '" + self.stsfu + "', '" + self.stsgp + "', '" + self.paral + "', '" + self.glive + "', '" + self.nross + "', '" + self.artft + "', '" + self.justf + "', '" + self.qtdcp + "', '" + self.datdv + "', '" + self.gongo + "')")
            # then, delete data from tbgaps table
            queryDelete = "delete from tbgaps where gapid=? and versa=?"
            c.execute(queryDelete, (gapidd,versad))
            
            banco.conexao.commit()
            c.close()

            return "GAP deleted sucessfully!"
        except:
            return "An error occured at the GAP deletion"

    def selectGap(self, gapid, versa):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            querySelect = "select * from tbgaps where gapid=? and versa=?"
            c.execute(querySelect, (gapid, versa))

            for linha in c:
                self.gapid = linha[0]   
                self.onda = linha[1]    
                self.cenar = linha[2]
                self.proce = linha[3]
                self.descr = linha[4]
                self.tipog = linha[5]
                self.modul = linha[6] 
                self.versa = linha[7] 
                self.ust1 = linha[8] 
                self.ust2 = linha[9]  
                self.ustr = linha[10]  
                self.nrrdm = linha[11]
                self.stsfu = linha[12]
                self.stsgp = linha[13] 
                self.paral = linha[14]
                self.glive = linha[15]
                self.nross = linha[16]
                self.artft = linha[17]
                self.qtdcp = linha[18]
                self.datdv = linha[19]
                self.gongo = linha[20]
                  
            c.close()

            return "Data search performed sucessfully!"
        except:
            return "An error occured at the GAP search."
