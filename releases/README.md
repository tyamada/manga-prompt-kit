# GitHub Releasesの公開と移行計画

**最新状況（2026年11月27日）**：[公開記録](pixiv-publication-status.md)は33作品・X告知25件（新規2件はユーザー手動投稿報告）。第1話の表紙と全13回（14/14枚）のpixiv投稿完了報告がそろいました。[第1話の本文画像Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)を公開し、全18添付の匿名取得・整合性検証を完了しました。以下の日付付き更新欄は各日時点の履歴です。

**最新版のPDFとpixiv用画像の公開先は、この制作資料リポジトリのGitHub Releasesに統一します。** 制作資料と[PDF用Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261103-v1)を公開済みです。人物紹介4枚のReleaseは公開済み、[第1話本文画像14枚](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)も公開済みです。旧アプリ用2配布先は現在公開中ですが、移行後に廃止する予定です。廃止日は未定です。

## PDFダウンロードページ

[日本語](https://tyamada.github.io/manga-prompt-kit/samples/ja/)・[English](https://tyamada.github.io/manga-prompt-kit/samples/en/)・[全14言語](https://tyamada.github.io/manga-prompt-kit/samples/)で、話数と言語地域を選んでダウンロードできます。PDF実体は下記Releaseへ維持し、アプリ向けJSONのURLは変更していません。

## 配布対象と状態

| 対象 | 新しい配布先の状態 | 内容 | タグ候補 |
|---|---|---|---|
| アプリ用公開版PDF | 公開済み・匿名取得検証済み | 第1〜3話51冊＋第4話日本語1冊、計52冊 | manga-pdf-20261103-v1 / manga-pdf-20261127-ep4-ja-v1 |
| ためし部 pixiv本文 | 公開済み・全18添付検証済み | 11月11日採用版の表紙1枚と全13回、計14枚 | pixiv-tameshibu-ep01-20261111-v1 |
| ためし部 人物紹介 | 公開済み | こよみv10、凪・くるみ・すみれv1、計4枚 | pixiv-tameshibu-characters-20261109-v1 |
| 瀬尾家 pixiv本文 | 公開予定 | 三姉妹の中心v2、最後のアイスv2、お風呂の順番v6、宿題の先生v12、休日の予定v2、しっかり者のお願いv2、計6枚 | pixiv-seo-strips01-06-20261108-v1 |

PDF・第1話本文画像・人物紹介のタグは作成済みです。瀬尾家本文画像のタグは未作成の候補です。公開先はtyamada/manga-prompt-kitです。Release作成前に、既存タグと重複しないことを確認します。将来の版は新しい固定タグを使い、アプリのURLにlatest/downloadを使いません。

## アプリ用PDFの移行

旧配布先は次の2つです。2026年11月12日のAPI確認では各51冊が公開中です。

- [Viewer sample-manga-v2 旧配布先 将来廃止予定](https://github.com/tyamada/MihirakiPDFViewer_Android/releases/tag/sample-manga-v2)
- [Utility sample-manga-v2 旧配布先 将来廃止予定](https://github.com/tyamada/MihirakiPDFUtility_Android/releases/tag/sample-manga-v2)

Utility側はアプリ最新版との混同を避けるためプレリリース区分ですが、PDF自体は公開済みの完成版です。API取得時の一覧は[旧Release一覧](published-legacy.json)に保存しています。

同じ51冊が両側へ重複しているため、新しいReleaseは51冊に集約します。PDFを再生成せず、内容の版数・作者表示・第三者素材の表示を保持します。新しいReleaseの配布ファイル名はViewer側を基準にしています。Utilityの第1・2話のフィリピン語 `_fil.pdf` は、同一ハッシュのViewer側 `_tl.pdf` へ対応付けます。言語キーfilと既存サンプルIDは保持します。

[PDF一覧](pdf-manifest.json)には話数・言語・地域・ファイル名・ページ数・サイズ・SHA-256を、[移行対応表](pdf-migration.csv)には旧2配布先の102件から新しい51冊への対応を収録しています。リポジトリ名はtyamada/manga-prompt-kitで確定し、PDF Releaseの固定URLはJSONとCSVへ反映済みです。第1話本文画像と人物紹介のダウンロードURLは確定し、画像一覧に収録しています。瀬尾家の画像Releaseは未作成です。

読みやすい[全52冊の一覧表](pdf-catalog.md)も収録しています。

全51冊のローカル原本を、両旧ReleaseのAPIメタデータにあるバイト数とSHA-256へ照合しました。PDF本体約1.25GBは確認用ZIPへ重複同梱していません。新しいReleaseには各PDFを個別添付済みです。公開後に全51冊と付属4件を匿名ダウンロードし、最終HTTP 200、HTTPS、サイズ、SHA-256、PDF実体と8ページ構成を確認しました。[全件検証記録](pdf-public-verification.json)を参照してください。

## 移行の順序

1. 制作資料リポジトリtyamada/manga-prompt-kitを公開する（資料の初版公開段階）。
2. 新しいPDF用Releaseの下書きに51冊、manifest、SHA256SUMS、ライセンス、アプリ別移行対応表を添付する。
3. 新URLを確定してmanifestと対応表を更新し、下書きの添付数・サイズ・ハッシュを確認する。
4. 新しいReleaseの公開後、全51冊を匿名取得し、HTTPS、最終HTTP 200、PDF実体、バイト数、SHA-256を検証する。
5. 利用アプリのカタログ・固定URL・チェックサムを新Releaseへ更新する。ViewerとUtilityを含む参照箇所を調べ、旧IDと取得済みファイルの対応を保つ。表示・検索・再取得・オフラインを確認する。
6. アプリ更新の配信と移行状況を確認し、旧配布先へ移行先を案内する。案内の追記やアプリ配信は別の公開作業として実施する。
7. 旧URLが必要なアプリの扱い、移行期間、廃止日を確定した後に旧2配布先を廃止する。今は削除・非公開化しない。

GitHub Releaseの移動だけでアプリの参照先は切り替わりません。新規公開が終わるまでは旧URLを利用できるよう維持します。今回の作業でアプリのコード、ストア配信、旧Releaseは変更していません。

## pixiv用画像の配布

合計24枚の完成JPEGを、3つの画像Releaseに分ける予定です。[画像一覧](image-manifest.json)に各版、寸法、色空間、サイズ、SHA-256を記録しています。個別JPEGと、作品単位のZIP、manifest、SHA256SUMS、LICENSE.mdを添付します。

確認用一式のrelease-stagingには、元の採用画像を変更せず収録した3つのZIPと個別ファイルがあります。第1話本文14枚と人物紹介4枚はReleaseで公開済みで、瀬尾家6枚の一式は未公開です。本文中の画像は解説用としてGit管理し、完成画像一式のダウンロード先はReleaseへ案内します。完成データには比較用の旧版を混ぜません。

JPEG24枚はすべて長辺2400px以内です。2026年11月12日の公開前確認では、ためし部18枚は埋め込みICCでsRGB、瀬尾家6枚はEXIF ColorSpace=1でsRGBの指定を確認しました。全24枚を目視し、公開前に必須となる画像修正は見つかりませんでした。原本は変更していません。[公開前確認結果](image-preflight.md)を参照してください。画像Releaseはpixiv投稿後まで待機します。各Releaseに含む全画像の投稿完了を公開URLまたはユーザー報告で確認してから公開します。予約時刻の経過だけでは公開済みとみなしません。

GitHubへの公開日時とpixivへの投稿日時は別です。先行して見せたくない回があれば、公開直前に収録範囲と日時を調整します。瀬尾家の未制作表紙は含めません。

## ライセンスと添付データ

資料集・プロンプト・作品の許諾範囲は[CC BY 4.0](../LICENSE.md)です。PDFに埋め込まれたフォント等の既存条件は保持します。新しいReleasesを公開しても、旧ファイルの権利表示を変更する必要はありません。

GitHubが自動的に作るSource code ZIPと、ここで配布する完成画像・PDFの添付ファイルは別です。[GitHubのRelease説明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)を参照してください。

## 画像Releaseの待機方針

2026年11月12日のユーザー指定により、画像の先行公開は行わずpixiv投稿後まで待ちます。3つの画像Releaseはそれぞれの収録画像すべての投稿完了を確認してから公開します。自動公開は設定しません。既存の資料内の実例画像はそのままとし、PDFの移行Releaseは別工程で扱います。

## 現在の移行段階

PDFの公開と全件取得検証まで完了しました。次は[アプリ側の移行](application-handoff.md)です。旧2Releaseはまだ維持しています。第1話本文画像Releaseは公開済み、瀬尾家は待機中です。

## 2026年11月13日の公開確認

[公開済み11作品と採用版制作プロンプト](pixiv-publication-status.md)を更新しました。本文は7/14枚、人物紹介は4/4枚の投稿完了をユーザー報告で確認しています。11月12日の確認記録は当時の状態として保持します。最新の画像配布状態はreleases/README.mdを参照してください。

人物紹介4枚の完成JPEGは[GitHub Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-characters-20261109-v1)で配布しています。本文14枚と瀬尾家6枚のReleaseは待機中です。

## 2026年11月14日の公開確認

第7回「数字にできない」と11月季節イラスト「秋をひとつ、持ち帰ろう。」の公開URL・採用版プロンプト・制作工程を[公開記録](pixiv-publication-status.md)へ追加しました。本文は8/14枚の投稿完了をユーザー報告で確認。第8〜13回の投稿完了まで本文Releaseは待機中です。季節イラストの画像Releaseは今回作成していません。

## 2026年11月16日の公開確認

第9回「地図の盲点」の[公開記録と採用版制作資料](pixiv-publication-status.md)を追加しました。本文は表紙・第1〜9回の10/14枚をユーザー報告で確認しています。第10〜13回の完了確認がそろうまで本文画像Releaseは待機中です。実際の公開時刻とX告知完了は未確認です。

第8回「窓のむこう」はチャット「pixivマンガ投稿」の11月15日の公開URL報告を読み返し、[制作資料と公開記録](pixiv-publication-status.md)へ追加しました。本文Releaseは引き続き待機中です。

## 2026年11月16日の全体照合結果

[公開記録とX告知一覧](pixiv-publication-status.md)を全体照合しました。現行採用版の公開済み15作品の制作資料・画像ハッシュ・原文プロンプトの対応を確認し、第7回・第9回・11月季節イラストのX告知URL漏れを修正しました。X告知7件は完了記録あり、残る8作品は完了記録・URL未確認です。上の日付付き更新欄の未実施・未確認表記は当時の状態で、現在の状態はこの一覧を参照してください。本文Releaseは第10〜13回の投稿完了まで待機中です。

## 2026年11月17日の公開確認

第10回「案内上手」の[公開記録と採用版制作資料](pixiv-publication-status.md)を追加しました。現行採用版の公開済み作品は16作品、本文は表紙＋第1〜10回の11/14枚です。X告知は報告時点で未実施。本文Releaseは第11〜13回の投稿完了まで待機中です。

## 2026年11月18日の公開確認

第11回「満場一致」の公開URLを[既存制作資料と公開記録](pixiv-publication-status.md)へ反映しました。現行採用版の公開済み作品は17作品、本文は表紙＋第1〜11回の12/14枚です。X告知は報告時点で未投稿。本文Releaseは第12〜13回の投稿完了まで待機中です。

## 2026年11月19日の公開確認

第12回「地図の置き場所」の[制作資料・公開記録・X告知URL](pixiv-publication-status.md)を追加しました。公開済み採用版は18作品、本文は表紙＋第1〜12回の13/14枚です。本文Releaseは第13回の投稿完了まで待機します。

## 2026年11月21日の公開記録更新

第13回「次の依頼」の制作資料・公開URL・画像付きX告知を追加しました。第10回「案内上手」のX告知URLも補完しました。第2話・制服設定の予約報告は公開済み一覧に追加していません。

## 2026年11月21日 第1話画像Release公開

[表紙と全13回の完成JPEG14枚・ZIP](https://github.com/tyamada/manga-prompt-kit/releases/tag/pixiv-tameshibu-ep01-20261111-v1)を公開しました。付属資料を含む18添付すべてを匿名取得し、HTTP 200・容量・SHA-256一致とZIP内18ファイルの一致を確認しました。[検証記録](ep01-public-verification.json)。CC BY 4.0。アプリ用PDFの最新版Releaseは維持し、第2話・制服設定・瀬尾家の未公開作品は追加していません。

## 2026年11月21日 第2話の初回公開

第2話「机、ひろがる。」の表紙と第1回「ひらく机」の[制作資料・実使用プロンプト・公開記録](pixiv-publication-status.md)を追加しました。ユーザー提供URLと対応の明示確認が根拠です。公開済み採用版は21作品です。この2件の画像付きX告知は同日19:57 JSTに完了し、X告知完了は13件になりました。第2話第2〜13回の資料・画像は追加せず、第2話の画像Releaseも未作成です。

## 2026年11月22日 第2回と夏服の公開確認

第2話第2回「もうひとつの新居」の制作資料・実使用プロンプトと、既存の夏服設定資料へpixiv公開URL・画像付きX告知URLを反映しました。[公開記録](pixiv-publication-status.md)は23作品、X告知完了15件です。第2話第3〜13回・他の衣装・部室背景v2は公開済み扱いにせず、画像Releaseも追加していません。

## 2026年11月23日 第3回と冬服の公開確認

第2話第3回「最初の一個」の制作資料・実使用プロンプトと、冬服室内設定のpixiv公開URLを[公開記録](pixiv-publication-status.md)へ反映しました。公開25作品、X告知完了17件。新規2件も同日18:17 JSTに画像付きX告知を完了し、個別URLを制作資料と公開記録へ追記しました。他の回・衣装・部室背景v2は公開済み扱いせず、画像・Releaseの追加も行っていません。

## 2026年11月24日 第4回とブレザーの公開確認

第2話第4回「全部できる」の制作資料・実使用プロンプトと、冬服ブレザーの公開URL・画像付きX告知URLを[公開記録](pixiv-publication-status.md)へ反映しました。公開27作品、X告知完了19件です。他の未公開回・衣装・部室背景v2は公開済み扱いせず、画像本体・新しいReleaseは追加していません。

## 2026年11月25日 第5回と冬の外出着の公開確認

第2話第5回「遠くなったもの」の制作資料・実使用プロンプトと、冬の外出着設定の公開URL・画像付きX告知URLを[公開記録](pixiv-publication-status.md)へ反映しました。公開29作品、X告知完了21件。未公開回・衣装・部室背景や非公開の正月所沢版は公開対象へ追加せず、画像本体・新しいReleaseも追加していません。

## 2026年11月26日 第6回と夏の体育着の公開確認

第2話第6回「第一便」の制作資料・実使用プロンプトと、夏の体育着設定の公開URL・画像付きX告知URLを[公開記録](pixiv-publication-status.md)へ反映しました。公開31作品、X告知完了23件です。未公開回・衣装・部室背景、非公開の正月所沢版は公開対象へ追加せず、画像本体・新しいReleaseも追加していません。

## 2026年11月27日 第7回と体育用ジャージの公開確認

第2話第7回「注文の多い船」の制作資料・実使用プロンプトと体育用ジャージ設定の公開URLを[公開記録](pixiv-publication-status.md)へ反映しました。公開33作品、X告知完了25件。新規2件はユーザーの手動投稿完了報告と作品対応確認に基づき告知URLを追記しました。本文・添付画像は直接未確認です。衣装6案すべてのpixiv公開報告を確認しましたが、新しい画像Releaseは作成していません。未公開回・背景・非公開の正月所沢版は追加していません。

## 2026年11月27日 第4話日本語版追加

[第4話の新規PDF Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261127-ep4-ja-v1)を公開し、PDFと付属3件を匿名取得・容量・SHA-256照合しました。既存51冊は旧固定版のまま維持。最新版JSONは同一schemaにep4_jaを加えた52冊で、14言語の案内も更新しました。PDF移行の過去記録の51冊は当時の対象数です。[最終確認](ep04-ja-final-review.json)・[公開取得検証](ep04-ja-public-verification.json)。

2026年11月28日0:42（JST）、正式公開・取得確認後に[@tyamada22で第4話の公開案内](https://x.com/tyamada22/status/2126340932371132648)を投稿しました。[本文・確認記録](ep04-ja-announcement.json)。

2026年11月28日、公開記録・制作資料・最新版JSON・14言語ページ・X告知URLを[全体照合]( ep04-ja-consistency-review.json)しました。
