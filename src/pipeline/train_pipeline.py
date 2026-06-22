("""Train pipeline: runs ingestion, transformation, and model training.

Run with:
	python src\pipeline\train_pipeline.py

""")
import sys
from src.logger import logging
from src.exception import CustomException

from src.component.data_ingestion import DataIngestion
from src.component.data_transformation import DataTransformation
from src.component.model_trainer import ModelTrainer


def run_pipeline():
	try:
		ingestion = DataIngestion()
		train_path, test_path = ingestion.initiate_data_ingestion()

		transformer = DataTransformation()
		train_arr, test_arr, _ = transformer.initiate_data_transformation(train_path, test_path)

		trainer = ModelTrainer()
		r2 = trainer.initiate_model_trainer(train_arr, test_arr)

		logging.info(f"Model training completed with R2 score: {r2}")

	except Exception as e:
		raise CustomException(e, sys)


if __name__ == "__main__":
	run_pipeline()

