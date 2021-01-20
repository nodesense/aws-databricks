#APP = "file:////c:/aws-data-bricks/day1"

APP= "file:////C:/Users/Gopalakrishnan/aws-databricks/day1/"

DATA_PATH = "data"
OUTPUT_PATH = "/output"

def get_data_path(filename):
    return APP + DATA_PATH + "/" + filename

def get_output_path(filename):
    return APP + OUTPUT_PATH + "/" + filename
