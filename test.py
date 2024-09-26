import facebook_scraper as fs

# Replace with the post ID you want to scrape
POST_ID = "your_post_id_here"

# Number of comments to download (set to True to download all comments)
MAX_COMMENTS = 100

# Get the post (this gives a generator)
post = next(fs.get_posts(post_urls=['https://www.facebook.com/share/p/UX1M6NLEFyJVYjRb/'], options={"comments": True}))

# Extract comments
comments = post['comments_full'][:MAX_COMMENTS]

# Print comments
for comment in comments:
    print(f"User: {comment['commenter_name']}")
    print(f"Comment: {comment['comment_text']}")
    print("-" * 40)
