import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, 'src'))

from app import app, db

try:
    with app.app_context():
        db.create_all()
        print("データベースの初期化に成功しました")
except Exception as e:
    print(f"データベースの初期化に失敗しました: {e}", file=sys.stderr)
    sys.exit(1)

