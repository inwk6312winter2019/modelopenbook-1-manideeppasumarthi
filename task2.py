def replace_list():
    try:
        fopen = open("running-config.cfg",'r')
    #fopen = fopen.read()
    #fopen = fopen.split("\n")

        fwrite = open("running-config-new.cfg", "w")

        for v in fopen:
            print(v)
            if "192" in v:
                v = v.replace("255" , "10")
                fwrite.write(v)
            elif "172" in v:
                v = v.replace("172" , "10")
                fwrite.write(v)
            elif "255.255.0.0" in v:
                v = v.replace("255.255.0.0" , "255.0.0.0")
                fwrite.write(v)
            elif "255.255.255.0" in v:
                v = v.replace("255.255.255.0" , "255.0.0.0")
                fwrite.write(v)
            else:
                fwrite.write(v)
    except:
        print("gotit")  


replace_list()
