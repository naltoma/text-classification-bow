# bag-of-words + TF-IDF で作成した文書ベクトルを用いて、ロジスティック線形モデルで分類学習してみる例

## クイックスタート
```
cd src
python BagOfWords.py
```

## やってること
- 文書の前処理
    - mecabを使って、動詞のみステミング処理。
    - 分かち書き処理（形態素を半角スペース区切りで並べたstrオブジェクトを用意）。
    - [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)で、出現単語回数をカウントし、単語文書ベクトル作成。
    - [TfidfTransformer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html)で、TF−IDF処理。
- 機械学習
    - [LogisticRegression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)で、学習。
    - [Pipeline](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)で、モデルとパラメータの組み合わせを用意。
    - [GridSearchCV](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)で、パラメータ調整。

## 設定方法
- config.json　を参考に、文書を置くディレクトリとクラスの設定を記述。
    - base_directory の直下に「クラス名」でディレクトリを用意すること。
    - 「クラス名」ディレクトリの中に、1文書を1テキストファイル（拡張子txt）で用意すること。txtじゃないファイルは無視されます。

## 動作確認環境
- Mac OS X 10.11.6
- Python 3.5.2
- 以下、pip freezeでの主なライブラリ情報
```
mecab-python3==0.7
numpy==1.11.1
scikit-learn==0.17.1
scipy==0.17.1
```
