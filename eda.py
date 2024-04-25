import streamlit as st
import pandas as pd

def run_eda():
    st.sidebar.title('탐색적 데이터 분석')  # sidebar 메소드 대신 title 속성을 사용하여 사이드바 제목 설정

    st.text('데이터 프레임 보기 / 통계치 보기를 할 수 있습니다.')

    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    print(df)

    radio_menu = ['데이터 프레임', '통계치']

    choice_radio = st.radio('선택하세요', radio_menu)

    if choice_radio == radio_menu[0]: 
        st.dataframe(df)
    elif choice_radio == radio_menu[1]:
        st.dataframe(df.describe())

        # 각 컬럼별로 최대/최소값을 보여주는 화면 개발,
        # 유저가 컬럼을 선택하면, 해당 컬럼의 최대/최소값을 보여주도록 하자.

        st.text('컬럼을 선택하면, 각 컬럼별 최대/최소 데이터를 보여드립니다.')
        column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
        selected_column = st.selectbox('컬럼을 선택하세요.', column_list)  # 선택된 값을 변수에 저장

        if selected_column:
            st.text(f"최대값: {df[selected_column].max()}")
            st.text(f"최소값: {df[selected_column].min()}")
