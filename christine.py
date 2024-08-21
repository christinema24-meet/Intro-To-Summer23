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

def add_comment(youtube_video, username, comment_text):
    youtube_video['comments'] = {}
    youtube_video['comments'][username] = comment_text
    return youtube_video


video = create_youtube_video("how to tie your shoes ", "A tutorial about how to tie your shoes in easy way,just in 5 sec!")

for _ in range(495):
   video = like(video)
   video = dislike(video)
   video = add_comment(video, "user123", "Great tutorial!")
print(video)



