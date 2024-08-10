### Build a Probability Calculator Project Instructions
URL: [https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-probability-calculator-project/build-a-probability-calculator-project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-probability-calculator-project/build-a-probability-calculator-project)  
  
次のような帽子があるとします。帽子には青いボールが5個、赤いボールが4個、緑のボールが2個入っています。4個のボールをランダムに引いたときに、少なくとも1個の赤いボールと2個の緑のボールが含まれている確率はどれくらいでしょうか？高度な数学を使って確率を計算することもできますが、より簡単な方法として、大量の試行を実施して近似確率を推定するプログラムを書くことができます。  
  
このプロジェクトでは、帽子から特定のボールをランダムに引く確率を近似するプログラムを作成します。  
  
まず、main.pyにHatクラスを作成します。このクラスは、帽子に含まれる各色のボールの数を指定する可変引数を受け取ります。例えば、以下のようにクラスオブジェクトを作成できます：  
```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```
帽子は常に少なくとも1個のボールで作成されます。帽子オブジェクトの作成時に渡された引数は、contentsというインスタンス変数に変換されるべきです。contentsは、帽子のボールのリストで、各アイテムはその色の単一のボールを表す文字列です。例えば、帽子が {'red': 2, 'blue': 1} の場合、contents は ['red', 'red', 'blue'] となります。  
  
Hatクラスにはdrawメソッドが必要です。このメソッドは、引数として引き出すボールの数を受け取り、contents からランダムにボールを取り除いて、そのボールを文字列のリストとして返します。ボールは引き出した後、帽子に戻ることはありません（回収なしの実験と同様です）。引き出すボールの数が利用可能な量を超える場合は、すべてのボールを返します。  
  
次に、main.pyにexperiment関数を作成します（Hatクラスの内部ではなく）。この関数は以下の引数を受け取る必要があります：  
  
Hat: ボールが含まれている帽子オブジェクトで、この関数内でコピーされるべきです。  
expected_balls: 帽子から引き出そうとするボールの正確なグループを示すオブジェクト。例えば、2個の青いボールと1個の赤いボールを引き出す確率を求める場合、expected_balls は {'blue':2, 'red':1} です。  
num_balls_drawn: 各実験で引き出すボールの数。  
num_experiments: 実施する実験の数。（実験の数が多いほど、近似確率はより正確になります。）  
experiment関数は確率を返す必要があります。  
  
例えば、6個の黒いボール、4個の赤いボール、3個の緑のボールが入った帽子から5個のボールを引き出すとき、少なくとも2個の赤いボールと1個の緑のボールを得る確率を求める場合、以下のようにexperiment関数を呼び出します：  
```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```
出力は次のようになるでしょう：  
```
0.356
```
これはランダムな引き出しに基づいているため、コードを実行するたびに確率はわずかに異なる場合があります。  
  
ヒント：ファイル内でランダムシードを初期化しないでください。すでにインポートされているモジュールの使用を考慮してください。  
  
注意：テストの詳細な出力を確認するには、ブラウザコンソールをF12キーで開いてください。  
