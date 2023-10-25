import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title('My_Playground')
first_df_tab, dashboard_test_tab, sine_tab, custom_button_tab, bar_graph_tab, circ_graph_tab = st.tabs(['Dataframe', 'A Dashboard', 'A sine function', 'A Custom button', 'A Bar graph', 'A circular Graph'])

with first_df_tab:
    st.header('olalala')
    st.write("Here's our first attempt at using data to create a table:")
    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

    df = df.style.bar(subset=['first column'], color='blue')
    st.dataframe(df)

with dashboard_test_tab:
    st.header('Test DashBoard')
    st.button("Reset", type="primary")
    if st.button('Click me'):
        st.write('Wow you clicked!')
    else:
        st.write('Sad button :cry:')

    age = st.slider('Select Age', 0,100,25)
    st.write(f'You are {age} years old!')

    st.header('Widgets playground')

    name = st.text_input('Name',label_visibility='hidden', placeholder='Enter your name')
    st.write(f'Hi {name} !')

    details =  st.checkbox('Render Details')
    if details: 
        st.write('Details are visible!')

with sine_tab:
    st.header('Viz!')

    freq = st.slider('Frequency',0,20,value=10)
    amp = st.slider('Amplitude',0.0,1.0,value=0.5)
    phase = st.slider('Phase', 0,360,value=1)
    t = np.linspace(0,1,500)
    y= amp*np.sin(2*np.pi*freq*t+ 2*np.pi/360*phase)
    sinus = pd.DataFrame({ 't' : t,
                        'y' : y})
    # st.dataframe(sinus)
    st.line_chart(data=sinus, x='t',y='y')

    # st.header('A better version')

    # def sinusoids(a,f,Fs,T,phase):
    #     t = np.arange(0,Fs*T) #1 sec
    #     s = 0
    #     # for i, freq in enumerate(f):
    #         # s+=a[i] * np.sin(2*np.pi*freq*t/Fs + 2*np.pi/360*phase[i])
    #     s =a * np.sin(2*np.pi*freq*t/Fs + 2*np.pi/360*phase)
    #     return s

    # N = st.slider('n sin',1,50, value=10)
    # a = np.random.rand(N)
    # f = st.slider('frequence',1,1000,value=440)
    # phase = st.slider('Phase',0,360,value=100)
    # Fs = st.slider('Sample Freq',0,4098, value = 2048)
    # T = st.slider('Time',1,50,value=10)

    # x = sinusoids(a, f, Fs,T,phase)
    # fig = plt.figure(figsize=(16,8))
    # plt.plot(np.arange(0,Fs*T)/Fs, x)
    # st.pyplot(fig)

with custom_button_tab:
    st.header('Personalized Widgets!')

    button= st.button('Click Me')

    button_style = '''<style> .stButton>button {  background-color: #A8D5BA;
        color: #FFFFFF; 
        border: 2px solid #000000;
        border-radius: 10px; 
        padding: 10px 20px; 
        text-align: center;
        text-decoration: none; 
        display: inline-block;
        font-size: 16px; 
        cursor: pointer;} </style> '''

    st.markdown(
        button_style,
        unsafe_allow_html=True)

    if button:
        st.write('oui')

with bar_graph_tab:
    st.header('A bar graph example')

    
    x= ['a','b','c']
    y= [40,70,50]

    fig = plt.figure(figsize=(8,8))
    plt.ion()
    plt.isinteractive()
    plt.bar(x=x, height=y)

    st.pyplot(fig)

    st.header('A better one i guess?')

    bar_data = pd.DataFrame(np.random.randn(3,3), columns=x)
    st.bar_chart(bar_data)

with circ_graph_tab:
    st.header('A nice circular chart')
    data_circ = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

    fig = px.sunburst(data_circ,
                      names='character',
                      parents='parent',
                      values='value')
    st.plotly_chart(fig)


