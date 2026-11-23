# こよみ Live2Dモデル

『ためし部』の小坂こよみのLive2D制作データです。元絵の顔立ちを使ってパーツ境界を調整した **v17** を収録しています。

![正面](preview/front.jpg)

[音声付き確認動画（9.5秒）](preview/self-introduction.mp4) · [動きの比較画像](preview/motion-contact-sheet.jpg)

## フォルダー構成

| フォルダー | 内容 |
| --- | --- |
| `runtime/` | MOC3、モデル設定、テクスチャ、モーション。フォルダー一式で利用 |
| `source/` | Cubism編集用CMO3、レイヤーPSD、分割PNG・境界SVG、レイヤー一覧 |
| `audio/` | セリフ、VOICEVOX調声設定。WAVのローカル生成・追加手順 |
| `preview/` | 正面画像、実機録画から作った確認動画、比較画像 |
| `docs/` | 制作・再生・利用条件の説明 |
| `verification/` | 実機確認結果、各ファイルの容量・SHA-256 |

## 再生・編集

1. Live2D Cubism Viewerで [`runtime/koyomi.model3.json`](runtime/koyomi.model3.json) を開きます。
2. `motions > Greeting > self-introduction` を選択して再生します。配布モデルは無音で動きます。音声の追加は[audio/README.md](audio/README.md)を参照してください。
3. 編集にはCubism Editorで [`source/koyomi-v17.cmo3`](source/koyomi-v17.cmo3) を開きます。原画の変更にはPSD・分割素材を使います。

書き出し・確認環境はCubism 5.3.04 FREE、SDK 5.3対応です。Editorから再書き出しした場合は、モーション・音声の参照設定も保持または再設定してください。

顔の小さな左右・上下向きと傾き、まばたき、口の開閉に対応しています。肩は顔の変形から分離しています。大きな横顔向けの作り込みは含みません。

音声：**VOICEVOX:春日部つむぎ**。音声・音声を含む動画の利用は[クレジットと利用条件](docs/credits.md)を確認してください。

詳細：[制作と確認記録](docs/production.md)。独自のモデル・素材・文章・映像は[CC BY 4.0](LICENSE.md)で提供します。合成音声は対象外です。[無音版動画](preview/self-introduction-silent.mp4)はCC BY 4.0で利用できます。
