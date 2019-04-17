from flask import Flask, Response, request
from flask_caching import Cache
from json import dumps
from BaseService import BaseService

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)
JSON_MIME_TYPE = 'application/json'
base_service = BaseService()

@app.route('/get_mined_blocks')
@app.cache.cached(timeout=60)
def get_mined_blocks():
    mined_blocks = base_service.get_mined_blocks(request.remote_addr)

    api_response = Response(dumps({"Mined blocks" : mined_blocks}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_av_time')
@app.cache.cached(timeout=60)
def get_av_time():
    av_time = base_service.get_av_time(request.remote_addr)

    api_response = Response(dumps({"Average time between blocks" : av_time}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_tx_count')
@app.cache.cached(timeout=60)
def get_tx_count():
    tx_count = base_service.get_tx_count(request.remote_addr)

    api_response = Response(dumps({"Tx count" : tx_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_fee_count')
@app.cache.cached(timeout=60)
def get_fee_count():
    fee_count = base_service.get_fee_count(request.remote_addr)

    api_response = Response(dumps({"Fee amount" : fee_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_input_count')
@app.cache.cached(timeout=60)
def get_input_couunt():
    input_count = base_service.get_input_count(request.remote_addr)

    api_response = Response(dumps({"Input count" : input_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_output_count')
@app.cache.cached(timeout=60)
def get_output_count():
    output_count = base_service.get_output_count(request.remote_addr)

    api_response = Response(dumps({"Output count" : output_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

if __name__ == '__main__':
    app.run(debug = True)