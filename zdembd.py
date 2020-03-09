# This is part of the PyZDEM solution - Written by Tiago Ferreira Veiga (aka Tiuks Ferve)
# veigatf@gmail.com // instagram: @tiuksferve // Mobile: +351 910-869-393 // ABAP SENIOR DEVELOPER & SAP HANA Developer
# PLEASE DO NOT REMOVE CREDITS - YOU CAN CHANGE THE CODE - ADD YOUR NAME AT THE "CONTRIBUTORS" AREA 
# Contributors: NONE (05.12.2017 - dd.mm.aaaa)
# Edited on 09.03.2020 (dd.mm.aaaa)
# This code turned into a huge Python3 laboratory... Enjoy!
import sqlite3

class Banco():
    def __init__(self):
# setting the DB name        
        self.conexao = sqlite3.connect('banco.db')
# Calling create table functions        
        self.createGaps()
        self.createDelet()
        self.createModul()
        self.createInsert()
        self.createStatus()
        
# Master Table - all the modifications are made here - Valid data        
    def createGaps(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbgaps (gapid text, onda text, cenar text, proce text, descr text, tipog text, modul text, versa text, ust1 text, ust2 text, ustr text, nrrdm text, stsfu text, stsgp text, paral text, glive text, nross text, artft text, qtdcp text, datdv text, gongo text)""")
        self.conexao.commit()
        c.close()

# Deleted Items Table - Table that holds deleted Items (delta)        
    def createDelet(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbdel (gapid text, onda text, cenar text, proce text, descr text, tipog text, modul text, versa text, ust1 text, ust2 text, ustr text, nrrdm text, stsfu text, stsgp text, paral text, glive text, nross text, artft text, justf text, qtdcp text, datdv text, gongo text)""")
        self.conexao.commit()
        c.close()

# Inserted Items Table - Table that holds inserted items (delta)       
    def createInsert(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbins (gapid text, onda text, cenar text, proce text, descr text, tipog text, modul text, versa text, ust1 text, ust2 text, ustr text, nrrdm text, stsfu text, stsgp text, paral text, glive text, nross text, artft text, qtdcp text, datdv text, gongo text)""")
        self.conexao.commit()
        c.close()

# SAP Modules Table - Table that holds Module information        
    def createModul(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbmod (modul text, mtext text)""")
        c.execute("""select count(*) from tbmod""")
        data = c.fetchone()[0]
        if data == 0:
            c.execute("""insert into tbmod values ("", "")""")
            c.execute("""insert into tbmod values ("FI", "FINANCE")""")
            c.execute("""insert into tbmod values ("FM", "FUNDS MGMT.")""")
            c.execute("""insert into tbmod values ("TV", "TRAVEL MGMT.")""")
            c.execute("""insert into tbmod values ("CO", "CONTROLLING")""")
            c.execute("""insert into tbmod values ("TR", "TREASURY")""")
            c.execute("""insert into tbmod values ("EC", "ENTRERPRISE CONTR.")""")
            c.execute("""insert into tbmod values ("IM", "INVESTMENT MGMT.")""")
            c.execute("""insert into tbmod values ("PS", "PROJECT SYSTEM")""")
            c.execute("""insert into tbmod values ("WF", "WORKFLOW")""")
            c.execute("""insert into tbmod values ("ECM", "ENTRERPRISE CONT.M.")""")
            c.execute("""insert into tbmod values ("IS", "INDUSTRY SOLUTIONS")""")
            c.execute("""insert into tbmod values ("SD", "SALES & DISTRIBUTION")""")
            c.execute("""insert into tbmod values ("MM", "MATERIAL MGMT.")""")
            c.execute("""insert into tbmod values ("PP", "PRODUCTION PLANING")""")
            c.execute("""insert into tbmod values ("QM", "QUALITY MGMT.")""")
            c.execute("""insert into tbmod values ("PM", "PLANT MAINT.")""")
            c.execute("""insert into tbmod values ("HCM", "HUMAN CAPITAL M.")""")
            c.execute("""insert into tbmod values ("BW", "BUSINESS WAREHOUSE")""")
            c.execute("""insert into tbmod values ("CRM", "CUST. RELATION M.")""")
            c.execute("""insert into tbmod values ("FS", "FINANCIAL SOLUTIONS")""")           

        self.conexao.commit()
        c.close()

# GAP Status - Custom GAP status             
    def createStatus(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbsts (stsfn text, stsgr text)""")
        c.execute("""select count(*) from tbsts""")
        data2 = c.fetchone()[0]
        if data2 == 0:            
            c.execute("""insert into tbsts values ("", "")""")
            c.execute("""insert into tbsts values ("Identified", "Identified")""")
            c.execute("""insert into tbsts values ("On Analisys", "On Analisys")""")
            c.execute("""insert into tbsts values ("SPEC writing", "SPEC Writing")""")
            c.execute("""insert into tbsts values ("On hold - Metrics review", "On hold - Metrics review")""")
            c.execute("""insert into tbsts values ("Released for coding", "Released for coding")""")   
            c.execute("""insert into tbsts values ("Coding", "Coding")""")
            c.execute("""insert into tbsts values ("Unit Test", "Unit Test")""")
            c.execute("""insert into tbsts values ("Functional Test", "Functional Test")""")
            c.execute("""insert into tbsts values ("Integration Tests", "Integration Tests")""")            
            c.execute("""insert into tbsts values ("Closed", "Closed/Production")""")
            c.execute("""insert into tbsts values ("Cancelled", "Cancelled")""")            

        self.conexao.commit()
        c.close()
