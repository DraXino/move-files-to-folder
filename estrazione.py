import os
import shutil
import glob

def appiattimento(pathname,profondita):
    while(profondita>=0):   #Determino quante volte eseguire l'iterazione
        try:
            pathlist=os.listdir(pathname) #esploro la directory fornita
        except:
            #print "Errore: la directory fornita non va bene"
            break
        for i in pathlist:
                newpath=os.path.join(pathname,i) #creo un nuovo pathname  
                try:
                    newpathlist=os.listdir(newpath)
                except:
                    continue #se listdir da errore proseguo nel ciclo
                for j in newpathlist:
                    src=os.path.join(newpath,j)
                    dst=pathname
                    try:
                        shutil.move(src,dst)    #sposto file e cartelle dalla sub-directory a quella che la contiene
                    except:
                        continue
                    #print "Copiato ",src," in", dst 
        profondita-=1
        #print "profondita", profondita
    deletedir(pathname)
    #return pathname

def ordina_aut(pathname):
    try:
        os.mkdir(os.path.join(pathname,"Musica"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Video"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Documenti"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Immagini"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Programmi"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Archivi"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Torrent"))
    except:
        pass
    try:
        os.mkdir(os.path.join(pathname,"Codice"))
    except:
        pass

    elenco=os.listdir(pathname)
    
    for i in elenco:
        try:
            percorso,ext = os.path.splitext(i) # controllo l'estensione del file
        except:
            continue
        if(ext==".mkv" or ext==".mp4" or ext==".flv" or ext==".avi" or ext==".mov" or ext==".mpeg" or ext==".MP4"):
            dst=os.path.join(pathname,"Video")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue

        if(ext==".mp3" or ext==".m4a"):
            dst=os.path.join(pathname,"Musica")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue

        if(ext==".pdf" or ext==".odt" or ext==".txt" or ext==".docx" or ext==".rtf" or ext==".odt" or ext==".sxw"):
            dst=os.path.join(pathname,"Documenti")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue
            
        if(ext==".msi" or ext==".exe"):
            dst=os.path.join(pathname,"Programmi")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue
            
        if(ext==".jpg" or ext==".png" or ext==".bmp" or ext==".gif" or ext==".jpeg"):
            dst=os.path.join(pathname,"Immagini")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue
            
        if(ext==".rar" or ext==".zip"):
            dst=os.path.join(pathname,"Archivi")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue
            
        if(ext==".torrent"):
            dst=os.path.join(pathname,"Torrent")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue

        if(ext==".c" or ext==".h" or ext==".py"):
            dst=os.path.join(pathname,"Codice")
            src=os.path.join(pathname,i)
            try:
                shutil.move(src,dst)
            except:
                continue
    deletedir(pathname)
    
            
def deletedir(pathname):
    elenco=os.listdir(pathname)
    for i in elenco:
        try:
            os.rmdir(pathname+"/"+i)
        except:
            continue

def ordina_man(pathname,newfldr,chiave):
    try:
        os.mkdir(os.path.join(pathname,newfldr))
    except:
        pass
    #metto il lista i file che corrispondono alla chiave di ricerca
    lista=glob.glob(os.path.join(pathname,"*"+chiave+"*")) 
    #print lista
    for i in lista:
        if(os.path.isfile(os.path.join(pathname,i))): #verifico di spostare solo i file
            src=os.path.join(pathname,i)
            dst=os.path.join(pathname,newfldr)
            shutil.move(src,dst)
            
def rinomina(pathname,chiave,newnm,ext):
    lista=glob.glob(os.path.join(pathname,"*"+chiave+"*"))
    #print lista
    num=0;
    for i in lista:
        if(os.path.isfile(os.path.join(pathname,i))):
            old=os.path.join(pathname,i)
            new=os.path.join(pathname,newnm+"_"+str(num)+"."+ext)
            try:
                os.rename(old,new)
            except:
                continue
            num+=1
"""   
argument=input ("Dimmi la profodita' di appiattimento dell'albero: ")
pathname=appiattimento(argument)
flag=raw_input ("Vuoi ordinare in cartelle i file una volta estratti? (Y/N)")
if(flag=='Y'):
    ordina(pathname)
else:
    deletedir(pathname)
print "GOOD JOB"
"""
