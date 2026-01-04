# CHANGE THE CODE INTO GUI BY MAKING THEM FUNCTIONS!

import os 
import shutil

def load_extensions():
    with open("extensions/image_extension.txt") as f :
        image_extension = f.read().split()
    with open("extensions/audio_extension.txt") as f :
        audio_extension = f.read().split()
    with open("extensions/video_extension.txt") as f :
        video_extension = f.read().split()
    with open("extensions/document_extension.txt") as f :
        doc_extension = f.read().split()
    with open("extensions/app_extension.txt") as f :
        app_extension = f.read().split()
    return image_extension, audio_extension, video_extension, doc_extension, app_extension

def sort1(loc:str) :
    total = os.listdir(loc)
    imgfold = []
    vidfold = []
    docsfold = []
    audfold = []
    appfold = []
    extrasfold = []
    img_extension, audio_extension, video_extension, document_extension, app_extension = load_extensions()

    try :
        for i in total : 
            if not os.path.isfile(f"{loc}/{i}") :
                file_list = os.listdir(f"{loc}/{i}")
                if len(file_list) == 0 :
                    os.rmdir(f"{loc}/{i}")
            j = i.split(".")[-1].lower()
            if j in img_extension : 
                imgfold.append(i)
            elif j in video_extension : 
                vidfold.append(i)
            elif j in document_extension : 
                docsfold.append(i)
            elif j in app_extension : 
                appfold.append(i)
            elif j in audio_extension : 
                audfold.append(i)
            else : 
                extrasfold.append(i)

        if len(imgfold) > 0 : 
            if not os.path.exists(f"{loc}/images_"):
                os.mkdir(f"{loc}/images_")   
            for x in imgfold : 
                shutil.move(f"{loc}/{x}", f"{loc}/images_/{x}")     
        if len(vidfold) > 0 : 
            if not os.path.exists(f"{loc}/videos_"):
                os.mkdir(f"{loc}/videos_")   
            for x in vidfold : 
                shutil.move(f"{loc}/{x}", f"{loc}/videos_/{x}")     
        if len(docsfold) > 0 : 
            if not os.path.exists(f"{loc}/documents_"):
                os.mkdir(f"{loc}/documents_")   
            for x in docsfold : 
                shutil.move(f"{loc}/{x}", f"{loc}/documents_/{x}")     
        if len(appfold) > 0 : 
            if not os.path.exists(f"{loc}/images_"):
                os.mkdir(f"{loc}/apps_")   
            for x in appfold : 
                shutil.move(f"{loc}/{x}", f"{loc}/apps_/{x}")     
        if len(audfold) > 0 : 
            if not os.path.exists(f"{loc}/images_"):
                os.mkdir(f"{loc}/audios_")    
            for x in audfold : 
                shutil.move(f"{loc}/{x}", f"{loc}/audios_/{x}")    
        if len(extrasfold) > 0 : 
            if not os.path.exists(f"{loc}/images_"):
                os.mkdir(f"{loc}/extras_")     
            for x in extrasfold : 
                shutil.move(f"{loc}/{x}", f"{loc}/extras_/{x}")   
            
    except Exception as e : 
        return f"\nLooks like some error occured. Here what you can do : 1. Make sure you entered the correct directory without any typo.\n2. See if you are pointing to the correct directory. \nIf you are still getting the error then here's what the error message says : {e}\n"        

def sort2(loc:str, option:int, keyword:str) :
    # 1. start with keyword
    # 2. ends with keyword
    # 3. contains keyword    
    allfiles = os.listdir(loc)
    if not os.path.exists(f"{loc}/{keyword}") :
        os.mkdir(f"{loc}/{keyword}")
    if option == 1 :
        lis = list(filter(lambda x: x.split(".")[0].startswith(keyword), allfiles))
    elif option == 2 :
        lis = list(filter(lambda x:x.split(".")[0].endswith(keyword), allfiles))
    elif option == 3:
        lis = list(filter(lambda x: keyword in x.split(".")[0], allfiles))
    if len(lis) != 0 :
        for i in lis :
            shutil.move(f"{loc}/{i}", f"{loc}/{keyword}/{i}")
    return lis

if __name__ == "__main__" :
    try :
        loc = input("Enter a valid directory path : ")
        loc = loc.replace("\\", "/")
        total = os.listdir(loc)
        print(f"The total number of files are : {len(total)}")
        if len(total) == 0 :
            exit()
        print("1. Sort by type\n2. Sort by keyword pattern")
        choice = int(input("ENTER NUMBER OF CHOICE : "))
        if choice == 1 :
            sort1(loc)
        elif choice == 2 :
            sort2(loc, int(input()), input())
    except Exception as e : 
        print(f"\nLooks like some error occured. Here what you can do : \n1. Check if there is no folder named with images, audios, videos, apps, documents or extras.\n2. Make sure you entered the correct directory without any typo.\n3. See if you are pointing to the correct directory. \nIf you are still getting the error then here's what the error message says : {e}\n")   
        exit()


# DIVIDE FILE INTO MORE FUNCTIONS

    
                
            
