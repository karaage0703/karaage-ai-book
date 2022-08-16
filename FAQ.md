# FAQ

　良くある質問です。

## P.43: `uploaded = files.upload()`でエラー

　ファイルアップロードの以下のコマンド実行時

```python
from google.colab import files
uploaded = files.upload()
```

　以下のエラーがでるケースです。

```
Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
```

　Third PartyのCookieをブロックする設定になっている可能性があるので、Google Chromeブラウザの設定を見直してください。設定は、[こちらのGoogleのサイトの説明](https://support.google.com/chrome/answer/95647?co=GENIE.Platform%3DDesktop&hl=ja#zippy=%2Ccookie-%E3%82%92%E8%A8%B1%E5%8F%AF%E3%81%BE%E3%81%9F%E3%81%AF%E3%83%96%E3%83%AD%E3%83%83%E3%82%AF%E3%81%99%E3%82%8B)を参考にしてください。

　設定は、デフォルトの設定が「シークレットモードでサードパーティのCookieをブロックする」なので、特にこだわりなければそちらに設定するのが良いと思います。

## P.76: use_cam() が NameError になる

　書籍の誤記となります。以下の通り修正ください。

```
誤：use_cam()
正：colab_camera.use_cam()
```

参考: [#3](https://github.com/karaage0703/karaage-ai-book/issues/3)

## P.75: colab_camera.use_cam() で DeprecationWarning が繰り返し出力される

　以下の通り修正ください。

```
誤：img_str = encimg.tostring()
正：img_str = encimg.tobytes()
```

参考： [#4](https://github.com/karaage0703/karaage-ai-book/issues/4)


## P.242: `%tensorflow_version 1.x`で`Tensorflow 1 is unsupported in Colab.`と表示される

 Google Colabの仕様変更によるエラーです。

`%tensorflow_version 1.x`の代わりに `!pip install tensorflow-gpu==1.15.2` を入力ください。


Google Colabのノートブックも修正しています。Google Colab ノートブック メニューの「ランタイム -> ランタイムのタイプを変更」でハードウェア アクセラレータがGPUになっていることを確認ください。

https://colab.research.google.com/drive/1dtBgF774jFSc405ik4C1Em0KM8IYUvTX?usp=sharing

参考： [#36](https://github.com/karaage0703/karaage-ai-book/issues/36)



## P.281: スクリプト inspect_camera_pi.py がエラーで終了します

　バージョン不一致によるエラーが発生するケースがあるようです。以下コマンドを実行ください。

```sh
$ sudo pip3 uninstall h5py
$ sudo pip3 install h5py==2.10.0
```

参考： [#16](https://github.com/karaage0703/karaage-ai-book/issues/16)
