from deepsort import nn_matching
from deepsort.tracker import Tracker
from tools import generate_detections as gdet


def load_model():
    # set thread 
    max_cosine_distance = 0.3
    nn_budget = None
    nms_max_overlap = 1.0#1.0
   # model of tracker     
    model_filename = 'MODELS/TRACK_PERSON/model_data/mars-small128.pb'
    encoder = gdet.create_box_encoder(model_filename,batch_size=1)
    metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
    #metric = nn_matching.NearestNeighborDistanceMetric("euclidean", max_cosine_distance, nn_budget)
    tracker = Tracker(metric)
    return tracker, encoder