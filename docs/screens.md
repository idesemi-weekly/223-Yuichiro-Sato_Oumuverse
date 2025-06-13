# STEP 3  画面設計・画面遷移図

```mermaid
graph TD
    subgraph "非ログイン時"
        Top["トップ画面 (/)"]
        Signup["サインアップ画面 (/signup)"]
        Login["ログイン画面 (/login)"]
    end

    subgraph "ログイン後（共通）"
        MyPost["自分の投稿一覧 (/mypost)"]
        Logout["ログアウト処理 (/logout)"]
    end

    subgraph "一般ユーザー機能"
        EveryonePost["みんなの投稿一覧 (/everyonepost)"]
        NewPost["投稿作成画面 (/newpost)"]
        EditPost["投稿編集画面 (/<id>/edit)"]
    end
    
    subgraph "管理者機能"
        Admin["管理者ページ (/admin)"]
        Admin -- "招待コード発行" --> Admin
        InvitationCode["招待コード (データ)"]
        Admin --> InvitationCode
    end

    %% 画面遷移
    Top --> Signup
    Top --> Login

    Login --> MyPost
    
    MyPost <--> EveryonePost
    MyPost --> NewPost
    MyPost --> EditPost
    MyPost -- "削除処理" --> MyPost
    MyPost --> Logout
    Logout --> Login

    %% 管理者への遷移 (条件付き)
    MyPost -- "ユーザーが管理者の場合" --> Admin
    
    %% 招待コードを使ったサインアップ
    InvitationCode -. "コードを利用" .-> Signup
    Signup -- "コード無効・エラー" --> Signup
    Signup -- "登録成功" --> MyPost
