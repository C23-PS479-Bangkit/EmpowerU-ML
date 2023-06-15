from fastapi import FastAPI
import uvicorn
import pickle

from pydantic import BaseModel


class Comment(BaseModel):
    comments: list

app = FastAPI(debug=True)

@app.get('/')
def home():
    return {"model" : "Sentiment Analysis"}

@app.post('/predict')
async def predict(listComment: Comment):
    listComment = listComment.comments
    print(listComment)
    # openPickle = open("model/test.pkl", "rb")
    # model = pickle.load(openPickle)
    # sum = 0
    # for comment in listComment:
    #     makeprediction = model.predict(comment)
    #     sum += int(makeprediction)
    # # cari nilai rata2 dari komentar yang di masukkin atau mungkin lu ada cara lain idk
    # return sum/len(listComment)
    return "Berhasil jalan"

if __name__ == "__main__":
    uvicorn.run(app)