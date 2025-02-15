import streamlit as st
import datetime
import pyperclip

# ライフパスナンバーの意味を辞書で管理
numerology_meanings = {
    1: "リーダーシップに優れ、自立心が強い。",
    2: "協調性があり、平和を愛する。",
    3: "創造的で、表現力が豊か。",
    4: "努力家で、安定を好む。",
    5: "自由を愛し、冒険心が強い。",
    6: "責任感が強く、家庭的。",
    7: "知的で、分析力に優れる。",
    8: "野心的で、成功を求める。",
    9: "博愛主義者で、精神的に成熟している。",
    11: "直感が鋭く、カリスマ性がある（マスターナンバー）。",
    22: "現実的な夢を実現できる強い力を持つ（マスターナンバー）。",
    33: "奉仕の精神を持ち、カリスマ性にあふれる（マスターナンバー）。",
}

# ライフパスナンバーを計算する関数
def calculate_life_path_number(birthdate):
    digits = [int(d) for d in birthdate.replace("-", "")]  # 例: "1995-07-23" → [1,9,9,5,7,2,3]
    total = sum(digits)
    
    # マスターナンバー（11, 22, 33）は保持
    while total > 9 and total not in (11, 22, 33):
        total = sum(map(int, str(total)))  # 各桁を再度足す
    return total

# Streamlit UI
st.title("🔮 数秘術占いアプリ 🔮")
st.write("あなたの誕生日を入力すると、ライフパスナンバーと占い結果をお伝えします！")

# ユーザーに誕生日を入力させる
birthdate = st.date_input("誕生日を選択してください", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

if birthdate:
    # 数秘術ナンバーを計算
    life_path_number = calculate_life_path_number(birthdate.strftime("%Y-%m-%d"))
    
    # 結果を表示
    st.subheader(f"あなたのライフパスナンバーは【{life_path_number}】です！")
    st.write(f"**{numerology_meanings.get(life_path_number, 'データがありません')}**")

    # X（旧Twitter）投稿用テキスト
    tweet_text = f"私のライフパスナンバーは【{life_path_number}】🎉 {numerology_meanings.get(life_path_number, '')} #数秘術 #占い"

    st.text_area("📌 Xに投稿するには、このテキストをコピーしてください:", tweet_text, height=100)

    if st.button("📋 コピーする"):
        pyperclip.copy(tweet_text)
        st.success("コピーしました！Xに貼り付けて投稿してください。")

# フッター
st.write("📅 ライフパスナンバーは、誕生日の数字をすべて足して計算します。11, 22, 33は特別なマスターナンバーです。")
