import os
import argparse


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def read_template():
    return read_file("index.html")


def create_index_html(app_content, requirements=None):
    if requirements is None:
        requirements = ["streamlit", "pandas", "matplotlib"]

    template = read_template()
    # "app.py": null の部分を実際のコンテンツで置換
    return template.replace('"app.py": null', f'"app.py": `{app_content}`')


def main():
    # コマンドライン引数のパーサーを作成
    parser = argparse.ArgumentParser(description='Convert Python file to HTML')
    parser.add_argument('--input', '-i',
                       default='src/app.py',
                       help='Input Python file path (default: src/app.py)')

    # 引数をパース
    args = parser.parse_args()

    # 指定されたファイルの内容を読み込む
    app_content = read_file(args.input)

    # index.htmlを生成
    html_content = create_index_html(app_content)

    # buildディレクトリを作成
    os.makedirs("build", exist_ok=True)

    # index.htmlを書き出し
    with open("build/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    main()
