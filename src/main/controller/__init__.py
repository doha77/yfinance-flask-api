from flask_restx import Api
from .info_controller import api as info_api
from .history_controller import api as history_api

api = Api(
    title='MyPortfolio Ticker Service',
    version='1.0',
    description='MyPortfolio microservice to retrieve ticker info from yahoo finance api',
    doc='/swagger'
)

api.add_namespace(info_api, '/api/v1/tickers')
api.add_namespace(history_api, '/api/v1/tickers')
