from app import app, db
import sys

try:
    with app.app_context():
        db.create_all()
        print("データベースの初期化に成功しました")
except Exception as e:
    print(f"データベースの初期化に失敗しました: {e}", file=sys.stderr)
    sys.exit(1)
