def create_youtube_video (title,description):
	video = {"title": title,"description": description,"likes":0,"dislikes":0, "comments":{}}
	return video

def like (youtube_video):
	if "likes" in video:
		video["likes"] +=1
	return youtube_video

def dislike (youtube_video):
	if "dislikes" in video:
		video["dislikes"] +=1
	return youtube_video

def add_comment(youtubevideo, username, comment_text):
	


