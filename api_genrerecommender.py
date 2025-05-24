from flask import Flask
from flask_restx import Api, Resource, fields

from predict_genre import predecir_genero



app = Flask(__name__)

# Definición API Flask
api = Api(
    app, 
    version='1.0', 
    title='Genre Recommender API',
    description='API for predicting movie genres based on plot descriptions using a trained model.',
)

ns = api.namespace('recommend', description='Genre Prediction Endpoint')

# Definición argumentos o parámetros de la API (JSON input expected)
input_fields = api.model('MoviePlot', {

    'plot': fields.String(required=True, description='Plot description of the movie'),

})

# Output definition
resource_fields = api.model('RecommendationResult', {
    'result': fields.Raw(description='Dictionary of genre probabilities')
})

# Definición de la clase para disponibilización
@ns.route('/')
class PopularityApi(Resource):

    @ns.expect(input_fields)
    @ns.marshal_with(resource_fields)
    def post(self):
        input_data = api.payload  # JSON input
        recommendation = predecir_genero(input_data)
        
        return {
            "result": recommendation.to_dict(orient="records")[0]  # returns a flat dict
        }, 200
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
