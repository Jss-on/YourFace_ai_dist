from backend import *
import os
import numpy as np

def add_user_data(personName: str, imageFiles: list):
    bk = Utility(personName, imageFiles)
    file_check = os.path.isfile('data.npz')
    if not file_check:
        print("step1")
        user_enc = {}
        encoding_list = []
        for image in imageFiles:
            im = bk.encode(image)
            if im == "no_face":
                return "no_face"
            else:
                encoding_list.append(im)
        user_enc[personName] = encoding_list
        bk.savedata(user_enc)
        print(np.load("data.npz").files)
        
        print("{} is registered".format(personName))
    elif bk.userHasEnc(personName):
        print("step2")
        total_enc = {}
        encoding_list = []
        #breakpoint()
        #user_prev_enc = np.load('data.npz',allow_pickle=True)
        user_prev_enc = bk.get_user_encoding(personName) #list
        user_prev_enc1 = []
        for uenc in user_prev_enc:
            user_prev_enc1.append(uenc)
        #print(type(user_prev_enc))
        #print("prev")
        
        
        for image in imageFiles:
            im = bk.encode(image)
            if im == "no_face":
                return "no_face"
            else:
                
                if not any((im == x).all() for x in user_prev_enc1):                
                    encoding_list.append(im)
                else:
                    print("Image: {} already exists.".format(image))
                    return "image_exist"
        #user_enc[personName] = encoding_list #dict
        
        for arr in user_prev_enc:
            encoding_list.append(arr)
        
        
        all_enc = bk.get_all_enc() #ndarray
        all_users = all_enc.files
        #print(all_users)
        #breakpoint()
        for user in all_users:
            if not(user == personName):
                temp_list = []
                temp_ndarr = bk.get_user_encoding(user)
                for temp_arr in temp_ndarr:
                    temp_list.append(temp_arr)
                total_enc[user] = temp_list
        
        total_enc[personName] = encoding_list
        
        bk.savedata(total_enc)
        print(np.load("data.npz").files)
        print("{} is registered".format(personName))
    else:
        total_enc = {}
        encoding_list = []
        print("step3")
        for image in imageFiles:
            im = bk.encode(image)
            if im == "no_face":
                return "no_face"
            else:
                encoding_list.append(im)
            
           

       
        

        
        all_enc = bk.get_all_enc() #ndarray
        all_users = all_enc.files
        #print(all_users)
        #breakpoint()
        for user in all_users:
            #if not(user == personName):
            temp_list = []
            temp_ndarr = bk.get_user_encoding(user)
            for temp_arr in temp_ndarr:
                temp_list.append(temp_arr)
            total_enc[user] = temp_list

        total_enc[personName] = encoding_list
        
        
    

        bk.savedata(total_enc)
        print(np.load("data.npz").files)
        print("{} is registered".format(personName))


def all_person_names(personName,fname):
    bk = Utility(personName,fname)
    users_data = bk.load_user_data()
    return list(users_data.keys())

def deleteUsers(names:list):
    total_enc = {}
    all_enc = np.load('data.npz',allow_pickle = True) #ndarray
    all_users = all_enc.files
    #print(all_users)
    #breakpoint()
    
    for user in all_users:
        #if not(user == personName):
        temp_list = []
        temp_ndarr = all_enc[user]
        for temp_arr in temp_ndarr:
            temp_list.append(temp_arr)
        total_enc[user] = temp_list
    for u_del in names: #u_del means user name to be deleted
        total_enc.pop(u_del)
    
    np.savez_compressed('data.npz',**total_enc)
    print(np.load("data.npz").files)
def runWebCam(source):
    vd = videoHandler(0)
    vd.setupWebcam()
    pass

