# 正誤表

現時点で判明している誤植を掲載しています。重版時に修正予定です。

表で見辛い箇所、訂正の理由を知りたい場合は、詳細の項目のリンク先を参照ください。

また、重要な修正内容に関しては、[FAQ](./FAQ.md)にまとめていますので、そちらも参照ください。

| 該当箇所 | 誤 | 正 | 詳細 |
| -- | -- | -- | -- |
| P.34 | AIを用いて、きゅうりの等級（ランク）を選別する作業を、AIにより実現しています。 | AIを用いて、きゅうりの等級（ランク）を選別する作業を実現しています。| [#5](https://github.com/karaage0703/karaage-ai-book/issues/5)|
| P.73 下部 | `!wget https://raw.githubusercontent.com/karaage0703/karaage-ai-book/util/colab_camera.py` | `!wget https://raw.githubusercontent.com/karaage0703/karaage-ai-book/master/util/colab_camera.py` | [#2](https://github.com/karaage0703/karaage-ai-book/issues/2) |
| P.75, P.246, P.255 | `img_str = encimg.tostring()` | `img_str = encimg.tobytes()` | [#4](https://github.com/karaage0703/karaage-ai-book/issues/4), [#20](https://github.com/karaage0703/karaage-ai-book/issues/20) |
| P.76 中ほど | `use_cam()` | `colab_camera.use_cam()` | [#3](https://github.com/karaage0703/karaage-ai-book/issues/3) |
| P.92 中ほど | ki_concat.jpg（画像名） | concat.jpg（画像名） | [#15](https://github.com/karaage0703/karaage-ai-book/issues/15) |
| P.96 | `!cp '/content/drive/My Drive/my_model.h5' './my_model.h5'` | `!cp '/content/drive/My Drive/my_model_aug.h5' './my_model_aug.h5'` | [#7](https://github.com/karaage0703/karaage-ai-book/issues/7) |
| P.97の1行目 | `keras_model = tf.keras.models.load_model("efficientnet_model.h5")` | `import tensorflow_hub as hub`<br>`keras_model = tf.keras.models.load_model("efficientnet_model.h5", custom_objects={'KerasLayer':hub.KerasLayer})` | [#6](https://github.com/karaage0703/karaage-ai-book/issues/6) |
| P.100の前半 | サボートサイト | サポートサイト | [#9](https://github.com/karaage0703/karaage-ai-book/issues/9) |
| P.152中ほど | `history = model.fit(x, y, batch_size=BATCH_SIZE, epochs=EPOCHS)` | `history = model.fit(x, y, batch_size=BATCH_SIZE, epochs=EPOCHS, callbacks=[print_callback])` | [#10](https://github.com/karaage0703/karaage-ai-book/issues/10) |
| P.155 テキストボックス内2段落目 | `char_numb = 100 diversity = 1.0` | `diversity = 1.0` | [#11](https://github.com/karaage0703/karaage-ai-book/issues/11) |
| P.160 3つめのテキストボックス1行目 | `import urllib` | `import urllib.request` | [#22](https://github.com/karaage0703/karaage-ai-book/issues/22) |
| P.161 1行目 | `text = normalize_text(text)` | （削除） | [#12](https://github.com/karaage0703/karaage-ai-book/issues/12) |
| P.162 2つめのテキストボックス内2行目 | `encoding='shift_jis'` | `encoding='utf-8'` | [#13](https://github.com/karaage0703/karaage-ai-book/issues/13) |
| P.186 最下行 | `model.eval()` | `model_mask.eval()` | [#14](https://github.com/karaage0703/karaage-ai-book/issues/14) |
| P.187 1つ目のテキストボックス3行目 | `outputs = model(tokens_tensor)` | `outputs = model_mask(tokens_tensor)` | [#14](https://github.com/karaage0703/karaage-ai-book/issues/14) |
| P.250の下1/3のあたり | 骨格を描画しているのは「estimator.py」の「PoseEstimator」というクラス | 骨格を描画しているのは「estimator.py」の「TfPoseEstimator」というクラス | [#25](https://github.com/karaage0703/karaage-ai-book/issues/25) |
| P.296 中ほど | Google Colabのノートブックで実践していきます。 | Google Colabのノートブック「06_karaage_ai_book_tflite_convert.ipynb」で実践していきます。 | [#18](https://github.com/karaage0703/karaage-ai-book/issues/18) |
| P.298 下から2つめのテキストボックス | `keras_model = ...` | `keras_mnist_model = ...` | [#17](https://github.com/karaage0703/karaage-ai-book/issues/17) |
