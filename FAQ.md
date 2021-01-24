# FAQ

　良くある質問です。

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

## P.281: スクリプト inspect_camera_pi.py がエラーで終了します

　バージョン不一致によるエラーが発生するケースがあるようです。以下コマンドを実行ください。

```sh
$ sudo pip3 uninstall h5py
$ sudo pip3 install h5py==2.10.0
```

参考： [#16](https://github.com/karaage0703/karaage-ai-book/issues/16)
