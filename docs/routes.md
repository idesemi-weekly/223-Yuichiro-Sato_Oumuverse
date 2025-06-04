<!-- docs/routes.md -->
# STEP 6  詳細設計（URL ルーティング）

| URL パス | メソッド | 説明 |
|-----------|---------|------|
| `/` | GET | トップ画面（公開） |
| `/signup` | GET／POST | サインアップ（招待トークン付き） |
| `/signin` | GET／POST | サインイン |
| `/posts` | GET | 投稿一覧（要ログイン） |
| `/posts/new` | GET／POST | 投稿新規作成 |
| `/posts/<id>` | GET | 投稿詳細 |
| `/posts/<id>/edit` | GET／POST | 投稿編集 |
| `/posts/<id>/delete` | POST | 投稿削除 |
| `/admin/invitations` | GET／POST | 招待リンク発行・管理（管理者のみ） |
