from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd

# # Inisialisasi downloader
# downloader = YoutubeCommentDownloader()

# # URL video YouTube
# url = "https://youtu.be/6uPpUvyU7dU"

# comments = []

# # Ambil komentar
# for comment in downloader.get_comments_from_url(url):
#     text = comment.get("text", "").strip()
#     if text:
#         comments.append(text)

# # Simpan ke DataFrame
# df = pd.DataFrame(comments, columns=["komentar"])

# # Simpan ke CSV
# df.to_csv("komentar_youtube_internet_rakyat.csv", index=False, encoding="utf-8")

# print("Jumlah komentar:", len(df))
# print(df.head())

url = "https://youtu.be/6uPpUvyU7dU?si=CGRGcUl8BM1GWpil"

downloader = YoutubeCommentDownloader()
comments = downloader.get_comments_from_url(url)

data = []

for c in comments:
    data.append({
        "author": c["author"],
        "text": c["text"],
        "time": c["time"],
        "likes": c["votes"]
    })

df = pd.DataFrame(data)
df.to_csv("internet_rakyat.csv", index=False, encoding="utf-8-sig")
print(df.head())