# 瀬尾凪 新規正面モデルの波音リツ口パク v2

[Viewer用モデル](runtime/nagi-new-front-ritsu-lipsync-v2.model3.json) · [口パクモーション](runtime/nagi-new-front-ritsu-lipsync-v2.motion3.json) · [編集元の口リグ v2](../nagi-new-front-mouth-rig-v2/)

[口パク v1](../nagi-new-front-ritsu-lipsync-v1/)を基に、波形上の音量と既存の推定時刻を照合し、冒頭・フレーズ間・末尾の計10区間で閉口と標準の口幅を保持する範囲を調整しました。10ミリ秒窓のRMSが0.001未満の状態が3窓続く箇所を静音の目安にしました。[休止の比較表](pause-timing.csv)音声とモーションの長さは約13.003秒です。[全フレーズ確認版と発音境界](../front-separation/nagi-narration-v2-accent-v3-full-sync/)

Cubism Viewer 5.3.05でモデルを開き、motions → Narration のモーションを選択して再生します。音声を合わせる場合は、モーションにローカルのアクセント試聴版3のWAVを指定してください。音声を割り当てた状態で再生し、再生中の口形と終端の閉口を目視確認しました。休止の境目を波形で確認し、発音ごとの境界は全フレーズ確認版から引き継いでいます。

確認に使用した音声は **VOICEVOX:波音リツ** です。[波音リツの音声利用規約](https://voicevox.hiroshiba.jp/product/namine_ritsu/) · [モデル素材の利用条件](../../LICENSE.md)
