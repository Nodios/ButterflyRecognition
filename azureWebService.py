import urllib.request # If you are using Python 3+, import urllib instead of urllib2
import imageToCSV as service #import our module
import json 


def getImage(species=0, butterfly=1, testFolder=False, customImage=''):
    '''
    Retrieves image object containing all the data needed for the prediction.

    Input the numbers from 0 to 3 for species and 1 to 15 for the butterfly in the folders used for learning.
    If testFolder is set to True, alghoritm will use test images inside Testing Images folder also goruped by
    species. There are only 2 test images of each species avaliable. They are called 1 and 2.

    To import custom images just provide path to an image.

    Folder structure:
        0. American Snout
        1. Blue Morpho
        2. Garden Tiger Moth
        3. Goliath Birdwing

    Butterfly: 1 - 15
    Test Images butterfly: 1 or 2

    Output is Image object.
    '''
    return service.outputSingle(species,butterfly,testFolder,customImage)

def predictButterfly(image):
    '''
    After you get an Image object with image data. Call this method with Image object as the parametar.

    Input: Image object
    Output: JSON from Azure ML Experiment
    '''
    data =  {
            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["rd", "gd", "bd", "r1", "g1", "b1", "r2", "g2", "b2", "r3", "g3", "b3", "r4", "g4", "b4", "r5", "g5", "b5", "r6", "g6", "b6", "name"],
                        "Values": [ [ image.rd, image.gd, image.bd, image.r1, image.g1, image.b1, image.r2, image.g2, image.b2, image.r3, image.g3, image.b3, image.r4, image.g4, image.b4, image.r5, image.g5, image.b5, image.r6, image.g6, image.b6, image.name ] ]
                    },
            },
            "GlobalParameters": {
            }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/40874969104b4d6e804f1f1e5e317f1b/services/a6ea0ace5a79421fad507e5a3940ad64/execute?api-version=2.0&details=true'
    api_key = 't75kz56azS1gdErntK8/RmH9X02yHE0wdKU9BkIyKgXo+Rvs8RCfDnyY5uziItpzXEKNNhpCbqxZ+/NYpTFt4g=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result) 
    except urllib.HTTPError.error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))
