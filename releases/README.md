# GitHub Releasesの公開と移行計画

**最新版のPDFとpixiv用画像の公開先は、この制作資料リポジトリのGitHub Releasesに統一します。** 制作資料のリポジトリは公開し、PDF・画像の新しいReleaseはまだ公開していません。旧アプリ用2配布先は現在公開中ですが、移行後に廃止する予定です。廃止日は未定です。

## 配布対象と状態

| 対象 | 新しい配布先の状態 | 内容 | タグ候補 |
|---|---|---|---|
| アプリ用公開版PDF | 公開予定 | 第1〜3話、14言語・17言語地域区分、51冊 | manga-pdf-20261103-v1 |
| ためし部 pixiv本文 | 公開予定 | 11月11日採用版の表紙1枚と全13回、計14枚 | pixiv-tameshibu-ep01-20261111-v1 |
| ためし部 人物紹介 | 公開予定 | こよみv10、凪・くるみ・すみれv1、計4枚 | pixiv-tameshibu-characters-20261109-v1 |
| 瀬尾家 pixiv本文 | 公開予定 | 三姉妹の中心v2、最後のアイスv2、お風呂の順番v6、宿題の先生v12、休日の予定v2、しっかり者のお願いv2、計6枚 | pixiv-seo-strips01-06-20261108-v1 |

タグは候補で、まだ作成していません。公開先はtyamada/manga-prompt-kitです。Release作成前に、既存タグと重複しないことを確認します。将来の版は新しい固定タグを使い、アプリのURLにlatest/downloadを使いません。

## アプリ用PDFの移行

旧配布先は次の2つです。2026年11月12日のAPI確認では各51冊が公開中です。

- [Viewer sample-manga-v2 旧配布先 将来廃止予定](https://github.com/tyamada/MihirakiPDFViewer_Android/releases/tag/sample-manga-v2)
- [Utility sample-manga-v2 旧配布先 将来廃止予定](https://github.com/tyamada/MihirakiPDFUtility_Android/releases/tag/sample-manga-v2)

Utility側はアプリ最新版との混同を避けるためプレリリース区分ですが、PDF自体は公開済みの完成版です。API取得時の一覧は[旧Release一覧](published-legacy.json)に保存しています。

同じ51冊が両側へ重複しているため、新しいReleaseは51冊に集約します。PDFを再生成せず、内容の版数・作者表示・第三者素材の表示を保持します。新しいReleaseの配布ファイル名はViewer側を基準にしています。Utilityの第1・2話のフィリピン語 `_fil.pdf` は、同一ハッシュのViewer側 `_tl.pdf` へ対応付けます。言語キーfilと既存サンプルIDは保持します。

[PDF一覧](pdf-manifest.json)には話数・言語・地域・ファイル名・ページ数・サイズ・SHA-256を、[移行対応表](pdf-migration.csv)には旧2配布先の102件から新しい51冊への対応を収録しています。リポジトリ名はtyamada/manga-prompt-kitで確定しています。Releaseは未作成のため、ダウンロードURLはJSONではnull、CSVでは空欄です。

読みやすい[全51冊の一覧表](pdf-catalog.md)も収録しています。

全51冊のローカル原本を、両旧ReleaseのAPIメタデータにあるバイト数とSHA-256へ照合しました。PDF本体約1.25GBは確認用ZIPへ重複同梱していません。新しいRelease公開時は各PDFを個別添付する計画です。

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

確認用一式のrelease-stagingには、元の採用画像を変更せず収録した3つのZIPと個別ファイルがあります。これはアップロード済みのReleaseではありません。本文中の画像は解説用としてGit管理し、完成画像一式のダウンロード先はReleaseへ案内します。完成データには比較用の旧版を混ぜません。

JPEG24枚はすべて長辺2400px以内です。2026年11月12日の公開前確認では、ためし部18枚は埋め込みICCでsRGB、瀬尾家6枚はEXIF ColorSpace=1でsRGBの指定を確認しました。全24枚を目視し、公開前に必須となる画像修正は見つかりませんでした。原本は変更していません。[公開前確認結果](image-preflight.md)を参照してください。画像Releaseはpixiv投稿後まで待機します。各Releaseに含む全画像の投稿完了を公開URLまたはユーザー報告で確認してから公開します。予約時刻の経過だけでは公開済みとみなしません。

GitHubへの公開日時とpixivへの投稿日時は別です。先行して見せたくない回があれば、公開直前に収録範囲と日時を調整します。瀬尾家の未制作表紙は含めません。

## ライセンスと添付データ

資料集・プロンプト・作品の許諾範囲は[CC BY 4.0](../LICENSE.md)です。PDFに埋め込まれたフォント等の既存条件は保持します。新しいReleasesを公開しても、旧ファイルの権利表示を変更する必要はありません。

GitHubが自動的に作るSource code ZIPと、ここで配布する完成画像・PDFの添付ファイルは別です。[GitHubのRelease説明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)を参照してください。

## 画像Releaseの待機方針

2026年11月12日のユーザー指定により、画像の先行公開は行わずpixiv投稿後まで待ちます。3つの画像Releaseはそれぞれの収録画像すべての投稿完了を確認してから公開します。自動公開は設定しません。既存の資料内の実例画像はそのままとし、PDFの移行Releaseは別工程で扱います。
