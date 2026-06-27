import time, os, logging, sys, json, base64


print("---------- KEEP YOUR DATA SAFE ----------")


def logger():
    log=logging.getLogger("ACTIVITY")
    log.setLevel(logging.INFO)

    adr=os.getcwd()
    adress=os.path.join(adr,"Activity.log")

    handler=logging.FileHandler(adress)

    frmt=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    handler.setFormatter(frmt)
    log.addHandler(handler)

    return log,adress


def get_info(log,adress):
    try:
        name=input("NAME:  \n").upper()
        time.sleep(.5)
        contact=input("CONTACT: \n").upper()
        time.sleep(.5)
        location=input("LOCATION: \n").upper()
        time.sleep(.5)
        info=input("ADDITIONAL INFO.:\n").upper()
        time_now=time.ctime()
        while True:
            choice=input("DO YOU WANT TO CHOOSE DEFAULT ADDRESS? Y/N").upper()
            if choice=="Y":
                directory=os.getcwd()
                path=os.path.join(directory, "Data.txt")
                break
            elif choice=="N":
                while True:
                    folder=input("DIRECTORY NAME :").strip('"').strip()
                    if os.path.isdir(folder):
                        file_name=input("PLEASE ENTER THE FILE NAME: ").strip().strip('"')
                        path=os.path.join(folder,file_name)
                        print("CHECKED.")
                        break
                    else:
                        print("NO PATH EXISTS. PLEASE CHECK THE DIRECTORY NAME.")
                break
            else:
                print("INVAID CHOICE. PLEASE CHOOSE Y OR N.")
    except:
        print("SOMETHING WENT WRONG...")
    else:
        print("PLEASE CHECK YOUR DATA.")
        print(time_now)
        print(f"NAME : {name}")
        print(f"CONTACT : {contact}")
        print(f"LOCATION : {location}")
        print(f"INFO. : {info}")
        print(f"PATH : {path}")
        print(f"LOG FILE ADRESS: {adress}")
        print("------- ------- ------- -------")
        input("PLEASE PRESS ENTER.")
        time.sleep(1)
    return name,contact,location,info,time_now,path
    

def encoding_data(record,path,log):
    file=json.dumps(record)
    print("-------- -------- --------")
    print(f"ORIGINAL DATA: {file}")
    time.sleep(.3)
    text=file.encode("utf-8")
    encrypted=base64.b64encode(text)
    decrypted=encrypted.decode("utf-8")
    print("-------- -------- --------")
    print(f"ENCODED DATA: {decrypted}")
    print("-------- -------- --------")
    time.sleep(.3)
    print("DATA SAVED SUCESSFULLY.")
    print(f"YOUR DATA IS SAVED IN {path}")
    return decrypted

def saving_data(decrypted,path,log):
    with open(path,"a") as f:
        f.writelines(f"{decrypted} \n")

def choice_(log):
    question=input("DO YOU WANT TO ENCODE OR DECODE? ").upper().strip()
    if question=="ENCODE":
        name,contact,location,info,time_now,path=get_info(log,adress)
        record={
            "NAME ": name,
            "CONTACT ": contact,
            "LOCATION ": location,
            "ADDITIONAL INFO. ": info,
            "TIME ": time_now,
            }
        decrypted=encoding_data(record,path,log)
        saving_data(decrypted,path,log)
        log.info(f"------DATA ENCODED IN: {path}")
        
        
    elif question=="DECODE":
        while True:
            try:
                file_name=input("PLEASE ENTER THE FILE ADDRESS: ").strip().strip('"')
                if os.path.isfile(file_name):
                    print("FILE EXISTS.")
                else:
                    raise Exception("NO ADDRESS FOUND.")
            except Exception as e:
                print("ERROR: ",e)
                log.warning(f"------{e}:{file_name}")
            else:
                try:
                    with open (file_name,"r") as file:
                        lines=file.readlines()
                        for line in lines:
                            encoded=line.strip().encode("utf-8")
                            decoded=base64.b64decode(encoded)
                            original=decoded.decode("utf-8")
                            print(original)
                        log.info(f"------DATA DECODED FROM: {file_name}")
                except:
                    print("CORRUPTED LINE SKIPPED.")
                else:
                    break
    else:
        print("INVALID OPTION.")
        log.warning("------INVALiD OPTION SELECTED.")
            
log,adress=logger()
while True:
    choice_(log)
    again=input("DO YOU WANT TO CONTINUE? Y/N").upper().strip()
    if again in("Y" , "YES"):
        choice_(log)
    else:
        print("EXITTING...")
        time.sleep(1.3)
        exit()
        
        
