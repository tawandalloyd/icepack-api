from apiHelper import apiHelper  # Assuming 'apiHelper.py' is in the same directory
import tsp_mcvfz472gty6_pb2
import pandas as pd

# Load your DataFrame (replace 'your_dataframe.csv' with the actual file path)
df = pd.read_csv('sample_data/publist.csv')

# Initialize API Helper with the specified model type
api = apiHelper(modelType="tsp-mcvfz472gty6")

# Create a SolveRequest and set the solveType
sr = tsp_mcvfz472gty6_pb2.SolveRequest()
sr.solveType = 0

# Access the model within SolveRequest
m = sr.model

# Add geocode points from the DataFrame
for index, row in df.iterrows():
    l = tsp_mcvfz472gty6_pb2.Geocode()
    l.id = row['id']
    l.x = row['X']
    l.y = row['Y']
    m.points.append(l)

# Print the resulting model
print(m)


reqId = api.Post(sr)
print(reqId)

