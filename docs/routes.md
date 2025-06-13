# STEP 6  詳細設計（URL ルーティング）

| URL パス | メソッド | 説明 |
|-----------|---------|------|
| `/` | GET | トップ画面（公開） |
| `/signup` | GET／POST | サインアップ画面・処理 |
| `/login` | GET／POST | ログイン画面・処理 |
| `/logout` | GET | ログアウト処理（要ログイン） |
| `/mypost` | GET | 自分の投稿一覧（要ログイン） |
| `/everyonepost` | GET | 全員の投稿一覧（要ログイン） |
| `/newpost` | GET／POST | 投稿新規作成（要ログイン） |
| `/<id>/edit` | GET／POST | 投稿編集（要ログイン） |
| `/<id>/delete` | GET | 投稿削除（要ログイン） |
| `/admin` | GET | 管理者画面（要ログイン、機能はプレースホルダー） |
