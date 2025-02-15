import streamlit as st
import pyperclip
import re

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

# 相性診断スコア
def calculate_compatibility_score(num1, num2):
    compatibility_matrix = {
        (1, 2): (85, "リーダー(1)とサポーター(2)の相性は抜群！"),
        (3, 5): (90, "自由を愛する二人、楽しい関係になりそう！"),
        (4, 8): (75, "安定志向(4)と成功志向(8)、仕事なら最強コンビ。"),
        (7, 9): (80, "知性(7)と精神性(9)が深い理解を生む関係。"),
    }
    key = tuple(sorted((num1, num2)))
    return compatibility_matrix.get(key, (50, "普通の相性です。お互いを尊重しましょう。"))

# ライフパスナンバーを計算する関数
def calculate_life_path_number(birthdate):
    digits = [int(d) for d in re.sub(r"\D", "", birthdate)]  # 数字のみ抽出
    total = sum(digits)
    while total > 9 and total not in (11, 22, 33):
        total = sum(map(int, str(total)))  # 各桁を再度足す
    return total

# Streamlit UI
st.title("🔮 数秘術占い & 相性診断 🔮")
st.write("誕生日を入力すると、ライフパスナンバーと占い結果をお伝えします！")

# 誕生日入力
birthdate = st.text_input("あなたの誕生日を入力（例: 20250215, 2015/02/15）:", "")

if birthdate:
    try:
        life_path_number = calculate_life_path_number(birthdate)
        st.subheader(f"あなたのライフパスナンバーは【{life_path_number}】です！")
        st.write(f"**{numerology_meanings.get(life_path_number, 'データがありません')}**")
        
        # X（旧Twitter）投稿用テキスト
        tweet_text = f"私のライフパスナンバーは【{life_path_number}】🎉 {numerology_meanings.get(life_path_number, '')} #数秘術 #占い"
        st.text_area("📌 Xに投稿するには、このテキストをコピーしてください:", tweet_text, height=100)

        if st.button("📋 コピーする"):
            pyperclip.copy(tweet_text)
            st.success("コピーしました！Xに貼り付けて投稿してください。")

    except ValueError:
        st.error("⚠️ 正しい誕生日を入力してください（例: 20250215, 2015/02/15）")

# 相性診断
st.subheader("❤️ 気になる人との相性診断 ❤️")
partner_birthdate = st.text_input("相手の誕生日を入力（例: 20250215, 2015/02/15）:", "")
relationship_type = st.selectbox("関係性を選択:", ["恋人", "同性の友達", "異性の友達", "同僚"])

if partner_birthdate:
    try:
        partner_life_path = calculate_life_path_number(partner_birthdate)
        st.write(f"相手のライフパスナンバーは【{partner_life_path}】です！")

        # 相性スコアとコメント
        score, compatibility_comment = calculate_compatibility_score(life_path_number, partner_life_path)
        
        st.subheader(f"✨ {relationship_type}の相性診断 ✨")
        st.write(f"❤️ **相性スコア: {score}/100**")
        st.write(f"📝 **{compatibility_comment}**")

        # 関係性ごとのアドバイス
        if relationship_type == "恋人":
            st.write("💖 **恋愛アドバイス:** お互いの価値観を尊重し合うことで関係が深まります！")
        elif relationship_type == "同性の友達":
            st.write("😊 **友情アドバイス:** 無理せず自然体で接すると、長続きする友情に！")
        elif relationship_type == "異性の友達":
            st.write("🎭 **異性の友達:** 恋愛感情を持たず、素直に話せる関係が◎")
        elif relationship_type == "同僚":
            st.write("💼 **職場アドバイス:** 役割分担を意識すると、お互いの強みを活かせます！")

    except ValueError:
        st.error("⚠️ 正しい誕生日を入力してください（例: 20250215, 2015/02/15）")

# フッター
st.write("📅 ライフパスナンバーは、誕生日の数字をすべて足して計算します。11, 22, 33は特別なマスターナンバーです。")
