# 4コママンガのプロンプトと制作手順

**最新状況（2026年11月25日）**：[公開記録](releases/pixiv-publication-status.md)は29作品・X告知21件。第1話の表紙と全13回（14/14枚）のpixiv投稿完了報告がそろいました。[第1話の本文画像Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)を公開し、全18添付の匿名取得・整合性検証を完了しました。以下の日付付き更新欄は各日時点の履歴です。

『ためし部』と『瀬尾家』の制作を実例に、人物設定、4コマ脚本、作画、縦書き、部分修正、投稿用画像の準備をまとめた資料集です。検索できる冊子PDFと多言語版の作り方も扱います。

プロンプトを一度送って完成を待つだけでなく、試作を読んで修正し、採用稿を選ぶ工程を重視しています。画像生成AIを使い、作品を自分で確認しながら作りたい方を対象にしています。

**初版 2026年11月12日**。[GitHubリポジトリ](https://github.com/tyamada/manga-prompt-kit)で制作資料を公開しています。アプリ用PDF51冊をReleasesで公開しています。人物紹介4枚はReleasesで公開済み、[第1話本文画像14枚](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)もReleasesで公開済みです。

![こよみの人物紹介](examples/01-character/assets/adopted.jpg)

## こよみLive2Dモデル

『ためし部』小坂こよみの[Live2Dモデル v38・編集素材・再生手順](live2d/koyomi/README.md)を公開しています。穏やかな顔向き・傾き、まばたき、口の開閉と、前髪・横髪の6毛束の控えめな揺れ、専用の笑顔目・上下左右の視線・6表情に対応しています。

- [モデル・PSD・CMO3・確認動画をZIPでダウンロード](https://github.com/tyamada/manga-prompt-kit/releases/tag/koyomi-live2d-v38-20261125)
- [鼻筋・遠い目・耳の重なりを調整したv34（開発版）](live2d/koyomi/development/v34-depth-study/README.md)
- [左斜め向きの土台を追加したv35（開発版）](live2d/koyomi/development/v35-left-turn-study/README.md)
- [左向きの目・鼻・耳を調整したv36（開発版）](live2d/koyomi/development/v36-left-depth-study/README.md)
- [右80度の専用原画と開閉終点を確認するv37（独立試作）](live2d/koyomi/development/v37-right80-study/README.md)
- 採用音声Iを反映。口との測定差は約12ms。モデル本体は確認済みv36の顔立ち・6表情・髪揺れを保持。
- [音声付き確認動画](live2d/koyomi/preview/showcase-30s.mp4)／[無音版動画](live2d/koyomi/preview/showcase-30s-silent.mp4)
- **CC BY 4.0**：独自のモデル、編集素材、画像、モーション、文章、動画の映像部分。[適用範囲](live2d/koyomi/LICENSE.md)を参照してください。
- **音声の例外**：音声付き動画の「VOICEVOX:春日部つむぎ」の音声部分はCC BY 4.0の対象外です。公式規約に従います。音声単体WAVは同梱せず、配布モデルは無音で再生します。[音声の追加手順](live2d/koyomi/audio/README.md)を用意しています。

こよみの[右80度開閉の開発版v39](live2d/koyomi/development/v39-right80-continuous/README.md)も保存しています。45度からの接続は未完成で、通常配布はv38を維持します。

[こよみv40の右80度への切り替え確認モデル](live2d/koyomi/development/v40-right80-switching/README.md)を追加しました。まばたき中の排他的な表示切り替えで二重輪郭を解消し、v38の顔立ち・採用音声I・6表情とv39の開閉を保持しています。連続モーフとは区別しています。

連続モーフ用の[中間原画候補・仮分割PSD v41](live2d/koyomi/development/v41-intermediate-art/README.md)も追加しました。原画準備の段階で、Cubismへの組み込みと動作確認は未完了です。

## 瀬尾凪Live2D口リグ試作

『ためし部』瀬尾凪の正面モデルで、口パクに左右独立のまばたきを重ねた試作をCubism Viewerで確認しました。白目の縁を調整した視線v2と、まばたきv4のViewer用モデル、編集用CMO3、閉じ目のPSD、口リグv3を収録しています。波音リツのナレーションv2に合わせた口パクの別版と、原稿・合成クエリも収録しています。発音境界の開閉と口幅を調整した版も収録しています。アクセント試聴版3に合わせた口パクも収録しています。全フレーズを区間再生して発音境界を調整した版も掲載しています。波音リツの音声付き通し再生動画も掲載しています。顔角度用の左右斜め参考画と肌パーツ素材も掲載しています。補足作画を分けた正面PSDと重なり確認用CMO3を追加しました。[瀬尾凪の素材と再生手順](live2d/nagi/README.md)

## 最初の4コマを作る

1. [準備と最短の手順](docs/quickstart.md)を読む。
2. [汎用プロンプト集](prompts/README.md)から「人物設定」「脚本」「作画」を順に使う。
3. [カラー4コマの制作手順](docs/color-workflow.md)に沿い、1本を試作する。
4. 文字・話者・小物を確認し、[修正プロンプト](prompts/05-local-edit.md)で必要な箇所を直す。
5. 採用した画像だけを投稿用へ書き出す。画像の完成と外部サイトへの投稿は別の工程です。

必要なものは、文章を扱えるAI、参照画像を渡せる画像生成・編集手段、文字と画像を配置できる編集環境です。特定サービスの契約やAPIを必須にはしていません。既存の作例は内蔵画像生成ツールを使った記録に基づき、個別のモデル名は断定していません。同じ文面でも生成結果は変わります。

## 実際の制作例

| 実例 | 学べること | 完成までの工程 |
|---|---|---|
| [1 こよみの人物紹介](examples/01-character/README.md) | 性格に合う表情、人物の同一性、設定画と組版 | 表情を個別生成し、立ち絵・紹介文と合成 |
| [2 役割分担](examples/02-roles/README.md) | 小物、話者、背景の描き込みと省略 | 全体試作から3コマ目の背景を局所修正 |
| [3 名前の長さ](examples/03-name/README.md) | 長文、縦書き、紙上の文字の向き | 作画後、長い紙の印字を別画像として変形・合成 |
| [4 満場一致](examples/04-unanimous/README.md) | 席順、俯瞰、地図の向き、塗りの回復 | 複数の修正指示と正常な色参照を使い分ける |

追加資料として、[瀬尾家の設定と制作例](series/seo/README.md)に三姉妹の設定画、リビング、ギャグ表現、4コマ「宿題の先生」の最新版を収録しています。

## 資料の案内

- [プロンプト一覧](prompts/README.md)：他作品にも使える編集済みテンプレート9本。
- [ためし部の設定](series/tameshibu.md)：主役4人、追加4人、季節と小物。
- [採用部室寸法と4方向背景v2の設定](series/tameshibu/clubroom-20261121/README.md)：寸法・壁面・カメラ・制作プロンプト。背景画像本体は未公開・未収録。
- [採用衣装6案と4人の最新設定](series/tameshibu/wardrobe-20261118/README.md)：夏冬制服・防寒コート・体育着、JPEG/PNG設定画。
- [瀬尾家の設定](series/seo/README.md)：三姉妹、家庭内の服装と呼び方。
- [共通の作画方針](docs/art-direction.md)：通常版とギャグ表現、人物と背景の塗り分け。
- [文字と吹き出し](docs/lettering.md)：縦書き、発言順、紙上の印字。
- [検索できるPDF](docs/pdf-workflow.md)：冊子構成と検索可能な文字層。
- [翻訳と地域別編集](docs/localization.md)：会話とオチを保つ翻訳。
- [採用版と修正記録](docs/versioning.md)：参照画像、版、採用状態の管理。
- [出典と資料の読み方](docs/sources.md)：実使用文と編集済みテンプレートの区別。
- [ライセンス](LICENSE.md)：文章・プロンプト・脚本・収録画像はCC BY 4.0。第三者素材の条件は別途維持。
- [Releasesの公開と移行計画](releases/README.md)：アプリ用PDFとpixiv用画像の配布先・対象・公開状態。

## 作品と版を分ける

『ためし部』の冊子版はA5縦・右綴じ・8ページ、13本の4コマを収録する設計です。表紙と8ページはカラー、2〜7ページはモノクロが基本です。pixivリメイク版は1本1枚のカラー画像で、改稿した脚本と別の採用記録があります。両者を同じ完成版として扱いません。

『瀬尾家』は三姉妹の家庭での日常を描く別作品です。瀬尾凪は共通の人物ですが、妹や普段着を学校の漫画へ自動的に持ち込みません。『ためし部』のすみれと『瀬尾家』の澄は別人です。

## サンプルPDFをダウンロード

[日本語のダウンロードページ](https://tyamada.github.io/manga-prompt-kit/samples/ja/)・[English](https://tyamada.github.io/manga-prompt-kit/samples/en/)・[全14言語](https://tyamada.github.io/manga-prompt-kit/samples/)。各ページで話数・言語地域・容量を確認してPDFを選べます。PDF実体は既存Releasesで配布し、アプリ向け最新版一覧JSONのURLも維持します。

[ページの更新手順](docs/sample-download-maintenance.md)。

## 完成作品と制作記事

- [第1話の表紙と全13回のカラー画像・ZIPをダウンロード](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)

- [最新版アプリ用PDF51冊をダウンロード](https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261103-v1)

- [ためし部の第1回をpixivで読む](https://www.pixiv.net/artworks/151828086)
- [マンガ制作記事の連載一覧](https://qiita.com/tyamada22/stocks/ea14e9a9d04ec8292263)
- [PDF改訂と配布を扱った記事](https://qiita.com/tyamada22/items/eee3433d069cbdd2db04)
- [旧PDF配布先 Viewer（将来廃止予定）](https://github.com/tyamada/MihirakiPDFViewer_Android/releases/tag/sample-manga-v2)
- [旧PDF配布先 Utility（将来廃止予定）](https://github.com/tyamada/MihirakiPDFUtility_Android/releases/tag/sample-manga-v2)

この資料集はPDFビューアアプリ本体を含みません。最新版のPDFと投稿用画像は、**この制作資料リポジトリのGitHub Releasesへ集約する計画**です。アプリ側の既存2つのReleaseは移行中の旧配布先で、将来廃止予定です。新しいReleaseの公開・検証と利用アプリの移行が終わるまでは旧URLを維持します。

アプリ用PDF51冊は[新しいPDF Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261103-v1)で公開済みです。全件の匿名ダウンロードと整合性を確認しました。pixiv用人物紹介4枚をReleaseで公開済みです。第1話本文画像14枚も公開済みで、瀬尾家6枚は投稿完了未確認のため待機中です。アプリ側の参照先更新と旧2配布先の廃止は未実施です。[配布対象と移行手順](releases/README.md)を参照してください。

## ライセンス

本資料集は[CC BY 4.0](LICENSE.md)です。作者名と出典、ライセンスへのリンクを示し、変更があれば表示してください。アプリ本体や第三者フォントのライセンスは変更しません。

作者名：こまいろ日和 / Komairo Hiyori。作画・修正には生成AIを使用しています。最終的な採用判断は制作者が行います。

## 2026年11月13日の公開確認

[公開済み11作品と採用版制作プロンプト](releases/pixiv-publication-status.md)を更新しました。本文は7/14枚、人物紹介は4/4枚の投稿完了をユーザー報告で確認しています。11月12日の確認記録は当時の状態として保持します。最新の画像配布状態はreleases/README.mdを参照してください。

人物紹介4枚の完成JPEGは[GitHub Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-characters-20261109-v1)で配布しています。本文14枚と瀬尾家6枚のReleaseは待機中です。

## 2026年11月14日の公開確認

第7回「数字にできない」と11月季節イラスト「秋をひとつ、持ち帰ろう。」の公開URL・採用版プロンプト・制作工程を[公開記録](releases/pixiv-publication-status.md)へ追加しました。本文は8/14枚の投稿完了をユーザー報告で確認。第8〜13回の投稿完了まで本文Releaseは待機中です。季節イラストの画像Releaseは今回作成していません。

## 2026年11月16日の公開確認

第9回「地図の盲点」の[公開記録と採用版制作資料](releases/pixiv-publication-status.md)を追加しました。本文は表紙・第1〜9回の10/14枚をユーザー報告で確認しています。第10〜13回の完了確認がそろうまで本文画像Releaseは待機中です。実際の公開時刻とX告知完了は未確認です。

第8回「窓のむこう」はチャット「pixivマンガ投稿」の11月15日の公開URL報告を読み返し、[制作資料と公開記録](releases/pixiv-publication-status.md)へ追加しました。本文Releaseは引き続き待機中です。

## 2026年11月16日の全体照合結果

[公開記録とX告知一覧](releases/pixiv-publication-status.md)を全体照合しました。現行採用版の公開済み15作品の制作資料・画像ハッシュ・原文プロンプトの対応を確認し、第7回・第9回・11月季節イラストのX告知URL漏れを修正しました。X告知7件は完了記録あり、残る8作品は完了記録・URL未確認です。上の日付付き更新欄の未実施・未確認表記は当時の状態で、現在の状態はこの一覧を参照してください。本文Releaseは第10〜13回の投稿完了まで待機中です。

## 2026年11月17日の公開確認

第10回「案内上手」の[公開記録と採用版制作資料](releases/pixiv-publication-status.md)を追加しました。現行採用版の公開済み作品は16作品、本文は表紙＋第1〜10回の11/14枚です。X告知は報告時点で未実施。本文Releaseは第11〜13回の投稿完了まで待機中です。

## 2026年11月18日の公開確認

第11回「満場一致」の公開URLを[既存制作資料と公開記録](releases/pixiv-publication-status.md)へ反映しました。現行採用版の公開済み作品は17作品、本文は表紙＋第1〜11回の12/14枚です。X告知は報告時点で未投稿。本文Releaseは第12〜13回の投稿完了まで待機中です。

## 2026年11月19日の公開確認

第12回「地図の置き場所」の[制作資料・公開記録・X告知URL](releases/pixiv-publication-status.md)を追加しました。公開済み採用版は18作品、本文は表紙＋第1〜12回の13/14枚です。本文Releaseは第13回の投稿完了まで待機します。

## 2026年11月21日の公開記録更新

第13回「次の依頼」の制作資料・公開URL・画像付きX告知を追加しました。第10回「案内上手」のX告知URLも補完しました。第2話・制服設定の予約報告は公開済み一覧に追加していません。

## 2026年11月21日 第1話画像Release公開

[表紙と全13回の完成JPEG14枚・ZIP](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)を公開しました。付属資料を含む18添付すべてを匿名取得し、HTTP 200・容量・SHA-256一致とZIP内18ファイルの一致を確認しました。[検証記録](releases/ep01-public-verification.json)。CC BY 4.0。アプリ用PDFの最新版Releaseは維持し、第2話・制服設定・瀬尾家の未公開作品は追加していません。

## 2026年11月21日 第2話の初回公開

第2話「机、ひろがる。」の表紙と第1回「ひらく机」の[制作資料・実使用プロンプト・公開記録](releases/pixiv-publication-status.md)を追加しました。ユーザー提供URLと対応の明示確認が根拠です。公開済み採用版は21作品です。この2件の画像付きX告知は同日19:57 JSTに完了し、X告知完了は13件になりました。第2話第2〜13回の資料・画像は追加せず、第2話の画像Releaseも未作成です。

## 2026年11月22日 第2回と夏服の公開確認

第2話第2回「もうひとつの新居」の制作資料・実使用プロンプトと、既存の夏服設定資料へpixiv公開URL・画像付きX告知URLを反映しました。[公開記録](releases/pixiv-publication-status.md)は23作品、X告知完了15件です。第2話第3〜13回・他の衣装・部室背景v2は公開済み扱いにせず、画像Releaseも追加していません。

こよみLive2Dの[全体計画・残作業](live2d/koyomi/docs/roadmap.md)と[6表情・全身・手の開発資料](live2d/koyomi/development/README.md)を追加しました。安定配布はv31（斜め向き・閉眼中の口線表示を修正、左右独立の眉上下・角度・6毛束の物理演算・顔の6表情・専用笑顔目・視線）、全身や手などの開発資料は試作です。

## 2026年11月23日 第3回と冬服の公開確認

第2話第3回「最初の一個」の制作資料・実使用プロンプトと、冬服室内設定のpixiv公開URLを[公開記録](releases/pixiv-publication-status.md)へ反映しました。公開25作品、X告知完了17件。新規2件も同日18:17 JSTに画像付きX告知を完了し、個別URLを制作資料と公開記録へ追記しました。他の回・衣装・部室背景v2は公開済み扱いせず、画像・Releaseの追加も行っていません。

## 2026年11月24日 第4回とブレザーの公開確認

第2話第4回「全部できる」の制作資料・実使用プロンプトと、冬服ブレザーの公開URL・画像付きX告知URLを[公開記録](releases/pixiv-publication-status.md)へ反映しました。公開27作品、X告知完了19件です。他の未公開回・衣装・部室背景v2は公開済み扱いせず、画像本体・新しいReleaseは追加していません。

## 2026年11月25日 第5回と冬の外出着の公開確認

第2話第5回「遠くなったもの」の制作資料・実使用プロンプトと、冬の外出着設定の公開URL・画像付きX告知URLを[公開記録](releases/pixiv-publication-status.md)へ反映しました。公開29作品、X告知完了21件。未公開回・衣装・部室背景や非公開の正月所沢版は公開対象へ追加せず、画像本体・新しいReleaseも追加していません。
