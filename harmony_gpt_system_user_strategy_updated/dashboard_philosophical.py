
import streamlit as st
from memory.shared_declaration_board import SharedDeclarationBoard

# 대시보드 제목
st.set_page_config(page_title="HarmonyGPT 철학적 대시보드", layout="wide")
st.title("🧠 HarmonyGPT 철학적 루프 대시보드")

# 선언 보드 로딩
board = SharedDeclarationBoard()

# 시각화 섹션
st.subheader("🔁 최근 선언 흐름")
latest = board.latest(10)
for i, line in enumerate(latest[::-1]):
    st.markdown(f"{len(latest)-i}. **{line}**")

# 전체 흐름 확인
if st.checkbox("전체 흐름 보기"):
    st.subheader("🌐 전체 선언 흐름")
    for i, line in enumerate(board.full_board()):
        st.text(f"{i+1}: {line}")
