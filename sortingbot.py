# -*- coding: cp1252 -*-

from Tkinter import *
import tkMessageBox
from estrazione import *


def start_process():

    #provenienti dai campi entry
    percorso = path.get()
    folder=newfldr.get()
    mankey=keyO.get()
    rinkey=keyM.get()
    newnm=newname.get()
    estensione=ext.get()
    
    #profondita ricerca
    dpt= depth.get()
    
    #tutti i booleani del campo opzioni
    estr = checkestr.get()
    auto = checkauto.get()
    man=checkman.get()
    rin=checkrin.get()

    msg="Questo è il percorso che hai indicato: "+percorso+".\nOperare su una directory diversa da quella voluta può far diventare il tuo computer un TERMINATOR in grado di ucciderti"

    sicuro = tkMessageBox.askyesno(title="Sicuro di proseguire?", message=msg)

    #qui vengono definite le operazioni che il programma esegue in base alle opzioni impostate
    if (sicuro):
        if((estr==False) and (auto==False) and (man==False) and (rin==False)):
           tkMessageBox.showwarning(message="Devi specificare almeno un'opzione")
        if(estr or auto):
            if (estr and auto):
                appiattimento(percorso,dpt)
                ordina_aut(percorso)
            if (estr):
                appiattimento(percorso,dpt)
            if (auto):
                ordina_aut(percorso)
            if(rin or man):
                tkMessageBox.showwarning(message="Ordinamento manuale e Ridenominazio Files devono essere eseguiti singolarmente")
                return
        if(rin or man):
            if(rin and man):
                tkMessageBox.showwarning(message="Ordinamento manuale e Ridenominazio Files devono essere eseguiti singolarmente")
                return
            if(rin):
                rinomina(percorso,rinkey,newnm,estensione)
            if(man):
                ordina_man(percorso,folder,mankey)    
    tkMessageBox.showinfo(message="Operazione Terminata")   
    

finestra = Tk()
finestra.geometry("800x400+600+300")

finestra.title("Ordinamento Cartelle")

#creo i labelframe per i widget
opzioni= LabelFrame(finestra,text="Options",padx=5,pady=5)
opzioni.pack(side=RIGHT,fill=Y, expand=1)

pathname = LabelFrame(finestra,text="Pathname Assoluto",padx=5,pady=5)
pathname.pack(fill=BOTH, expand=1)

profondita = LabelFrame(finestra,text="Profondità Estrazione",padx=5,pady=5)
profondita.pack(fill=BOTH, expand=1)

Ordi_man = LabelFrame(finestra,text="Ordinamento Manuale",padx=5,pady=5)
Ordi_man.pack(fill=BOTH, expand=1)

Rinomina = LabelFrame(finestra,text="Ridenominazione Files",padx=5,pady=5)
Rinomina.pack(fill=BOTH, expand=1)

avvio=LabelFrame(finestra,text="Start Process",padx=5,pady=5)
avvio.pack(fill=BOTH, expand=1)

#Casella inserimento pathname
path = StringVar()
casella_testo = Entry(pathname,textvariable = path,width=60).pack(side=LEFT,fill=BOTH,expand=1)

#creo i widget per le opzioni del programma
checkestr=IntVar()
checkauto=IntVar()
checkman=IntVar()
checkrin=IntVar()

radioEstrazione=Checkbutton(opzioni,text="Abilita Estrazione Files",variable=checkestr).grid(row=0,sticky=W)
radioOrdina=Checkbutton(opzioni,text="Abilita Ordinamento Auto",variable=checkauto).grid(row=1,sticky=W)
radioOrdman=Checkbutton(opzioni,text="Abilita Ordinamento Manuale",variable=checkman).grid(row=2,sticky=W)
radioRin=Checkbutton(opzioni,text="Abilita Ridenominazione Files",variable=checkrin).grid(row=3,sticky=W)

#Spinbox per definire la profondita di estrazione
depth=IntVar()
spindepth=Spinbox(profondita,from_=1, to = 50, textvariable=depth,width=60).pack(fill=BOTH,expand=1)

#Inserisco i campi per ordinamento manuale
newfldr=StringVar()
keyO=StringVar()

testoO1=Label(Ordi_man,text="Inserisci nome cartella: ").grid(row=0,column=0,sticky=W)
entryfldr=Entry(Ordi_man,textvariable = newfldr,width=30).grid(row=0,column=1,sticky=E)

testoO2=Label(Ordi_man,text="Inserisci chiave raggruppamento: ").grid(row=1,column=0,sticky=W)
entrykeyO=Entry(Ordi_man,textvariable = keyO,width=30).grid(row=1,column=1,sticky=E)

#inserisco i campi per ridenominazione files
ext=StringVar()
keyM=StringVar()
newname=StringVar()

testoM1=Label(Rinomina,text="Inserisci chiave raggruppamento: ").grid(row=0,column=0,sticky=W)
entryfldr=Entry(Rinomina,textvariable = keyM,width=30).grid(row=0,column=1,sticky=E)

testoM2=Label(Rinomina,text="Inserisci nuovo nome files: ").grid(row=1,column=0,sticky=W)
entrykeyO=Entry(Rinomina,textvariable = newname,width=30).grid(row=1,column=1,sticky=E)

testoM2=Label(Rinomina,text="Inserisci estensione files: ").grid(row=2,column=0,sticky=W)
entrykeyO=Entry(Rinomina,textvariable = ext,width=30).grid(row=2,column=1,sticky=E)

#bottone per far partire il programma
bottone = Button(avvio,text="START",bg="green",command=start_process).pack(fill=BOTH)

finestra.mainloop()
