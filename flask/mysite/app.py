import os, csv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
    
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'
    
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)
    
@app.route('/html_file')
def html_file():
    return render_template('html_file.html')
    
@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name_in_html=name)
    
@app.route('/fruits')
def fruits():
    fruits = ['apple', 'banana', 'mango', 'melon']
    return render_template('fruits.html', fruits=fruits)
    
@app.route('/send')
def send():
    return render_template('send.html')
    
@app.route('/receive')
def receive():
    who = request.args.get('who') # 변수 두개 받아오기
    # request.args
    # {'who': 'yoonju', 'message': 'hello'}
    message = request.args.get('message') 
    # request(요청).args(값)는 딕셔너리 형태 => .get 사용 가능(특정한 key로 value를 가져옴)
    
    with open('guestbook.csv','a',encoding='utf8',newline='') as f: # a에 내용이 날아가지 않도록 append
        writer = csv.DictWriter(f, fieldnames=['who', 'message'])
        writer.writerow({
            'who': who,
            'message':message
        }) # 들어가는 값은 딕셔너리 형태 (key, value)
    
    return render_template('receive.html', name=who, message=message) # 변수 who를 name에 넘겨줌
    
    
@app.route('/guestbook')
def guestbook():
    messages = []
    with open('guestbook.csv','r',encoding='utf8',newline='') as f:
        reader = csv.DictReader(f)
        for row in reader: # 한 줄씩 읽어온다 => message = [] 빈 리스트에
            messages.append(row)            
    
    return render_template('guestbook.html', messages=messages)
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
    