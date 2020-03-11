# karaage-ai-book util

## split_train_val.py
### 概要
教師データのディレクトリを、訓練データのディレクトリ(train)と検証データのディレクトリ(val)に分けるスクリプト

### 使い方
　コマンドは以下。
```sh
$ python split_train_val.py <original_dir> <target_dir> train_size
```

- `<original_dir>` : 教師データのディレクトリ
- `<target_dir>` : 対象のディレクトリ（この下に訓練データと検証データのディレクトリが生成される）
- train_size : 訓練データの割合（0.0〜1.0）

使用例

```sh
$ python split_train_val.py datasets split_dir 0.7
```

### 参考サイト
- https://qiita.com/komiya-m/items/c37c9bc308d5294d3260