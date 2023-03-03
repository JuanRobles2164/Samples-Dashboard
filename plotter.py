import pandas as pd
from plotly.subplots import make_subplots 
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

labels = ['Fase A','Fase B','Fase C']
values = [50, 30, 20]

max = float(df['AAPL_y'].max())
min_date = df['AAPL_x'].min()


# Creating a grid called dashboard
dashboard = make_subplots(rows=4, cols=3, # especificacoes gerais
subplot_titles=['', '', '', '', '', ' '],
column_widths=[0.15, 0.15, 0.70], # tamanho das colunas
# Espaçamentos 
horizontal_spacing= 0.02, 
vertical_spacing = 0.03,
# Configuracao dos tamanhos dos graficos de acordo com o tamanho do grid, 
# Quantas colunas ocumpam, em uma matriz 5x3 que representa o grid criado
specs=[[{'rowspan': 1, 'colspan':1}, {'rowspan': 1, 'colspan': 1}, {'rowspan': 2, 'colspan': 1}], [{'rowspan': 1, 'colspan':1}, {'rowspan': 1, 'colspan': 1}, None],
        [{'rowspan': 1, 'colspan':2, 'type': 'pie'}, None, {'rowspan': 2, 'colspan': 1}], [{'rowspan': 1, 'colspan':2}, None, None]])

demandaMedia = 268
consumoTotal = 241
aumento = 12
# make_subplots return an object of type image, which can be manipuled via individual row and col arguments

chart1 = go.Scatter(x = df['AAPL_x'], y=df['AAPL_y'], mode='lines', showlegend=False, line=dict(color="#252525", width=4))
chart2 = go.Bar()
# Since plotly doesn't offer full support for pie chart title styling, we added a break tag in order to have a space between the title and the chart
chart3 = go.Pie(labels=labels, values=values, showlegend=True, 
                title=dict(font=dict(color="#252525", size=20), 
                text="<b>Demanda por fase <b> <br> <br>", position="top center"))
                

# Adding the plots to the grid dashboard previously created
dashboard.add_trace(chart2, row=1, col=1)
dashboard.add_trace(chart2 ,row=1, col=2)
dashboard.add_trace(chart2, row=2, col=1)
dashboard.add_trace(chart2, row=2, col=2)
dashboard.add_trace(chart1, row=1, col=3)
dashboard.add_trace(chart3, row=3, col=1)
dashboard.add_trace(chart2, row=4, col=1)
dashboard.add_trace(chart1, row=3, col=3)


# Remove ticks and disable zoom for informative charts 
for i in range(1, 5):
    for j in range(1, 3):
        dashboard.update_xaxes(ticks="", range=[0,1], showticklabels=False, zeroline=False, showgrid=False, row=i, col=j, fixedrange=True, automargin=False)
        dashboard.update_yaxes(ticks="", range=[0,1], showticklabels=False, zeroline=False, showgrid=False, row=i, col=j, fixedrange=True, automargin=False)

# Editing "Curva de carga"
dashboard.update_xaxes(showgrid=False, tickfont=dict(color='#252525', size=15), row=1, col=3)
dashboard.update_yaxes(showgrid=True, gridcolor='#d4d4d4', tickfont=dict(color='#252525', size=15), row=1, col=3)
dashboard.add_annotation({'font': {'size': 30, 'color':'#252525'}},  x='2014-01-06', y=max - 2, text="<b>Curva de carga<b>", showarrow=False, row=1, col=3)

# Editing "Consumo acumulado"
dashboard.update_xaxes(showgrid=False, tickfont=dict(color='#252525', size=15), row=3, col=3)
dashboard.update_yaxes(showgrid=True, gridcolor='#d4d4d4', tickfont=dict(color='#252525', size=15), row=3, col=3)
dashboard.add_annotation({'font': {'size': 30, 'color':'#252525'}}, xref='paper', yref='paper', x='2014-01-06', y=max - 2, text="<b>Consumo acumulado<b>", showarrow=False, row=3, col=3)

# Creating chart "Consumo total"
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.35, y=0.9, text="<b>Consumo total<b>", showarrow=False, row=1, col=1)
dashboard.add_annotation({'font': {'size': 30, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.35, y=0.6, text="<b>" + str(consumoTotal) + " kWh<b>", showarrow=False, row=1, col=1)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.35, text="+" + str(aumento) + "%", showarrow=False, row=1, col=1)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.15, text="Desde ontem", showarrow=False, row=1, col=1)

# Creating chart "Demanda média"
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.38, y=0.9, text="<b>Demanda média<b>", showarrow=False, row=1, col=2)
dashboard.add_annotation({'font': {'size': 30, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.35, y=0.6, text="<b>" + str(demandaMedia) + " kWh<b>", showarrow=False, row=1, col=2)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.35, text="+" + str(aumento) + "%", showarrow=False, row=1, col=2)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.15, text="Desde ontem", showarrow=False, row=1, col=2)

# Creating chart "Horário de pico"
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.35, y=0.9, text="<b>Horário de pico<b>", showarrow=False, row=2, col=1)
dashboard.add_annotation({'font': {'size': 28, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.45, y=0.6, text="<b>15h30 - 16h30<b>", showarrow=False, row=2, col=1)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.35, text="16h30 - 17h30", showarrow=False, row=2, col=1)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.15, text="Horário de pico de ontem", showarrow=False, row=2, col=1)

# Creating chart "Demanda máxima"
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.41, y=0.9, text="<b>Demanda máxima<b>", showarrow=False, row=2, col=2)
dashboard.add_annotation({'font': {'size': 30, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.35, y=0.6, text="<b>" + str(demandaMedia) + " kWh<b>", showarrow=False, row=2, col=2)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.35, text="+" + str(aumento) + "%", showarrow=False, row=2, col=2)
dashboard.add_annotation({'font': {'size': 15, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.1, y=0.15, text="Desde ontem", showarrow=False, row=2, col=2)

# Creating charts "fases"
# Creating chart "Demanda máxima"
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.04, y=0.9, text="<b>Fase A: Computadores, fileiras de lâmpadas<b>", showarrow=False, row=4, col=1)
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.04, y=0.5, text="<b>Fase B: Insufladores, monitores e alarme<b>", showarrow=False, row=4, col=1)
dashboard.add_annotation({'font': {'size': 20, 'color':'#252525'}}, xref='x domain', yref='y domain', x=0.04, y=0.1, text="<b>Fase C: Servidor, mesa do Michelet<b>", showarrow=False, row=4, col=1)

# General settings and legend positioning
dashboard.update_layout(paper_bgcolor='#F5F5F5', plot_bgcolor='white', legend=dict(xanchor="left", yanchor="middle", y=0.45, x=0.25), margin=dict(l=10, r=10, t=10, b=10))
dashboard.write_html('./dashboard.html')