"""
A partir de l'adresse IPVS, récup du NFT au format PNG
Auteur: Fabrice Heuvrard
Date : 18/04/2022
Entrée : Adresse IPVS du de l'image qui s'incrémente
Résultat : fichier svg des NFT
"""

# importation des modules nécessaires
import urllib.request
import requests
import json

adresse_generique = "https://bafybeihpjhkeuiq3k6nqa3fkgeigeri7iebtrsuyuey5y6vy36n345xmbi.ipfs.dweb.link/"

x=5964
while x <10000:
   try:
      #URL = json.loads(requests.get(str(adresse_generique)+str(x)).content)
      URL_image = json.loads(requests.get(str(adresse_generique)+str(x)).content)['image']
      URL_Cloudfare = "https://cloudflare-ipfs.com/ipfs/"+URL_image[7:]
      print(URL_Cloudfare) 
      print("Image : ",x,"======>","Reste :", 10000-x)
      nom_fichier = "NFT_Bored Ape Yacht Club_" + str(x) + ".png"
      f = open(nom_fichier,'wb')
      urllib.request.urlretrieve(URL_Cloudfare, nom_fichier)
      x=x+1
   except:
      x=x
