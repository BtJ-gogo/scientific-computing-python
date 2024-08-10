### Build a Polygon Area Calculator Project Instructions
URL: [https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-polygon-area-calculator-project/build-a-polygon-area-calculator-project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-polygon-area-calculator-project/build-a-polygon-area-calculator-project)  
このプロジェクトでは、オブジェクト指向プログラミングを使用して、RectangleクラスとSquareクラスを作成します。SquareクラスはRectangleのサブクラスであり、Rectangleのメソッドと属性を継承する必要があります。  
  
Rectangleクラス  
Rectangleオブジェクトが作成されるときは、widthとheightの属性で初期化される必要があります。このクラスには以下のメソッドを含める必要があります：  
  
* set_width：幅を設定するメソッド  
* set_height：高さを設定するメソッド  
* get_area：面積を返すメソッド（width * height）  
* get_perimeter：周囲の長さを返すメソッド（2 * width + 2 * height）  
* get_diagonal：対角線の長さを返すメソッド（(width ** 2 + height ** 2) ** .5）  
* get_picture：'*'の行を使って形状を表す文字列を返すメソッド。行の数は高さと等しく、各行の'*'の数は幅と等しい。各行の末尾には改行（\n）が必要です。幅または高さが50を超える場合は、文字列 'Too big for picture.' を返します。  
* get_amount_inside：別の形状（正方形または長方形）を引数として受け取り、渡された形状がどれだけその形状の中に収まるかを返すメソッド（回転は考慮しない）。例えば、幅4、高さ8の長方形は、幅4の正方形2つが収まります。  
さらに、Rectangleのインスタンスが文字列として表現される場合、次のように表示される必要があります：'Rectangle(width=5, height=10)'。  
  
Squareクラス  
SquareクラスはRectangleクラスのサブクラスである必要があります。Squareオブジェクトが作成されるときは、一辺の長さが渡されます。__init__メソッドは、Rectangleクラスの幅と高さの両方に一辺の長さを保存する必要があります。  

SquareクラスはRectangleクラスのメソッドにアクセスできる必要がありますが、set_sideメソッドも含める必要があります。Squareのインスタンスが文字列として表現される場合、次のように表示される必要があります：'Square(side=9)'。  

さらに、Squareクラスのset_widthおよびset_heightメソッドは、幅と高さの両方を設定する必要があります。  
  
使用例  
```
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
このコードは次の結果を返すべきです：  
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```
注：ブラウザコンソールをF12キーで開くと、テストの詳細な出力を確認できます。
