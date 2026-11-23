# 自分の環境で音声を追加する

配布モデルは無音でモーションを再生します。音声単体の再配布を避けるためWAVは同梱していません。音声付き確認動画は `../preview/self-introduction.mp4` で確認できます。

1. VOICEVOXおよび春日部つむぎの利用規約を確認し、自分の環境にVOICEVOXを用意します。
2. `script.txt` のセリフを春日部つむぎ・ノーマルで生成します。話速1.05、音高+0.02。細かい調声値は `self-introduction.audio-query.json` を参照してください。エンジンの版や読みの違いにより、既存モーションとの同期には調整が必要な場合があります。
3. WAVを `../runtime/sounds/self-introduction.wav` に保存します。
4. `../runtime/koyomi.model3.json` の `FileReferences.Motions.Greeting[0]` に `"Sound": "sounds/self-introduction.wav"` を追加すると、Viewerでモーションと一緒に読み込めます。

ローカル生成WAVはこの公開フォルダーの `.gitignore` で除外しています。生成音声の再配布条件は公式規約を確認してください。

クレジット：VOICEVOX:春日部つむぎ
