from flask_restx import Namespace, Resource, fields, marshal
from flask import Response, jsonify
from src.main.service.ticker_service import get_ticker_info

api = Namespace('tickers', description='Tickers')
wild = fields.Wildcard(fields.String)
api_response = {
    'status': Response.status,
    '*': wild
}


@api.route("/<ticker_id>/info", endpoint='tickers')
@api.doc(params={'ticker_id': 'Ticker id'})
class TickerController(Resource):
    def get(self, ticker_id):
        return get_ticker_info(ticker_id)
