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
| P.96 | `!cp '/content/drive/My Drive/my_model.h5' './my_model.h5'` | `!cp '/content/drive/My Drive/my_model_aug.h5' './my_model_aug.h5'` | [#7](https://github.com/karaage0703/karaage-ai-book/issues/7) |
| P.97の1行目 | `keras_model = tf.keras.models.load_model("efficientnet_model.h5")` | `import tensorflow_hub as hub`<br>`keras_model = tf.keras.models.load_model("efficientnet_model.h5", custom_objects={'KerasLayer':hub.KerasLayer})` | [#6](https://github.com/karaage0703/karaage-ai-book/issues/6) |
| P.100の前半 | サボートサイト | サポートサイト | [#9](https://github.com/karaage0703/karaage-ai-book/issues/9) |
| P.152中ほど | `history = model.fit(x, y, batch_size=BATCH_SIZE, epochs=EPOCHS)` | `history = model.fit(x, y, batch_size=BATCH_SIZE, epochs=EPOCHS, callbacks=[print_callback])` | [#10](https://github.com/karaage0703/karaage-ai-book/issues/10) |



