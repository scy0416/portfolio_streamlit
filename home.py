import streamlit as st

col1, col2 = st.columns(2)
with col1:
    st.header("송찬영")

    job_groups = ["백엔드 개발자", "LLM 활용 개발자", "프롬프트 엔지니어", "컨텍스트 엔지니어"]
    job_groups_md = ""
    for job_group in job_groups:
        job_groups_md += f":green-badge[{job_group}] "
    st.markdown(job_groups_md)
with col2:
    with st.container(border=True):
        st.subheader("Contact")
        st.badge(":material/mail: scy0416@gmail.com")
        st.badge("https://github.com/scy0416")
with st.container(border=True):
    st.write("**간단한 소개**")
    st.write("LLM으로 :blue[플레이 가능한 세계]를 만들고자하는 개발자입니다.")
    st.write("웹·게임 개발을 지향하며, LLM 활용 연구·개발을 통해 :blue['플레이 가능한 AI 경험']을 구현합니다.")
    st.write("사용자가 :blue[아직 경험해보지 못한 즐거움]을 제공하는 것을 목표로 합니다.")

st.divider()

col1, col2 = st.columns(2, border=True)
with col1:
    st.subheader(":material/stacks: 기술 스택")
    st.caption("주 사용 언어")
    st.markdown(":blue-badge[Python]")
    st.caption("프레임워크")
    st.markdown(":blue-badge[FastAPI] :blue-badge[Streamlit] :blue-badge[LangChain] :blue-badge[LangGraph]")
    st.caption("데이터베이스 경험")
    st.markdown(":blue-badge[MySQL] :blue-badge[Firebase-Firestore]")
    st.caption("DevOps/Infra 경험")
    st.markdown(":blue-badge[Docker] :blue-badge[Docker Compose]")
with col2:
    st.subheader(":material/school: 경력/학력")
    st.caption("대학")
    st.markdown("- 순천향대학교 - 컴퓨터소프트웨어공학과 20년도 입학")
    st.caption("자격증")
    st.markdown(":blue-badge[정보처리기사]")

st.divider()

with st.container(border=True):
    st.header("프로젝트")