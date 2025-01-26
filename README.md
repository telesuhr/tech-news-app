# Tech Gadget News Website

最新のガジェットニュースを表示するWebサイトです。NewsAPIを利用して、最新のテクノロジーニュースを自動的に取得・表示します。

## 機能
- 最新のガジェットニュース表示
- レスポンシブデザイン
- ニュースのカテゴリー別表示
- 記事の検索機能

## セットアップ方法
1. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

2. NewsAPI APIキーの設定:
- NewsAPI (https://newsapi.org/) でアカウントを作成し、APIキーを取得
- `.env`ファイルを作成し、以下の形式でAPIキーを設定:
```
NEWS_API_KEY=your_api_key_here
```

3. アプリケーションの起動:
```bash
python app.py
```

## 技術スタック
- Flask (Webフレームワーク)
- NewsAPI (ニュースデータ取得)
- Bootstrap 5 (UIフレームワーク)
