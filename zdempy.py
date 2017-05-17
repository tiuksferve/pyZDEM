# This is part of the PyZDEM solution - Written by Tiago Ferreira Veiga (aka Tiuks Ferve)
# veigatf@gmail.com // instagram: @tiuksferve // Mobile: +55 61 999-682-129 // ABAP SENIOR DEVELOPER
# PLEASE DO NOT REMOVE CREDITS - YOU CAN CHANGE THE CODE - ADD YOUR NAME AT THE "CONTRIBUTORS" AREA 
# Contributors: NONE (05.12.2017 - mm.dd.aaaa)
# This code turned into a huge Python3 laboratory... Enjoy!
from zdemfm import Gaps
from zdembd import Banco
from tkinter import *
from tkinter import ttk
import csv
import time

class Main:
    def __init__(self,master): # Main screen
        # Font - Styles
        self.fontn = ("Arial", "9") # General Font style
        self.fontmsg = ("Arial", "9") # Message font style
        self.fontl = ("Verdana", "9", "italic") # Label font style
        self.fontc = ("Arial", "9", "bold") # Counter style 
        # Additional fields screen variables
        self.varQtdcp = StringVar()
        self.varDatdv = StringVar()
        self.varGongo = StringVar()
        self.gapidFix = StringVar()
        self.versaFix = StringVar()
        self.varQtdcp = ""
        self.varDatdv = ""
        self.varGongo = ""
        self.gapidFix = ""
        self.versaFix = ""
        # Tab function
        self.abas = ttk.Notebook(master, width=480, height=250) # Sized for POCKETCHIP
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        # TAB 1        
        # List implementation
        self.tree = ttk.Treeview(self.frame_aba1)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)             
        # Label - search counter TAB 1
        self.lblSearch = Label(self.frame_aba1, text="GAPs found:", font=self.fontmsg)
        self.lblSearch.place(x=5, y=225)
        # label - Counter number        
        self.countVar = Label(self.frame_aba1, text="", font=self.fontc)
        self.countVar.place(x=100, y=225)
        # label - Table filter
        self.lblFilter2 = Label(self.frame_aba1, text="Tab:", font=self.fontl)
        self.lblFilter2.place(x=200, y=225)
        # Combobox - Table Filter
        self.filtTab = ttk.Combobox(self.frame_aba1, textvariable=table, width=7)
        self.filtTab["values"] = ("tbgaps", "tbdel", "tbins")
        self.filtTab.current(0)
        self.filtTab.place(x=230, y=225)
        # label - Module filter
        self.lblFilter = Label(self.frame_aba1, text="Mod:", font=self.fontl)
        self.lblFilter.place(x=310, y=225)
        # ComboBox - Module Filter
        self.filtMod = ttk.Combobox(self.frame_aba1, textvariable=modul, width=5)
        self.filtMod["values"] = ("*", "AA", "MM", "FI", "TV", "PM", "PS", "SRM", "FM", "CO")
        self.filtMod.current(0)
        self.filtMod.place(x=345, y=225)
        self.refreshList()   
        # List - refresh button
        self.btnList = Button(self.frame_aba1, text="Refresh", command=self.refreshList, font=self.fontn, width=5) 
        self.btnList.place(x=405, y=220)
        # TAB 2
        # Label - GAP number
        self.lblGap = Label(self.frame_aba2, text="GAP:", font=self.fontl)
        self.lblGap.place(x=5, y=5)
        # Entry - GAP Number
        self.txtGap = Entry(self.frame_aba2, font=self.fontn, width=11, bg="yellow")
        self.txtGap.place(x=40, y=5)
        # Label - Version
        self.lblVersion = Label(self.frame_aba2, text="Ver:", font=self.fontl)
        self.lblVersion.place(x=124, y=5)
        # Entry - Version
        self.txtVersion = Entry(self.frame_aba2, font=self.fontn, width=2, bg="yellow")
        self.txtVersion.place(x=153, y=5)
        # Button - Search GAP
        self.btnBuscar = Button(self.frame_aba2, text="Search", command=self.selectGap, font=self.fontn, width=5)
        self.btnBuscar.place(x=178, y=3)
        # Entry - GAP description (name)
        self.txtName = Entry(self.frame_aba2, font=self.fontn, width=32)
        self.txtName.place(x=245, y=5)
        # Line separator 1
        self.sep = ttk.Separator(self.frame_aba2, orient="horizontal")
        self.sep.pack(fill="x", pady="32")
        # Label - Delivery wave
        self.lblWave = Label(self.frame_aba2, text="Wave:", font=self.fontl)
        self.lblWave.place(x=5, y=41)
        # Entry - Delivery Wave
        self.txtWave = Entry(self.frame_aba2, font=self.fontn, width=2)
        self.txtWave.place(x=45, y=41)
        # Label - GoLive
        self.lblGolive = Label(self.frame_aba2, text="GoLive:", font=self.fontl)
        self.lblGolive.place(x=70, y=41)
        # Entry - GoLive
        self.txtGolive = Entry(self.frame_aba2, font=self.fontn, width=2)
        self.txtGolive.place(x=118, y=41)
        # Label - Module
        self.lblModul = Label(self.frame_aba2, text="Module:", font=self.fontl)
        self.lblModul.place(x=145, y=41)
        # Entry - Module
        self.txtModul = ttk.Combobox(self.frame_aba2, textvariable=modul_db, width=4)
        self.txtModul["values"] = self.srchModul()
        self.txtModul.current(1)
        self.txtModul.place(x=200, y=41)
        # Label - GAP Type
        self.lblTypeg = Label(self.frame_aba2, text="Type:", font=self.fontl)
        self.lblTypeg.place(x=255, y=41)
        # Entry - GAP Type
        self.txtTypeg = ttk.Combobox(self.frame_aba2, textvariable=tipog, width=4)
        self.txtTypeg["values"] = ("GAP", "INT", "MIG")
        self.txtTypeg.current(0)
        self.txtTypeg.place(x=292, y=41)
        # Label - GAP on hold
        self.lblHold = Label(self.frame_aba2, text="On Hold:", font=self.fontl)
        self.lblHold.place(x=345, y=41)
        # Checkbox - GAP on hold
        self.ckHold = Checkbutton(self.frame_aba2, variable=ckp)
        self.ckHold.deselect()
        self.ckHold.place(x=400, y=41)
        # Line separator 2
        self.sep2 = ttk.Separator(self.frame_aba2, orient="horizontal")
        self.sep2.pack(fill="x", pady="3")
        # Label - Service Order (in order to control GAP billing)
        self.lblSo = Label(self.frame_aba2, text="SO:", font=self.fontl)
        self.lblSo.place(x=5, y=77)
        # Entry - Service Order
        self.txtSo = Entry(self.frame_aba2, font=self.fontn, width=14)
        self.txtSo.place(x=30, y=77)
        # Label - GAP Status
        self.lblStatus = Label(self.frame_aba2, text="Status:", font=self.fontl)
        self.lblStatus.place(x=140, y=77)
        # Entry - GAP Status
        self.txtStatus = ttk.Combobox(self.frame_aba2, textvariable=status, width=30)
        self.txtStatus["values"] = self.srchStatus()
        self.txtStatus.current(1)
        self.txtStatus.place(x=190, y=77)
        # Line Separator 3
        self.sep3 = ttk.Separator(self.frame_aba2, orient="horizontal")
        self.sep3.pack(fill="x", pady="30")
        # Label - Time (Hours to develop)
        self.lblHrs = Label(self.frame_aba2, text="HRS:", font=self.fontl)
        self.lblHrs.place(x=5, y=110)
        # Entry - Time (Hours to develop) - first metric
        self.txtHrs = Entry(self.frame_aba2, font=self.fontn, width=4)
        self.txtHrs.place(x=37, y=110)
        # Label - Second Metric
        self.lblHrs2 = Label(self.frame_aba2, text="2 HRS:", font=self.fontl)
        self.lblHrs2.place(x=75, y=110)
        # Entry - Second Metric
        self.txtHrs2 = Entry(self.frame_aba2, font=self.fontn, width=4)
        self.txtHrs2.place(x=120, y=110)
        # Label - Time for Change Requests
        self.lblHrsr = Label(self.frame_aba2, text="HRS CR:", font=self.fontl)
        self.lblHrsr.place(x=158, y=110)
        # Entry - Time for Change Requests
        self.txtHrsr = Entry(self.frame_aba2, font=self.fontn, width=4)
        self.txtHrsr.place(x=212, y=110)
        # Label = Time total
        self.lblHrst = Label(self.frame_aba2, text="Total:", font=self.fontl)
        self.lblHrst.place(x=255, y=110)
        # Entry - Time total
        self.txtHrst = Entry(self.frame_aba2, font=self.fontn, width=4, text=ustTot)
        self.txtHrst.place(x=295, y=110)
        self.txtHrst.config(state=DISABLED)
        # Label - Time variation between first and second metrics (in %)
        self.lblHrsv = Label(self.frame_aba2, text="Variation:", font=self.fontl)
        self.lblHrsv.place(x=330, y=110)
        # Entry - Time variation between first and second metrics (in %)
        self.txtHrsv = Entry(self.frame_aba2, font=self.fontn, width=6, text=varMet)
        self.txtHrsv.place(x=395, y=110)
        self.txtHrsv.config(state=DISABLED)
        # Label - % symbol
        self.lblHrst = Label(self.frame_aba2, text="%", font=self.fontl)
        self.lblHrst.place(x=445, y=110)
        # Line Separator 4
        self.sep4 = ttk.Separator(self.frame_aba2, orient="horizontal")
        self.sep4.pack(fill="x", pady="2")
        # Label - Scenario
        self.lblScen = Label(self.frame_aba2, text="Scenario:", font=self.fontl)
        self.lblScen.place(x=5, y=145)
        # Entry - Scenario
        self.txtScen = Entry(self.frame_aba2, font=self.fontn, width=30)
        self.txtScen.place(x=67, y=145)
        # Label - Process
        self.lblProc = Label(self.frame_aba2, text="Process:", font=self.fontl)
        self.lblProc.place(x=5, y=170)
        # Entry - Process
        self.txtProc = Entry(self.frame_aba2, font=self.fontn, width=30)
        self.txtProc.place(x=68, y=170)
        # Label - Change reques reference
        self.lblCr = Label(self.frame_aba2, text="CR:", font=self.fontl)
        self.lblCr.place(x=290, y=145)
        # Entry - Change reques reference
        self.txtCr = Entry(self.frame_aba2, font=self.fontn, width=15)
        self.txtCr.place(x=315, y=145)
        # Button - Additional Fields
        self.btnAdc = Button(self.frame_aba2, text="Additional Fields", command=self.popAdc1, font=self.fontn, width=12)
        self.btnAdc.place(x=317, y=166)
        # Line Separator 5
        self.sep5 = ttk.Separator(self.frame_aba2, orient="horizontal")
        self.sep5.pack(fill="x", pady="52")  
        # Action buttons
        self.bntInsert = Button(self.frame_aba2, text="Insert", command=self.insertGaps, font=self.fontn, width=8)
        self.bntInsert.place(x=45, y=200)
        self.bntChange = Button(self.frame_aba2, text="Change", command=self.updateGap, font=self.fontn, width=8)
        self.bntChange.place(x=145, y=200)
        self.bntDelete = Button(self.frame_aba2, text="Delete", command=self.deleteGap1, font=self.fontn, width=8)
        self.bntDelete.place(x=245, y=200)
        self.bntErase = Button(self.frame_aba2, text="Clear", command=self.eraseFields, font=self.fontn, width=8)
        self.bntErase.place(x=345, y=200)
        # Bottom page messages - TAB 2
        self.labelMsg = Label(self.frame_aba2, text="", font=self.fontmsg)
        self.labelMsg.place(x=180, y=230)
        # TAB 3
        self.info1 = Label(self.frame_aba3, text="Data will be recorded @ ")
        self.info1.pack(anchor=W)
        self.path = Entry(self.frame_aba3, font=self.fontn, width=20)
        self.path.insert(INSERT, "/home/chip/pyZDEM/")
        self.path.place(x=160,y=1)
        self.info12 = Label(self.frame_aba3, text="Please do not specify file name. Files are named with table names.", font=self.fontn)
        self.info12.pack(anchor=W)        
        self.sep13 = ttk.Separator(self.frame_aba3, orient="horizontal")
        self.sep13.pack(fill="x", pady="10")  

        self.info2 = Label(self.frame_aba3, text="Choose one of the options below:", font=self.fontn)
        self.info2.pack(anchor=W)
        self.opc1 = Radiobutton(self.frame_aba3, command=self.radioCheck, text="Export GAPs table.", variable=v, value=1).pack(anchor=W)
        self.opc2 = Radiobutton(self.frame_aba3, command=self.radioCheck, text="Export Delta tables.", variable=v, value=2).pack(anchor=W)
        self.opc3 = Radiobutton(self.frame_aba3, command=self.radioCheck, text="Perform total backup.", variable=v, value=3).pack(anchor=W)  
        self.opc4 = Radiobutton(self.frame_aba3, command=self.radioCheck, text="Delete GAPs table", variable=v, value=4).pack(anchor=W)
        self.opc5 = Radiobutton(self.frame_aba3, command=self.radioCheck, text="Delete Delta tables", variable=v, value=5).pack(anchor=W)                    
        self.opc6 = Radiobutton(self.frame_aba3, command=self.radioCheck, text="Delete all tables", variable=v, value=6).pack(anchor=W)                                 
        self.bntDelal = Button(self.frame_aba3, text="Execute", font=self.fontn, command=self.ExecCommand, width=8)
        self.bntDelal.pack(anchor=W) 
        # Bottom page message - TAB 3
        self.labelMsg3 = Label(self.frame_aba3,text="", font=self.fontmsg)
        self.labelMsg3.place(x=50, y=225)                    
        # TABs names     
        self.abas.add(self.frame_aba1,text="List")
        self.abas.add(self.frame_aba2,text="GAP Control")
        self.abas.add(self.frame_aba3,text="Tools")
        self.abas.pack()    

    # when a line is chosen, the data is filled at the GAP CONTROL tab (tab 2)
    def on_tree_select(self, event):
        if self.filtTab.get() == "tbgaps":
            for values in self.tree.selection():
                item_values = self.tree.item(values,"values")    

            # Clear all fields at TAB 2 before fill up with the data recovered.
            self.eraseFields()
            # Select the DATA for GAP search at TAB 2 - Fields GAP and VERSION
            self.txtGap.insert(INSERT, self.tree.item(self.tree.selection())["values"][0])
            self.txtVersion.insert(INSERT, self.tree.item(self.tree.selection())["values"][3])
            # Call the GAP search function to fill up TAB 2
            if self.tree.item(self.tree.selection())["values"][3] in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                self.txtVersion.delete(0, END)
                self.txtVersion.insert(INSERT, "0" + str(self.tree.item(self.tree.selection())["values"][3]))

            self.selectGap()

  # function to search GAP information
    def selectGap(self):
        user = Gaps()

        gapid = self.txtGap.get()
        versa = self.txtVersion.get()

        # Fix variables - Update Data control
        self.versaFix = versa
        self.gapidFix = gapid

        self.labelMsg["text"] = user.selectGap(gapid, versa)

        self.txtGap.delete(0, END)
        self.txtGap.insert(INSERT, user.gapid)
        self.txtName.delete(0, END)
        self.txtName.insert(INSERT, user.descr)
        self.txtWave.delete(0, END)
        self.txtWave.insert(INSERT, user.onda)  
        self.txtScen.delete(0, END)
        self.txtScen.insert(INSERT, user.cenar)
        self.txtProc.delete(0, END)
        self.txtProc.insert(INSERT, user.proce)
        self.txtName.delete(0, END)
        self.txtName.insert(INSERT, user.descr)
        self.txtTypeg.delete(0, END)
        self.txtTypeg.insert(INSERT, user.tipog)
        self.txtModul.delete(0, END)
        self.txtModul.insert(INSERT, user.modul)
        self.txtVersion.delete(0, END)
        self.txtVersion.insert(INSERT, user.versa)
        self.txtHrs.delete(0, END)
        self.txtHrs.insert(INSERT, user.ust1)
        self.txtHrs2.delete(0, END)
        self.txtHrs2.insert(INSERT, user.ust2)
        self.txtHrsr.delete(0, END)
        self.txtHrsr.insert(INSERT, user.ustr)
        # HRS Sum
        self.txtHrst.config(state=NORMAL)        
        self.txtHrst.delete(0, END)
        # place ZERO at the HRS variables if SPACE/EMPTY
        self.checkZero()
        ustTot = ""     
        ustTot = int(self.txtHrs.get()) + int(self.txtHrs2.get()) + int(self.txtHrsr.get())
        self.txtHrst.insert(INSERT, ustTot)
        self.txtHrst.config(state=DISABLED)
        # HRS variation -- In %
        # ((V2-V1)/V1 × 100
        self.txtHrsv.config(state=NORMAL)
        self.txtHrsv.delete(0, END)
        if self.txtHrs.get() != "0":
            varMet = ""
            varMet = (int(self.txtHrs2.get()) - int(self.txtHrs.get())) / int(self.txtHrs.get()) * 100
            # fix decimals with 2 positions
            varMet = round(varMet, 2)
            self.txtHrsv.insert(INSERT, varMet)
        self.txtHrsv.config(state=DISABLED)
        self.txtCr.delete(0, END)
        self.txtCr.insert(INSERT, user.nrrdm)
        self.txtStatus.delete(0, END)
        self.txtStatus.insert(INSERT, user.stsfu)
        if user.paral == "1":
            self.ckHold.select()
        else:
            self.ckHold.deselect()
        self.txtGolive.delete(0, END)
        self.txtGolive.insert(INSERT, user.glive)
        self.txtSo.delete(0, END)
        self.txtSo.insert(INSERT, user.nross)
        if user.qtdcp == None:
            self.varQtdcp = ""    
        else:          
            self.varQtdcp = user.qtdcp          
        if user.datdv ==  None:
            self.varDatdv = ""
        else:           
            self.varDatdv = user.datdv
        if user.gongo == None:
            self.varGongo = ""
        else:              
            self.varGongo = user.gongo

# Insert data into DB function
    def insertGaps(self):
        user = Gaps()

        user.gapid = self.txtGap.get()
        user.onda = self.txtWave.get()
        user.cenar = self.txtScen.get()
        user.proce = self.txtProc.get()
        user.descr = self.txtName.get()
        user.tipog = self.txtTypeg.get()
        user.modul = self.txtModul.get()
        user.versa = self.txtVersion.get()
        user.ust1 = self.txtHrs.get()
        user.ust2 = self.txtHrs2.get()
        user.ustr = self.txtHrsr.get()
        user.nrrdm = self.txtCr.get()
        user.stsfu = self.txtStatus.get()
        user.paral = ckp.get()
        user.glive = self.txtGolive.get()
        user.nross = self.txtSo.get()
        user.qtdcp = self.varQtdcp
        user.datdv = self.varDatdv
        user.gongo = self.varGongo
        if user.versa in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                user.versa1 = "0" + user.versa
                user.versa = user.versa1

        self.labelMsg["text"] = user.insertGap()

        # I can call this function to clear all fields. But I have to control the labelMsg field - In progress
        #self.eraseFields()

        self.txtGap.delete(0, END)
        self.txtWave.delete(0, END)
        self.txtScen.delete(0, END)
        self.txtProc.delete(0, END)
        self.txtName.delete(0, END)
        self.txtTypeg.delete(0, END)
        self.txtModul.delete(0, END)
        self.txtVersion.delete(0, END)
        self.txtHrs.delete(0, END) 
        self.txtHrs2.delete(0, END)
        self.txtHrsr.delete(0, END)
        self.txtCr.delete(0, END)
        self.txtStatus.delete(0, END)
        self.ckHold.deselect()
        self.txtGolive.delete(0, END)
        self.txtSo.delete(0, END)
        self.varQtdcp = ""
        self.varDatdv = ""
        self.varGongo = ""
        self.txtHrst.config(state=NORMAL)
        self.txtHrst.delete(0, END)
        self.txtHrst.config(state=DISABLED)
        self.txtHrsv.config(state=NORMAL)
        self.txtHrsv.delete(0, END)
        self.txtHrsv.config(state=DISABLED)                          

    # Function to update data
    def updateGap(self):
        user = Gaps()
    
        # the FIX variables are set at the selectGap()   
        gapidu = self.gapidFix
        versau = self.versaFix

        user.gapid = self.txtGap.get()
        user.onda = self.txtWave.get()
        user.cenar = self.txtScen.get()
        user.proce = self.txtProc.get()
        user.descr = self.txtName.get()
        user.tipog = self.txtTypeg.get()
        user.modul = self.txtModul.get()
        user.versa = self.txtVersion.get()
        user.ust1 = self.txtHrs.get()
        user.ust2 = self.txtHrs2.get()
        user.ustr = self.txtHrsr.get()
        user.nrrdm = self.txtCr.get()
        user.stsfu = self.txtStatus.get()
        user.paral = ckp.get()
        user.glive = self.txtGolive.get()
        user.nross = self.txtSo.get()
        user.qtdcp = self.varQtdcp
        user.datdv = self.varDatdv
        user.gongo = self.varGongo
        self.labelMsg["text"] = user.updateGap(gapidu, versau)

        # I can call this function to clear all fields. But I have to control the labelMsg field - In progress
        #self.eraseFields()

        self.txtGap.delete(0, END)
        self.txtWave.delete(0, END)
        self.txtScen.delete(0, END)
        self.txtProc.delete(0, END)
        self.txtName.delete(0, END)
        self.txtTypeg.delete(0, END)
        self.txtModul.delete(0, END)
        self.txtVersion.delete(0, END)
        self.txtHrs.delete(0, END)
        self.txtHrs2.delete(0, END)
        self.txtHrsr.delete(0, END)
        self.txtCr.delete(0, END)
        self.txtStatus.delete(0, END)
        self.ckHold.deselect()
        self.txtGolive.delete(0, END)
        self.txtSo.delete(0, END)
        self.varQtdcp = ""
        self.varDatdv = ""
        self.varGongo = ""
        self.txtHrst.config(state=NORMAL)
        self.txtHrst.delete(0, END)
        self.txtHrst.config(state=DISABLED)
        self.txtHrsv.config(state=NORMAL)
        self.txtHrsv.delete(0, END)
        self.txtHrsv.config(state=DISABLED)

    # This screen is called in order to fill out a justification to delete GAP item
    def deleteGap1(self):
        user = Gaps()

        self.popup = Toplevel(self.frame_aba2, height=20, width=20)
        self.lblPop = Label(self.popup, text="Justify GAP deletion")
        self.lblPop.pack(anchor=CENTER)
        self.txtJust = Entry(self.popup, font=self.fontn, width=50)
        self.txtJust.pack(anchor=CENTER)
        self.bntJust = Button(self.popup, text="Save and Delete", command=self.deleteGap, font=self.fontn, width=10)
        self.bntJust.pack(anchor=CENTER)      

    # Function to delete selected GAP
    def deleteGap(self):
        user = Gaps()

        if self.txtJust.get() == "":
            self.labelMsg["text"] = "Please insert justify for GAP deletion."
            self.popup.destroy()            
        else:
            gapidd = self.txtGap.get()
            versad = self.txtVersion.get()

            user.gapid = self.txtGap.get()
            user.onda = self.txtWave.get()
            user.cenar = self.txtScen.get()
            user.proce = self.txtProc.get()
            user.descr = self.txtName.get()
            user.tipog = self.txtTypeg.get()
            user.modul = self.txtModul.get()
            user.versa = self.txtVersion.get()
            user.ust1 = self.txtHrs.get()
            user.ust2 = self.txtHrs2.get()
            user.ustr = self.txtHrsr.get()
            user.nrrdm = self.txtCr.get()
            user.stsfu = self.txtStatus.get()
            user.paral = ckp.get()
            user.glive = self.txtGolive.get()
            user.nross = self.txtSo.get()
            user.artft = "DELETED"
            user.justf = self.txtJust.get()
            user.qtdcp = self.varQtdcp
            user.datdv = self.varDatdv
            user.gongo = self.varGongo
            self.labelMsg["text"] = user.deleteGap(gapidd,versad)

            # I can call this function to clear all fields. But I have to control the labelMsg field - In progress
            #self.eraseFields()
            self.txtGap.delete(0, END)
            self.txtWave.delete(0, END)
            self.txtScen.delete(0, END)
            self.txtProc.delete(0, END)
            self.txtName.delete(0, END)
            self.txtTypeg.delete(0, END)
            self.txtModul.delete(0, END)
            self.txtVersion.delete(0, END)
            self.txtHrs.delete(0, END) 
            self.txtHrs2.delete(0, END)
            self.txtHrsr.delete(0, END)
            self.txtCr.delete(0, END)
            self.txtStatus.delete(0, END)
            self.txtGolive.delete(0, END)
            self.txtSo.delete(0, END)
            self.ckHold.deselect()
            self.txtJust.delete(0, END)
            self.varQtdcp = ""
            self.varDatdv = ""
            self.varGongo = ""
            self.txtHrst.config(state=NORMAL)
            self.txtHrst.delete(0, END)
            self.txtHrst.config(state=DISABLED)
            self.txtHrsv.config(state=NORMAL)
            self.txtHrsv.delete(0, END)
            self.txtHrsv.config(state=DISABLED)
            self.popup.destroy()

    # Function to clear all fields
    def eraseFields(self):

        self.txtGap.delete(0, END)
        self.txtWave.delete(0, END)
        self.txtScen.delete(0, END)
        self.txtProc.delete(0, END)
        self.txtName.delete(0, END)
        self.txtTypeg.delete(0, END)
        self.ckHold.deselect()
        self.txtModul.delete(0, END)
        self.txtVersion.delete(0, END)
        self.txtHrs.delete(0, END) 
        self.txtHrs2.delete(0, END)
        self.txtHrsr.delete(0, END)
        self.txtCr.delete(0, END)
        self.txtStatus.delete(0, END)
        self.txtGolive.delete(0, END)
        self.txtSo.delete(0, END)
        self.varQtdcp = ""
        self.varDatdv = ""
        self.varGongo = ""
        self.txtHrst.config(state=NORMAL)
        self.txtHrst.delete(0, END)
        self.txtHrst.config(state=DISABLED)
        self.txtHrsv.config(state=NORMAL)
        self.txtHrsv.delete(0, END)
        self.txtHrsv.config(state=DISABLED)
        self.labelMsg["text"] = ""            

    # Open popup screen for additional fields
    def popAdc1(self):
        self.popUpadc = Toplevel(self.frame_aba2, height=150, width=250)
        # Label - Title
        self.lblPopad = Label(self.popUpadc, text="Additional Fields")
        self.lblPopad.place(x=5,y=5)
        # Label - Interface fields number
        self.lblQtdcp = Label(self.popUpadc, font=self.fontn, text="Fields number (int):")
        self.lblQtdcp.place(x=10,y=40)
        # Label - Delivery Date
        self.lblDatdv = Label(self.popUpadc, font=self.fontn, text="Delivery Date:")
        self.lblDatdv.place(x=10,y=60)
        # Label - Is it GO or NOGO GAP
        self.lblGongo = Label(self.popUpadc, font=self.fontn, text="GO / NoGO:")
        self.lblGongo.place(x=10,y=80)        
        # Entry - Interface Fields number
        self.txtQtdcp = Entry(self.popUpadc, font=self.fontn, width=5)
        self.txtQtdcp.place(x=120,y=40)
        # Entry - Delivery Date
        self.txtDatdv = Entry(self.popUpadc, font=self.fontn, width=10)
        self.txtDatdv.place(x=120,y=60)
        # Entry - GO or NOGO
        self.txtGongo = Entry(self.popUpadc, font=self.fontn, width=5)           
        self.txtGongo.place(x=120,y=80)
        # Fill out interface fields number into Additional Fields screen
        self.txtQtdcp.delete(0, END)
        self.txtQtdcp.insert(INSERT, self.varQtdcp)
        # Fill out delivery date into Additional Fields screen        
        self.txtDatdv.delete(0, END)     
        self.txtDatdv.insert(INSERT, self.varDatdv)
        # Fill out GO or NOGO info into Additional Fields screen        
        self.txtGongo.delete(0, END)        
        self.txtGongo.insert(INSERT, self.varGongo)
        # Button - Ok button to close the screen and transfer entry values
        self.bntAdcok = Button(self.popUpadc, text="OK", command=self.popAdc, font=self.fontn, width=6)
        self.bntAdcok.place(x=100,y=110)

    # transfering values from additional fields screen to global variables
    def popAdc(self):
        self.varQtdcp = self.txtQtdcp.get()
        self.varDatdv = self.txtDatdv.get()
        self.varGongo = self.txtGongo.get()
        # destroy popup screen
        self.destroy()

    # popup screen destroy command
    def destroy(self):
        self.popUpadc.destroy()

    # Function to refresh list at TAB 1 for each table/mopdule selected at the combobox
    def refreshList(self):
        user = Gaps()         

        self.count=0

        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        # Open DB to fill up the list        
        banco = Banco()

        c = banco.conexao.cursor()

        # Use the command above to debug the code (this is an example)
        # print("Filter and Table--->", self.filtMod.get(), "-", self.filtTab.get())
        if self.filtTab.get() == "tbgaps":

            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            if self.filtMod.get() == "*":
                self.tree["columns"]=("gapid","onda","descr","versa","glive")
                self.tree.column("gapid", width=100)
                self.tree.column("onda", width=60)
                self.tree.column("descr", width=180)
                self.tree.column("versa", width=60)
                self.tree.column("glive", width=60)
                self.tree.heading("gapid", text="GAP")
                self.tree.heading("onda", text="Wave")
                self.tree.heading("descr", text="Description")        
                self.tree.heading("versa", text="Version")
                self.tree.heading("glive", text="GoLive")
                self.tree["show"] = "headings"              
                querySelect = "select gapid, onda, descr, versa, glive from tbgaps"
                c.execute(querySelect)                       
            else:
                self.tree["columns"]=("gapid","onda","descr","versa","glive")            
                self.tree.column("gapid", width=100)
                self.tree.column("onda", width=60)
                self.tree.column("descr", width=180)
                self.tree.column("versa", width=60)
                self.tree.column("glive", width=60)
                self.tree.heading("gapid", text="GAP")
                self.tree.heading("onda", text="Wave")
                self.tree.heading("descr", text="Description")        
                self.tree.heading("versa", text="Version")
                self.tree.heading("glive", text="GoLive")
                self.tree["show"] = "headings"             
                c.execute("select gapid, onda, descr, versa, glive from tbgaps where modul=(?)", (self.filtMod.get(),))            
            for row in c:
                self.count += 1
                self.tree.insert("", END, text="GAP", values=row)          
                self.tree.pack()
        elif self.filtTab.get() == "tbins":
            if self.filtMod.get() == "*":
                self.tree["columns"]=("gapid","descr","versa")
                self.tree.column("gapid", width=100)
                self.tree.column("descr", width=280)
                self.tree.column("versa", width=70)
                self.tree.heading("gapid", text="GAP")
                self.tree.heading("descr", text="Description")        
                self.tree.heading("versa", text="Version")
                self.tree["show"] = "headings"              
                querySelect = "select gapid, descr, versa from tbins"
                c.execute(querySelect)                       
            else:
                self.tree["columns"]=("gapid","descr","versa")            
                self.tree.column("gapid", width=100)
                self.tree.column("descr", width=280)
                self.tree.column("versa", width=70)
                self.tree.heading("gapid", text="GAP")
                self.tree.heading("descr", text="Description")        
                self.tree.heading("versa", text="Version")
                self.tree["show"] = "headings"             
                c.execute("select gapid, descr, versa from tbins where modul=(?)", (self.filtMod.get(),))            
            for row in c:
                self.count += 1
                self.tree.insert("", END, text="GAP", values=row)          
                self.tree.pack()        
        elif self.filtTab.get() == "tbdel":
            if self.filtMod.get() == "*":
                self.tree["columns"]=("gapid","descr","versa","justf")
                self.tree.column("gapid", width=100)
                self.tree.column("descr", width=180)
                self.tree.column("versa", width=50)
                self.tree.column("justf", width=110)
                self.tree.heading("gapid", text="GAP")
                self.tree.heading("descr", text="Description")        
                self.tree.heading("versa", text="Version")
                self.tree.heading("justf", text="Justify")
                self.tree["show"] = "headings"              
                querySelect = "select gapid, descr, versa, justf from tbdel"
                c.execute(querySelect)                       
            else:
                self.tree["columns"]=("gapid","descr","versa","justf")            
                self.tree.column("gapid", width=100)
                self.tree.column("descr", width=180)
                self.tree.column("versa", width=50)
                self.tree.column("justf", width=110)
                self.tree.heading("gapid", text="GAP")
                self.tree.heading("descr", text="Description")        
                self.tree.heading("versa", text="Version")
                self.tree.heading("justf", text="Justify")
                self.tree["show"] = "headings"             
                c.execute("select gapid, descr, versa, justf from tbdel where modul=(?)", (self.filtMod.get(),))            
            for row in c:
                self.count += 1
                self.tree.insert("", END, text="GAP", values=row)          
                self.tree.pack()

        c.close()

        self.countVar["text"] = self.count

    # Export to CSV and delete tables
    def ExecCommand(self):
        banco = Banco()

        c = banco.conexao.cursor()
        # download GAPS      
        if v.get() == 1:
            query='select * from tbgaps'
            c.execute(query)
            with open(self.path.get() + "tbgaps.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)                
        # download Delta
        if v.get() == 2:
            query='select * from tbins'
            c.execute(query)
            with open(self.path.get() + "tbins.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)
            query='select * from tbdel'
            c.execute(query)
            with open(self.path.get() + "tbdel.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)                
        # download todas as tabelas para backup
        if v.get() == 3:
            #GAPS 
            query='select * from tbgaps'
            c.execute(query)
            with open(self.path.get() + "tbgaps_bckp.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)              
            # INSERTED
            query='select * from tbins'
            c.execute(query)
            with open(self.path.get() + "tbins_bckp.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)             
            #DELETED
            query='select * from tbdel'
            c.execute(query)
            with open(self.path.get() + "tbdel_bckp.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)               
            #MODULES
            query='select * from tbmod'
            c.execute(query)
            with open(self.path.get() + "tbmod_bckp.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)
            #STATUS
            query='select * from tbsts'
            c.execute(query)
            with open(self.path.get() + "tbsts_bckp.csv", "w", newline='') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow([i[0] for i in c.description])
                 csv_writer.writerows(c)                                 
        # Delete command options
        if v.get() == 4 or v.get() == 5 or v.get() == 6:
            self.popupDel()

        c.close()

    # Description for each radiobutton selected - bottom message TAB 3
    def radioCheck(self):
        if v.get() == 1:
            self.labelMsg3["text"] = "Export GAPs list. File name: TBGAPS.CSV"
        if v.get() == 2:
            self.labelMsg3["text"] = "Export Delta (inserted and deleted). File name: TBDEL.CSV and TBINS.CSV"
        if v.get() == 3:
            self.labelMsg3["text"] = "Perform total backup. TBGAPS, TBINS, TBDEL, TBMOD and TBSTS.CSV"
        if v.get() == 4:
            self.labelMsg3["text"] = "Delete GAP table."
        if v.get() == 5:
            self.labelMsg3["text"] = "Delete Delta tables."
        if v.get() == 6:
            self.labelMsg3["text"] = "Delete all tables."

    # confirmation screeen
    def popupDel(self):
        self.popdel = Toplevel(self.frame_aba3, height=20, width=20)
        self.lblPopdel1 = Label(self.popdel, text="Data will be erased.")
        self.lblPopdel1.pack(anchor=CENTER)
        self.lblPopdel2 = Label(self.popdel, text="Are you sure you want to continue?")
        self.lblPopdel2.pack(anchor=CENTER)        
        self.bntSim = Button(self.popdel, text="Yes", command=lambda: self.OnButtonClick(1), font=self.fontn, width=8)
        self.bntSim.pack(anchor=CENTER)
        self.bntNao = Button(self.popdel, text="No", command=lambda: self.OnButtonClick(2), font=self.fontn, width=8)
        self.bntNao.pack(anchor=CENTER)

    # Function to perform DELETION from popupDel Function
    def OnButtonClick(self, btnid):
        banco = Banco()

        c = banco.conexao.cursor()
        # Button YES
        if btnid == 1:
            if v.get() == 4:
                query='delete from tbgaps'
                c.execute(query)
                banco.conexao.commit()
            if v.get() == 5:
                query='delete from tbdel'
                c.execute(query)
                query='delete from tbins'
                c.execute(query)
                banco.conexao.commit()
            if v.get() == 6:
                query='delete from tbgaps'
                c.execute(query)
                query='delete from tbdel'
                c.execute(query)
                query='delete from tbins'
                c.execute(query)
                query='delete from tbmod'
                c.execute(query)
                query='delete from tbsts'
                c.execute(query)
                banco.conexao.commit()

            self.popdel.destroy()
            self.labelMsg3["text"] = "Success."
        # Button No 
        elif btnid == 2:
                self.popdel.destroy()
                self.labelMsg3["text"] = "Canceled."

        c.close()

    #Function to recover data from STATUS table and use for combobox itens        
    def srchStatus(self):
        banco = Banco()

        c = banco.conexao.cursor() 
        query='select * from tbsts'
        c.execute(query)

        data=[]

        for row in c.fetchall():
            data.append(row[0])

        return data        

        c.close()
    
    #Function to recover data from MODULE table and use for combobox itens
    def srchModul(self):
        banco = Banco()

        c = banco.conexao.cursor() 
        query='select * from tbmod'
        c.execute(query)

        data=[]

        for row in c.fetchall():
            data.append(row[0])

        return data        

        c.close()

    # function to check if fields are blank and then fill out with ZERO (INT CALCULATION)
    def checkZero(self):
        if self.txtHrs.get() == "":
            self.txtHrs.insert(INSERT, "0")

        if self.txtHrs2.get() == "":
            self.txtHrs2.insert(INSERT, "0")     

        if self.txtHrsr.get() == "":
            self.txtHrsr.insert(INSERT, "0")                    

root = Tk()
v = IntVar()
modul = StringVar()
modul_db = StringVar()
tipog = StringVar()
table = StringVar()
tableAd = StringVar()
status = StringVar()
ckp = StringVar()
ustTot = StringVar()
varMet = StringVar()
sizex = 480
sizey = 272
posx  = 5
posy  = 5
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
root.title("GAP Manager")
Main(root)
root.mainloop()