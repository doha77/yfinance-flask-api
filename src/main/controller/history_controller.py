import json

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource, reqparse
from src.main.service.ticker_service import get_ticker_history

api = Namespace('tickers', description='Tickers')

parser = reqparse.RequestParser()
parser.add_argument('period',
                    help="Period",
                    default='1y', required=True)
parser.add_argument('interval',
                    help="Interval",
                    default='1d', required=True)


@api.route("/<ticker_id>/history", endpoint='history')
@api.doc(params={'ticker_id': 'Ticker id', 'interval': 'Interval'})
class HistoryController(Resource):
    @api.expect(parser)
    def get(self, ticker_id):
        period = request.args.get('period')
        interval = request.args.get('interval')
        data = get_ticker_history(ticker_id, period, interval).reset_index().to_json(orient='records')
        response = dict()
        response["history"] = json.loads(data)
        return jsonify(response)
