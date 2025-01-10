import json

# Charger le fichier JSON
with open("tiktok.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Vérifier si "itemList" est présent
if "itemList" in data:
    videos = data["itemList"]
    
    # Parcourir chaque vidéo et extraire les informations
    for video in videos:
        title = video.get("desc", "Titre indisponible")
        stats = video.get("stats", {})
        video_info = video.get("video", {})
        author_info = video.get("author", {})
        
        views = stats.get("playCount", 0)
        likes = stats.get("diggCount", 0)
        comments = stats.get("commentCount", 0)
        shares = stats.get("shareCount", 0)
        source = video_info.get("playAddr", "Source indisponible")
        creator = author_info.get("nickname", author_info.get("uniqueId", "Créateur inconnu"))
        
        print(f"Titre: {title}")
        print(f"Vues: {views}")
        print(f"Likes: {likes}")
        print(f"Commentaires: {comments}")
        print(f"Partages: {shares}")
        print(f"Source: {source}")
        print(f"Créateur: {creator}")
        print("-" * 40)
else:
    print("Le fichier JSON ne contient pas de 'itemList'.")
