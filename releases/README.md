# GitHub Releasesの公開と移行計画

**最新版のPDFとpixiv用画像の公開先は、この制作資料リポジトリのGitHub Releasesに統一します。** 制作資料と[PDF用Release](https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261103-v1)を公開済みです。人物紹介4枚のReleaseは公開済み、本文画像Releaseは投稿後まで待機中です。旧アプリ用2配布先は現在公開中ですが、移行後に廃止する予定です。廃止日は未定です。

## 配布対象と状態

| 対象 | 新しい配布先の状態 | 内容 | タグ候補 |
|---|---|---|---|
| アプリ用公開版PDF | 公開済み・全件匿名取得検証済み | 第1〜3話、14言語・17言語地域区分、51冊 | manga-pdf-20261103-v1 |
| ためし部 pixiv本文 | 公開予定 | 11月11日採用版の表紙1枚と全13回、計14枚 | pixiv-tameshibu-ep01-20261111-v1 |
| ためし部 人物紹介 | 公開済み | こよみv10、凪・くるみ・すみれv1、計4枚 | pixiv-tameshibu-characters-20261109-v1 |
| 瀬尾家 pixiv本文 | 公開予定 | 三姉妹の中心v2、最後のアイスv2、お風呂の順番v6、宿題の先生v12、休日の予定v2、しっかり者のお願いv2、計6枚 | pixiv-seo-strips01-06-20261108-v1 |

PDFと人物紹介のタグは作成済みです。本文画像のタグは未作成の候補です。公開先はtyamada/manga-prompt-kitです。Release作成前に、既存タグと重複しないことを確認します。将来の版は新しい固定タグを使い、アプリのURLにlatest/downloadを使いません。

## アプリ用PDFの移行

旧配布先は次の2つです。2026年11月12日のAPI確認では各51冊が公開中です。

- [Viewer sample-manga-v2 旧配布先 将来廃止予定](https://github.com/tyamada/MihirakiPDFViewer_Android/releases/tag/sample-manga-v2)
- [Utility sample-manga-v2 旧配布先 将来廃止予定](https://github.com/tyamada/MihirakiPDFUtility_Android/releases/tag/sample-manga-v2)

Utility側はアプリ最新版との混同を避けるためプレリリース区分ですが、PDF自体は公開済みの完成版です。API取得時の一覧は[旧Release一覧](published-legacy.json)に保存しています。

同じ51冊が両側へ重複しているため、新しいReleaseは51冊に集約します。PDFを再生成せず、内容の版数・作者表示・第三者素材の表示を保持します。新しいReleaseの配布ファイル名はViewer側を基準にしています。Utilityの第1・2話のフィリピン語 `_fil.pdf` は、同一ハッシュのViewer側 `_tl.pdf` へ対応付けます。言語キーfilと既存サンプルIDは保持します。

[PDF一覧](pdf-manifest.json)には話数・言語・地域・ファイル名・ページ数・サイズ・SHA-256を、[移行対応表](pdf-migration.csv)には旧2配布先の102件から新しい51冊への対応を収録しています。リポジトリ名はtyamada/manga-prompt-kitで確定し、PDF Releaseの固定URLはJSONとCSVへ反映済みです。本文画像ReleaseのダウンロードURLは未確定です。人物紹介のURLは確定しました。

読みやすい[全51冊の一覧表](pdf-catalog.md)も収録しています。

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

確認用一式のrelease-stagingには、元の採用画像を変更せず収録した3つのZIPと個別ファイルがあります。人物紹介4枚の一式はReleaseへアップロード済みで、本文の2つの一式は未公開です。本文中の画像は解説用としてGit管理し、完成画像一式のダウンロード先はReleaseへ案内します。完成データには比較用の旧版を混ぜません。

JPEG24枚はすべて長辺2400px以内です。2026年11月12日の公開前確認では、ためし部18枚は埋め込みICCでsRGB、瀬尾家6枚はEXIF ColorSpace=1でsRGBの指定を確認しました。全24枚を目視し、公開前に必須となる画像修正は見つかりませんでした。原本は変更していません。[公開前確認結果](image-preflight.md)を参照してください。画像Releaseはpixiv投稿後まで待機します。各Releaseに含む全画像の投稿完了を公開URLまたはユーザー報告で確認してから公開します。予約時刻の経過だけでは公開済みとみなしません。

GitHubへの公開日時とpixivへの投稿日時は別です。先行して見せたくない回があれば、公開直前に収録範囲と日時を調整します。瀬尾家の未制作表紙は含めません。

## ライセンスと添付データ

資料集・プロンプト・作品の許諾範囲は[CC BY 4.0](../LICENSE.md)です。PDFに埋め込まれたフォント等の既存条件は保持します。新しいReleasesを公開しても、旧ファイルの権利表示を変更する必要はありません。

GitHubが自動的に作るSource code ZIPと、ここで配布する完成画像・PDFの添付ファイルは別です。[GitHubのRelease説明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)を参照してください。

## 画像Releaseの待機方針

2026年11月12日のユーザー指定により、画像の先行公開は行わずpixiv投稿後まで待ちます。3つの画像Releaseはそれぞれの収録画像すべての投稿完了を確認してから公開します。自動公開は設定しません。既存の資料内の実例画像はそのままとし、PDFの移行Releaseは別工程で扱います。

## 現在の移行段階

PDFの公開と全件取得検証まで完了しました。次は[アプリ側の移行](application-handoff.md)です。旧2Releaseはまだ維持しており、本文画像Releaseは待機中です。

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
