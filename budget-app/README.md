### Build a Budget App Project Instructions
URL: [https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-budget-app-project/build-a-budget-app-project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-budget-app-project/build-a-budget-app-project)

Categoryクラスを完成させてください。このクラスは、食品、衣服、娯楽など、異なる予算カテゴリに基づいてオブジェクトをインスタンス化できる必要があります。オブジェクトが作成されるとき、カテゴリの名前が渡されます。クラスには、ledgerというリストのインスタンス変数も必要です。このクラスには以下のメソッドを含める必要があります。  

* depositメソッドは、金額と説明を受け取ります。説明がない場合は空の文字列をデフォルトにします。このメソッドは、{'amount': amount, 'description': description}の形式でオブジェクトをledgerリストに追加する必要があります。
* withdrawメソッドは、depositメソッドに似ていますが、渡される金額は負の数としてledgerに保存される必要があります。資金が足りない場合は、何もledgerに追加しないようにします。このメソッドは引き出しが行われた場合にTrueを返し、それ以外の場合はFalseを返す必要があります。
* get_balanceメソッドは、これまでに行われた入金と引き出しに基づいて予算カテゴリの現在の残高を返します。
* transferメソッドは、金額と別の予算カテゴリを引数として受け取ります。このメソッドは、その金額で'Transfer to [送信先の予算カテゴリ]'という説明付きの引き出しを追加し、次に他の予算カテゴリにその金額で'Transfer from [送信元の予算カテゴリ]'という説明付きの入金を追加する必要があります。資金が足りない場合は、どちらのledgerにも何も追加しないようにします。このメソッドは転送が行われた場合にTrueを返し、それ以外の場合はFalseを返す必要があります。
* check_fundsメソッドは、金額を引数として受け取ります。このメソッドは、その金額が予算カテゴリの残高を超えている場合にFalseを返し、それ以外の場合はTrueを返します。このメソッドはwithdrawメソッドとtransferメソッドで使用される必要があります。

予算オブジェクトを印刷（print）したときには、以下の形式で表示される必要があります：

* カテゴリ名が30文字で、中央に配置されたタイトル行が*文字で囲まれています。  
* ledgerの項目のリスト。各行には説明と金額が表示されます。説明の最初の23文字を表示し、次に金額を表示します。金額は右揃えで、小数点以下2桁、最大7文字で表示される必要があります。
* カテゴリ合計を表示する行。
  
使用例は以下の通りです： 
```
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```
出力例は以下の通りです：  
```
*************Food*************
deposit              1000.00
groceries            -10.15
restaurant and more foo -15.89
Transfer to Clothing -50.00
Total: 923.96
```
このCategoryクラスの他に、create_spend_chartという名前の関数（クラスの外部）を作成してください。この関数はカテゴリのリストを引数として受け取り、バーグラフを表す文字列を返します。  
  
このグラフは、関数に渡された各カテゴリで使われた金額の割合を表示する必要があります。使われた金額の割合は、入金ではなく引き出しに基づいて計算する必要があります。グラフの左側には0から100までのラベルを表示する必要があります。バーグラフはo文字で作成されます。各バーの高さは10の最も近い整数に切り捨てて計算する必要があります。バーの下には、各カテゴリの名前が縦に書かれます。バーの下の横線は、最後のバーを超えて2スペース進む必要があります。グラフの上部には'Percentage spent by category'というタイトルを表示する必要があります。  
  
この関数は、最大4つのカテゴリでテストされます。  
  
以下の出力例をよく見て、出力の間隔が例と完全に一致するようにしてください。  
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
注：F12キーを押してブラウザーコンソールを開くと、テストの詳細な出力を確認できます。
