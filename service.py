from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def translate_word(word):
    # Papago API나 구글 번역 API를 사용하여 단어를 번역합니다.
    # 여기서는 예제로 Papago API를 사용하도록 하겠습니다.
    # 실제로는 API 키를 사용해야 합니다.

    client_id = '5AlIRHjdk1gdk6OrcuJH'  # 본인의 Papago API 클라이언트 ID
    client_secret = 'iQai6Wh5uF'  # 본인의 Papago API 클라이언트 시크릿

    url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }

    data = {
        'source': 'ko',
        'target': 'en',
        'text': word
    }

    response = requests.post(url, headers=headers, data=data)
    translated_text = response.json()['message']['result']['translatedText']
    return translated_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text_file = request.files['textfile']
    text = text_file.read().decode("utf-8")
    translated_text = translate_word(text)
    return render_template('result.html', original_text=text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
