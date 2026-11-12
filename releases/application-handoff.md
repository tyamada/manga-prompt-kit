# アプリ側のPDF配布先移行

## 公開先と入力資料

新PDF Release：https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261103-v1

Release添付のpdf-manifest.json、pdf-migration.csv、SHA256SUMSを使います。公開後の全件取得検証は[pdf-public-verification.json](pdf-public-verification.json)です。

## 実施すること

1. PDFを参照する利用アプリとカタログを調べる。ViewerとUtilityのAndroid版だけに限定せず、iOS等も旧URLを参照していれば対象へ追加する。
2. 既存sample_idと言語キーを維持し、対応表に従って固定ダウンロードURLを新配布先へ更新する。latest/downloadは使わない。
3. Utilityの第1・2話のフィリピン語filの旧ファイル名は、新配布先のtl名へ対応付ける。言語キーfilと既存IDを一括改名しない。
4. PDF本体は同一ハッシュなので、取得済みファイルを不要に削除・再取得しない。既存ファイル名とキャッシュの扱いをアプリごとに確認する。
5. 51件の一覧、地域別選択、新規取得、旧版取得済み、オフライン、再取得、破損検出を確認する。実機または利用可能な環境で表示・検索・コピーを確認し、未実施項目は明記する。
6. 公開ページと利用者向け案内を更新し、アプリ更新の配信を別途実施する。

## 残すもの

旧2Releaseと既存URLは、利用アプリの移行確認が終わるまで維持します。今回のPDF公開では、アプリのコード、ストア設定、既存Releaseの編集・削除は実施していません。画像Releaseも公開していません。
