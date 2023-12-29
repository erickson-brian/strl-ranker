import streamlit as st
import random
import pandas as pd
from rankit.Table import Table
from rankit.Ranker import KeenerRanker
from rankit.Ranker import MasseyRanker
from rankit.Ranker import ColleyRanker

class Game:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0
        self.losses = 0

if 'results' not in st.session_state:
    st.session_state['results'] = []

if 'votes' not in st.session_state:
    st.session_state['votes'] = 0

if 'games' not in st.session_state:
    gz = ['Elden Ring','God of War Ragnarok','Neon White','Horizon Forbidden West','Marvel Snap','Fortnite Zero Build','Vampire Survivor','Tinykin','Mario Strikers: Battle League', 'Super Auto Pets']
    #gz = ['one','two','three','four','five','six','seven','eight','nine','ten']
    games = []
    for ii in gz:
        games.append(Game(ii))
    st.session_state['games'] = games

def log():
    st.session_state['votes'] = st.session_state['votes'] + 1
    if st.session_state["btn_g1"] == True:
        st.session_state['results'].append([st.session_state["g1"].name,st.session_state["g2"].name,1,0])
    if st.session_state["btn_g2"] == True:
            st.session_state['results'].append([st.session_state["g2"].name,st.session_state["g1"].name,1,0])

st.write('Votes: ' + str(st.session_state['votes']))


st.session_state['g1'], st.session_state['g2'] = random.sample(st.session_state['games'],2)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.button(st.session_state['g1'].name, key="btn_g1", on_click=log)
    with col2:
        st.button(st.session_state['g2'].name, key="btn_g2", on_click=log)


if st.button("Current Standings"):
    df = pd.DataFrame(st.session_state['results'])
    df.columns = ['Winner','Loser','WScore','LScore']

    data = Table(df, col = ['Winner','Loser','WScore','LScore'])

    ranker = KeenerRanker()
    keenerRank = ranker.rank(data)
    st.write("Keener Rank")
    st.write(keenerRank)

    ranker = MasseyRanker()
    masseyRanker = ranker.rank(data)
    st.write("Massey Rank")
    st.write(masseyRanker)

    ranker = ColleyRanker()
    ColleyRanker = ranker.rank(data)
    st.write("Colley Rank")
    st.write(masseyRanker)    


    st.write(df)
    gl = pd.unique(df[['Winner','Loser']].values.ravel('K'))
    for gg in gl:
        st.write(gg)

with st.expander("Debug Session Data"):
    st.write(st.session_state)


with st.expander("Current Results"):
    st.write(st.session_state['results'])