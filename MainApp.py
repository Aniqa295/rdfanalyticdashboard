import dash
import dash_core_components as dcc


# Build App
dcc._css_dist[0][‘relative_package_path’].append(‘styles.css’)
app = dash.Dash(__name__,suppress_callback_exceptions=True)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
