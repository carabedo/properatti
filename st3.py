import shap
import streamlit as st
import streamlit.components.v1 as components
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import pandas as pd
print(shap.__version__)
shap.initjs()
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
    print(type(shap)
    print(dir(shap))
    js=shap.getjs()
    
    shap_html = f"<head>{js}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)

st.title("Tasador de propiedades")




#st.dataframe(df.drop('pricem2',axis=1).head()) 



# train XGBoost model
df=get_data()





model,X_test=get_model(df)
# explain the model's predictions using SHAP
# (same syntax works for LightGBM, CatBoost, scikit-learn and spark models)

st.text('Visualizando el modelo para 500 predicciones:')
explainer0,shap_values0=explainer(model)
st_shap(shap.force_plot(explainer0.expected_value, shap_values0, X_test[:500]), 400)



tipo = st.selectbox(
     'Tipo de inmueble?',df.tipo.unique())

barrio= st.selectbox(
     'Barrio del inmueble?',df.barrio.unique())

sup = st.slider('Superficie del inmueble?', df.sup.min(), 400.0, 2.0)


habs= st.slider('Cantidad de habitaciones?', df.habs.min(), df.habs.max(), 1.0)



pred=[tipo,barrio,sup,0,habs]
df2=df.reset_index(drop=True).copy()

df2.loc[len(df2)] = pred

df2=pd.get_dummies(df2,drop_first=True)


pred=df2.drop('pricem2',axis=1).iloc[-1]


xtest=X_test[:500].reset_index(drop=True).append(pred)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(xtest)


st.text('Analizando la prediccion:')
# visualize the first prediction's explanation (use matplotlib=True to avoid Javascript)
st_shap(shap.force_plot(explainer.expected_value, shap_values[-1,:], xtest.iloc[-1,:]))



