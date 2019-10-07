import streamlit as st
import pandas as pd
import numpy as np 
from collections import Counter


URL = 'https://gist.githubusercontent.com/TedisAgolli/2b06ff8d8ed7d79ced288b098bd4e437/raw/0fc82b9b188e5d0d0483214c78cfa39618f1a51c/cap_distribution.csv'
st.title('TEST')

@st.cache
def loadData():
    return pd.read_csv('dataset.csv')

data = loadData()
st.subheader('Cap to timeout')
st.write(data)

x = st.slider('Num families',5,20)


d = dict(Counter(data['label']))
hist = pd.DataFrame(d.items(),index=list(d.keys()))
hist = hist.nlargest(x,1)
st.write(hist)
print(hist)
st.bar_chart(hist)


#basic test
# d = pd.DataFrame([[20,30,50]],columns=['a','b','c']).T
# st.bar_chart(d)