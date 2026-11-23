# こよみ Live2Dモデル

『ためし部』の小坂こよみのLive2D制作データ **v27** です。v26の顔立ち・音声同期・専用の笑顔目・上下左右の視線・6表情を保ち、**顔の動きに応じて6毛束が控えめに揺れる物理演算**を追加しました。

![6表情](preview/six-expressions.jpg)

[音声付き確認動画（30秒）](preview/showcase-30s.mp4) · [無音版](preview/showcase-30s-silent.mp4) · [視線・閉眼・笑顔目の動画](preview/gaze-check.mp4) · [視線の比較画像](preview/gaze-comparison.jpg)

音声：**VOICEVOX:春日部つむぎ**。最初の約9秒が自己紹介、続いて6表情を比較します。動画の音声・映像を別々にずらす同期補正は行っていません。

[モデル・PSD・CMO3・確認動画のZIP](https://github.com/tyamada/manga-prompt-kit/releases/tag/koyomi-live2d-v27-20261123)

## 再生・編集

1. Cubism Viewerで [`runtime/koyomi.model3.json`](runtime/koyomi.model3.json) を開きます。SDK 5.3対応です。
2. `motions > HairStrandsCheck` は6毛束の個別確認、`motions > Showcase` は30秒の自己紹介動作と6表情、`GazeCheck` は上下左右・斜めの視線と閉眼・笑顔目の確認です。配布モデルは無音です。[音声を自分の環境で追加する手順](audio/README.md)を参照してください。
3. `Showcase` と `PhysicsCheck` は**物理演算をオン**にします。`HairStrandsCheck` は直接パラメータを動かすため**物理演算をオフ**にします。自動目パチ・カーソル追従・呼吸・アイドリングモーションと手動表情は解除してください。別版の確認ウィンドウを閉じると描画負荷を減らせます。
4. 手動の `expressions` ではノーマル・嬉しい・びっくり・ひらめき・やってみよう！・気づいたを選べます。表情を有効にし、モーションを停止して切り替えてください。表情設定は口の開閉値を上書きしないため、音声の口開閉と併用できます。
5. 編集は [`source/koyomi-v27.cmo3`](source/koyomi-v27.cmo3) をCubism Editorで開きます。原画は [`source/koyomi-v27.psd`](source/koyomi-v27.psd)（35層）と分割PNG・SVGです。追加笑顔目のみのPSDと、髪7パーツだけのPSD・分割PNGも保存しています。v17/v21/v25/v26素材は履歴参照用です。

## 目・表情とv27の髪揺れ

- `ParamEyeBallX/Y`：虹彩・瞳孔・ハイライトを両眼一緒に移動します。白目・まぶた・顔は固定し、既存の閉眼制御を保持しています。
- `ParamEyeLSmile`：左右共通の専用笑顔目を制御します。左目だけの制御ではありません。使用時は両眼の `ParamEyeLOpen/ROpen` を0にします。収録した嬉しい表情では自動的に設定します。
- 嬉しいは笑顔目、びっくりは丸い口と上がった眉、ひらめきは上向きの視線、やってみよう！は少し下げた眉と笑顔、気づいたは横への視線と小さな口で違いを付けています。左右の眉は共通制御で、独立した眉演技は未実装です。
- 髪は固定の頭頂部と可動6毛束に分割。`ParamHairOuterL/SideL/BangC/BangR/SideR/OuterR`（各-1〜1、初期値0）で個別に動きます。左右は本人基準です。根元を抑え、既存の頭部変形・全体髪揺れに追従させています。
- `Showcase` は顔・音声・6表情をモーションで、6毛束を物理演算で動かします。個別毛束の焼き込み曲線を外し、二重制御を避けました。
- `PhysicsCheck` は顔だけを動かす21秒の確認モーションです。[物理演算オン](preview/physics-on.mp4)・[オフ](preview/physics-off.mp4)・[比較画像](preview/physics-comparison.jpg)を保存しました。停止後の控えめな髪の収束を確認できます。
- [毛束別の実行動画](preview/hair-strands-check.mp4)と[視線動画](preview/gaze-check.mp4)は同一メッシュのv26記録を保持しています。`HairStrandsCheck` は物理演算オフで1本ずつ直接動かします。
- 大きな横顔、独立眉、体・リボン・手の演技、VTube Studio追従は未完了です。

[実機確認記録](verification/v27-runtime.json) · [制作記録](docs/production.md) · [全体計画と残作業](docs/roadmap.md) · [開発資料](development/README.md)

## フォルダー構成と利用条件

| フォルダー | 内容 |
| --- | --- |
| `runtime/` | MOC3・物理演算・設定・テクスチャ・モーション・6表情。一式で利用 |
| `source/` | 編集CMO3・PSD・分割PNG/SVG・レイヤー一覧 |
| `audio/` | セリフ・調声設定・利用者の環境での音声追加手順 |
| `preview/` | モデル部分だけの確認動画・比較画像。旧版の記録も保持 |
| `verification/` | 実機検証・容量・SHA-256 |
| `development/` | 大きな横顔・旧毛束試作・全身・手の制作途中資料 |

独自のモデル・素材・文書・動画の映像部分は[CC BY 4.0](LICENSE.md)。**合成音声は対象外**で、VOICEVOXおよび春日部つむぎの規約に従います。[クレジットと利用条件](docs/credits.md)を確認してください。単体WAV、個人パスが映る全画面録画、SDK本体は配布しません。
