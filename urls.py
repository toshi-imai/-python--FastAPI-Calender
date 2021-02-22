from controllers import *

app.add_api_route('/', index)
app.add_api_route('/todo/{year}/{month}/{day}', blank)
