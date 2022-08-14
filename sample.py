# 必要モジュールのインポート
import os
from dotenv import load_dotenv
import streamlit as st
import requests



st.header("チャットボット_高橋")
# .envファイルの内容を読み込見込む
load_dotenv()

# os.environを用いて環境変数を表示させます
print(os.environ['API_KEY'])
