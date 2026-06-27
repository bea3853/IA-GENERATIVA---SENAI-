# procoding 
# vou  usar a biblioteca
import streamlit as st

st.title('CALCULADORA...')

n1  = st.number_input('numero:', )
n2  = st.number_input('numero:', value = 0.0)

soma, sub, div, mult = st.columns(4)

if soma.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif sub.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif div.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       
elif mult.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)      


# ------------------------------------------------

st.title('Desafio 1: O Cartão de Visitas Digital')

st.header('CARTÃO DE VISITA')

st.text('Isso ')

st.markdown('Isso é um paragrafo de comentario')

# ------------------------------------------------


st.number_input('nº', format = "%0.2f", )
st.image('images.jpg')


idade  = st.number_input('idade', value = 0)




if idade >= 18:
    st.success('maior de idade')
else:
    st.error('menor de idade ')    