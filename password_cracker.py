import hashlib

hash = hashlib.sha1("password".encode()).hexdigest()

def crack_sha1_hash(hash, use_salts=False):
  fhandlePW = open("top-10000-passwords.txt", "r")
  fhandleSalt = open("known-salts.txt", "r") if use_salts else None

  for line in fhandlePW:
    if use_salts:
      # reset the file pointer to the beginning of the file
      fhandleSalt.seek(0)
      for salt in fhandleSalt:
        h1 = hashlib.sha1((salt.strip() + line.strip()).encode("UTF-8")).hexdigest()
        h2 = hashlib.sha1((line.strip() + salt.strip()).encode("UTF-8")).hexdigest()
        if h1 == hash or h2 == hash:
          fhandlePW.close()
          fhandleSalt.close()
          return line.strip()
    else:
      if hashlib.sha1((line.strip()).encode("UTF-8")).hexdigest() == hash:
        fhandlePW.close()
        return line.strip()
  try: 
    fhandlePW.close()
    fhandleSalt.close()
  except:
    pass
  return "PASSWORD NOT IN DATABASE"

# def supermancracker(hash):
  fhandleSalt = open("known-salts.txt", "r")
  fwrite = open("superman.txt", "w")
  for salt in fhandleSalt:
    str1 = salt.strip() + "superman"
    str2 = "superman" + salt.strip()
    h1 = hashlib.sha1((salt.strip() + "superman").encode("UTF-8")).hexdigest()
    h2 = hashlib.sha1(("superman" + salt.strip()).encode("UTF-8")).hexdigest()
    fwrite.write(f"{str1} {h1}\n")
    fwrite.write(f"{hash}\n")
    fwrite.write(f"{str2} {h2}\n")
    if h1 == hash or h2 == hash:
      fwrite.write(f"FOUND: {salt.strip()}")
      fwrite.close()
      fhandleSalt.close()
      return "superman"
  fwrite.close()
  fhandleSalt.close()
  return "PASSWORD NOT IN DATABASE"
        
