from  flask  import  Flask , request , jsonify , render_template , send_from_directory
importer  os
 journalisation des importations

application  =  Flask ( __nom__ )
journalisation.basicConfig ( niveau = journalisation.INFO )​​​​

# Page d'accueil
@ app . route ( '/' )
def  index ():
    retourner  render_template ( 'index.html' )

# Route pour recevoir la géolocalisation
@ app.route ( '/geoloc' , methods = [ ' POST ' ])
def  geoloc ():
    essayer :
        données  =  requête.json​​
        lat  =  data.get ( ' lat ' )
        lon  =  data.get ( ' lon ' )
        mapLink  =  data.get ( ' mapLink ' )
        
        # Log la position
        app.logger.info ( f " 📍 Localisation / { lat } , { lon }   /   { mapLink } " )
        
        # Sauvegarde dans un fichier (optionnel)
        avec  open ( 'positions.txt' , 'a' ) as  f :
            f.écrire ( f " { lat } , { lon } \ n " )
        
        retourner  jsonify ({
            "statut" : "succès" ,
            "message" : f"Position reçue : { lat } , { lon } "
        })
    sauf  Exception  comme  e :
        application . enregistreur . erreur ( f"Erreur : { e } " )
        return  jsonify ({ "status" : "error" , "message" : str ( e )}), 400

# Route pour les fichiers statiques (images)
@ app.route ( '/static/ < path:filename> ' )
def  fichiers_statiques ( nom_de_fichier ):
    renvoyer  send_from_directory ( 'static' , nom_de_fichier )

# Route pour les images à la racine (pour compatibilité)
@ app.route ( '/ <nom_de_fichier> ' )
def  serve_image ( nom_de_fichier ):
    si  le nom de fichier se termine par ( ' .jpg' ) ou  par ( '.png' ) :
        renvoyer  send_from_directory ( '.' , nom_de_fichier )
    return  "Fichier non trouvé" , 404

# Route de santé pour Render
@ app . route ( '/health' )
def  santé () :
    renvoie  jsonify ({ "status" : "healthy" }), 200

# Route pour voir les positions (optionnel - protégez-la en production)
@ app . route ( '/admin/positions' )
def  position_vue ():
    essayer :
        avec  open ( 'positions.txt' , 'r' ) as  f :
            positions  =  f.readlines ( )​
        renvoie  jsonify ({ "positions" : positions })
    sauf :
        renvoie  jsonify ({ "positions" : []})

si  __name__  ==  '__main__' :
    port  =  int ( os . environ . get ( 'PORT' , 5000 ))
    app.run ( host = ' 0.0.0.0 ' , port = port , debug = True )
