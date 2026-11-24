# 瀬尾凪 Live2D Windows制作記録

## 2026-11-23 作業開始時

- 作業場所はWindows上の `manga-prompt-kit` 作業ツリー。ブランチは `main`、追跡先は `origin/main`、HEADは `381cad304ed4ea1e9adb41591c88ad53b1ddb645`。originのfetch/pushは共に `https://github.com/tyamada/manga-prompt-kit.git`。ローカル追跡参照との差分と未コミット変更は表示なし。
- セッションで渡された作業指示を適用。リポジトリ直下と `live2d/` に適用範囲の追加AGENTS.mdは見つからなかった。直下は `docs/`、`examples/`、`live2d/`、`prompts/`、`releases/`、`scripts/`、`series/`。
- 凪の既存データは正面全身PNG、制作・引き継ぎ文書、プロンプト、検証記録。開始時点で凪のPSD、CMO3、MOC3、runtimeは見つからなかった。
- [既存のSHA256SUMS](../verification/SHA256SUMS) 8項目は全件一致。PNGはディスク上のバイト列そのまま。テキスト7件はGitインデックスがLF、Windows作業ツリーがCRLFのため、照合時にメモリ上でLFに正規化した。

## デザインの根拠

- 顔・前髪・頭身は[採用プロフィールv1](../../../examples/published/nagi-profile/README.md)（2026-11-09）を優先。GitHub Release APIで `nagi_profile.jpg` の公開と既存記録に対応するSHA-256を確認した。画像本体は今回の環境で取得できず、採用JPEGとの直接比較は保留。
- 衣装は2026-11-18の[採用台帳](../../../series/tameshibu/wardrobe-20261118/adopted.json)と[冬服資料](../../../series/tameshibu/wardrobe-20261118/README.md)を参照。原画と冬服資料を目視し、青黒の長髪、ティールのリボン、白長袖ブラウス、紺プリーツ・ハイソックス、茶ローファーを確認。体育着の低い結び髪と瀬尾家の私服は、それぞれの場面の資料とする。
- [瀬尾家の通常表情](../../../series/seo/assets/nagi-expressions.png)と[A案](../../../series/seo/assets/nagi-expressions_A.png)を目視。冬服モデルの表情は[プロフィールの6表情の指示](../../../examples/published/nagi-profile/prompts/production-v1.json)に合わせ、通常表情集の抑制された演技を参照する。A案の簡略目・口は将来のギャグ差分用。
- [ためし部の設定](../../../series/tameshibu.md)のタブレットは濃いグレーで無銘。背面の縦持ちは画面左上に黒いカメラ1個、その直下に消灯した灰色LED1個。横持ちは右がカメラ、左がLED。本人の左手で端末を支え、右手でスタイラスを持つ。正面原画は両手に持ち物なし。

## 原画と試作PSD

原画は1024×1536のRGBA単層PNG。完全透明1,192,886画素、アルファ1〜15が22,002画素、アルファ255は0画素。表示上で輪郭外の半透明のにじみが認められた。制作用のアルファ調整では、輪郭のアンチエイリアスと実際の毛先を維持し、暗背景と明背景で確認する。一律しきい値で輪郭を削らない。

[試作PSD](../development/front-separation/nagi-front-hands-draft.psd) は本人右手、本人左手、残りの全身の3レイヤー。原画の見えている画素を分けた。FFmpegでPSDの合成画像をRGBAに復号し、同条件で復号した元PNGとSHA-256が一致した。合成RGBAのSHA-256は `2d1dbb0c6d58a82f3cee114f297f3bec67ac89a85da2997c919c50127c759f6b`。分割境界の最終仕上げ、袖内に隠れる手首、手のポーズ変更、Cubismへの読み込みと動作検証は未実施。[静的検証記録](../development/front-separation/draft-check.json)

## こよみから再利用する工程

| 既存資料 | 凪で使う工程 | 既存機能の範囲 |
|---|---|---|
| v21 CMO3・PSD・MOC3・runtime・Viewer録画 | 目の素材とマスク、口内部と口形の変形、顔と肩を分離する親子関係、録画による部位別の比較 | 小さい顔向き、独立まばたき、口、3表情を確認済み。髪揺れは主に一枚の素材とモーション |
| v22 毛束と横顔試作 | 毛束の固定部と可動部の分け方、隠れ領域、合成比較 | 7領域の素材と作業CMO3。個別揺れと大きな横顔の完成は未確認 |
| v23 表情試作 | exp3と30秒モーション、Viewer上の6表情比較、肩の移動量測定 | 6プリセットを実機再生。専用目・独立眉・視線・全身・手は未完 |
| 全身・手3ポーズ資料 | 肩まで含む差し替え作画と切替試験 | 作画資料段階 |

[こよみの制作記録](../../koyomi/docs/production.md) ・ [こよみのロードマップ](../../koyomi/docs/roadmap.md)

## Windows制作環境

WindowsのOSアーキテクチャはx64。PowerShell、Python 3.10、FFmpeg／FFprobe、Git、Node.jsを確認。Cubism Editor／Viewer、Photoshop、Krita、GIMP、CLIP STUDIO PAINTは、登録済みアプリ・通常のインストール先・実行中プロセスに見つからなかった。AcrobatとClipchampは確認。Pythonでレイヤー処理、Gitで出典と差分、FFmpegで静的比較と録画の抽出を実行できる。CubismのPSDインポート、変形、物理設定、書き出しはEditorのGUI、実機再生はViewerを使用する。対象アプリでのWindows GUI操作、画面キャプチャ、OpenGL実動作は導入後に確認する。

[公式ダウンロード](https://www.live2d.com/cubism/download/editor/) ・ [動作環境](https://www.live2d.com/en/cubism/download/spec/) ・ [PSD読み込み](https://docs.live2d.com/en/cubism-editor-manual/psd-import/)

## 実装順と完了条件

| 順序 | 作業 | 完了条件 |
|---|---|---|
| 1 | 採用JPEGの照合、左右斜めの参考作画、輪郭のにじみ処理 | 目の形・前髪・顎・頭身と冬の室内制服を確認。左右の資料で横顔の鼻・頬・耳と遠い目の隠れ方を確認 |
| 2 | 額と輪郭、耳、鼻、左右独立の眉・まぶた・白目・虹彩・光、口と中の歯・舌、首、髪、胴、袖と手、リボン、スカート、脚、靴、小物の作画と分割 | まぶたの背後、前髪下の肌、首、肩、袖内の手首、袖・手の背後の胴、リボン下の襟、スカート下の脚を描く。素立ちの正面を再合成し、レイヤー単独でも境界と隠れ領域を確認 |
| 3 | ArtMesh、顔角度XYZ、独立まばたき・視線・眉・口、表情 | 顔向きの上下左右と中間点で、視線・片目閉じ・口開閉・表情を組み合わせる。閉じた目から虹彩が見えず、顔・首の境が開かず、顔だけでは肩が動かない |
| 4 | 胴・肩・手、長髪と服の物理 | 胴を基準に肩・袖・腕を連結し、頭部用の変形を分離する。前髪の束、左右横髪、後ろ髪と先端は独立させ、重なる部分の揺れに時間差を持たせる。呼吸・傾き・軽い前のめりで足滑りや隙間がなく、リボンと服の揺れが控えめ |
| 5 | タブレット・スタイラス・小さな身振り | 通常、保持、筆記、身振りで腕の重複がなく、指の本数と左右が正しく、端末と手の接点が外れない。端末・ペン・袖・手を別に保持 |
| 6 | Viewerで個別試験と総合再生、約30秒の撮影 | 顔の比較、6表情の小サイズ比較、可動域と境界、物理の揺り戻し、保持から復帰を実画面で記録。EditorでPSD・CMO3を開き直し、ViewerでMOC3と参照ファイル一式を読み込めることを確認 |

6表情は、通常の伏し目がちな視線、微笑みの小さな口角、驚きのわずかな開眼と小さな開口、好奇心の横への視線、真剣の絞った眉と正面視、思案の片眉と小さな傾きで識別する。大きな顔角度と同時に安全に使える範囲は実機で決める。基本衣装の検証後に、衣装追加、ギャグ、音声同期、VTube Studioを進める。

完成時は `source/` に原画・分割PSD・CMO3、`runtime/` にMOC3・model3.json・テクスチャ・6 exp3・モーション・physics3、`preview/` に画像と約30秒の動画、`docs/` と `verification/` に記録・検証とSHA-256を保存する。現在の成果は着手記録と両手分割の試作段階。

## プロフィール添付とCubism導入後の確認

添付されたプロフィールを既存正面原画と目視で照合した。青黒の長い髪、目にかかる斜めの前髪、紫寄りの瞳、細身の体格、冬服の配色は一貫している。プロフィールの全身は斜め向きの筆記姿勢で、正面原画は左右の腕を軽く開いた素立ち。正面原画のわずかに上がった口角は添付の「ほほえみ」に近い。通常顔の初期値では「ノーマル」の短く平らな口を目安にし、現状の口角は微笑み用の基準にする。画像添付を目視資料として使用し、公開JPEGとのバイト同一性は未確認。

表情の基準は、ノーマルの半開きの目と平らな口、ほほえみの小さな口角、意外の開いた目と小さな開口、興味の横への視線と軽い笑み、真剣の下がった眉と閉じた口、疑問の首の傾きと片眉・小さな開口。タブレットは本人の左手が下側を支え、右手のスタイラスが画面側に向かう。保持姿勢では袖口から手、端末の重なりを専用に作画する。

Windowsの `C:\Program Files\Live2D Cubism 5.3` に Editor と Viewer の実行ファイルを確認。試作PSDのインポートと動作検証は別途確認する。

Cubism Editor 5.3.05 FREEで、初回PSDの読込時にPSD署名エラーが出た。PSD書き出しにVersion Info画像リソースを追加して再生成したところ、同Editorで3枚のArtMeshと正面全身の表示を確認できた。正面合成のRGBAは修正後も元PNGと一致した。Editorから [試作CMO3](../development/front-separation/nagi-front-hands-draft.cmo3) を保存した。可動設定とViewer再生は未実施。`draft-check.json` は生成処理だけの検証結果で、Editorの実機確認はこの記録を参照する。

## 正面原画の分割試作 v2

元の3レイヤー試作とは別に、両手、左右の目、口、顔の肌、リボン、左右の横髪、頭頂側の髪、スカート、左右の脚、胴・袖・後ろ髪の残りの計14レイヤーへ分けた。目と口は見えている画素の切り出し。髪・肌・衣服の境界は多角形マスクの仮置きで、見切れ・混入は部位単独で要確認。隠れた領域の描き足し、輪郭外のにじみ処理、通常口への描き直しは未実施。

元PNGに存在する全可視画素が試作レイヤーの再合成と一致し、FFmpegでPSDのプレビューを復号したRGBAも元のRGBAと一致。Cubism Editor 5.3.05 FREEで新規モデルに読み込み、ArtMesh一覧と正面全身の表示を確認して、[v2 CMO3](../development/front-separation/nagi-front-separation-v2.cmo3)を別ファイルとして保存。[v2 PSD](../development/front-separation/nagi-front-separation-v2.psd) と [検証JSON](../development/front-separation/separation-v2-check.json)。可動域・描き足し・Viewer再生は未検証。

## 手首と袖口の重なり試作 v3

v2とは別に、左右の手首が袖の内側へ続くよう肌色の重なりを描き足した。手のレイヤーを袖口を含むレイヤーの下に置き、正面姿勢（比較画像の上）と両手を下へ5px・外へ2pxずらした姿勢（下）を画像合成で比較した。試した位置では、修正後の袖口に大きな隙間は見えなかった。輪郭外の半透明のにじみと小さな境界の乱れは残る。回転、可動設定、Cubismでのv3読み込み・再生は未検証。v3では手首の画素を追加しているため、v2の元画像との画素一致はv3に適用しない。

- [v3 PSD](../development/front-separation/nagi-wrist-overlap-v3.psd)
- [袖口の比較画像](../development/front-separation/nagi-wrist-overlap-v3-comparison.png)
- [描き足しと移動量の検証JSON](../development/front-separation/wrist-overlap-v3-check.json)

## 凪の声と調声の基準（2026-11-24）

ユーザー提示の「② クールでマイペース」を凪の声の基準とする。落ち着いた低めの声で、観察や説明は明瞭に、ツッコミは一拍おいて淡々と返す。穏やかな聞き役とは、声の低さと短く言い切る語尾で聞き分けられるようにする。妹たちを気遣う場面では語尾を少し柔らかくする。

| 項目 | 試聴時の設定 |
|---|---|
| VOICEVOX音源候補 | No.7（ノーセブン）、波音リツ |
| 話速 | 0.95〜1.00 |
| 音高 | −0.06〜−0.04 |
| 聞き比べの開始値 | 両候補とも話速0.97、音高−0.05 |
| 採用音源 | VOICEVOX: 波音リツ（ノーマル、スタイル9） |

記録係としての説明、短いツッコミ、さりげない気遣いを、同じ台詞・調声値で両候補から試聴する。掛け合いでは凪を低音側に置き、行動派・賑やかな役より少し間を持たせる。Live2Dの口の動きや間の調整には、採用後の音声を使う。

## 凪の声の試聴サンプル（2026-11-24）

同じ台詞で No.7（ノーマル、スタイル29）と波音リツ（ノーマル、スタイル9）を合成した。話速0.97、音高−0.05、モノラル24kHz。音源ごとの既定のアクセントと音量を保った。利用したのはインストール済みのVOICEVOX Core 0.17.0。聞き比べの結果、ユーザーが波音リツを採用した。試聴版のノーマル、話速0.97、音高−0.05を制作時の初期値とする。

- VOICEVOX:No.7（11.73秒、制作時の試聴用）
- VOICEVOX:波音リツ（12.43秒、制作時の採用音声）
- [共通台詞](../development/voice-audition/script.txt)

## 波音リツの口パク試作

採用音声の試聴WAVから20msの窓で音量を測り、30fpsの `ParamMouthOpenY` カーブを作成した。音声とモーションは同時に開始する前提。音声12.426666…秒、モーション12.426667秒。374点のうち113点が閉口。冒頭と終端を閉口にし、音量の小さい区間にはゲートと減衰を適用した。

[モーション](../development/voice-audition/nagi-namine-ritsu-lipsync.motion3.json) ・ [検証JSON](../development/voice-audition/lipsync-check.json)。音量由来の開閉で、母音ごとの口形は未設定。凪モデルの口のArtMeshへの割り当てと、Cubism Viewerでの音声同期確認は未実施。

## 母音に合わせた口形モーション試作

波音リツの合成クエリから母音・子音・休止の区間を抽出。推定全長12.504821秒を音声の12.426667秒に合わせ、区間の長さを一律0.993750倍した。個々の発音境界は音声波形に照合していない。前回の音量カーブと母音別の開き具合を組み合わせ、口の横幅・丸めの目安を `ParamMouthForm` に追加した。休止と両端は閉口。1軸で横幅・丸めを表す試作値で、既存の表情の口形と併用する場合はパラメータの競合を確認する。

[母音対応モーション](../development/voice-audition/nagi-namine-ritsu-vowels.motion3.json) ・ [検証JSON](../development/voice-audition/vowel-motion-check.json)。PSDへの開口画の追加、モデル上のキー設定、Viewerでの再生は未実施。

## 閉口・母音5種の口パーツ試作 v4

v3の手首の重なりを含む全身分割に、共通の中心を持つ閉口と5母音の口パーツを追加。原画の微笑みは参照として保持し、v4の顔レイヤーでは口の下を周囲の肌色で補った。PSDの初期表示は閉口。あ・い・う・え・おは個別レイヤーで初期非表示。比較画像は上段左から「閉口・あ・い」、下段左から「う・え・お」。FFmpegでPSDを読み戻し、閉口の合成RGBAと一致した。Cubismへの取り込み後は各ArtMeshの表示状態を確認する。

口形をリグへ接続する際の目安は、`ParamMouthForm` の「あ +0.10、い +0.75、う −0.45、え +0.48、お −0.72」。`ParamMouthOpenY` で開閉し、値0では閉口だけを表示する。各母音は輪郭の目安として使い、途中値で口内や輪郭が二重にならないよう実機で確認する。v4に可動キーは未設定。

[v4 PSD](../development/front-separation/nagi-mouth-parts-v4.psd) ・ [口形比較](../development/front-separation/nagi-mouth-parts-v4-comparison.png) ・ [検証JSON](../development/front-separation/mouth-parts-v4-check.json)

## 波音リツの音声付き口パク確認

v4の閉口と母音口パーツを基準に、`ParamMouthOpenY` と `ParamMouthForm` の値から口の縦横を補間し、顔の拡大プレビューを作成した。各フレームで一つの口形を描画し、波音リツの採用WAVと同じ開始時刻で合成。30fps・373フレーム、音声と映像の長さの差は約7ms。MP4の映像・音声を最後まで復号できることを確認した。

[音声付きMP4（VOICEVOX:波音リツ）](../development/front-separation/nagi-ritsu-lipsync-preview.mp4) ・ [検証JSON](../development/front-separation/lipsync-preview-check.json)。この動画は画像合成による口形の確認用。編集用CMO3へのパラメータ割り当てとCubism Viewerでの確認は未実施。

## Cubismの口リグ用の形状基準

波音リツの口パク確認動画と同じ補間から、`ParamMouthOpenY`（上から0、0.25、0.5、1）と `ParamMouthForm`（左から−1、−0.72、−0.45、0、0.10、0.48、0.75、1）の組み合わせ32通りを描画した。正面原画上の口の中心は (515.5, 224.8) px。各組み合わせの輪郭範囲をJSONに記録した。閉口の列間で画素が一致することを自動照合し、比較画像で開き方と幅の変化を目視確認した。

リグでは閉口線と開口側を別に管理し、開口側の輪郭・口内・舌は同じ変形に追従させる。表は口を1形状で描画する方式の目標値。各母音レイヤーを同時に表示する設計には使わない。Cubism Editorへの可動キー入力とViewer再生は未実施。

[口形比較](../development/front-separation/nagi-mouth-keyform-grid.png) ・ [輪郭座標](../development/front-separation/nagi-mouth-keyform-targets.json)

## 口リグ用分割PSD v5

v4の顔と全身を基に、閉口線・舌・口内・開口輪郭の4レイヤーを収録。開口輪郭は口内の下に敷く下地を兼ねる。開口側3枚は初期非表示。比較画像は左から閉口、開口合成、舌、口内、輪郭下地。閉口の合成画像はPSDを読み戻してRGBA一致を確認した。

Cubismでは開口側3枚を同じワープデフォーマの子にし、開きと横幅の目標に合わせる。閉口線は開口側と重ならないよう不透明度を調整する。v5 PSDのCubism読み込みと可動キーの割り当ては未実施。v4の5母音別素材は口形参照として保存している。

[v5 PSD](../development/front-separation/nagi-mouth-rig-source-v5.psd) ・ [パーツ比較画像](../development/front-separation/nagi-mouth-rig-source-v5-preview.png) ・ [検証JSON](../development/front-separation/mouth-rig-source-v5-check.json)

## 口リグ試作とViewerでの確認（2026-11-24）

Cubism Editor 5.3.05 FREEでv5 PSDを新規モデルに読み込み、口の4つのArtMeshを確認した。開口側の3枚を同じワープデフォーマに置き、口の開閉に2キー、口幅に3キーを設定した。CMO3は別名で保存し、2048 × 2048のテクスチャ1枚を使って書き出した。

v2では推定音素時刻と波形から、促音などでの閉口と母音切り替えを調整した。Viewerでv2を6区間に分けて再生し、v3ではVOICEVOX Core 0.17.0の量子化と疑問文末の延長を含めた合成時刻に合わせた。WAVは1,165合成フレーム（12.426667秒）に対応する。v2の推定と合成時刻の最大差は約116ms。「願望じゃない？」末尾の「い」の延長は約149ms。発音境界の照合には合成フレームと音量しきい値を使い、Viewerでv3の開閉・口幅の変化と休止・終端の閉口を目視確認した。

[編集用CMO3](../development/front-separation/mouth-rig-v5-prototype/nagi-mouth-rig-v5-prototype.cmo3) · [v2](../development/front-separation/mouth-rig-v5-ritsu-timing-v2/) · [v3](../development/front-separation/mouth-rig-v5-ritsu-timing-v3/) · [発音境界の比較CSV](../development/front-separation/mouth-rig-v5-ritsu-timing-v3/phoneme-boundaries-v2-v3.csv) · [VOICEVOX Core 0.17.0の合成処理](https://github.com/VOICEVOX/voicevox_core/blob/0.17.0/crates/voicevox_core/src/engine/talk/interpret_query.rs)
