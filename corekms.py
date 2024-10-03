import os
#import progressbar
#print("python windows activation v.1.0.0, Education, Pro, Pro Workstation Users only")
#print("using kms server:" + server)
#print("please make shure that you run this as admin")
#system_ver=input("please select system version: Windows Education[1] ; Windows Professional[2] ; Windows Professional Workstation[3]:")
def activationcore(system_ver, server="kms.digiboy.ir"):
    match system_ver:
        case 1:
            #with progressbar.ProgressBar(max_value=3) as bar:
            os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
            os.system("slmgr /skms "+server)
            os.system("slmgr /ato")
            return 0
        case 2:
            
            os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")           
            os.system("slmgr /skms "+server)            
            os.system("slmgr /ato")
            return 0
        case 3:
            
            os.system("slmgr /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J")
            os.system("slmgr /skms "+server)
            os.system("slmgr /ato")
            return 0