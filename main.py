import time 

st.title("Streamlit 超入門")
st.write("プログレスバーの表示")

"start!!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ回答１")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ回答２")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ回答３")
expander4 = st.expander("問い合わせ")
expander4.write("問い合わせ回答４")




