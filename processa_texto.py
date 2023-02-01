from textblob import TextBlob
import pandas as pd
from deep_translator import GoogleTranslator

df = pd.read_csv('sales.csv')
list_aval = df['Deixe seu feedback com alguma sugestão de melhoria, comentário ou elogio/Leave your feedback with any suggestions for improvement, comments or compliments/Deje su opinión con cualquier sugerencia de mejora, comentario o elogio'].to_list()
#list_aval = df['Observações HR']
df_final=pd.DataFrame(columns=['original','traduzido','sentimento','subjetividade'])
for aval in list_aval:

    try:
        translated = GoogleTranslator(source='auto', target='en').translate(aval)
        text_blob = TextBlob(translated)
        analise = text_blob.sentiment
        sentimento = analise[0]
        subjetividade = analise[1]
        if sentimento < 0:
            sentimento_txt = 'negativo'
        elif sentimento >0 and sentimento <0.3:
            sentimento_txt = 'neutro'
        else:
            sentimento_txt = 'positivo'
        if subjetividade < 0:
            subjetividade_txt = 'subjetivo'
        else:
            subjetividade_txt = 'objetivo'
    except:
        print('Texto vazios')
        
    row = pd.Series([aval,translated,sentimento_txt,subjetividade_txt],index=df_final.columns)
    df_final = df_final.append(row,ignore_index=True)
df_final.to_csv('teste.csv',index=False)
