import shap
import streamlit as st
import streamlit.components.v1 as components
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import pandas as pd

#funciones auxiliares:

@st.cache()
def explainer(model):
    explainer0 = shap.TreeExplainer(model)

    shap_values0= explainer0.shap_values(X_test[:500])
    return(explainer0,shap_values0)


@st.cache
def get_data():
    df=pd.read_csv('df_limpio.csv',index_col=0) 
    return(df)


@st.cache
def get_model(df):
    df=pd.get_dummies(df,drop_first=True)
    gbm = lgb.LGBMRegressor()
    X_train, X_test, y_train, y_test = train_test_split(df.drop('pricem2',axis=1), df.pricem2)
    model=gbm.fit(X_train, y_train)
    return(model,X_test)



def st_shap(plot, height=None):
    print(type(shap))
    print(dir(shap))
    js=shap.getjs()
    shap_html = f"<head>{js}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)
    
    
    
# aca empieza la 'pagina'
st.title("Tasador de propiedades")







# levanto la data con la funcion que arme arriba

df=get_data()




# entreno el modelo
model,X_test=get_model(df)


st.header('Visualizando el modelo para 500 predicciones:')

# genero la expliacion para los datos del test

explainer,shap_values0=explainer(model)

# ploteo resulados
st_shap(shap.force_plot(explainer.expected_value, shap_values0, X_test[:500]), 400)

# formato del input



st.header('Elija las variables de la propiedad que quiere predecir:')

tipo = st.selectbox(
     'Tipo de inmueble?',df.tipo.unique())

barrio= st.selectbox(
     'Barrio del inmueble?',df.barrio.unique())

sup = st.slider('Superficie del inmueble?', df.sup.min(), 400.0, 2.0)


habs= st.slider('Cantidad de habitaciones?', df.habs.min(), 10.0, 1.0)



pred=[tipo,barrio,sup,0,habs]

# voy a generar una fila con la prediccion del input, formateada con las dummis

df2=df.reset_index(drop=True).copy()
df2.loc[len(df2)] = pred
df2=pd.get_dummies(df2,drop_first=True)
pred=df2.drop('pricem2',axis=1).iloc[-1]

#crotada para generar df apartir de una row

xpred=pd.DataFrame(columns=list(pred.index))
xpred.loc[0]=pred

# generamos la explicacion para la propiedad input
shap_value = explainer.shap_values(xpred)

# printeamos el grafico
st.subheader('Analizando la prediccion:')
st_shap(shap.force_plot(explainer.expected_value, shap_value, xpred))


