# v44：奥側の目と肌の下塗りの修正試作

**右80度の完成版ではありません。** v43の連続変形試作を基に、奥側の目の表示切り替えと肌の下塗りを修正しました。v42の中間向きのリグは未統合です。鼻の突出・近い目と口の配置・顎と首・遠い耳と輪郭の仕上げが残っています。通常配布とReleasesは[v38](../../README.md)を維持します。

## 保存物

- [向きの往復・採用音声I・開閉・6表情（30秒）](preview/study-turn-30s.mp4)／[無音版](preview/study-turn-30s-silent.mp4)
- [中間向きの音声同期・6表情（30秒）](preview/study-voice-30s.mp4)／[無音版](preview/study-voice-30s-silent.mp4)
- [向きの途中フレーム](preview/turn-states.jpg)／[6表情比較](preview/study-turn-six-expressions.jpg)
- 編集原本：`source/koyomi-v44.cmo3`、実行モデル：`runtime/koyomi.model3.json`
- 横向き用の肌：`source/R44_SkinClean.png`、読み込みPSD：`source/skin-clean-add.psd`
- [編集箇所と残る作業](source/editing-notes.json)

## 今回の変更

奥側の白目・まぶた・閉じ目・笑顔目と虹彩を、既存の視線移動や開閉の階層を残したまま連動させました。`ParamProfileR80` の0.4から0.85で透明度を下げ、0.85以降は隠します。画像を透明にする補正であり、鼻による立体的な遮蔽の完成を意味しません。

肌に描き込まれていた前髪の線を除いた下塗り画像を用意し、元の193頂点の肌を複製して適用しました。通常は元画像、横向きでは新画像を表示します。新画像が十分に表示されてから元画像を隠し、肌に穴が空かない順序にしています。肌の追加親枠で形状差が出た試行は不採用とし、元メッシュを復元したうえで透明度を直接設定しました。

元の50パーツのUVとテクスチャ参照は完全一致、既存の参照画像領域の変更は0画素です。[画像参照の照合](verification/atlas-verification.json)。通常状態・正面〜45度・閉眼・開口・6表情の頂点位置はv38との差1e-6未満、101段階×3通りの開閉で新たな表示面の反転は0でした。[Core検証](verification/core-verification.json)。[肌と奥側の目の切り替え](verification/visibility-verification.json)。これらは右80度の作画・自然さの合格を意味しません。

## 再生と音声

Viewerの `StudyTurn` は最初の約10秒で往復し、後半で中間形状の6表情を表示します。`StudyVoice` は中間形状を保持します。`ParamProfileR45=1`、`ParamProfileR80Visible=0` を保ち、`ParamProfileR80` を0〜1へ動かす試作です。値1を右80度の完成形として扱わないでください。

**音声：VOICEVOX:春日部つむぎ**（採用音声I）。既存の目・口・表情・傾き・髪の動作曲線と6表情JSON・髪物理を保持しています。[動作曲線照合](verification/motion-preservation.json)。映像と音声を同じ時間だけ切り出し、音声単独の同期補正は行っていません。[録画の同期測定](verification/video-sync.json)。30fpsでの測定限界があります。

公開モデルには単体WAVとSound参照を含めません。[音声の利用案内](../../audio/README.md)に従って各自の環境で組み合わせてください。個人パスが映る全画面・ウィンドウ録画、アプリ・SDKも公開物に含めません。

## 利用条件

独自モデル・素材・モーション・文書・検証記録・映像部分は、権利の存在と保有の範囲で **CC BY 4.0**。**合成音声は適用対象外**で、VOICEVOXと春日部つむぎの利用条件に従います。[利用条件](LICENSE.md)・[クレジット](CREDITS.md)。AIで編集した肌の下塗りも、権利の存在と保有の範囲で同じ条件とします。第三者の権利を許諾するものではありません。
