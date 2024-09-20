import csv
from google_play_scraper import reviews, Sort, reviews_all

def fetch_reviews(app_name, lang, country, sort, count):
    return reviews_all(
        app_name,
        lang=lang,
        country=country,
        sort=sort,
        count=count
    )

def save_reviews (app_name, lang, country, sort, count, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['userName', 'score', 'content', 'at']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
            
        writer.writeheader()

        for review in fetch_reviews(app_name, lang, country, sort, count):
            writer.writerow({
                'content': review['content'],
                'score': review['score'],
                'userName': review['userName'],
                'at': review['at']
            })

save_reviews(
    'com.gojek.app',
    'en',
    'id',
    Sort.MOST_RELEVANT,
    10000,
    'review_gojek_en.csv'
)            
