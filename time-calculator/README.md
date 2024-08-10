### Build a Time Calculator Project
[https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-time-calculator-project/build-a-time-calculator-project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-time-calculator-project/build-a-time-calculator-project)




このプロジェクトでは次の関数を作成します。  

関数名: add_time  

引数:  
12時間形式の開始時間（AMまたはPMで終わる）  
継続時間（時間と分を示す）  
（オプション）開始曜日（大文字小文字を区別しない）  

この関数は、開始時間に継続時間を加算し、その結果を返します。  

もし結果が次の日になる場合、「(next day)」を時間の後に表示します。  
もし結果が数日後になる場合、「(n days later)」を時間の後に表示します。この場合、「n」は日数を表します。  
もしオプションの開始曜日が指定されている場合、出力には結果の曜日を表示します。曜日は時間の後、日数の前に表示します。  

以下は関数が処理するさまざまなケースの例です。結果のスペーシングと句読点に注意してください。  

add_time('3:00 PM', '3:10')  
#戻り値: 6:10 PM  

add_time('11:30 AM', '2:32', 'Monday')  
#戻り値: 2:02 PM, Monday  

add_time('11:43 AM', '00:20')  
#戻り値: 12:03 PM  

add_time('10:10 PM', '3:30')  
#戻り値: 1:40 AM (next day)  

add_time('11:43 PM', '24:20', 'tueSday')  
#戻り値: 12:03 AM, Thursday (2 days later)  

add_time('6:30 PM', '205:12')  
#戻り値: 7:42 AM (9 days later)  

注意点:  
Pythonのライブラリは使用しないこと。  
開始時間は有効な時間であると仮定すること。  
継続時間の分は60未満の整数であり、時間は任意の整数である。  
