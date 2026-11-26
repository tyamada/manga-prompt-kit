# v47 右向きの中間輪郭と顎の調整

v46を基に、既存の肌パーツにv42の中間向きの輪郭を参照したキーを追加し、鼻先側と顎を調整しました。深く向いた終点では鼻先側の2頂点を調整し、顎はv46の形へ戻しました。顎を寄せた試行では段差が見つかりました。v42のリグ自体の移植、鼻先の突出と首の描画の仕上げは制作中です。

- [採用音声I付きのViewer確認動画](preview/study-turn-speaker-30s.mp4)
- [顔向き・まばたき・口・6表情のViewer確認動画（無音）](preview/study-turn-30s-silent.mp4)
- [6表情の比較](preview/study-turn-six-expressions.jpg)
- [Cubism編集データ](source/koyomi-v47.cmo3)
- [実行用モデル](runtime/koyomi.model3.json)
- [検証記録](verification/)

45度では元の形を保ち、その先で中間の形を経由します。101段階の向きと3通りの開閉で新しい面の反転はありませんでした。モーション、6表情、髪の物理設定はv46と同一です。

音声は **VOICEVOX:春日部つむぎ**（採用音声I）です。Bluetooth出力での録画では発話途中に約0.32秒のずれが再現しました。ViewerだけをMacの内蔵スピーカー経由に設定すると、収録音の途中でのずれは観測されず、音声と口の動きの測定差は約0.014秒でした（30fps）。映像と音声は同じ位置で切り出し、音声単独の補正は行っていません。[出力経路の比較](verification/audio-route-comparison.json)・[同期測定](verification/video-sync-speaker.json)・[採用音声Iの案内](../../audio/README.md)

独自モデル・素材・モーション・文書・映像部分には権利の保有範囲でCC BY 4.0を適用します。合成音声は対象外で、VOICEVOXと春日部つむぎの利用条件に従います。単体WAVと全画面録画は公開物から除外しています。[利用条件](LICENSE.md)・[クレジット](CREDITS.md)
