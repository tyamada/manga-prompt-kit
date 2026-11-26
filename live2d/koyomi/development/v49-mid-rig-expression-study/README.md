# v49 中間リグの眉の表情連動

v48に移植したv42のリグを基に、手前の眉を既存の表情パラメーターに連動させました。眉の設定値が0のときはv48と同じ形で、上下の端では眉がそれぞれ移動します。目と口、ほかのパーツの形はその操作で変わりません。

- [中間向き固定の採用音声I付きViewer動画](preview/study-voice-30s.mp4)
- [中間向きの表情比較](preview/study-voice-six-expressions.jpg)
- [Cubism編集原本](source/koyomi-v49.cmo3)・[実行用モデル](runtime/koyomi.model3.json)
- [眉の動きの照合](verification/rig-transfer-verification.json)・[同期測定](verification/video-sync.json)

二重輪郭と襟元の境目、右80度の鼻先と顎から首の形は未完成です。衣装を手前に重ねる試行は首に新たな段差が出たため取り除きました。眉が既存の表情に連動する一方、移植先での6表情の仕上げは制作中です。

音声は **VOICEVOX:春日部つむぎ**（採用音声I）です。Viewerを内蔵スピーカー経由で再生し、映像と音声は同じ時刻で切り出しました。動画側の同期補正は行っていません。[採用音声Iの利用案内](../../audio/README.md)

独自モデル・編集素材・モーション・文書・映像部分は権利の保有範囲でCC BY 4.0です。合成音声は対象外で、VOICEVOXと春日部つむぎの利用条件に従います。単体WAVと全画面録画は公開物から除外しています。[利用条件](LICENSE.md)・[クレジット](CREDITS.md)
