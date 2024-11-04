# Stlite Chat Application

Streamlit アプリケーションを静的サイトとして配布するためのプロジェクト

## 機能

- Streamlit アプリケーションを静的 HTML として出力
- stlite を使用してブラウザ上で Python コードを実行

## 前提条件

- Python 3.12以上
- uv (Python パッケージマネージャー)

## インストール

```bash
git clone [repository-url]
cd stlite-chat
uv venv
source .venv/bin/activate  # Windowsの場合: .venv\Scripts\activate
uv pip install -e .
```

## 使い方

### 開発サーバーの起動

```bash
make run
```

http://localhost:8501 でアクセス

### 静的サイトの生成

```bash
make build
```

`build/` ディレクトリにファイルが生成されます。

### ビルドしたサイトの確認

```bash
cd build
python -m http.server 8000
```

http://localhost:8000 でアクセス

## プロジェクト構造

```
.
├── src/
│   ├── app.py         # メインアプリケーション
│   └── pages/         # 追加ページ
├── tests/             # テスト
├── scripts/           # ビルドスクリプト
├── index.html        # stlite テンプレート
└── build/            # ビルド出力
```

## 開発ガイド

- `src/app.py`: メインアプリケーションコード
- `src/pages/`: 追加ページのコード
- `index.html`: stlite のテンプレート
- `scripts/`: ビルドスクリプトやユーティリティ
