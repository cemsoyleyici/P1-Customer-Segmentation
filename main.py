from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_validation import DataValidationPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.pipeline.stage_04_model_generation import ModelGenerationPipeline


def main():
    
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        
        obj = DataIngestionPipeline()
        dataframe = obj.main()
        
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Data Validation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        
        obj = DataValidationPipeline()
        obj.main(dataframe)
        
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        
        obj = DataTransformationPipeline()
        transformed_dataframe = obj.main(dataframe)

        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Model Generation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        
        obj = ModelGenerationPipeline()
        obj.main(transformed_dataframe)

        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
if __name__ == "__main__":
    main()