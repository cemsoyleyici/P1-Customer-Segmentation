
import subprocess
from src import logger
from src.pipeline.stage_05_prediction import PredictionPipeline
from flask import Flask, request, render_template, jsonify


def main(country: str, os: str, sex: str, age: int):
    
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        
        obj = PredictionPipeline()
        pred = obj.main(country, os, sex, age)
        
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
        return pred
    
    except Exception as e:
        logger.exception(e)
        raise e


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    
    if request.method == 'POST':
        try:
            # Get form inputs
            country = request.form['country']
            os = request.form['os']
            sex = request.form['sex']
            age = int(request.form['age'])
            
            # Call the prediction function
            pred = main(country, os, sex, age)
            
            if pred is not None:
                prediction_result = {
                    'income': round(pred[0], 2),
                    'segment': pred[1]
                }
            else:
                prediction_result = {
                    'income': "N/A",
                    'segment': "N/A"
                }
            
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            prediction_result = {'error': str(e)}
    
    return render_template('index.html', prediction=prediction_result)

@app.route('/generate_model', methods=['POST'])
def generate_model():
    try:
        # main.py'yi çalıştır
        result = subprocess.run(['python', 'main.py'], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode == 0:
            return jsonify({'result': 'Model successfully generated!', 'status': 'success'})
        else:
            return jsonify({'result': f'Error generating model: {result.stderr}', 'status': 'error'})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}', 'status': 'error'})
    
if __name__ == '__main__':
    app.run(debug=False)