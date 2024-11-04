from typing import Optional

import streamlit as st


class StliteApp:
    def __init__(self):
        self.title: str = "My Stlite Application"

    def setup(self) -> None:
        """アプリケーションの初期設定"""
        st.set_page_config(page_title=self.title, page_icon="🚀", layout="wide")

    def main(self) -> None:
        """メインアプリケーションロジック"""
        self.setup()
        st.title(self.title)

        with st.sidebar:
            st.title("Navigation")

        # メインコンテンツ
        name: Optional[str] = st.text_input("Enter your name")
        if name:
            st.write(f"Hello, {name}!")


if __name__ == "__main__":
    app = StliteApp()
    app.main()
