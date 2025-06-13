# STEP 4  データベース設計（ER図）

```mermaid
erDiagram
  User ||--o{ Post : "owns"

  User {
    INTEGER id PK
    TEXT username
    TEXT password
  }

  Post {
    INTEGER id PK
    INTEGER user_id FK
    TEXT title
    TEXT body
    DATETIME updated_at
  }
