import streamlit as st
import meilisearch 

st.set_page_config(
    page_title="Main",
    page_icon="👋"
)

client = meilisearch.Client('http://localhost:7700', 'api_key')
st.title('9 Mois à Croquer')
st.sidebar.markdown('# Main Page')

def inverser_ordre_mots(phrase):
    # Diviser la phrase en une liste de mots
    mots = phrase.split()

    # Inverser l'ordre des mots
    mots_inverse = mots[::-1]
    
    # Rejoindre les mots dans une nouvelle phrase
    phrase_inverse = ' '.join(mots_inverse)
    return phrase_inverse


search = st.text_input('Search')
search = inverser_ordre_mots(search)

if search:
    # st.write(f'Bonjour, {nom_prenom}!')
    reponse = client.multi_search(
        [
            {'indexUid': 'food', 'q': search, 'showRankingScore': True,  'matchingStrategy': 'last'},
            {'indexUid': 'recipes', 'q': search, 'showRankingScore': True, 'matchingStrategy': 'last'},
            {'indexUid': 'articles', 'q': search, 'showRankingScore': True, 'matchingStrategy': 'last'},
            {'indexUid': 'questions', 'q': search, 'showRankingScore': True, 'matchingStrategy': 'last'}
        ]
    )

    tables = {
        0:{
            'table_name': 'food',
            'fields': 'code, name, img',
            'primary_key': 'code'
        },
        1:{
            'table_name': 'recipes',
            'fields': 'id, name, time, difficulty, budget, img, review, nb_portions, side_food, steps, food',
            'primary_key': 'id'
        },
        2:{
            'table_name': 'articles',
            'fields': 'id, title, content, img',
            'primary_key': 'id'
        },
        3:{
            'table_name': 'questions',
            'fields': 'id, question, answer, state, url_article',
            'primary_key': 'id'
        }
    }

    for table in tables:
        table_name = tables[table]['table_name']
        fields = tables[table]['fields']

        list_of_values = reponse["results"][table]["hits"]
        if list_of_values:
            st.write("\n"*5)
            st.write('*'*20)
            st.write(f"## {table_name.capitalize()} ##")
            st.write('*'*20)
        if list_of_values:
            for values in list_of_values:
                st.write("*"*20)
                for k, v in values.items():
                    if k not in ('id','code','img'):
                        st.write(f"### {k.capitalize()} ###")
                        st.write(v,unsafe_allow_html=True)          
            