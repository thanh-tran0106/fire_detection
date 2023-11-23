from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Open311 Endpoint Simulation', description='A simple Open311 endpoint with Swagger UI and Geo-location support')

open311_ns = api.namespace('open311', description='Open311 operations')

post_payload = api.model('PostData', {
    'data': fields.String(required=True, description='Sample data'),
    'longitude': fields.Float(required=True, description='Longitude of the location'),
    'latitude': fields.Float(required=True, description='Latitude of the location'),
})

@open311_ns.route('/endpoint')
class Open311Endpoint(Resource):
    @api.expect(post_payload)
    def post(self):
        """Simulate an Open311 POST endpoint with Geo-location support"""
        data = request.json['data']
        longitude = request.json['longitude']
        latitude = request.json['latitude']

        # Print the received geo-location to the log (server console)
        print(f"Received Geo-location - Longitude: {longitude}, Latitude: {latitude}")

        # Here, you can process or store the geo-location data as required.

        return jsonify(status='success', data=data, longitude=longitude, latitude=latitude)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

