from flask import Flask, render_template, request
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

app = Flask(__name__)

# NewsAPIの初期化
newsapi = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

@app.route('/')
def home():
    # メインのガジェットニュースを取得
    gadget_news = newsapi.get_everything(
        domains='japanese.engadget.com,techcrunch.com,gizmodo.jp',
        sort_by='publishedAt',
        page_size=12
    )
    
    # トレンドキーワードのニュースを取得
    trend_keywords = {
        'Apple': 'Apple OR iPhone OR iPad OR Mac',
        'Android': 'Android OR Galaxy OR Pixel',
        'AI': 'AI OR ChatGPT OR 人工知能',
        'VR': 'VR OR メタバース OR Quest',
        'ゲーム': 'PlayStation OR Xbox OR Nintendo'
    }
    
    trend_news = {}
    for key, query in trend_keywords.items():
        trend_results = newsapi.get_everything(
            q=query,
            domains='japanese.engadget.com,techcrunch.com,gizmodo.jp',
            sort_by='publishedAt',
            page_size=3
        )
        trend_news[key] = trend_results['articles']
    
    return render_template('index.html', 
                         articles=gadget_news['articles'],
                         trend_news=trend_news,
                         trend_keywords=trend_keywords)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        search_results = newsapi.get_everything(
            q=query,
            domains='japanese.engadget.com,techcrunch.com,gizmodo.jp',
            sort_by='publishedAt',
            page_size=12
        )
        return render_template('search.html', articles=search_results['articles'], query=query)
    return render_template('search.html', articles=[], query='')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
