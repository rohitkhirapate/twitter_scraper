import requests,os,io
from google.cloud import vision
#This function processes tweet image to generate hashtag
def process_image(image_url,path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='client_secrets.json'
    client = vision.ImageAnnotatorClient()
    image_loc = path+'.jpg'
    with io.open(image_loc, 'rb') as image_file:
        content = image_file.read()
    # pylint: disable=no-member
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    output_str=''
    for label in labels:
            output_str+="#"
            output_str+=label.description.replace(' ','')
            output_str+=" "
    return output_str

#This function processes Tweet dictionary to save them as Tweet Text and Tweet Media(Image) File in the Pics folder.
def process_tweets(tweets):
    counter = 0
    for key in tweets:
        counter+=1
        file_name = 'InstaPost_'+str(counter)
        resp = requests.get(tweets[key], stream=True)
        path = 'pics/'+file_name
        with open(path+'.jpg', 'wb') as f:
            for ch in resp:
                f.write(ch)
            print(path+'.jpg saved in Pics')
        hashtags=process_image(tweets[key],path)
        key+=" "+hashtags
        with open(path+'.txt', 'w') as f:
            print(key, file=f)
            print(path+'.txt saved in Pics')

