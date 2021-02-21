import dash



# Build App
external_stylesheets = ['http://jsfiddle.net/ne9ar/4ny7s0ou.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

