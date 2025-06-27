import os
import sys

from dotenv import load_dotenv

from app import app, db

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path = os.path.join(project_root, ".env.staging")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
    print(f"'{dotenv_path}' を読み込みました。")
else:
    load_dotenv()

sys.path.append(os.path.join(project_root, "src"))

instance_path = os.path.join(project_root, "instance")
os.makedirs(instance_path, exist_ok=True)

if os.environ.get("FLASK_ENV") == "staging":
    db_filename = "mypost-staging.db"
else:
    db_filename = "mypost.db"

db_path = os.path.join(instance_path, db_filename)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
print(f"データベースパスを '{db_path}' に設定しました。")

try:
    with app.app_context():
        db.create_all()
    print("データベースの初期化に成功しました")
except Exception as e:
    print(f"データベースの初期化に失敗しました: {e}", file=sys.stderr)
    sys.exit(1)
