import json
from data_loading import load_data
# from openneuro_query import query_rawdata

def main(dataset_id, tag):
    print("Fetching sub-001 files...")
    eeg_file = query_rawdata(dataset_id, tag)
    print(json.dumps(eeg_file, indent=2))



if __name__ == "__main__":
    dataset_id = "ds005194"
    tag = "1.1.0"
    
    # main(dataset_id, tag)
    
    # data_path = mne.datasets.sample.data_path()
    # print(f"Sample dataset path: {data_path}")

    load_data()
   