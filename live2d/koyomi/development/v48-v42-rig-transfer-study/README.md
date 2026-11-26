# v48 v42中間向きリグの移植試作

v47のCubismモデルへ、v42の頭部、両目、眉、口の17描画パーツとその変形を移しました。中間位置でv42の目と口が動きます。既存と移植側の画像を1枚のテクスチャアトラスに再配置しました。

- [採用音声I付きのViewer確認動画](preview/study-turn-30s.mp4)
- [中間向き固定での音声と開閉の確認動画](preview/study-voice-30s.mp4)
- [45度側での6表情](preview/study-turn-six-expressions.jpg)
- [Cubism編集原本](source/koyomi-v48.cmo3)・[実行用モデル](runtime/koyomi.model3.json)
- [移植したパーツ・マスク・開閉形状の照合](verification/rig-transfer-verification.json)

動作確認では顔向きパラメーター `ParamProfileR80` の0.4でv42が表示されます。0と1ではv47の形状と表示を保ちます。途中は両頭部の透明度で切り替える試作のため輪郭が重なります。襟元の境目、右80度の鼻先と顎・首の形、およびv42側への専用の笑顔目など6表情の移植は未完成です。動画後半の6表情は45度側で確認できます。

音声は **VOICEVOX:春日部つむぎ**（採用音声I）です。Viewerを内蔵スピーカー経由で再生し、収録した音声と映像を同じ時刻で切り出しています。音声単独の同期補正はありません。[同期測定](verification/video-sync.json)・[採用音声Iの利用案内](../../audio/README.md)

独自モデル・編集素材・モーション・文書・映像部分は権利の保有範囲でCC BY 4.0です。合成音声は対象外で、VOICEVOXと春日部つむぎの利用条件に従います。単体WAVと全画面録画は公開物から除外しています。[利用条件](LICENSE.md)・[クレジット](CREDITS.md)
