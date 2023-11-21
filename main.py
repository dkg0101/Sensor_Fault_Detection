from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline



# logging.info("this is first log")
# print('successs')

# if __name__=='__main__':
#     training_pipeline = TrainPipeline()
#     training_pipeline.run_pipeline()

#     from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == '__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)