import requests
import json

def query_rawdata(dataset_id, tag):
    url = 'https://openneuro.org/crn/graphql'
    query = f"""
    query {{
      snapshot(datasetId: "{dataset_id}", tag: "{tag}") {{
        files {{
          id
          key
          filename
          size
          directory
          annexed
        }}
      }}
    }}
    """
    response = requests.post(url, json={'query': query})
    return response.json()

# import requests
# import json

# def fetch_dataset_info(dataset_id):
#     url = 'https://openneuro.org/crn/graphql'
#     query = f"""
#     query {{
#       dataset(id: "{dataset_id}") {{
#         id
#         name
#       }}
#     }}
#     """
#     response = requests.post(url, json={'query': query})
#     return response.json()

# def fetch_snapshot_info(dataset_id, tag):
#     url = 'https://openneuro.org/crn/graphql'
#     query = f"""
#     query {{
#       snapshot(datasetId: "{dataset_id}", tag: "{tag}") {{
#         id
#         tag
#         description {{
#           Name
#           DatasetDOI
#         }}
#       }}
#     }}
#     """
#     response = requests.post(url, json={'query': query})
#     return response.json()

# def fetch_snapshot_files(dataset_id, tag):
#     url = 'https://openneuro.org/crn/graphql'
#     query = f"""
#     query {{
#       snapshot(datasetId: "{dataset_id}", tag: "{tag}") {{
#         files {{
#           id
#           key
#           filename
#           size
#           directory
#           annexed
#         }}
#       }}
#     }}
#     """
#     response = requests.post(url, json={'query': query})
#     return response.json()

# if __name__ == "__main__":
#     dataset_id = "ds005342"
#     tag = "1.0.3"

#     print("Fetching dataset info...")
#     dataset_info = fetch_dataset_info(dataset_id)
#     print(json.dumps(dataset_info, indent=2))

#     print("\nFetching snapshot info...")
#     snapshot_info = fetch_snapshot_info(dataset_id, tag)
#     print(json.dumps(snapshot_info, indent=2))

#     print("\nFetching snapshot files...")
#     snapshot_files = fetch_snapshot_files(dataset_id, tag)
#     print(json.dumps(snapshot_files, indent=2))