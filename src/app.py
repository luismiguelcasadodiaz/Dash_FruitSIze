import dash
import dash_bootstrap_components as dbc

import param

app= dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

selector = dash.html.Div([
    dbc.Row(
        [
        dash.html.H5(children="PARAMETROS",
                     style={'margin-top': '5px', 'margin-left': '2px'})
        ],className='bg-primary text-white font-italic'
    ),
    dbc.Row(
        [
        dash.html.Div(
            [
            dash.html.I(children="Empresa"),
            dash.html.Br(),
            dash.dcc.Input(id="empresa", type="text", placeholder="Nombre empresa")
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Finca"),
            dash.html.Br(),
            dash.dcc.Input(id="finca", type="text", placeholder="Nombre finca")
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Código parcela"),
            dash.html.Br(),
            dash.dcc.Input(id="parcela", type="text", placeholder="Código parcela")
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Fruta"),
            dash.html.Br(),
            dash.dcc.Dropdown(id="fruta", options=param.frutas,optionHeight=15, placeholder="Fruta")
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Variedad"),
            dash.html.Br(),
            dash.dcc.Input(id="variedad", type="text", placeholder="Variedad")
            ]
            ),

        dash.html.Div(
            [
            dash.html.I(children="Fichero de medidas"),
            dash.html.Br(),
            dash.dcc.Upload(id="medidas",
                            children=dash.html.Div(['Drag and drop ',dash.html.Br(),'or ', 
                                                    dash.html.A('Seleccionar Archivo')]
                                                ),
                            accept=".csv",
                            multiple=False,
                            style={ 'width': '100%',
                                    'height': '60px',
                                    'lineHeight': '2LO de los otros 0px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin': '10px',
                                    'font-size':'10px'}

                            ),
            dash.html.P(id='output-medidas')
            ]
        ),
        dash.html.Div(
            [
            dash.html.I(children="Diámetro comercial"),
            dash.html.Br(),
            dash.dcc.Slider(id="mindiacom", min=0, max=100, step = 1, value =50, marks = None, tooltip={"placement":"left","always_visible": True})
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Tamaño Cajón"),
            dash.html.Br(),
            dash.dcc.Slider(id="binsize", min=2, max=15, step = 1, value =5, marks = None, tooltip={"placement":"left","always_visible": True})
            ]
            ),
        dash.html.Hr(),
        dash.html.P(id="parametros",children="vacio")       
        ]
    )
])

graficos = dash.html.Div([])

app.layout = dbc.Container(
    [
    dbc.Row(
        [
        dbc.Col(selector, width=1),
        dbc.Col(graficos, width=11)
        ]
        )
    ],
    fluid=True
)

@app.callback(dash.Output('output-medidas', 'children'),
              dash.Input('medidas', 'filename'),
              dash.State('medidas', 'contents'))
              #dash.State('medidas', 'last_modified'))
def update_output(filename, contents):

    return filename

@app.callback(
    dash.Output("parametros", "children"),
    dash.Input("empresa", "value"),
    dash.Input("finca", "value"),
    dash.Input("parcela", "value"),
    dash.Input("fruta", "value"),
    dash.Input("variedad", "value"),
    dash.Input("mindiacom", "value"),
    dash.Input("binsize", "value"),
)
def parametros(empresa, finca, parcela, fruta, variedad, mindiacon, binsize):
    return "La parcela {2} de la finca {1} de la empresa {0} tiene {3} de la variedad {4}. Su calibre comercial es {5}. Clasificamos en cajones de tamaño {6}mm.".format(empresa, finca, parcela, fruta, variedad, mindiacon, binsize)

if __name__ == "__main__":
    app.run_server(debug=True, port=1234)