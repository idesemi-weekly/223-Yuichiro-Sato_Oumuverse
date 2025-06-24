import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(project_root, 'src'))
from app import app, db

instance_path = os.path.join(project_root, 'instance')
db_path = os.path.join(instance_path, 'mypost.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
print(f"データベースパスを '{db_path}' に上書き設定しました。")

os.makedirs(instance_path, exist_ok=True)

try:
    with app.app_context():
        db.create_all()
    print("データベースの初期化に成功しました")
except Exception as e:
    print(f"データベースの初期化に失敗しました: {e}", file=sys.stderr)
    sys.exit(1)