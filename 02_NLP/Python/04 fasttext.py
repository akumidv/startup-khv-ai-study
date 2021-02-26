import fasttext

comment = 'Очень жарко. 28 градусов. A из окна дует холод. Особенно на нижней полке.'

model = fasttext.train_supervised(input='./review_tone.train.txt', epoch=100)
model.save_model('./review_model')

print(model.predict(comment))
