# 採用音声Iを自分の環境で再生成する

配布モデルとZIPにはWAVを含みません。音声付き確認は[動画](../preview/showcase-30s.mp4)を使用してください。音声：VOICEVOX:春日部つむぎ。

採用Iの調声値は `self-introduction.audio-query.json`、台本は `script.txt`。ノーマル（speaker8）、話速1.05、音高+0.02。確認時はVOICEVOXエンジン0.26.1、音源0.16.1、44100Hz、398429サンプル、約9.034671秒でした。JSONは合成用クエリであり、VOICEVOX Editor用vvprojではありません。

公式規約を確認して用意したローカルVOICEVOXエンジンの `/synthesis?speaker=8&enable_interrogative_upspeak=true` にクエリを渡して再生成します。版や音源が異なる場合、同じ音声・時間になるとは保証しません。生成したWAVを `../runtime/sounds/self-introduction.wav` に保存し、model3.jsonの `FileReferences.Motions.ShowcaseBoth[0]` または `ShowcaseL45[0]` 等へ `"Sound": "sounds/self-introduction.wav"` を追加するとViewerで音声付き再生できます。曲線は採用Iの発音時間に対応しています。自分の音声に替えた場合は同期を再確認してください。

単体音声はCC BY 4.0の対象外で、VOICEVOXおよび春日部つむぎの規約に従います。生成WAVを公開用フォルダーへ登録しないでください。
