import os


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
    # src/app.pyの内容を読み込む
    app_content = read_file("src/app.py")

    # index.htmlを生成
    html_content = create_index_html(app_content)

    # buildディレクトリを作成
    os.makedirs("build", exist_ok=True)

    # index.htmlを書き出し
    with open("build/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    main()
