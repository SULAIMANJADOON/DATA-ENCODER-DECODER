import logging, os, re, time, json, base64

def log():
    adress=os.getcwd()
    path=os.path.join(adress ,"Activity.log")

    logging.basicConfig(filename=path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    
def main():
    while True:
        choice=input("DO YOU WANT TO ENCODE OR DECODE? ").upper().strip()
        if choice.startswith("E"):
            return choice
        elif choice.startswith("D"):
            return choice
        else:
            print("ERROR: Invalid Option.")

def encode(choice):
    if choice.startswith("E"):
        while True:
            path_select=input("DO YOU WANT TO CHOOSE DEFAULT PATH: YES/NO").upper().strip()
            if path_select.startswith("Y"):
                adress=os.getcwd()
                path=os.path.join(adress,"Enc_Data.txt")
                break
            elif path_select.startswith("N"):
                while True:
                    adress=input("ENTER THE DIRECTORY NAME: ").strip().strip('"')
                    if os.path.isdir(adress):
                        while True:
                            path=input("PLEASE ENTER THE FILE NAME: ").strip('"')
                            if re.match(r"^[A-Za-z0-9._-]+$",path):
                                print("ADRESS VERIFIED.")
                                break
                                
                            else:
                                print("ERROR: Invalid Filename.")
                                print("ONLY A-Z a-z 0-9 ._- CHARACTERS ARE ALLOWED")
                        break
                    else:
                        print("ERROR: No Directory Found.")
                break
            else:
                print("ERROR: Invalid Choice")

        name=input("NAME:")
        contact=input("CONTACT:")
        location=input("LOCATION:")
        additional_info=input("ADDITIONAL INFORMATION:")

        data={"TIME":time.ctime(),"NAME":name,"CONTACT":contact,"LOCATION":location,"ADDITIONAL INFORMATION":additional_info}

        print("PLEASE CHECK YOUR DATA.")
        print(data)
        print(f"FILE ADRESS: {path} ")
        input("PLEASE PRESS ENTER.")

        data=json.dumps(data)
        encode=data.encode("utf-8")
        encoded=base64.b64encode(encode)
        decode=encoded.decode("utf-8")

        with open (path,"a") as f:
            f.write(decode+"\n")
            time.sleep(2)
            print("YOUR DATA IS ENCODED SUCESSFULLY")
            logging.info(f"DATA ENCODED IN {path} ")

def decode(choice):
    if choice.startswith("D"):
        while True:
            line=""
            path=input("PLEASE ENTER THE FILE ADRESS: ").strip().strip('"')
            if os.path.isfile(path):
                with open (path,"r")as f:
                    lines=f.readlines()
                    try:
                        for line in lines:
                            if not line:
                                continue
                            
                    except Exception as e:
                        print("ERROR",e)
                        print("YOUR FILE MAY HAVE SOME CORRUPTED LINES.")
                    else:
                        line=line.strip()
                        encode=line.encode("utf-8")
                        decoded=base64.b64decode(encode,validate=True)
                        decode=decoded.decode("utf-8")
                        time.sleep(1)
                        print(decode)
                        time.sleep(1)
                        print("YOUR DATA IS DECODED SUCESSFULLY")
                        logging.info(f"DATA DECODED SUCESSFULLY FROM {path} ")
                        return decode
            else:
                print("ERROR: No file found")

            
        
            



log()
choice=main()
encode(choice)
decode=decode(choice)
while True:
    question=input("DO YOU WANT TO QUIT OR CONTINUE? ").strip().upper()
    if question.startswith("C"):
        log()
        choice=main()
        encode(choice)
        decode=decode(choice)
    elif question.startswith("E"):
        print("EXITING...")
        time.sleep(2)
        exit()
    else:
        print("ERROR: Invalid option.")
        print("PLEASE ANSWER IN QUIT OR CONTINUE.")
        time.sleep(2)
        
