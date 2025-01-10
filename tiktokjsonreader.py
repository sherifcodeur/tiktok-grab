import json
import csv

# Charger le fichier JSON
with open("tiktok2.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Créer un fichier CSV pour l'exportation
output_file = "tiktok_videos.csv"

# Vérifier si "itemList" est présent
if "itemList" in data:
    videos = data["itemList"]
    
    # Préparer les données pour le CSV
    with open(output_file, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Écrire les en-têtes
        writer.writerow([
            "ID Vidéo", "Titre", "Vues", "Likes", "Commentaires", 
            "Partages", "Source", "Lien de téléchargement", 
            "Créateur", "Musique", "Hashtags"
        ])
        
        # Parcourir chaque vidéo et extraire les informations
        for video in videos:
            video_id = video.get("id", "ID indisponible")
            title = video.get("desc", "Titre indisponible")
            stats = video.get("stats", {})
            video_info = video.get("video", {})
            author_info = video.get("author", {})
            music_info = video.get("music", {})
            challenges = video.get("challenges", [])
            
            views = stats.get("playCount", 0)
            likes = stats.get("diggCount", 0)
            comments = stats.get("commentCount", 0)
            shares = stats.get("shareCount", 0)
            source = video_info.get("playAddr", "Source indisponible")
            download_link = video_info.get("downloadAddr", "Téléchargement indisponible")
            creator = author_info.get("nickname", author_info.get("uniqueId", "Créateur inconnu"))
            music_title = music_info.get("title", "Musique indisponible")
            hashtags = ", ".join([challenge.get("title", "Sans titre") for challenge in challenges])
            
            # Écrire une ligne dans le CSV
            writer.writerow([
                video_id, title, views, likes, comments, shares, 
                source, download_link, creator, music_title, hashtags
            ])

    print(f"Les données ont été exportées avec succès dans le fichier '{output_file}'.")
else:
    print("Le fichier JSON ne contient pas de 'itemList'.")
