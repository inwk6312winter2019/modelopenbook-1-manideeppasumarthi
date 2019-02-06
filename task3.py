def list_ifname_ip():
  t = dict()
  
  fin = open("running-config.cfg","r")
  for word in fin:
    if "no" not in word:
      word = word.strip()
      if "ip address" in word:
        tmp = word.split()
        t[tmp[1]]=(tmp[2],tmp[3])
        print(t)

print(list_ifname_ip()
