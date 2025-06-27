# Oumuverse

> **My very first original web‑service project** — an SNS where users share *highly abstracted* images with a short title.

Flask と SQLite で構築中の SNS **Oumuverse** は、ユーザーが投稿した画像をサーバー側で自動的に抽象化し、視覚情報と言葉をミニマルに融合させたタイムラインを実現します。もとは「画像＋タイトル＋本文」を投稿できるポートフォリオサイトとして企画していましたが、類似サービスが多いため差別化を検討。友人とのブレインストーミングで「**画像を抽象化して“意味”より“イメージ”でつながる空間にしよう**」というアイデアが生まれ、SNS へとピボットしました。

---

## AI 活用について

* 設計ドキュメント（`docs/` 以下）は **ChatGPT‑4.5** でドラフト生成し、必要に応じて手動修正しています。
* 2025‑06‑13 に **Gemini 2.5 Pro** で [`goal.md`](docs/goal.md) / [`screens.md`](docs/screens.md) / [`routes.md`](docs/routes.md) を更新しました。
* ソース内で AI による自動生成が入った箇所には **`[AI-gen]`** と明記しています。

## ドキュメント

設計資料は [`docs/`](docs/) ディレクトリに格納しています。

| 種別         | ファイル                                      |
| ---------- | ----------------------------------------- |
| ゴール定義      | [`goal.md`](docs/goal.md)                 |
| 機能リスト      | [`features.md`](docs/features.md)         |
| 画面設計・遷移    | [`screens.md`](docs/screens.md)           |
| データベース     | [`database.md`](docs/database.md)         |
| アーキテクチャ    | [`architecture.md`](docs/architecture.md) |
| URL ルーティング | [`routes.md`](docs/routes.md)             |

## 技術スタック

### Frontend

![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat\&logo=html5\&logoColor=white) ![Jinja2](https://img.shields.io/badge/-Jinja2-B41717?style=flat\&logo=jinja\&logoColor=white) ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat\&logo=css3\&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/-Tailwind%20CSS-06B6D4?style=flat\&logo=tailwindcss\&logoColor=white)

### Backend & Frameworks

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat\&logo=python\&logoColor=white) ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat\&logo=flask\&logoColor=white)

### Database

![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat\&logo=sqlite\&logoColor=white)

### Authentication

![Flask‑Login](https://img.shields.io/badge/-Flask%20Login-000?style=flat\&logo=python\&logoColor=white)

### Diagramming

![Mermaid](https://img.shields.io/badge/-Mermaid-64B587?style=flat\&logo=mermaid\&logoColor=white)
